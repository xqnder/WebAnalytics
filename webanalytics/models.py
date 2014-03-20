from sqlalchemy import Column, Index, Integer, Text, Float

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
    address = Column( Text, unique=True )
    visits = Column( Integer, default=0 )
    total_visit_time = Column( Float, default=0.0 )
    child_visits = Column( Integer, default=0 )
    total_child_visit_time = Column( Float, default=0.0 )

    def __init__( self, address, visits, total_visit_time ):
        self.address = address
        self.visits = visits
        self.total_visit_time = total_visit_time

    def __str__( self ):
        return 'ID: ' + str( self.id ) + '\tName: ' + self.address + '\tNumber of visits: ' + str( self.visits )