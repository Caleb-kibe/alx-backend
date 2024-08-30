Flask i18n & l10n Example
This project demonstrates a basic Flask application with internationalization (i18n) and localization (l10n) features using Flask-Babel. It includes examples of how to parametrize templates to display different languages, infer the correct locale from URL parameters, user settings, or request headers, and localize timestamps.

Features
Basic Flask App: A simple Flask application with a / route that renders a template.
Internationalization (i18n): Support for multiple languages (English, Spanish, and French) with Flask-Babel.
Locale Inference: Automatic locale selection based on URL parameters, user settings, or request headers.
Timestamp Localization: Displaying localized timestamps using Flask-Babel and pytz.
Prerequisites
Python 3.x
Flask
Flask-Babel
pytz
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/flask-i18n-l10n-example.git
cd flask-i18n-l10n-example
Create a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Install Flask-Babel and pytz:

bash
Copy code
pip install Flask-Babel pytz
Running the Application
Run the Flask App:

bash
Copy code
python3 0-app.py
Access the App:

Visit http://127.0.0.1:5000/ in your web browser. The application will display the content based on the inferred locale.
