# Auto-Archive: Run Module
# Version: v0.0.3-dev
# Path: `\run.py`
# Updated: 09-24-2023

#############################
# ⚠️ ACTIVE DEVELOPMENT ⚠️ #
## ## ## ## ## ## ## ## ## ##

from app.routes import home_routes, upload_routes, archive_routes, clericus_routes
import os
import sys
from flask import Flask
from core.logger import run_logger

# Add the project directory to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Flask configuration
app = Flask(__name__, template_folder='app/templates',
            static_folder='app/static')

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
