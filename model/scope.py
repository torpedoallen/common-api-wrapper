# coding=utf8



class Scope(object):

    READ, WRITE = range(2)

    def __init__(self):
        pass

    @classmethod
    def scope_urls(cls, scope):
        return []

    @classmethod
    def url_scopes(cls, url):
        return []



class ScopeValidationMixin(object):
    '''
    {
        'apikey1': [write, read],
        'apikey2': [read],
    }

    http://a/b/c -> requires write scope
    usage: validate if one apikey has the right to access to some url
    '''

    @classmethod
    def validate_scope(cls, key, url):
        return True

