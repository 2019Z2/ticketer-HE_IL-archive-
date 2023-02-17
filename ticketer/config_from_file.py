from .config import config_t
import json

class config_from_file_t(config_t):
    """
    That child class is useable to injection config from json to class that
    dependent on config class.
    """

    def __init__(self, config_filename):
        """
        This function create config from file, that must be json file.
        :config_filename: JSON config file name
        """

        with open(config_filename) as file:
            super(config_from_file_t, self).__init__(json.load(file))


