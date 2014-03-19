from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Site( Base ):
    """ The SQLAlchemy declarative model class for a Site object. """
    __tablename__ = 'sites'
    id = Column( Integer, primary_key=True )
    name = Column( Text, unique=True )
    visits = Column( Integer, default=0 )

    def __init__( self, name, data ):
        self.name = name
        self.data = data