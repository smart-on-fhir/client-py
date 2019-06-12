#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware


class FlaskBeaker(SessionInterface):
    """ Beaker session interface class for Beaker sessions in Flask apps.
    Stolen from http://flask.pocoo.org/snippets/121/ (public domain)
    """
    @classmethod
    def setup_app(cls, app, session_opts=None):
        if session_opts is None:
            session_opts = {
                'session.type': 'file',
                'session.timeout': 3600,
                'session.cookie_expires': 3600,
                'session.data_dir': './session_data',
                'session.auto': True
            }
        
        app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
        app.session_interface = cls()
    
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session
    
    def save_session(self, app, session, response):
        session.save()
