from alerts.mmafightstore import under_150 
import subprocess
import requests
import platform 
import os

SERVER = "http://10.0.0.216:8081"
TOPIC = "alerts"


def ntfy_alert(title: str, data: str):
    requests.post(
        f"{SERVER}/{TOPIC}",
        data = data,
        headers = {
            "Title": title,
            "Priority": "default"
        }
    )


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
        error_message = f"Error with {scraper_name} scraper:\n{scraper_result.stderr}"
        ntfy_alert("SCRAPY", error_message)
        raise RuntimeError(error_message)

    success_message = f"Scraped {scraper_name} successfully."
    print(success_message)
    ntfy_alert("SCRAPY", success_message)


def run_dbt():
    print(f"Running dbt transformations...")
    dbt_result = subprocess.run(
        ["dbt", "run"],
        capture_output=True,
        text=True
    )
    
    if dbt_result.returncode != 0:
        error_message = f"Error with dbt transformation:\n{dbt_result.stdout}"
        ntfy_alert("DBT", error_message)
        raise RuntimeError(error_message)

    success_message = f"dbt transformations ran successfully."
    print(success_message)
    ntfy_alert("DBT", success_message)


def main():
    # scraping / processing data
    change_dir("retail_scraper")
    # run_scraper("mmafightstore-wrestling-shoes")
    # run_scraper("running-warehouse")

    change_dir("retaildbt")
    # run_dbt()

    #alerts
    under_150("./feeds/wrestlingshoes.parquet")

    
if __name__ == "__main__":
    main()

