
import mylogging
#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.basicConfig(format='%(asctime)s-%(levelname)s:%(message)s', level=logging.DEBUG)
mylogging.logging.debug('This message should go to the log file')
mylogging.logging.info('So should this')
mylogging.logging.warning('And this, too')
