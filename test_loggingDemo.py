import logging
def test_loggingCodeDemo():
    logger = logging.getLogger()  #__name__ = if you write this, then in runtime it take filename automatically
    #where to print
    fileHeadler = logging.FileHandler("logfile.log") #By using it, we know exactly where the file location with the help of parent(logging)

    #format for log
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHeadler.setFormatter(formatter)
    logger.addHandler(fileHeadler)
    #While level of logging show you want to print in console
    logger.setLevel(logging.INFO)

    #what to print (Levels in logging)
    logger.debug("Debug level of logging")
    logger.info("Basic Information")
    logger.warning("Waring just show some bug in code but it doesn't stop to run")
    logger.error("Error in test codes")
    logger.critical("Critical mode")