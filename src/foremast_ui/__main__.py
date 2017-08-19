"""Run Foremast web UI."""
import click

from .application import APP


@click.command()
@click.option('-d', '--debug', is_flag=True, help='Enable DEBUG mode')
@click.option('-p', '--port', type=int, help='Port to run webserver')
def main(debug, port):
    """Foremast UI entry point."""
    APP.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
