# Auto-Archive: Routes Module
# Version: v0.0.3-dev
# Path: `\app\routes.py`
# Updated: 09-22-2023

# 🚧 ACTIVE DEVELOPMENT 🚧 #
## ## ## ## ## ## ## ## ## ##

import os
import openai
from flask import request, render_template, redirect, url_for, jsonify
import core.document_processor as document_processor
import core.db_operations as db_ops
from core.clericus import generate_response
from core.log_config import routes_logger

# Clericus logger
clericus_logger = routes_logger

# OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

def clericus_routes(app):  # Routes for Clericus chatbot
    @app.route('/clericus', methods=['GET', 'POST'])
    def clericus_route():
        if request.method == 'GET':
            return render_template('clericus.html')
        if request.content_type != 'application/json':
            return jsonify({"error": "Expected Content-Type: application/json"}), 400
        try:
            if request.json and 'query' in request.json and 'session_id' in request.json:
                user_input = request.json['query']
                session_id = request.json['session_id']
                response = generate_response(user_input, session_id)
                return jsonify({"response": response})
            else:
                return jsonify({"error": "Missing 'query' in JSON payload"}), 400
        except Exception as e:
            clericus_logger.error(f"Exception in routes: {str(e)}")
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500


def home_routes(app):  # Routes for home page
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')


def upload_routes(app):  # Routes for 'Upload' page
    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        try:
            if request.method == 'POST':
                clericus_logger.info('Upload started')
                file = request.files['file']
                filename = file.filename
                filepath = os.path.join('uploads', filename)
                file.save(filepath)

                clericus_logger.info('Processing document')
                document_text, archive_profile, summary_embedding, entities = document_processor.process_document(
                    filepath)
                clericus_logger.info('Document processed')

                profile_id = db_ops.save_archive_profile(archive_profile)

                entity_ids = db_ops.save_entities(entities)
                for entity_id in entity_ids:
                    db_ops.save_profile_entity(profile_id, entity_id)

                return redirect(url_for('upload_successful'))

        except Exception as e:
            clericus_logger.error(f"Exception in routes: {str(e)}")
            return f"An error occurred: {str(e)}", 500

        return render_template('upload.html')

    @app.route('/upload_successful')
    def upload_successful():
        return render_template('upload_successful.html')


def archive_routes(app):  # Routes for 'Archive' page
    @app.route('/archive', methods=['GET'])
    def archive():
        with db_ops.get_db_connection() as conn:
            archive_profiles = []
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT p.profile_id, p.profile_title, p.profile_summary, p.profile_text, p.profile_date, c.category_name FROM archive_profiles AS p JOIN categories AS c ON p.category_id = c.category_id"
                    )
                    rows = cur.fetchall()

                for row in rows:
                    profile_id = row[0]
                    with conn.cursor() as cur:
                        cur.execute(
                            "SELECT e.entity_name, e.entity_type FROM entities AS e JOIN profile_entities AS pe ON e.entity_id = pe.entity_id WHERE pe.profile_id = %s",
                            (profile_id,)
                        )
                        entities_rows = cur.fetchall()
                    entities = [{'entity_name': entity_row[0], 'entity_type': entity_row[1]}
                                for entity_row in entities_rows]

                    archive_profiles.append({
                        'profile_id': profile_id,
                        'profile_title': row[1],
                        'profile_summary': row[2],
                        'profile_text': row[3],
                        'profile_date': row[4],
                        'category_name': row[5],
                        'entities': entities
                    })

            finally:
                pass

        return render_template('archive.html', profiles=archive_profiles)
