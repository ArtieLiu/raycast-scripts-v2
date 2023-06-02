from github import github
from log import log


def dispatch(appname, destination, subdivision):
    goto[destination](appname, subdivision)


goto = {
    "git": github,
    "log": log
}
