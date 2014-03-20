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
    parent_address = Column( Text, default='' )

    visits = Column( Integer, default=0 )
    total_visit_time = Column( Float, default=0.0 )
    child_visits = Column( Integer, default=0 )
    total_child_visit_time = Column( Float, default=0.0 )

    def __init__( self, origin, pathname ):
        self.address = origin + pathname
        self.parent_address = ''

        self.visits = 0
        self.child_visits = 0
        self.total_visit_time = 0.0
        self.total_child_visit_time = 0.0

        if pathname:
            self.parent_address = origin + pathname.rsplit( '/', 1)[0]
            parent = DBSession.query( Site ).filter_by( address=self.parent_address ).first()
            if not parent:
                parent = Site( origin, pathname.rsplit( '/', 1)[0] )
                DBSession.add( parent )

    def count_visit( self, total_visit_time ):

        self.visits += 1
        self.total_visit_time += total_visit_time
        if self.parent_address:
            parent = DBSession.query( Site ).filter_by( address=self.parent_address ).first()
            parent.count_child_visit( total_visit_time )

    def count_child_visit(self, total_visit_time ):
        self.child_visits += 1
        self.total_child_visit_time += total_visit_time
        if self.parent_address:
            parent = DBSession.query( Site ).filter_by( address=self.parent_address ).first()
            parent.count_child_visit( total_visit_time )

    def __str__( self ):
        return 'ID: ' + str( self.id ) + '\tName: ' + self.address + '\tNumber of visits: ' + str( self.visits )