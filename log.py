"""
Set up Python's logging module using dictConfig with JSON files.

Copyright (c) 2016 K Kollmann <code∆k.kollmann·moe>
"""

import json
import logging
from logging.config import dictConfig
from os import getenv


def setup_logging(fpath='logconfig.json',
                  env_lvl='WARNING',
                  env_conf_file='LOGCONF'):
    """
    Set up logging.
    Makes print statement for debugging etc. redundant.

    :param fpath: file path to JSON-based logging configuration
    :param env_lvl: the default logging level
    :param env_conf_file: environment variable to use in case it exists
    """
    level = getenv(env_lvl, None)
    conf_file = getenv(env_conf_file, None)
    if not level:
        level = 'WARNING'
    if conf_file:
        fpath = conf_file
    try:
        with open(fpath, 'r') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    except (FileNotFoundError, FileExistsError):
        logging.basicConfig(level=level)

# enable logging
setup_logging(fpath='logconf.json')
log = logging.getLogger(__name__)
