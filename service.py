#!/usr/bin/python

import ticketer

def main():
    """
    This function run when service starting. That create bot, with config 
    from config.json, in local dir.
    """

    config = ticketer.config_from_file_t("config.json")
    logger = ticketer.logger_stdout_t()

    bot = ticketer.ticketer_t(config, logger)
    bot.run()

"""
This call main, if it is main module.
"""
if __name__ == "__main__":
    main()
