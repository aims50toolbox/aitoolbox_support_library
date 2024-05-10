from abc import ABC, abstractmethod
import json
from .datatypes.rest_encoder import RestEncoder

class Destination(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set(self, param_name, value):
        pass

    @abstractmethod
    def get(self, param_name):
        pass
    
    
class TestDestination(Destination):
    def __init__(self, values = {}):
        self.values = values

    def set(self, param_name, value):
        self.values[param_name] = value
    
    def get(self, param_name):
        return self.values[param_name]


class RESTDestination(Destination):
    def __init__(self):
        self.values = {}
        self.single_mime = False

    def enable_single_mimetype(self,enable):
        self.single_mime = enable

    def set(self, param_name, value):
        self.values[param_name] = value

    def get(self, param_name):
        return self.values[param_name]

    def generate_response(self, handler):
        RestEncoder.encode(handler,self.values,self.single_mime)