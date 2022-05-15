import os


class Config:

    # SQLAlchemy and DB configurations
    DB_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        'postgresql',
        os.environ.get('PGUSER'),
        os.environ.get('PGPASSWORD'),
        os.environ.get('PGHOST'),
        os.environ.get('PGPORT', 5432),
        os.environ.get('PGDATABASE')
    )

    # JWT configs
    JWT_REFRESH_SECRET = os.environ['JWT_REFRESH_SECRET']
    JWT_ACCESS_SECRET = os.environ['JWT_ACCESS_SECRET']
    HASH_SECRET = os.environ['HASH_SECRET']
