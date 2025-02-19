from flask import Flask, render_template
from datetime import datetime
import yaml
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')

    @app.route('/')
    def home():
        site_updated = datetime.now().strftime('%Y-%m-%d')
        return render_template('index.html', site_updated=site_updated)
    
    
    @app.route('/templates')
    def templates():
        with open('data/templates.yaml', 'r') as file:
            templates = yaml.safe_load(file)
        return render_template('templates.html', templates=templates)
    
    @app.route('/resources')
    def resources():
        # Load the main resources.yaml
        with open('data/resources/resources.yaml', 'r') as file:
            main_yaml = yaml.safe_load(file)

        # Aggregate items from all section files
        resources = {}
        for section in main_yaml['sections']:
            section_name = section['name']
            file_path = os.path.join('data/resources', section['file'])
            with open(file_path, 'r') as sec_file:
                section_data = yaml.safe_load(sec_file)
            resources[section_name] = section_data['items']

        return render_template('resources.html', resources=resources)

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)