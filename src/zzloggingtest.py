import logging

def main():
    logging.debug("This is a debug message")

    logging.info("This is a info message")

    logging.warning("This is a warning message")

    logging.error("This is a error message")

    logging.critical("This is a critical message")

    logging.fatal("This is a fatal message")

if __name__ == "__main__":
    
    level = logging.DEBUG
    format = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=format)

    main()