from typing import *
from  bs4 import BeautifulSoup
import requests
import  webbrowser

def get_news(url:str)->List[Dict[str,str]]: #informacja o przyjmowanym typie argumentu i zwracanym typie
    response = requests.get(url=url) #response to obiekt klasy Response. Metoda get wskazuje, że próbujemy uzyskać lub pobrać dane z określonego zasobu.
    doc = BeautifulSoup(markup=response.text, features='html.parser') #doc jest instancją klasy BeautifulSoup. Tworząc ten obiekt przekazujemy argumenty (markup, features) magicznej metodzie własnej __init__ klasy BeautiofulSoup
    stories = doc.find_all('div',{'class' : 'gs-c-promo-body'}) #Metoda find all przemierza drzewo, zaczynając od danego punktu, i znajduje wszystkie obiekty 'Tag' i 'NavigableString', które spełniają podane kryteria (w tym przypadku ('div',{'class' : 'gs-c-promo-body'}).
    news_list=[] #tworze pusta liste
    for story in stories:

        news_dict = {} #tworze pusty slownik
        headline = story.find('h3') #Metoda find jest prawie dokładnie taka sama jak findAll, z tym wyjątkiem, że zamiast znaleźć wszystkie pasujące obiekty, znajduje tylko pierwszy.
        if headline:
            news_dict['headline'] = headline.text #do klucza 'headline' w slowniku przypisujemy wartosc. Dzięki .text otrzymujemy tekst odwołując się do atrybutu klasy SoupStrainer
        link = story.find('a')
        if link:
            if link['href'].split(':')[0]=='https': #.split zwraca listę słów wchodzących w skład napisu z wykorzystaniem napisu separator jako separatora wyrazów.
                news_dict['url'] = link['href']
            else:
                news_dict['url']= 'https://www.bbc.com'+ link['href']
        summary = story.find('p')
        if summary:
            news_dict['summary'] = summary.text

        news_list.append(news_dict) #dodajemy slownik do listy
    return news_list[1:] #zaczynamy od 1 a nie od 0, gdyż pierwszy nagłówek zawsze się powtarza

def open_url(url):
    webbrowser.open_new(url) #otwiera adres URL w nowym oknie domyślnej przeglądarki, jeśli to możliwe, w przeciwnym razie otwiera adres URL w jedynym oknie przeglądarki.

