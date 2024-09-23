from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask(__name__)

moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f"Page not found: {e}")  # Logging the error
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f"Internal server error: {e}")  # Logging the error
    return render_template('500.html'), 500

@app.route('/')
def index():
    current_time = datetime.utcnow()
    app.logger.info(f"Index page accessed at {current_time}")  # Logging access
    return render_template('index.html',
                           current_time=current_time)

@app.route('/user/<name>')
def user(name):
    current_time = datetime.utcnow()
    app.logger.info(f"User page for {name} accessed at {current_time}")  # Logging access
    return render_template('user.html', name=name, current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
