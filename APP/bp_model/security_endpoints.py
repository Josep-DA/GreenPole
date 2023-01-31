from flask import request
from user_agents import parse
from .setup import bp, secure_redirect, render_tool


# Security

@bp.route('/secure')
def secure():
    return render_tool('secure')

@bp.route('/model_appareil')
def check():
    ua_string = request.args.get("user_agent")
    print(ua_string)

    user_agent = parse(ua_string)

    # Computer
    if user_agent.is_pc:
        return secure_redirect(target='acceuil')

    # Tablet
    elif user_agent.is_tablet:
        print('tablet link')

    # Phone
    elif user_agent.is_mobile:
        print('mobile link')

    else:
        secure_redirect('secure')


setup_done = "**//IMPORTANT//** -- All security endpoints have been setted! ECODE: SECU-001!"