import pandas as pd
import streamlit as st
import pickle
import time


data = pd.read_excel('data/heart_disease.xlsx')

print(data.head())