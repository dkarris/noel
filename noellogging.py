"""
logging functions for Noel
"""
import logging

LOG_FILE_NAME = 'log.log'
DEBUG_PRINT = True

def to_log(*args):
    ''' wrapper around long name logging.info '''
    if DEBUG_PRINT:
        print (args)
    return logging.info(args)


logging.basicConfig(format='%(asctime)s %(message)s',
                    filename=LOG_FILE_NAME, level=logging.INFO)
