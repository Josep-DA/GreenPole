from flask import Flask, url_for, redirect, Blueprint


class AppSetup:
    def __init__(self, first_redirect: str = ""):
        
        self.app: Flask = self.create_app(first_redirect)

        self.variables: dict = self.set_variables()
    
    def create_app(self, first_redirect: str = ""):
        from .config import Config as config_object
        
        app = Flask(__name__)
        app.config.from_object(config_object)

        @app.route('/')
        def root():
            if first_redirect:
                return redirect(url_for(first_redirect))
            else:
                return "hello world" #redirect(url_for('main.root'))
    
        return app

    def set_variables(self):
        variables = {}
        return variables

    def register_blueprint(self, bp: Blueprint):
        if self.app:
            self.app.register_blueprint(bp)