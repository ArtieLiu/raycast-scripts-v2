from util import open_tab


def log(app_name, sub_destination):
    dev_log_url = "dev.url"
    stg_log_url = "stg.url"
    prd_log_url = "prd.url"

    default_url = dev_log_url

    match sub_destination:
        case "":
            open_tab(default_url)
        case "dev":
            open_tab(dev_log_url)
        case "stg":
            open_tab(stg_log_url)
        case "prd":
            open_tab(prd_log_url)
