
from pyramid.view import view_config
from pyramid.response import Response

from .models import DBSession, Site


@view_config( route_name='view_sites', renderer='sites.mako' )
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
    "/sites/123/visits registers a visit to site 123." - Phase 1
    """

    site_address = request.matchdict['address']
    site = DBSession.query( Site ).filter_by( address=site_address ).first()
    if site:
        # we are already tracking this site, just increment the counter:
        site.visits += 1
    else:
        # we should add a new Site object
        site = Site( site_address, 1, 0 )
        DBSession.add( site )

    return Response('Counted a visit to ' + site_address)

@view_config( route_name='register_visits' )
def register_visits( request ):
    """
    Addressing:
    - JavaScript snippet: You should provide a JavaScript snippet that can be inserted into any webpage to notify the
    service of visits automatically. (We will give you an example of a suitable snippet.)
    - Visit duration: Your service should track the average visit duration for each page that it tracks.
    """

    visit = request.GET['visit']
    site = DBSession.query( Site ).filter_by( address=visit ).first()
    if site:
        # we are already tracking this site, just increment the counter:
        site.visits += 1
    else:
        # we should add a new Site object
        site = Site( visit, 1, 0 )
        DBSession.add( site )

    return Response('Counted a visit to ' + visit)

@view_config( route_name='test_counting', renderer='test_counting.mako' )
def test_counting( request ):
    """
    Addressing:
    - JavaScript snippet: You should provide a JavaScript snippet that can be inserted into any webpage to notify the
    service of visits automatically. (We will give you an example of a suitable snippet.)
    - Visit duration: Your service should track the average visit duration for each page that it tracks.
    """

    return {}