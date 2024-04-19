import sys
import logging

# Add the directory containing your Flask application to the Python path
sys.path.insert(0, '/var/www/html/PhenoPhene')

# Set up logging to capture any errors
logging.basicConfig(stream=sys.stderr)
sys.stderr.write("Starting your WSGI application...\n")
sys.path.append('/var/www/html/PhenoPhene/venv/lib/python3.8/site-packages')
activate_this = '/var/www/html/PhenoPhene/venv/bin/activate_this.py'
# Import your Flask application instance
from app import app  # Replace 'app' with the actual name of your Flask application

# Define the WSGI callable (usually named 'application' by convention)
application = app

# Optional: If your Flask application requires any additional setup,
# you can do it here. For example, initializing a database connection,
# setting up configurations, etc.
# Make sure to modify this according to your application's requirements.



# app.wsgi

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application, use_reloader=True)

