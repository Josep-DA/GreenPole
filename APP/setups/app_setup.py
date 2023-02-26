from flask import Flask, Blueprint
from ..url_manager import UrlManager


class AppSetup(UrlManager):
    def __init__(self, website_name: tuple):
        self.name = 'app'

        self.login_manager = None
        self.db = None

        self.app: Flask = self.create_app()

        self.variables: dict = self.set_variables(website_name)

        super().__init__()
    
    def create_app(self):        
        app = Flask(__name__)
        return app

    def create_root(self):
        @self.app.route('/')
        def root():
            return self.render_tool('device_model', add_navbar_footer=False, redirect_back_to='home')

    def set_variables(self, website_name):
        variables = {
            'pages': {
                'home': 'app/home.html',
            },
            'tools': {
                'secure': 'tools/secure.html',
                'device_model': 'tools/device_model.html',
            },
            'prefix': '',
            'website_name': website_name
        }

        return variables

    def register_blueprint(self, bp: Blueprint):
        if self.app:
            self.app.register_blueprint(bp)