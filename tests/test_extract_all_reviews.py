from goje_scrapper.goje import *

movie_url = 'https://www.rottentomatoes.com/m/a_separation_2011'

movie_scraper = GojeScraper(movie_url=movie_url)

# When you want to grab every review in rotten tomato
review_list = list()
try:
    movie_scraper.number_of_review_pages()

    for i in range(1,movie_scraper.number_of_review_pages()):
        review_list.append(movie_scraper.extract_critic_reviews(page_number=movie_scraper.number_of_review_pages()))
        print("page {0} is scrapped!".format(i))
except IndexError:
    review_list.append(movie_scraper.extract_critic_reviews())

print(review_list)