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
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('search_result', '/search_result')
    config.add_route('login', '/login')
    config.add_route('register', '/register')
    config.add_route('history', '/history')
    config.add_route('top3', '/top3')
    config.scan()
    return config.make_wsgi_app()
