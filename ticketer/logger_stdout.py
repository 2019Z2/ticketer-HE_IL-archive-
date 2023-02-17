from .logger import logger_t
import datetime

class logger_stdout_t(logger_t):    
    """
    That class would log service informations into standard output stream. It
    use print to log all data.
    """

    def info(self, data):
        """
        This function log info level data.
        :data: Data to log
        """
        
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("INFO (" + date + "): " + str(data))


