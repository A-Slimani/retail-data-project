from alerts.mmafightstore import wrestlingshoes_under_100
from alerts.ntfy_alerts import ntfy_basic
import subprocess
import requests
import platform 
import os

SERVER = "http://10.0.0.216:8081"
TOPIC = "alerts"


def change_dir(folder: str):
    try:
        if platform.system() == "Linux":
            project_dir = "/home/aboud/programming/retail-data-project"
        else:
            project_dir = "/Users/aboud/programming/retail-data-project"

        os.chdir(f"{project_dir}/{folder}")
    except Exception as e:
        print(f"error: {e}")
        raise


def run_scraper(scraper_name: str):
    print(f"Running {scraper_name} scraper...")
    scraper_result = subprocess.run(
        [
            "scrapy", 
            "crawl", 
            scraper_name,
            "-s",
            f"LOG_FILE=../logs/{scraper_name}-scrapy.log"
        ],
        capture_output=True,
        text=True
    )

    if scraper_result.returncode != 0:
        error_message = f"Error with {scraper_name} scraper:\n{scraper_result.stderr}, {scraper_result.stdout}"
        ntfy_basic("SCRAPY", error_message, SERVER, TOPIC)
        raise RuntimeError(error_message)

    success_message = f"Scraped {scraper_name} successfully."
    print(success_message)
    ntfy_basic("SCRAPY", success_message, SERVER, TOPIC)


def run_dbt():
    print(f"Running dbt transformations...")
    dbt_result = subprocess.run(
        ["dbt", "run"],
        capture_output=True,
        text=True
    )
    
    if dbt_result.returncode != 0:
        error_message = f"Error with dbt transformation:\n{dbt_result.stdout}"
        ntfy_basic("DBT", error_message, SERVER, TOPIC)
        raise RuntimeError(error_message)

    success_message = f"DBT transformations ran successfully."
    print(success_message)
    ntfy_basic("DBT", success_message, SERVER, TOPIC)


def main():
    # scraping / processing data
    change_dir("retail_scraper")
    run_scraper("mmafightstore-wrestling-shoes")
    run_scraper("running-warehouse")

    change_dir("retaildbt")
    run_dbt()

    # alerts
    wrestlingshoes_under_100()

    
if __name__ == "__main__":
    main()

