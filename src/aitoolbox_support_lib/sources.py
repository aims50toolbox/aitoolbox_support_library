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
    
    
class TestSources(Sources):
    def __init__(self, values = {}):
        self.values = values

    def set(self, param_name, value):
        self.values[param_name] = value
    
    def get(self, param_name):
        return self.values[param_name]


class RESTSources(Sources):
    def __init__(self, req):
        self.req = RestDecoder.decode(req)

    def set(self, param_name, value):
        self.req[param_name] = value

    def get(self, param_name):
        return self.req[param_name]
    
    def __str__(self):
        return "\n".join((f"{k}: {v}" for k,v in self.req.items()))

