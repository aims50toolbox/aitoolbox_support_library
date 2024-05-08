import json

from base64 import b64decode
import imageio
import numpy

class RestEncoder():
    def encode(kvps):
        j = { k: RestEncoder.encode_argument(v) for k,v in kvps.items() }
        return json.dumps(j)

    def encode_argument(arg):
        if isinstance(arg, (int, float, complex, str)):
            return arg
        
        if isinstance(arg, numpy.ndarray):
            return arg.tolist()

        return arg
    