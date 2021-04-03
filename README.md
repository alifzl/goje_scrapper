# Unofficial Library for Scrapping [Rotten Tomato](http://rottentomatoes.com/)

Goje, in Persian (گوجه) means tomato.
_Goje_ is another library for scrapping Movie Metadata from  [Rotten Tomato](http://rottentomatoes.com) movie database.
it is mainly developed based on native python libraries. and believe me it is blazing fast!

## Installation

`pip install Goje`

## Usage

Currently Goje supports 3 main functions:

| Method Name  | Functionality  |
|---|---|
| GojeScraper.extract_extract_movie_links() | return all the Rotten Tomato Movie Links based on a given year range  |
| GojeScraper.extract_metadata() | scrape, extract and return all movie information upon a given Movie URL |
| GojeScraper.extract_reviews() | extract all the reviews of a Movie, based on a given Rotten Tomato movie URL and specified review page |


### GojeScraper.extract_extract_movie_links()

```python
from goje_scrapper import GojeScraper

movie_scraper = GojeScraper()
print(movie_scraper.extract_movie_links(2021,2022))
```

### GojeScraper.extract_metadata()

```python
from goje_scrapper import GojeScraper

# give a Rotten Tomato Movie URL
movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'
# Instantiate Goje via given URL
movie_scraper = GojeScraper(movie_url=movie_url)
# Scrape Movie Meta Data
movie_scraper.extract_metadata()
print(movie_scraper.metadata)
```

### GojeScraper.extract_reviews() (single page review)

```python
from goje_scrapper import GojeScraper

# give a Rotten Tomato Movie URL
movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'
# Instantiate Goje via given URL
movie_scraper = GojeScraper(movie_url=movie_url)
# When you want to extract one page of reviews
all_reviews = movie_scraper.extract_reviews(page_number=1)
print(all_reviews)
```

### GojeScraper.extract_reviews() (All reviews)

```python
from goje_scrapper import GojeScraper

# give a Rotten Tomato Movie URL
movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'
# Instantiate Goje via given URL
movie_scraper = GojeScraper(movie_url=movie_url)
# When you want to grab every review in rotten tomato
review_list = list()
try:
    movie_scraper.number_of_review_pages()

    for i in range(1,movie_scraper.number_of_review_pages()):
        review_list.append(movie_scraper.extract_reviews(page_number=movie_scraper.number_of_review_pages()))
        print("page {0} is scrapped!".format(i))
except IndexError:
    review_list.append(movie_scraper.extract_reviews())

print(review_list)
```


## Contribute, Issues and Stuff

Feel free to open an issue in Github repository of Goje.