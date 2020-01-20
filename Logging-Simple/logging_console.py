import logging

# logging.basicConfig(level=logging.WARNING) # default set
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)



# updating the basic config to include a format
LOG_FORMAT='%(levelname)s : %(name)s : %(message)s'
logging.basicConfig(format=LOG_FORMAT,
                    level=logging.DEBUG)

logging.debug("Detailed information used for later debugging")
logging.info("This is informative message")
logging.warning("This is a Warning! message")
logging.error("oh oh something went wrong ERROR!")
logging.critical("We have a BIG problem CRITICAL!")

# another way of writting the above
# logging.log(logging.DEBUG, "using .log: Detailed information used for later debugging")
# logging.log(logging.INFO, "using .log: This is informative message")
# logging.log(logging.WARNING, "using .log: This is a Warning! message")
# logging.log(logging.ERROR, "using .log: oh oh something went wrong ERROR!")
# logging.log(logging.CRITICAL, "using .log: We have a BIG problem CRITICAL!")

# can be used into a function
def create_log(log_level, message):
    logging.log(log_level, message)