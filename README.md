# Environment
Create a ``.env`` and then set:
* ``SECRET_KEY`` (see ``django.core.management.utils.get_random_secret_key``)
* ``ALLOWED_HOSTS``

# Development
Set ``DEBUG=True`` in ``.env``

Run:
``docker compose -f docker-compose.dev.yml up -d --build``

# Production
Set ``DEBUG=False`` in ``.env``

If you set ``DEMO=True``, it will run with SQLite and you need to set ``DATABASE_PATH=/db/db.sqlite3``.

Else, it'll run Postgres, and you'll need to set its env variables, check ``mcfatter/settings.py``.

Run:
``docker compose -f docker-compose.yml up -d --build``
