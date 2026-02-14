#!/bin/bash

cd /home/aboud/programming/retail-data-project

. .venv/bin/activate

cd retail_scraper

scrapy crawl mmafightstore-wrestling-shoes

