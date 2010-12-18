# -*- coding: utf-8 -*-
from elixir import *

metadata.bind = "sqlite:///samples.sqlite"
metadata.bind.echo = False

cleanup_all()



def get_or_create(cls, if_new_set={}, **params):
    """Call get_by; if no object is returned, initialize an
    object with the same parameters.  If a new object was
    created, set any initial values."""
    
    result = cls.get_by(**params)
    if not result:
        result = cls(**params)
        result.set(**if_new_set)
    return result

Entity.get_or_create = classmethod(get_or_create)

class Device(Entity):

    name = Field(Unicode(100))
    samples = OneToMany('Sample')

    def __repr__(self):
        return ('<Device %s>' % self.name).encode('utf8')

    @staticmethod
    def get_by_name(n):
        return Device.get_or_create(name=n)
             

class Sample(Entity):

    device = ManyToOne('Device')
    ts = Field(Integer, index=True)
    long = Field(Float, index=True)
    lat = Field(Float, index=True)
    
    def __repr__(self):
        return u'<%s sample %f %f>' % (self.self.title, self.year)


setup_all(True)

