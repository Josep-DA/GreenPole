# Import the urls / pages and Blueprint
from .setup import bp
from .endpoints import setup_done as desktop
from .security_endpoints import setup_done as security

print(
    '*** bp_model | Blueprint Launch Report ***',
    security + '\n',
    desktop + '\n',
    f'The blueprint for {bp.__class__.__name__} has been seted up',
)
