import logging
logger = logging.getLogger(__name__)
tlogger = logging.getLogger('tlog')

def example():
    logger.info("Logger inside example function.")
    tlogger.info("Tlogger also inside example function.")