"""
Unofficial Python Scrapper for Rotten Tomato.
Author: Ali Fazeli
Website: https://faze.li
"""

__author__ = "Ali Fazeli"
__email__ = "a.fazeli95@gmail.com"
__status__ = "develop"


import re
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import json


class Goje:
    BASE_URL = "https://www.rottentomatoes.com/api/private/v2.0"
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_URL)

    def __init__(self):
        self.metadata = dict()
        self.url = None

    def extract_url(self):
        pass

    def extract_metadata(self, **kwargs):
        pass

    def extract_reviews(self, **kwargs):
        pass

    def extract_movie_links(self,**kwargs):
        pass

    def _extract_section(self, section):
        pass

    def number_of_review_pages(self, **kwargs):
        pass

    @staticmethod
    def search(term, limit=10):
        r = requests.get(url=Goje.SEARCH_URL, params={"q": term, "limit": limit})
        r.raise_for_status()
        return r.json()


class GojeScraper(Goje):

    def __init__(self, **kwargs):
        Goje.__init__(self)
        self.movie_genre = None
        if 'movie_title' in kwargs.keys():
            self.movie_title = kwargs['movie_title']
            self.extract_url()
        if 'movie_url' in kwargs.keys():
            self.url = kwargs['movie_url']

    def extract_movie_links(self,start,end):
        list_link_all_year=[]
        for year in range(start,end):
            url = "https://www.rottentomatoes.com/top/bestofrt/?year=%s" % year
            html_data = requests.get(url)

            if html_data.status_code == 200:
                python_data = BeautifulSoup(html_data.content, 'lxml')

            list_tag = python_data.find_all('tr')
            list_tag_link=[]
            for tag in list_tag:
                list_new = tag.find('a', class_='unstyled articleLink')
                list_tag_link.append(list_new)

            list_tag_link = [i for i in list_tag_link if i is not None]
            list_link_year = []
            for tag in list_tag_link:
                list_single_movie = [0, 1, 2]
                list_single_movie[0] = tag.get_text().strip('\n').strip()[:-7]
                list_single_movie[1] = tag.get_text().strip('\n').strip()[-5:-1]
                list_single_movie[2] = 'https://www.rottentomatoes.com'+tag.get('href')
                list_link_year.append(list_single_movie)

            list_link_all_year.extend(list_link_year)

        return list_link_all_year

    def extract_url(self):
        search_result = self.search(term=self.movie_title)
        url_movie = 'https://www.rottentomatoes.com' + search_result['movies'][0]['url']
        if len(search_result['movies']) > 1:
            print('There are several movie records matching the search criteria.. The selected url is: {}'.format(url_movie))
        self.url = url_movie

    def number_of_review_pages(self):

        page_movie_reviews_pages_url = urlopen(self.url + '/reviews?type=&sort=&page=1')
        page_movie_reviews_pages = BeautifulSoup(page_movie_reviews_pages_url, "lxml")

        all_the_reviews = page_movie_reviews_pages.find_all('div', class_='reviews-movie')
        all_the_reviews_info = BeautifulSoup(str(all_the_reviews), "lxml")
        page_info = all_the_reviews_info.find_all('span',class_="pageInfo")
        page_info_start = str(page_info).find("Page")
        page_info_finish = [m.start() for m in re.finditer(r"</span>",str(page_info))][0]
        number_of_review_pages = int(str(page_info[0])[page_info_start+9:page_info_finish-1])
        return number_of_review_pages

    def extract_reviews(self,page_number=1):

        page_movie_reviews_url = urlopen(self.url + '/reviews')
        soup = BeautifulSoup(page_movie_reviews_url, "lxml")

        page_movie_reviews_pages_url = urlopen(self.url + '/reviews?type=&sort=&page={0}'.format(page_number))
        page_movie_reviews_pages = BeautifulSoup(page_movie_reviews_pages_url, "lxml")

        all_reviews = page_movie_reviews_pages.find_all('div', class_='row review_table_row')

        all_reviews_info = BeautifulSoup(str(all_reviews), "lxml")
        review = all_reviews_info.find_all('div', class_='the_review')

        review_overall = all_reviews_info.find_all('div', class_='col-xs-16 review_container')
        review_overall_info = BeautifulSoup(str(review_overall), "lxml")

        reviewer_type_info = review_overall_info.findAll("div", class_= { lambda L: L.startswith('review_icon')})

        critic_results = list()
        for i in range(len(all_reviews)):

            critic = all_reviews_info.find_all('div', class_='col-sm-17 col-xs-32 critic_name')
            critic_info = BeautifulSoup(str(critic[i]), "lxml")

            # Critic Name
            critic_name = critic_info.find_all('a',class_='unstyled bold articleLink')
            critic_name_info = BeautifulSoup(str(critic_name), "lxml")
            critic_name_info_finish = str(critic_name_info)[:-1].find("</a>")
            critic_name_info_start = [m.start() for m in re.finditer(r">",str(critic_name_info))][3]
            critic_name = str(critic_name_info)[critic_name_info_start+1:critic_name_info_finish]

            # Critic Publication Section
            critic_publication = critic_info.find_all('em',class_='subtle critic-publication')
            critic_publication_info = BeautifulSoup(str(critic_publication), "lxml")
            critic_publication_info_finish = str(critic_publication_info)[:-1].find("</em>")
            critic_publication_info_start = [m.start() for m in re.finditer(r">",str(critic_publication_info))][3]
            critic_publication = str(critic_publication_info)[critic_publication_info_start+1:critic_publication_info_finish]

            # Critic Review Section
            review_info = BeautifulSoup(str(review[i]), "lxml")
            review_info_finish = str(review_info)[:-1].find("</div>")
            review_info_start = [m.start() for m in re.finditer(r">",str(review_info))][2]
            review_end = str(review_info)[review_info_start+1:review_info_finish]
            critic_review = review_end.replace('\n', '').replace('\r','').strip()

            # Critic Date Section
            review_time = review_overall_info.find_all('div', class_='review-date subtle small')
            review_time_info = BeautifulSoup(str(review_time[i]), "lxml")
            review_time_info_finish = str(review_time_info)[:-1].find("</div>")
            review_time_info_start = [m.start() for m in re.finditer(r">",str(review_time_info))][2]
            review_time_ = str(review_time_info)[review_time_info_start+1:review_time_info_finish].replace('\n', '').replace('\r','').strip()

            # Critic Type Section (Fresh or Rotten)
            reviewer_type_finish_index = str(reviewer_type_info[i])[:-1].find(">")
            reviewer_type_start_index = str(reviewer_type_info[i]).find("small")
            reviewer_type = str(reviewer_type_info[i])[reviewer_type_start_index+6:reviewer_type_finish_index]

            # Wrapping up the results
            critic_results.append([critic_name,critic_publication,reviewer_type,review_time_,critic_review])

        return critic_results

    def extract_metadata(self, columns=('Rating', 'Genre', 'Box Office (Gross USA)', 'Production Co','Runtime','Original Language','Director','Producer','Writer',
                                       'Release Date (Theaters)','Release Date (Streaming)')):
        movie_metadata = dict()
        page_movie = urlopen(self.url)

        soup = BeautifulSoup(page_movie, "lxml")

        def saaf_o_soof(input_string):
            return input_string.replace(' ', '').replace('\n', '').split(',')

        # Score
        score = soup.find('score-board')
        movie_metadata['Score_Rotten'] = score.attrs['tomatometerscore']
        movie_metadata['Score_Audience'] = score.attrs['audiencescore']

        movie_scores = soup.find_all('script', id='score-details-json')
        movie_scores_info = BeautifulSoup(str(movie_scores[0]), "lxml")
        movie_scores_info_dict = json.loads(movie_scores_info.string)
        movie_metadata['movie_scores'] = movie_scores_info_dict

        # Movie Info
        movie_info_section = soup.find_all('div', class_='media-body')
        soup_movie_info = BeautifulSoup(str(movie_info_section[0]), "lxml")
        movie_info_length = len(soup_movie_info.find_all('li', class_='meta-row clearfix'))

        movie_synopsis = soup_movie_info.find_all('div', class_='movie_synopsis clamp clamp-6 js-clamp')
        movie_synopsis_koon = BeautifulSoup(str(movie_synopsis), "lxml")
        movie_synopsis_value = movie_synopsis_koon.find('div', class_='movie_synopsis clamp clamp-6 js-clamp').text.strip()
        movie_cast_section = soup.find_all('div', class_='panel-body content_body')

        for i in range(movie_info_length):
            x = soup_movie_info.find_all('li', class_='meta-row clearfix')[i]
            soup = BeautifulSoup(str(x), "lxml")
            label = soup.find('div', class_='meta-label subtle').text.strip().replace(':', '')
            value = soup.find('div', class_='meta-value').text.strip()

            if label in columns:
                if label == 'Rating':
                    value = re.sub(r'\s\([^)]*\)', '', value)

                if label == 'Genre':
                    value = saaf_o_soof(value)

                if label == 'Box Office (Gross USA)':
                    label = 'Box_Office'
                    value = saaf_o_soof(value)

                if label == 'Production Co':
                    label = 'Studio'
                    value = saaf_o_soof(value)

                if label == 'Runtime':
                    value = saaf_o_soof(value)

                if label == 'Original Language':
                    value = saaf_o_soof(value)

                if label == 'Director':
                    value = saaf_o_soof(value)

                if label == 'Producer':
                    value = saaf_o_soof(value)

                if label == 'Writer':
                    value = saaf_o_soof(value)

                if label == 'Release Date (Theaters)':
                    value = saaf_o_soof(value)

                if label == 'Release Date (Streaming)':
                    value = saaf_o_soof(value)

                movie_metadata[label] = value

        movie_metadata['info'] = movie_synopsis_value

        # Cast Section

        movie_cast_section_info = BeautifulSoup(str(movie_cast_section[1]), "lxml")
        # movie_reviews_info = BeautifulSoup(str(movie_cast_section[3]), "lxml")

        movie_qoute_info = BeautifulSoup(str(movie_cast_section[4]), "lxml")

        all_qoute_er = movie_qoute_info.find_all('td',class_="quote_actor")
        all_qoute = movie_qoute_info.find_all('td',class_="line")

        all_qoutes = list()
        for j in range(len(all_qoute_er)):
            all_qoutes.append([all_qoute_er[j].string,all_qoute[j].string])
        movie_metadata['movie_qoutes'] = all_qoutes

        main_casts = movie_cast_section_info.find_all('div', class_='cast-item media inlineBlock')
        other_casts = movie_cast_section_info.find_all('div', class_='cast-item media inlineBlock moreCasts hide')


        main_casts_and_crew = list()
        for i in range(len(main_casts)):
            tmp = BeautifulSoup(str(main_casts[i]), "lxml")

            x = tmp.find('span')
            xx = BeautifulSoup(str(x), "lxml")
            label = xx.find('span')

            main_cast_pictures = tmp.find_all('img', class_='js-lazyLoad actorThumb medium media-object')
            for element in main_cast_pictures:
                try:
                    main_cast_pictures_large_index = [match.start() for match in re.finditer('https', str(element['data-src']))][1]
                except IndexError:
                    main_cast_pictures_large_index = 0
                main_casts_and_crew.append([re.findall(r'"([^"]*)"', str(label)),element['data-src'][main_cast_pictures_large_index:]])

        movie_metadata['movie_main_casts'] = main_casts_and_crew

        other_casts_and_crew = list()
        for i in range(len(other_casts)):
            tmp = BeautifulSoup(str(other_casts[i]), "lxml")

            x = tmp.find('span')
            xx = BeautifulSoup(str(x), "lxml")
            label = xx.find('span')

            other_cast_pictures = tmp.find_all('img', class_='js-lazyLoad actorThumb medium media-object')
            for element in other_cast_pictures:
                try:
                    other_cast_pictures_large_index = [match.start() for match in re.finditer('https', str(element['data-src']))][1]
                except IndexError:
                    other_cast_pictures_large_index = 0
                other_casts_and_crew.append([re.findall(r'"([^"]*)"', str(label)),element['data-src'][other_cast_pictures_large_index:]])

        movie_metadata['movie_other_casts'] = other_casts_and_crew

        self.metadata = movie_metadata
        self.movie_genre = self.extract_genre(self.metadata)

    @staticmethod
    def extract_genre(metadata):
        try:
            if 'Genre' in metadata:
                movie_genre = metadata['Genre']
            else:
                movie_genre = ['None']

        except IOError:
            movie_genre = ['None']

        return movie_genre
