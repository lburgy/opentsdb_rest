import json
from dataconst import DataConst, DefaultConst


class Pointsdb(object):
    """
    Single Data Point definition model.
    """
    
    def __init__(self, metric, value, timestamp, **kwargs):
        self.metric = metric
        self.timestamp = timestamp
        self.tags = kwargs
        self.value = value
        
    def to_json(self):
        return json.dumps(self.__dict__)
    
    