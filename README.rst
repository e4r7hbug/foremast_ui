===========
Foremast UI
===========

Web application for generating Foremast configurations.

Install
-------

.. code-block:: bash

   pip install .


Running
-------

OpenAPI is available at http://127.0.0.1:8000/v1/ui/ after running with
`gunicorn`.

.. code-block:: bash

   gunicorn foremast_ui.application:API
