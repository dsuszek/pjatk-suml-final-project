# Uruchomienie aplikacji

Aby uruchomić całą aplikacje należy wpisać w konsoli następującą komendę:
```
docker pull s22660/zawal-serca && docker run -p 8501:8501 s22660/zawal-serca
```
Następnie wchodzimy w link wyświetlony w konsoli
```
http://localhost:8501
```
<img width="1601" alt="Zrzut ekranu 2024-06-29 o 00 50 25" src="https://github.com/dsuszek/pjatk-suml-final-project/assets/149255804/580d1d18-79aa-4a2d-bb29-5a9fa5165c43">



# Uruchamianie osobnych elementów aplikacji

## Uruchamianie potoku trenującego modele w kedro

Aby uruchomić projekt należy najpierw pobrać go z githuba. Następnie trzeba stworzyć wirtualne środowisko

``` 
conda create --name nazwa_srodowiska python=3.10 -y 
```

Następnie aktywujemy wybrane środowisko
```
conda activate nazwa_srodowiska
```

i instalujemy w nim nasze wymagania
```
pip install -r requirements.txt
```
Po tych krokach możemy uruchomić potok
```
kedro run
```

## Uruchamianie aplikacji streamlit

instalujemy wymagania
```
pip install -r requirements.txt
```

włączamy aplikację
```
streamlit run heart_disease_app.py
```


