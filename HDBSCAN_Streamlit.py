import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Navigation 
st.set_page_config(page_title="Klasterisasi Banjir", layout="wide")

# ======================
# SIDEBAR MENU
# ======================
menu = st.sidebar.radio("Pilih Halaman", [
    "Beranda",
    "Data",
    "Metode",
    "Peta Klaster",
    "Klasterisasi"
])

# ======================
# BERANDA
# ======================
if menu == "Beranda":
    st.title("🌊 Klasterisasi Banjir Indonesia")
    st.write("Aplikasi berbasis HDBSCAN dan Bayesian Optimization")

# ======================
# METODE
# ======================
elif menu == "Metode":
    st.title("📘 Metode")
    st.subheader("HDBSCAN")
    st.write("Metode clustering berbasis densitas")
    
    st.subheader("Bayesian Optimization")
    st.write("Optimasi parameter model")