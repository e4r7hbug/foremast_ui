"""Site root."""
from ..application import APP


@APP.route('/')
def index():
    """Serve index page."""
    return 'This is a test'
