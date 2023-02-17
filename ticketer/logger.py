class logger_t():
    """
    This class is useable to injection logger into dependent class. This can
    save log information to place prepare with child class.
    """
    
    def info(self, data):
        """
        This function is useable to log info level informations.
        :data: Data to log
        """

        raise NotImplementedError()


