#!/bin/sh

# Uruchomienie kedro run
kedro run

# Sprawdzenie statusu zakończenia kedro run
if [ $? -eq 0 ]; then
    echo "Kedro run zakończone sukcesem. Uruchamiam Streamlit..."
else
    echo "Kedro run zakończone niepowodzeniem. Nie uruchamiam Streamlit."
    exit 1
fi

# Uruchomienie Streamlit
streamlit run heart_disease_app.py --server.port=8501
