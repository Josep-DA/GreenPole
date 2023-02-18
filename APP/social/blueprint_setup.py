from flask import Blueprint, redirect, url_for, render_template
from APP.url_authenticater import redirect_back

# -------------------------------------------------------------------------- #


class BluprintSetup:
    def __init__(self, name: str, website_name: tuple):

        self.name = name

        self.bp: Blueprint = self.create_blueprint()

        self.variables: dict = self.set_variables(website_name)

        # Security

        self.SECURE_ENDPOINT = self.set_prefix('secure')

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
            return self.render_tool('device_model', add_navbar_footer=False)

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

    def add_template(self, page):
        self.variables['pages'][page] = f'{page}.html'

    def set_website_name(self, website_name):
        self.variables['website_name'] = website_name

    def get_template(self, page):
        return self.variables['pages'].get(page)

    def get_tool(self, tool):
        return self.variables['tools'].get(tool)

    def set_prefix(self, endpoint):
        return self.variables['prefix'] + endpoint

    # Templates

    def render_page(self, page: str, **kargs):
        return render_template(self.get_template(page), **kargs)

    def render_tool(self, tool: str, **kargs):
        return render_template(self.get_tool(tool), **kargs)

    # Security
    def secure_redirect(self, target: str, _bp_=True, _url_for_=True, **values):
        if _bp_:
            target = self.set_prefix(target)
            print(target)

        if _url_for_:
            target = url_for(target, **values)
            print(target)

        return redirect(redirect_back(target, url_for(self.SECURE_ENDPOINT)))
