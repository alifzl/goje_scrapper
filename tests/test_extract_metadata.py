from goje_scrapper.src.goje_scrapper.goje import *

movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'

movie_scraper = GojeScraper(movie_url=movie_url)

movie_scraper.extract_metadata()
print(movie_scraper.metadata)