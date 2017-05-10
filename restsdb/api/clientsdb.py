from conftsdb import ConfTsdb
import request




class Clientsdb(object):
    
    @staticmethod
    def put():
        """
        Put a point or a list of points to an opentsdb database.
        """
        request.post()