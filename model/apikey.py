# coding=utf8


from model.scope import ScopeValidationMixin
from model.authority import AuthorityBit


class APIKey(ScopeValidationMixin):

    def __init__(self, key):
        self.key = key


    @classmethod
    def load(cls, key):
        return ''


    @classmethod
    def create(cls, key):
        return ''


    @property
    def bits(self):
        return AuthrityBit.get_by_key(self.key)
