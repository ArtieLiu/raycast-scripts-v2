from destinations.github import github
from destinations.log import log


def dispatch(appname, destination, subdivision):
    goto[destination](appname, subdivision)


goto = {
    "git": github,
    "log": log
}
