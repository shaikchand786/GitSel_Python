import inspect
import logging

class baseclass():
    def getLogger(self):
        #How to add exact file name in output log
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        logger = logging.getLogger(__name__)  #__name__ = if you write this, then in runtime it take filename automatically
        #where to print
        fileHandler = logging.FileHandler("logfile.log") #By using it, we know exactly where the file location with the help of parent(logging)

        #format for log
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        #While level of logging show you want to print in console
        logger.setLevel(logging.DEBUG)

        return logger