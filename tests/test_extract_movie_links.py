from goje_scrapper.src.goje_scrapper.goje import *

movie_scraper = GojeScraper()
print(movie_scraper.extract_movie_links(2021,2022))