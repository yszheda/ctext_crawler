# ctext_crawler #

A simple crawler of [中國哲學書電子化計劃](http://ctext.org/zh)

Just for fun, do not use it to crawl too much data or you will get banned.

## Usage ##
1. Install `Scrapy`
2. Crawl [《全唐詩》](http://ctext.org/quantangshi/zh)
```
scrapy crawl quantangshi -o quantangshi.json
cat quantangshi.json | json_pp > quantangshi.json
```
