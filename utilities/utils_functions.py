import logging


class GenerateLog:
    @staticmethod
    def generate_log():
        logger = logging.getLogger()
        logger.handlers.clear()
        try:
            file_handler = logging.FileHandler(filename=".//Logs//Automation.log", mode='a')
        except FileNotFoundError:
            file_handler = logging.FileHandler(filename="../Logs/Automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
