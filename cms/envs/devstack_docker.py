""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

WEBPACK_LOADER['DEFAULT']['TIMEOUT'] = 5
