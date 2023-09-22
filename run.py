# Auto-Archive: Run Module
# Version: v0.0.3-dev
# Path: `\run.py`
# Updated: 09-20-2023

# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

import promptlayer
from app.routes import home_routes, upload_routes, archive_routes, clericus_routes
import os
import openai
from flask import Flask

app = Flask(__name__)

# Import log configuration

# Flask configuration
app = Flask(__name__, template_folder='app/templates',
            static_folder='app/static')

# OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# PromptLayer API key
promptlayer.api_key = os.getenv('PROMPTLAYER_API_KEY')

# Create uploads directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Initialize routes
home_routes(app)
upload_routes(app)
archive_routes(app)
clericus_routes(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
