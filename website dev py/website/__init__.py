from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ijsadbuasd89235421b316v3'

    from .views import views
    from .auth import auth
    
    # if you have more pre_fixes you can add them below
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    

    return app
