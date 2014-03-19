
from pyramid.view import view_config
from pyramid.response import Response

from .models import (
    DBSession,
    Site,
    )


@view_config(route_name='view_sites', renderer='templates/sites.pt')
def view_sites(request):
    """
    "listing the identifier numbers of visited sites and the number of visits to each site."
    """

    sites = DBSession.query( Site ).all()

    return {
        'sites': sites
    }

@view_config( route_name='increment_count' )
def increment_count( request ):
    """
    "/sites/123/visits registers a visit to site 123."
    """

    sitename = request.matchdict['sitename']
    site = DBSession.query( Site ).filter_by( name=sitename ).first()
    if site:
        # we are already tracking this site, just increment the counter:
        site.visits += 1
    else:
        # we should add a new Site object
        site = Site( name=sitename, visits=1 )
        DBSession.add( site )

    return Response('Counted a visit to ' + sitename)