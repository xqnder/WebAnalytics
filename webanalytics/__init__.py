from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.include('pyramid_mako')

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('view_sites', '/sites')
    config.add_route('register_visits', '/visits')
    config.add_route('test_counting', '/test_counting/*params')
    # config.add_route('test_counting', '/test_counting/{a}')
    # config.add_route('test_counting', '/test_counting/{a}/{b}')
    # config.add_route('test_counting', '/test_counting/{a}/{b}/{c}')

    config.scan()

    return config.make_wsgi_app()
