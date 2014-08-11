# coding=utf8

import json
import requests


class Client(object):
    """
    A class that has all the logic for communicating with Trello and returning
    information to the user
    """

    def __init__(self, api_key, user_auth_token=None):
        self.api_key = api_key
        self.user_auth_token = user_auth_token
        self._client = requests.api

    def add_authorisation(self, query_params):
        query_params['key'] = self.api_key

        if self.user_auth_token:
            query_params['token'] = self.user_auth_token

        return query_params

    def clean_path(self, path):
        """
        Ensure the path has a preceding /
        """
        if path[0] != '/':
            path = '/' + path
        return path

    #def check_errors(self, uri, response):
    #    """
    #    Check HTTP reponse for known errors
    #    """
    #    if response.status == 401:
    #        raise Unauthorised(uri, response)

    #    if response.status != 200:
    #        raise ResourceUnavailable(uri, response)

    def get(self, uri, query_params=None, headers=None):
        return self._fetch_json(uri, http_method='GET', query_params=query_params, headers=headers)

    def post(self, uri, query_params=None, body=None, headers=None):
        return self._fetch_json(uri, http_method='POST', query_params=query_params, body=body, headers=headers)

    def delete(self, uri, query_params=None, headers=None):
        return self._fetch_json(uri, http_method='DELETE', query_params=query_params, headers=headers)

    def put(self, uri, query_params=None, headers=None):
        return self._fetch_json(uri, http_method='PUT', query_params=query_params, headers=headers)

    def patch(self, uri, query_params=None, body=None, headers=None):
        return self._fetch_json(uri, http_method='POST', query_params=query_params, body=body, headers=headers)


    def _fetch_json(self, uri, http_method='GET', query_params=None, body=None, headers=None):
        query_params = query_params or {}
        headers = headers or {}

        query_params = self.add_authorisation(query_params)

        if http_method in ("POST", "PUT", "DELETE", "PATCH") and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        headers['Accept'] = 'application/json'
        response = self._client.request(
            url=uri,
            method=http_method,
            params=query_params,
            data=body,
            headers=headers,
        )

        #self.check_errors(uri, response)

        return response.content.encode('utf8')




