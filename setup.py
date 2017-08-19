"""Install Foremast Lathe."""
from setuptools import find_packages, setup

with open('README.rst') as readme_handle:
    LONG_DESCRIPTION = readme_handle.read()

setup(
    name='foremast ui',
    description='Foremast configuration generator web UI.',
    long_description=LONG_DESCRIPTION,
    author='',
    author_email='',
    install_requires=[
        'click',
        'connexion',
        'foremast',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    use_scm_version={'local_scheme': 'dirty-tag'},
    entry_points={
        'console_scripts': [
            'foremast_ui=foremast_ui.__main__:main',
        ],
    }, )
