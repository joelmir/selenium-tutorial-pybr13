from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, DateTime, text
import parameter

class Scope(object):

    def __init__(self):
        self._current_scope = None

    def set(self, scope):
        self._current_scope = scope

    def get(self):
        return self._current_scope
        
'''
    TODO - move DB configurations to a settings file / use var envs
'''
db_pass = 'localpass'
db_host = 'localhost'
db_name = 'selenium_tutorial'
db_user = 'selenium_tutorial'

scope = Scope()        
session = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=True,
                                 expire_on_commit=False,
                                 bind=create_engine('postgresql://{0}:{1}@{2}/{3}'.format(db_user, db_pass, db_host, db_name))),
                                 scopefunc=scope.get)

Base = declarative_base()
Base.query = session.query_property()