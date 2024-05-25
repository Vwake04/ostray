import logging

class Logger:
    def __init__(self, log_file: str):
        logging.basicConfig(level=logging.INFO, filename=log_file, filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger("LeadProcessingLogger")

    def log(self, message: str):
        self.logger.info(message)