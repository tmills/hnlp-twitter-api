#!/usr/bin/env python

import ConfigParser
import os.path
def get_credentials(fname = "credentials.ini"):
    if not os.path.isfile(fname):
        raise Exception("Missing credentials file. Create a file named credentials.ini with all the Twitter app identifiers.")

    config = ConfigParser.ConfigParser()
    config.read(fname)
    creds = {}
    for (key, val) in config.items('credentials'):
        creds[key] = val

    return creds
