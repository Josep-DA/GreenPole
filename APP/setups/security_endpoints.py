from flask import request
from user_agents import parse
from .setup import app, secure_redirect, render_tool, WEBSITE_NAME


# Security

@app.route('/secure')
def secure():
    return render_tool('secure', website_name=WEBSITE_NAME, add_navbar_footer=True, page_title="Secure")

@app.route('/device_model')
def check():
    ua_string = request.args.get("user_agent")
    print(ua_string)

    user_agent = parse(ua_string)
    print(user_agent)


    # Computer
    if user_agent.is_pc:
        return secure_redirect(target='home', _bp_=False)

    # Tablet
    elif user_agent.is_tablet:
        print('tablet link')

    # Phone
    elif user_agent.is_mobile:
        print('mobile link')

    else:
        secure_redirect(target='secure', _bp_=False)


setup_done = "**//IMPORTANT//** -- All security endpoints have been setted! ECODE: SECU-001!"