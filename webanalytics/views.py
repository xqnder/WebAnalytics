
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
    "/sites/123/visits registers a visit to site 123."
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