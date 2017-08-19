"""Main application."""
import connexion


APP = connexion.App(__package__, specification_dir='openapi')
APP.add_api('v1.yml', resolver=connexion.resolver.RestyResolver('.'.join([__package__, 'api.v1'])))
