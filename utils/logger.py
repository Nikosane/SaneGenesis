import logging

class Logger:
    def __init__(self, log_file="simulation.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger()

    def log(self, message, level="info"):
        """Logs a message with the given severity level."""
        if level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        else:
            self.logger.info(message)

    def log_event(self, event):
        """Logs a structured event."""
        self.logger.info(f"EVENT: {event}")
