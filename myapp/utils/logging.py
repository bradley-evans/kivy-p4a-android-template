import logging
import os


def log_generator(name, loglevel='DEBUG'):
    
    logger = logging.getLogger('myapp | ' + name)
    
    # Create handlers
    c_handler = logging.StreamHandler() # STDOUT Handler
    # f_handler = logging.FileHandler(logfile) # logfile handler
    c_handler.setLevel(loglevel)
    # f_handler.setLevel(loglevel)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    # f_format = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    c_handler.setFormatter(c_format)
    # f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    # logger.addHandler(f_handler)

    logger.setLevel(logging.DEBUG)

    return logger


logger = log_generator(__name__)
