from destinations import *


def dispatch(appname, destination, subdivision):
    eval(destination)(appname, subdivision)
