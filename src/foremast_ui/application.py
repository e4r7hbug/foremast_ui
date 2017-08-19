"""Main application."""
import connexion
from pkg_resources import get_distribution

APP = connexion.App(
    __package__, specification_dir='openapi', arguments={
        'foremast_version': get_distribution('foremast').version,
    })
APP.add_api('v1.yml', resolver=connexion.resolver.RestyResolver('.'.join([__package__, 'api.v1'])))
