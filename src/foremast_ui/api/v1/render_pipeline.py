"""Render pipeline.json configurations."""
import json

from foremast.utils import DeepChainMap, get_template


def post(pipeline_json):
    """Render pipeline.json file."""
    default_pipeline_json = json.loads(get_template('configs/pipeline.json.j2'))
    rendered = dict(DeepChainMap(pipeline_json, default_pipeline_json))
    return rendered
