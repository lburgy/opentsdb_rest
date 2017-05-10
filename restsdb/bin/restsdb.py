import argparse


class Restsdb(object):
    def __init__():
        pass
    def run():
        pass




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Put some data to opentsdb via the rest api')
    
    parser.add_argument('-n', dest='npoints', action='store_const', help='Number of data points to generate')
    
    
    args = parser.parse_args()