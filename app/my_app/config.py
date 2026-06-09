class config(object):
    pass
class config(object):
    pass

class ProdConfig(config):
    # SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://localhost\SQLEXPRESS/CursoFlask?driver=SQL+Server&trusted_connection=yes"
    pass
class DevConfig(config):
#  DEBUG = True
    SQLALCHEMY_DATABASE_URI = r"mssql+pyodbc://localhost\SQLEXPRESS/CursoFlask?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
#El debug nos ayudo a editar mientras 
# esta corriendo el proyecto