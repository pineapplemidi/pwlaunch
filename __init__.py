from __future__ import absolute_import, print_function, unicode_literals
from .PwLaunch import PwLaunch
from _Framework.Capabilities import *

def create_instance(c_instance):
    return PwLaunch(c_instance)
