def start_app(deployment: str = ''):
    from flask import url_for
    from .setups.app_setup import AppSetup
    from .setups.server_setup import ServerSetup
    from .main import bp as main_bp
    from .recherches import bp as recherches_bp
    

    # Create app
    app_setup = AppSetup('main.root')

    # Blueprints
    app_setup.register_blueprint(main_bp)

    app_setup.register_blueprint(recherches_bp)
    @app_setup.app.route('/recherches')
    def recherches():
        return app_setup.redirect(url_for('recherches.home'))


    # Create server & Link app to server
    server_setup = ServerSetup(_app_=app_setup.app)

    # Run server
    if deployment != '':
        server_setup.run_app(deploy_option=deployment)
    else:
        print('ok')
        server_setup.run_app()