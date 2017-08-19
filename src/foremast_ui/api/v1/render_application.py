"""Render application.json configuration."""
import json

import gogoutils
from foremast.consts import APP_FORMATS
from foremast.utils import DeepChainMap, get_template


def post(env, git_uri, application_json):
    """Render application.json."""
    generated = gogoutils.Generator(*gogoutils.Parser(git_uri).parse_url(), formats=APP_FORMATS)

    app_name = generated.app_name()
    profile = generated.iam()['profile']

    rendered_template = json.loads(get_template('configs/configs.json.j2', env=env, app=app_name, profile=profile))
    rendered = dict(DeepChainMap(application_json, rendered_template))
    return rendered
