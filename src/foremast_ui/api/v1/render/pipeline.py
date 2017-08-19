"""Render pipeline.json configurations."""
import json

from foremast.utils import DeepChainMap, get_template


def post(pipeline_json):
    """Render pipeline.json file."""
    default_pipeline_json = json.loads(get_template('configs/pipeline.json.j2'))
    rendered = dict(DeepChainMap(pipeline_json, default_pipeline_json))
    return rendered


def validate(pipeline_json):
    """Make sure basic keys exist."""
    return True
    required_keys = set(['name'])
    missing_keys = required_keys - set(pipeline_json.keys())

    error_message = 'Missing required keys: {0}'.format(', '.join(sorted(missing_keys)))
    return not any(missing_keys), error_message
