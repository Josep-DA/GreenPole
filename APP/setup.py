def start_app(deployment: str = ''):
    from .setups.app_setup import AppSetup
    from .setups.server_setup import ServerSetup
    from .main import bp as main_bp

    # Create app
    app_setup = AppSetup('main.root')

    # Blueprints
    app_setup.register_blueprint(main_bp)


    # Create server & Link app to server
    server_setup = ServerSetup(_app_=app_setup.app)

    # Run server
    if deployment != '':
        server_setup.run_app(deploy_option=deployment)
    else:
        print('ok')
        server_setup.run_app()