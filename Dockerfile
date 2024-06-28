# Użyj obrazu bazowego Python
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj katalogi app, data, model do katalogu roboczego
COPY app ./app
COPY data ./data
COPY model ./model

# Otwórz port 8501 (domyślny port Streamlit)
EXPOSE 8501

# Uruchom aplikację Streamlit
CMD ["streamlit", "run", "app/heart_disease_app.py"]