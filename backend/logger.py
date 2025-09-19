import logging


def setup_logger(name="AI-Healthcare-Assistant"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler=logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]")
    console_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    return logger


logger=setup_logger()