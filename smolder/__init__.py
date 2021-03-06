# -*- coding: utf-8 -*-

"""
Smolder Smoke Testing Library and cli

:copyright: (c) 2015 by Maxwell Cameron.
:license: BSD 3, see LICENSE for more details.

"""

__title__ = 'smolder'
# __version__ = '0.0.1'
# __build__ = 0x020501
__author__ = 'Max Cameron'
__license__ = 'BSD License'
__copyright__ = 'Copyright 2015 Maxwell Cameron'

from .smolder import run_test, tcp_test, curl_request, http_test, noop_test, failed_tests, passed_tests
