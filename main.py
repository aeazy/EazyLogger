# from logger import Logger


from eazylogger import Logger

logger = Logger(__name__)

logger.debug("Example debug message")
logger.info("Example info message")
logger.warn("Example warning message")
logger.error("Example error message")
logger.critical("Example critical message")
logger.success("Example success message")
