from pathlib import Path
import subprocess
import luigi
import json


class RunSpider(luigi.Task):

    def run(self):
        scrapy_project_path = Path("./retail_scraper").resolve()

        subprocess.run(
            ["scrapy", "crawl", "mmafightstore-wrestling-shoes"],
            cwd=scrapy_project_path,
            check=True
         )



