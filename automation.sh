#!/bin/bash

$PROJECT_DIR = /home/aboud/programming/retail-data-project

cd $PROJECT_DIR 

. .venv/bin/activate

cd retail_scraper

scrapy crawl mmafightstore-wrestling-shoes -s LOG_FILE=$PROJECT_DIR/logs/scrapy.logs

