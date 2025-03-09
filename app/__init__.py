from flask import Flask, render_template, send_from_directory
from datetime import datetime
import yaml
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')
    
    # Only disable caching when running locally
    if os.getenv("FLASK_ENV") == "development":
        @app.after_request
        def add_header(response):
            response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
            return response

        @app.route('/static/<path:filename>')
        def static_file(filename):
            return send_from_directory('static', filename, cache_timeout=0)

    @app.route('/')
    def home():
        site_updated = datetime.now().strftime('%Y-%m-%d')
        return render_template('index.html', site_updated=site_updated)
    
    
    @app.route('/templates')
    def templates():
        site_updated = datetime.now().strftime('%Y-%m-%d')
        with open('data/templates.yaml', 'r') as file:
            templates = yaml.safe_load(file)
            
        return render_template('templates.html', templates=templates, site_updated=site_updated)
    

    
    @app.route('/resources')
    def resources():
        site_updated = datetime.now().strftime('%Y-%m-%d')

        # Load YAML file
        with open('data/resources.yaml', 'r') as file:
            resources = yaml.safe_load(file)

        print("DEBUG: Resources YAML Loaded ->", resources)  # Add this

        # Ensure all categories contain a list of items
        for category in resources:
            if not isinstance(category.get("items", []), list):
                print(f"ERROR: 'items' in category {category.get('category')} is not a list!")
                category["items"] = []  # Set a default empty list to avoid crashes

        return render_template('resources.html', resources=resources, site_updated=site_updated)
    
    
    @app.route('/utility')
    def utility():
        site_updated = datetime.now().strftime('%Y-%m-%d')
        
        return render_template('utility.html', site_updated=site_updated)

    return app

# if __name__ == '__main__':
#     app = create_app()
#     app.config["ENV"] = "development"  # Ensure Flask knows it's running locally
#     port = int(os.environ.get('PORT', 5001))  # Set a unique port
#     app.run(host='0.0.0.0', port=port, debug=True)

# if __name__ == '__main__':
#     app = create_app()
#     port = int(os.environ.get('PORT', 8000))
#     app.run(host='0.0.0.0', port=port)



# FLASK_APP=app FLASK_ENV=development flask run --port=5001
