from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your secret key'
    
    return app

if __name__ == '__main__':
    create_app().run(debug=True)