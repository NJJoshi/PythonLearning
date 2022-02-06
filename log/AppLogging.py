from datetime import datetime


class ApplicationLogging:

    def __init__(self):
        self.now = None
        self.date = None
        self.current_time = None

    def log_info(self, file_obj, log_msg):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_obj.write(
            str(self.date) + ':' + self.current_time + 'INFO-' + '\t\t' + log_msg + '\n'
        )

    def log_error(self, file_obj, log_msg):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_obj.write(
            str(self.date) + ':' + self.current_time + 'ERROR-' + '\t\t' + log_msg + '\n'
        )