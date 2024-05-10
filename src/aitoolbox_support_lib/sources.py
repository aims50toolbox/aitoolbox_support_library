from abc import ABC, abstractmethod
import json
from .datatypes.rest_decoder import RestDecoder


class Sources(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set(self, param_name, value):
        pass

    @abstractmethod
    def get(self, param_name):
        pass

    @abstractmethod
    def to_dict(self):
        pass
    
    
class TestSources(Sources):
    def __init__(self, values = {}):
        self.values = values

    def set(self, param_name, value):
        self.values[param_name] = value
    
    def get(self, param_name):
        return self.values[param_name]

    def to_dict(self):
        return self.values

class RESTSources(Sources):
    def __init__(self, req):
        self.d = RestDecoder.decode(req)

    def set(self, param_name, value):
        self.d[param_name] = value

    def get(self, param_name):
        return self.d[param_name]
    
    def to_dict(self):
        return self.d

    def __str__(self):
        return "\n".join((f"{k}: {v} [{type(v)}]" for k,v in self.d.items()))

