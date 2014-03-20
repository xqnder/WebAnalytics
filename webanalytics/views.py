
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

@view_config( route_name='register_visits' )
def register_visits( request ):
    """
    Addressing:
    - JavaScript snippet: You should provide a JavaScript snippet that can be inserted into any webpage to notify the
    service of visits automatically. (We will give you an example of a suitable snippet.)
    - Visit duration: Your service should track the average visit duration for each page that it tracks.
    """

    visit = {
        'origin': request.GET['origin'],
        'path': request.GET['path'],
        'duration': float( request.GET['duration'] )
    }

    site = DBSession.query( Site ).filter_by( address=visit['origin'] + visit['path'] ).first()
    if not site:
        site = Site( visit['origin'], visit['path'] )
    site.count_visit( visit['duration'] )
    DBSession.add( site )

    return Response('Counted a visit to ' + visit['origin'] + visit['path'])

@view_config( route_name='test_counting', renderer='test_counting.mako' )
def test_counting( request ):
    """
    Addressing:
    - JavaScript snippet: You should provide a JavaScript snippet that can be inserted into any webpage to notify the
    service of visits automatically. (We will give you an example of a suitable snippet.)
    - Visit duration: Your service should track the average visit duration for each page that it tracks.
    """

    return { 'request': request }