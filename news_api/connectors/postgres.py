import psycopg2
from news_api.settings.db_entity import  db_ip,db_passw,db_port,db_user,db_logs_path
import logzero

logzero.logfile(db_logs_path+"db_ents.log", maxBytes=1e6, backupCount=3)


class Postgres(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            # normally the db_credenials would be fetched from a config file or the enviroment
            # meaning shouldn't be hardcoded as follow
            db_config = "host={} user={} password={} port={}".format(db_ip, db_user, db_passw,db_port)

            try:
                print('connecting to PostgreSQL database...')
                cls._instance.connection =  psycopg2.connect(db_config)
                cls._instance.cursor = Postgres._instance.cursor =  cls._instance.connection.cursor()
                cls._instance.cursor.execute('SELECT VERSION()')
                db_version =  cls._instance.cursor.fetchone()

            except Exception as error:
                print('Error: connection not established {}'.format(error))
                Postgres._instance = None

            else:
                print('connection established\n{}'.format(db_version[0]))

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def query(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.connection.close()
        self.cursor.close()