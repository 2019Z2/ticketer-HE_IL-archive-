class config_t():
    """
    This class is abstract class for store config and injection it to other
    class, from others sources.
    """

    def __init__(self, config):
        """
        This function create config from dict. It would be call with super
        construction, from child class init.
        :config: Config dict
        """

        if type(config) is not dict:
            raise Exception("Given config is not dict!")

        self.config = config


    def get(self, key):
        """
        This function would be used to get config from config dict. It return
        config value as string, or information that is not definiec, if key
        not found in config.
        :key: Key to get from config
        :return: Config string from dict or information that not exists
        """

        if key not in self.config:
            return key + " is not in config!"

        return str(self.config[key])


