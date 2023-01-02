import os
from peewee import Model, PostgresqlDatabase
DBN = 'DATA_BASE_NAME'
DBU = 'DATA_BASE_USER'
DBP = 'DATA_BASE_PASS'
DBH = 'DATA_BASE_HOST'
DBPO = 'DATA_BASE_PORT'

pg_db = PostgresqlDatabase(
    os.getenv(DBN),
    user=os.getenv(DBU),
    password=os.getenv(DBP),
    host=os.getenv(DBH),
    port=int(os.getenv(DBPO))
)


class BaseModel(Model):
    class Meta:
        database = pg_db