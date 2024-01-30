import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('test_logger') #can be named anything, reachable from other files usually: __name__ or appname -- appname.subfile, etc
logger.info('Info level')
logger.warning('This is a warning.')
logger.debug('This will be a debug message.')
logger.critical('Critical error. Please help.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""