"""Run Foremast web UI."""
import click
from gunicorn.app.wsgiapp import WSGIApplication

from .application import API


class CustomApplication(WSGIApplication):
    def __init__(self, app, options=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.callable = app
        self.options = options or {}

    def load_config(self):
        pass


@click.command()
@click.option('-d', '--debug', is_flag=True, help='Enable DEBUG mode')
@click.option('-p', '--port', type=int, help='Port to run webserver')
def main(debug, port):
    """Foremast UI entry point."""
    app = CustomApplication(API, options=None, usage=__package__, prog=__package__)
    app.run()


if __name__ == '__main__':
    main()
