from goje_scrapper.goje import *

movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'

movie_scraper = GojeScraper(movie_url=movie_url)

all_reviews = movie_scraper.extract_all_audience_reviews(page_number=6)
print(all_reviews)
print(len(all_reviews))
