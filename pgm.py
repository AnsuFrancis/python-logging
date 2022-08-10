import logging
#logging.basicConfig(filename='logs.log', level=logging.INFO)
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger.warn('Hey log a warning')
logger.error("Hey log a error")


'''import logging.handlers
logger = logging.getLogger('Synchronous Logging')
http_handler = logging.handlers.HTTPHandler(
    '127.0.0.1:3000',
    '/log',
    method='POST',
)
logger.addHandler(http_handler)'''
