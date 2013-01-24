import json, yaml

class YAMLy(object):
    def __init__(self, yaml):
        self.o = yaml
    
    def __getattr__(self, name):
        return YAMLy(self.o[name])
    
    def __repr__(self):
        return json.dumps(self.o)

def load(doc):
    # yea boy
    # this is the reason for this lib
    return YAMLy(yaml.load(doc))

def dump(obj):
    if type(obj) is YAMLy:
        return yaml.dump(obj.o, default_flow_style=False)
    else:
        raise TypeError
