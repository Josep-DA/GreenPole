# Import the urls / pages and Blueprint
from .setup import app_setup
from .endpoints import setup_done as desktop
from .security_endpoints import setup_done as security

print(
    '*** APP | app Launch Report ***',
    security + '\n',
    desktop + '\n',
    f'The app has been seted up',
)
