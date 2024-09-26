# from logger import Logger


from eazylogger import Logger

logger = Logger(
    __name__,
    info_fmt="[%(levelname)s] - %(message)s (%(name)s)",
)

logger.info("Example debug with custom info_fmt")
