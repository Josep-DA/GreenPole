# Import the urls / pages and Blueprint
from .setup import bp
from .endpoints import setup_done as desktop

print(
    '*** Main | Blueprint Launch Report ***',
    desktop + '\n',
    f'The blueprint for {bp.__class__.__name__} has been seted up',
)
