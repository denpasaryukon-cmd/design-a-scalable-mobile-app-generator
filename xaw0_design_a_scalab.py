import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database to store app templates
app_templates = {
    "todo_app": {"name": "Todo App", "description": "A simple todo list app"},
    "chat_app": {"name": "Chat App", "description": "A real-time chat app"},
    "blog_app": {"name": "Blog App", "description": "A simple blogging platform"},
}

# Database to store generated apps
generated_apps = {}

@app.route('/generate_app', methods=['POST'])
def generate_app():
    data = request.get_json()
    app_template = data['app_template']
    app_name = data['app_name']
    app_description = data['app_description']

    if app_template in app_templates:
        # Generate app code using the selected template
        app_code = generate_app_code(app_template, app_name, app_description)
        generated_apps[app_name] = app_code
        return jsonify({"message": f"App '{app_name}' generated successfully", "app_code": app_code})
    else:
        return jsonify({"message": "Invalid app template"}), 400

def generate_app_code(app_template, app_name, app_description):
    # This function generates the app code based on the selected template
    # For demonstration purposes, it returns a simple "Hello World" app code
    return f"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '{app_description}'

if __name__ == '__main__':
    app.run(debug=True)
"""

@app.route('/get_generated_apps', methods=['GET'])
def get_generated_apps():
    return jsonify(list(generated_apps.keys()))

if __name__ == '__main__':
    app.run(debug=True)