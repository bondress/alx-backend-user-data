#!/usr/bin/env python3
"""This is the Authentication Module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """This is the Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Auth function_
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if path[:p.find('*')] in p[:p.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header function
        """
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None

    def session_cookie(self, request=None):
        """ Session Cookie Function
        Return a cooke value from a request
        """
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
