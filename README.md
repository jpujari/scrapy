# scrapy
python scraping using selenium and beautiful soup

## Installation

How to setup an Environment?

### Option 1 

#### Requirements

```
Python3
Pip
```

#### Environment

Download chromedriver 
https://chromedriver.chromium.org/downloads
The version of chromedriver should match your chrome browser version.
Adjust chromedriver path in the script accordingly.

Install virutalenv

```pip install virtualenv```

Setup a virtual env

```python3 -m virtualenv venv```

Activate the virtualenv

```source venv/bin/activate```

install the dependent packages

```pip install -r requirements.txt```

run the app from the command line from root

```python3 scrapy.py```

The site will be loaded on localhost

```http://0.0.0.0:5000/```

### Option 2 (Dockerfile)

Install Docker
https://docs.docker.com/get-docker/

Build the docker file

```docker build -t scrapy .```

Run the docker file 

``` docker run -d -p 5000:5000 scrapy ```

The site will be loaded on localhost

```http://0.0.0.0:5000/```

Kill the docker container

```docker container ls```

Get the container id from the command above

```docker kill <container_id>```

## Screenshot

There is a screenshot which shows an example of the output
https://github.com/jpujari/scrapy/blob/master/Screen%20Shot%202020-06-21%20at%205.35.12%20PM.png

## Related Articles

https://medium.com/@mahmudahsan/how-to-scrap-data-from-javascript-based-website-using-python-selenium-and-headless-web-driver-531c7fe0c01f

https://stackoverflow.com/questions/38133759/how-to-get-text-from-span-tag-in-beautifulsoup

https://stackoverflow.com/questions/1475123/easiest-way-to-turn-a-list-into-an-html-table-in-python/54963455#54963455

https://github.com/ireapps/first-web-scraper/blob/master/scrapers/crime/scrape.py

https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed