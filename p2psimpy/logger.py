import logging

formatter = logging.Formatter('%(name)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO, mode='w'):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file, mode=mode)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
