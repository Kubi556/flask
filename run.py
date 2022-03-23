from flask import Flask, request, render_template

#by zaczac uzylem samouczka ze strony: https://analityk.edu.pl/python-flask-instalacja-oraz-hello-world/
#Uczy podstaw serwera webowego opartego na pythonie z uzyciem biblioteki flask

#Tworzenie virtual environment (venv) mozna poki co pominac;
#stworzenie virtualnego srodowiska daje nam to, ze pakiety jakie poinstalujemy
#dla danego projektu beda zainstalowane jedynie w tym virtualnym otoczeniu
#komenda: python -m venv venv  - tworzy to virtualne srodowisko o nazwie venv
#UWAGA: tworzone jest ono w folderze w ktorym sie znajdujemy w danej chwili
#Takze by je uruchomic nalezy wpisac: venv\Scripts\activate
#Widzimy ze jestesmy juz w tym virtualnym srodowisku dzieki dopiskowi (venv) na poczatku linii polecen

#nastepnie instalujemy flask:
#pip install flask
#nastpenie dodajemy zmienna dla Flask, by wiedzial, co uruchamiac:
#set FLASK_APP=run.py (zakladajac ze plik z kodem co stworzymy bedzie sie nazywac 'run.py')

#ponizej cala mini flaskowa aplikacja serwerowa:

app = Flask(__name__)

@app.route('/') #route od sciezka, w tym przypadku definiowane bedzie, co bedzie serwer robil, gdy ktos
                #polaczy sie z nim na odpowiednim porcie w glownej sciezce
def home():
    return render_template('index.html')    #render_template umozliwia wrzucenie gotowego pliku html
                                            #plik html domyslnie znajduje sie w folderze templates
                                            #do pliku html zostalo wprowadzone pole tekstowe
                                            #by wytestowac ponizsza sciezke (operacje 'post')

@app.route('/', methods=['POST'])   #tutaj akcja jest w przypadku gdy uzytkownik przekaze jakies dane do serwera
def my_form_post():
    osoba_imie = request.form['imie']
    osoba_nazwisko = request.form['nazwisko']
    adres_email = request.form['adres_email']
    data = request.form['pole_daty']
    czas = request.form['pole_czasu']
    tel = request.form['telefon']
    if (request.form.get('checkbox1')):
        checkbox1 = request.form.get('checkbox1')
    else:
        checkbox1 = 'off'
    color = request.form['color']
                                    #zapisanie danych uzytkownika do zmiennej
    #processed_text = osoba_imie.upper()   #zmiana danych wprowadzonych (wszystkie male litery na duze)
    return '<p style="color:' + color + ';align-text:center">Imie: ' + osoba_imie + '<br>'+ 'Nazwisko: '+ osoba_nazwisko + '<br> adres e-mail: ' + adres_email + '<br>Numer telefonu:' + tel + '<br>Wybrany kolor: ' + color + '<br>Data: '+data + '<br>Czas: '+ czas+'</p>'
    #po komendzie 'post' (submit, przeslij), serwer przetwarza dane i daje odpowiedz
#<p style="color:blue">






@app.route('/innastrona')           #analogicznie, przy sciezce dostepowej do serwera z dopiskiem /innastrona
def innastrona():
    return '<p>Witam na innej stronie<p>'   #odpowiedz serwera w formie HTML

@app.route('/klient/<numer>')       #wprowadzenie zmiennej do paska adresu
def klient(numer):
    return f'Klient o numerze {numer} to ...'

@app.route('/dodaj/<numer1>+<numer2>')
def dodaj(numer1,numer2):
    wynik = int(numer1) + int(numer2)
    return f'Wynik: {wynik}'
@app.route('/dodaj/<numer1>-<numer2>')    
def odejmij(numer1,numer2):
    wynik = int(numer1) - int(numer2)
    return f'Wynik: {wynik}'

if __name__ == '__main__':
    app.run(debug=False)