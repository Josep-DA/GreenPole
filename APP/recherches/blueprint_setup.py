from flask import Blueprint
from ..url_manager import UrlManager

class BluprintSetup(UrlManager):
    def __init__(self, name: str, website_name: tuple):
        self.name = name

        self.bp: Blueprint = self.create_blueprint()

        self.variables: dict = self.set_variables(website_name)

        super().__init__()

    def create_blueprint(self):
        bp = Blueprint(
            self.name,
            __name__,
            url_prefix=f'/{self.name}',
            static_folder=f'static/{self.name}',
            template_folder=f'templates/{self.name}'
        )

        @bp.route('/')
        def root():
            return self.render_tool('device_model', add_navbar_footer=False, rediract_back_to=self.url_for('recherches.home'))

        return bp

    def set_variables(self, website_name):

        variables = {
            'pages': {
                'home': 'home.html',
            },
            'tools': {
                'secure': 'tools/secure.html',
                'device_model': 'tools/device_model.html',
            },
            'prefix': f'{self.name}.',
            'website_name': website_name
        }

        return variables
