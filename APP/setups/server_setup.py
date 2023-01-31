from flask import Flask

class InvalidDeploymentRequest(Exception):
    """Raised when the deployment request is not in the ID_CODE deployment list

    Attributes:
        deploy_option - - input deployment option which caused the error
        message - - explanation of the error

    """

    def __init__(self, deploy_option, message="** Invalid request for deployment **"):
        self.deploy_option = deploy_option
        self.message = message
        super().__init__(self.message)
        


class ServerSetup:
    def __init__(self, _app_: Flask, port: int = 8080, host: str = '0.0.0.0', debug: bool = True):
        
        self.DEPLOYMENT_CODE = {'PRODUCTION': self.deploy_production, 'TEST': self.deploy_test}

        self.variables = {
            "port": port,
            "host": host,
            "debug": debug
        }

        self.app = _app_
    
    def run_app(self, deploy_option='TEST'):
        if self.app is not None:    
            try:
                if self.DEPLOYMENT_CODE.get(deploy_option) is None:
                    raise InvalidDeploymentRequest(deploy_option)
                else:
                    self.DEPLOYMENT_CODE.get(deploy_option)(
                        action=str(
                            print(f"The app was lunched as TEST at 'http://192.168.0.129:{self.variables['port']}' | 'http://127.0.0.1:{self.variables['port']}'.")),
                    )
        
            except TypeError:
                self.DEPLOYMENT_CODE.get(deploy_option)(
                    action=str(
                        print(f"The app was lunched as PRODUCTION at 'http://192.168.0.129:{self.variables['port']}' | 'http://127.0.0.1:{self.variables['port']}'."))
                )
    
    def deploy_production(self, action=None):
        if action is not None:
            exec(action)
    
        from gevent.pywsgi import WSGIServer
    
        http_server = WSGIServer(
            (self.variables.get('host'), self.variables.get('port')),
            self.app
        )

        http_server.serve_forever()
    
    def deploy_test(self, action=None):
        if action is not None:
            exec(action)
    
        self.app.run(
            debug=self.variables.get('debug'),
            host=self.variables.get('host'),
            port=self.variables.get('port')
        )

    