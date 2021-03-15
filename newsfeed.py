from utils import *

class CategoricalNews():

    def __init__(self, url):
        """Konstruktor klasy CategoricalNews."""
        self.categorical_news= get_news(url) #atrybut klasy CategoricalNews().

    def get_top_news(self, nr_of_news): #metoda klasy CategoricalNews()
        """

        :param nr_of_news: liczba newsow, ktora ma sie wyswietlac
        :return: newsy w zadanej ilosci. jesli ilosc przekracza liczbe wszystkich newsow na stronie, zwraca wszystkie newsy
        """
        return self.categorical_news[:nr_of_news] if len(self.categorical_news)>nr_of_news else self.categorical_news




class BBCNewsFeeder():

    def __init__(self):

        bbc_news_url: str = 'https://www.bbc.com/news/'
        list_of_categories: List[str] = ['business', 'technology', 'uk', 'science_and_environment', 'world']
        self.newsdict: Dict[str, CategoricalNews] = {category: CategoricalNews(bbc_news_url+category) for category in list_of_categories}  # atrybut klasy BBCNewsFeeder()
    def get_news_by_category(self, category: str)->CategoricalNews:
        """

        :param category: kategoria, z której chcemy wybierać
        :return: lista newsów z danej kategorii
        """
        return self.newsdict[category]
    pass

