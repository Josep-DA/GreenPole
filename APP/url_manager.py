from flask import redirect, url_for, render_template
from APP.url_authenticater import redirect_back

class UrlManager:
    def __init__(self):
        self.redirect_back = redirect_back

        self.render_template = render_template

        self.url_for = url_for
        
        self.redirect = redirect

        # Security

        self.SECURE_ENDPOINT = 'secure'

    def add_template(self, page):
        self.variables['pages'][page] = f'{self.name}/{page}.html'

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
        return self.render_template(self.get_template(page), **kargs)

    def render_tool(self, tool: str, **kargs):
        return self.render_template(self.get_tool(tool), **kargs)

    # Security
    def secure_redirect(self, target: str, _bp_=True, _url_for_=True, **values):
        if _bp_:
            target = self.set_prefix(target)
            print(target)

        if _url_for_:
            target = self.url_for(target, **values)
            print(target)

        return self.redirect(self.redirect_back(target, self.url_for(self.SECURE_ENDPOINT)))