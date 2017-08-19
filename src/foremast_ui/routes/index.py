"""Site root."""
import flask

from ..api.v1.render_application import post
from ..application import APP


@APP.route('/')
def index():
    """Serve index page."""
    default_application_json = post('test', 'group/project', {})

    rendered = flask.render_template('index.html.j2', application_json=default_application_json)

    return rendered
