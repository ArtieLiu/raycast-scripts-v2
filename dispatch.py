import webbrowser


def dispatch(app_alias, destination):
    app_fullname = app_name_binding[app_alias]
    goto[destination](app_fullname)


app_name_binding = {
    "init": "init-osx",
}


def github(app_name):
    url = f"https://github.com/ArtieLiu/{app_name}"
    webbrowser.open_new_tab(url)


def buildkite(app_name):
    url = f"https://buildkite.com/ArtieLiu/{app_name}"
    webbrowser.open_new_tab(url)


goto = {
    "git": github,
    "bui": buildkite
}
