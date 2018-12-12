import os
import logzero,logging

class log :

    def __init__(self) :
        self.logfile = os.path.join(os.getcwd() ,'test.log')
        logzero.logfile(self.logfile, maxBytes = 1e6, backupCount = 3)
        formatter = logging.Formatter('%(asctime)-15s - [%(filename)s: %(lineno)s] -%(levelname)s: %(message)s');
        logzero.formatter(formatter)
        logzero.loglevel(logging.INFO)
        self.logger = logzero.logger


if __name__ == '__main__':
    # input("You can not run main!")
    print(log().logfile)
    log().logger.info("test log start :")
    log().logger.error("test log error : this is en error message!")
    log().logger.info("test log end :")


