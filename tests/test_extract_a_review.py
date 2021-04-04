from goje_scrapper.goje import *

movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'

movie_scraper = GojeScraper(movie_url=movie_url)

# When you want to extract one page of reviews
all_reviews = movie_scraper.extract_critic_reviews(page_number=1)
print(all_reviews)