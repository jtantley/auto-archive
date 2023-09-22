# Auto-Archive: Database Operations
# Path: `\\core\\db_operations.py``
# Version: v0.0.3-dev
# Updated: 08-30-2023

# -- # --- # --- # --- # -- #
# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
# -- # --- # --- # --- # -- #

import os
import psycopg2
import time
import uuid
import logging
from core.log_config import logging
from contextlib import closing

#########################################################


# SUPABASE POSTGRESQL DATABASE

# Function to get Supabase credentials


def get_supabase_credentials():
    db_name = os.environ['SUPABASE_DB_NAME']
    db_user = os.environ['SUPABASE_DB_USER']
    db_password = os.environ['SUPABASE_DB_PASSWORD']
    db_host = os.environ['SUPABASE_DB_HOST']
    db_port = os.environ['SUPABASE_DB_PORT']

    return db_name, db_user, db_password, db_host, db_port

# Supabase database connection


def get_db_connection():
    db_name, db_user, db_password, db_host, db_port = get_supabase_credentials()

    for i in range(5):
        try:
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            logging.info("Successfully connected to the database")
            return conn
        except Exception as e:
            logging.error("Error while connecting to the database: " + str(e))
            if i < 5 - 1:  # i is zero indexed
                time.sleep(5)
                continue
            else:
                return None

# Function to get `category_id`` from category name


def get_category_id(category_name):
    logging.info(f"Fetching category id for: {category_name}")
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute("SELECT * FROM categories")
            rows = cur.fetchall()
            logging.info(f"All categories: {rows}")
            cur.execute(
                "SELECT category_id FROM categories WHERE category_name = %s",
                (category_name,)
            )
            logging.info("Executed query to fetch category id")
            category_id = cur.fetchone()
            if category_id is not None:
                return category_id[0]
            else:
                logging.error(
                    f"Category '{category_name}' not found in the database.")
                return None

# Function to get all categories from the database


def get_all_categories():
    logging.info(f"Fetching all categories")
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute("SELECT category_name FROM categories")
            rows = cur.fetchall()
            logging.info(f"All categories: {rows}")
            categories = [row[0] for row in rows]
            return categories

# Function to save entities to the database


def save_entities(entities):
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            entity_ids = []
            for entity in entities:
                cur.execute(
                    "SELECT entity_id FROM entities WHERE entity_name = %s",
                    (entity['entity'],)
                )
                entity_id = cur.fetchone()
                if entity_id is None:
                    cur.execute(
                        "INSERT INTO entities (entity_id, entity_name, entity_type) VALUES (%s, %s, %s) RETURNING entity_id",
                        (str(uuid.uuid4()), entity['entity'], entity['type'])
                    )
                    entity_id = cur.fetchone()
                entity_ids.append(entity_id[0])
            conn.commit()
            return entity_ids


def save_profile_entity(profile_id, entity_id):
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute(
                "INSERT INTO profile_entities (profile_entity_id, profile_id, entity_id) VALUES (%s, %s, %s)",
                (str(uuid.uuid4()), profile_id, entity_id)
            )
            conn.commit()

# Function: Save archive profile to database


def save_archive_profile(archive_profile):
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute(
                "INSERT INTO archive_profiles (profile_title, profile_summary, profile_text, profile_date, category_id, profile_embedding) VALUES (%s, %s, %s, %s, %s, %s) RETURNING profile_id",
                (archive_profile['profile_title'], archive_profile['profile_summary'], archive_profile['profile_text'],
                 archive_profile['profile_date'], archive_profile['category_id'], archive_profile['profile_embedding'])
            )
            profile_id = cur.fetchone()[0]
            conn.commit()
            return profile_id

# Function to get all archive profiles from the database


def get_archive_profiles():
    logging.info("Fetching all archive profiles")
    with closing(get_db_connection()) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute("SELECT * FROM archive_profiles")
            rows = cur.fetchall()
            logging.info(f"All profiles: {rows}")
            profiles = []
            for row in rows:
                profile = {
                    'profile_id': row[0],
                    'profile_title': row[1],
                    'profile_summary': row[2],
                    'profile_text': row[3],
                    'profile_date': row[4],
                    'category_id': row[5],
                    'profile_embedding': row[6]
                }
                profiles.append(profile)
            return profiles
