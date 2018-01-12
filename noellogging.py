"""
logging functions for Noel
"""
import logging

logging.basicConfig(format='%s(asctime)s %(message)s', level=logging.INFO)

def to_log(*args, **kwargs):
    ''' wrapper around long name logging.info '''
    return logging.info(*args, **kwargs)
