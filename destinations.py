from util import open_tab


def git(app_name, other_args):
    url = f"https://github.com/ArtieLiu/{app_name}"
    open_tab(url)


def log(app_name, target_env):
    dev_log_url = "dev.url"
    stg_log_url = "stg.url"
    prd_log_url = "prd.url"

    default_url = dev_log_url

    match target_env:
        case "" | "dev":
            open_tab(default_url)
        case "stg":
            open_tab(stg_log_url)
        case "prd":
            open_tab(prd_log_url)
