import logging

# Disable logging: to re-enable, comment it out
logging.disable(logging.CRITICAL)

# Try with logging.INFO, logging.WARNING, etc
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')

logging.debug('Test for debug')
logging.info('Test for info')
logging.warning('Test for warning')
logging.error('Test for error')
logging.critical('Test for critical')

