# Uruchomienie aplikacji

Aby uruchomić całą aplikacje wpisz w konsoli następującą komendę:
```
docker pull s22660/zawal-serca && docker run -p 8501:8501 s22660/zawal-serca
```

# Uruchamianie potoku trenującego modele kedro

Aby uruchomić projekt nalezy najpierw pobrać go z githuba. Następnie trzeba stworzyć wirtualne środowisko

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




