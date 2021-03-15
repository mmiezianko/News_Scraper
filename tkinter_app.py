from newsfeed import BBCNewsFeeder, CategoricalNews
from utils import open_url
import tkinter as tk




OptionList = ['business', 'technology', 'uk', 'science_and_environment','world']
app = tk.Tk() #tworzenie okna głównego; identyfikator app otrzymuje wskazanie na instancje klasy Tk

variable = tk.StringVar(app) #Instancje klasy StringVar przypisujemy do variable. Nie można przekazać zwykłej zmiennej do widgetu. Jedynymi rodzajami zmiennych, dla których to działa są zmienne, będące subklasą klasy o nazwie Variable, zdefiniowanej w module Tkinter. StrVar() przechowuje string.
variable.set(OptionList[0]) #metoda .set () służy do ustawiania i zmiany wartości przechowywanej w zmiennej Tkinter
opt = tk.OptionMenu(app, variable, *OptionList) #klasa OptionMenu to klasa pomocnicza, która tworzy wyskakujące menu oraz przycisk do jej wyświetlenia. Aby utworzyć menu opcji, wywołujemy konstruktor klasy OptionMenu i przekazujemy zmienną oraz listę opcji.
opt.config(width=30, font=('Helvetica', 12)) #Używamy metody config () z klasy tk, aby zaktualizować wiele atrybutów po utworzeniu obiektu (modyfikacja jednej lub wielu opcji widgetu).
OpeningLabel = tk.Label(text='Wybierz kategorię:', font=('Helvetica', 16), fg='red') #Label jest standardowym widżetem Tkinter służącym do wyświetlania tekstu lub obrazu na ekranie. Aby go użyć należy tylko określić, co ma się w nim wyświetlać (może to być tekst, mapa bitowa lub obraz).
OpeningLabel.grid(row=0,column=0,stick=tk.W) #Menedżer geometrii grid () organizuje widżety w strukturze przypominającej tabelę w widżecie nadrzędnym. Główny widget jest podzielony na wiersze i kolumny, a każda część tabeli może zawierać widget. Wykorzystuje kolumny, rozpiętość kolumn, ipadx, ipady, padx, pady, row, rozpiętość wierszy i stick.
opt.grid(row=0,column=1,stick=tk.W)




NewsFeeder=BBCNewsFeeder() #tworze instancje klasy BBCNewsFeeder
def shownews(*args): #tworze funkcje shownews o zmiennych argumentach (*args). Funkcja ta ładuje nowy wygląd okna i korzysta z poprzednio zdefiniowanych widgetów (np. OpeningLabel, opt)

    OpeningLabel = tk.Label(text='Wybierz kategorię:', font=('Helvetica', 16), fg='black')
    OpeningLabel.grid(row=0,column=0,stick=tk.W)
    opt.grid(row=1,column=0,stick=tk.W+tk.N) #używamy menadżera geometrii grid() i tym samym mocujemy widget o identyfikatorze opt

    #utworzenie pustych list dla kolejnych elementów newsa
    HeadingList=[]
    SummaryList=[]
    ButtonList=[]
    #iteracja po elementach z listy 8 pierwszych newsów danej kategorii uzuskanych przez wywołanie metody get_top_news()
    # obiektu klasy CategoricalNews zwróconego metodą get_news_by_category(), wywołanej  z parametrem aktualnej wartości zmiennej wigeta opt (metodą variable.get()).
    for i, news in enumerate(NewsFeeder.get_news_by_category(variable.get()).get_top_news(8)):
        Heading = tk.Label(text=news['headline']+'\t\t\t\t', font=('Helvetica', 15,'bold'), fg='black')
        Heading.grid(row=2+i*3+0,column=0,stick=tk.W)
        Summary = tk.Label(text=news['summary']+'\t\t\t\t', font=('Helvetica', 12), fg='black')
        Summary.grid(row=2+i*3+1,column=0,stick=tk.W)
        #Utworzenie obiektu klasy Button z zadanymi parametrami:
        Button = tk.Button(text='read more', # tekst na przycisku
                           font=('Helvetica', 12), # format czcionk
                           fg='black', #kolor czcionki
                           command=(lambda e=news['url']: open_url(e))) #obiekt funkcyjny, funkcja zostanie wywoływana przez naciśnięcie przycisku
        # lambada - funkcja anonimowa
        Button.grid(row=2+i*3+2,column=0,stick=tk.W)
        # Rozszerzenie poczczególnych list o dane newsy
        HeadingList.append(Heading)
        SummaryList.append(Summary)
        ButtonList.append(Button)

variable.trace("w", shownews) #ustalenie śledzenia zmiennej variable związanej z obiektem opt, oraz funkcji, która zostanie wywołana przy zmianie warości variable.
# 'w' - tryb write, funkcja będzie akualizować okno.
app.geometry('1800x800') #ustalenie domyślnych wymiarów okna
app.mainloop()
