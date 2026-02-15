#!/bin/bash

OS_NAME=$(uname)

if [ "$OS_NAME" = "Darwin" ]; then
  PROJECT_DIR="/Users/aboud/programming/retail-data-project"
else
  PROJECT_DIR="/home/aboud/programming/retail-data-project"
fi

cd $PROJECT_DIR 

. .venv/bin/activate

cd retail_scraper

scrapy crawl mmafightstore-wrestling-shoes -s LOG_FILE=$PROJECT_DIR/logs/scrapy.logs

