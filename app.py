import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# JUDUL APLIKASI
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    #baca file csv
    data = pd.read_csv("pddikti_example.csv")

    #tampilkan data di streamlit
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    #baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    #filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    #buat visualisasi
    plt.figure(figsize=(12,6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]

        #urutkan data berdasarkan id dengan ututan menurun
        subset = subset.sort_values(by="id", ascending=False)

        plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    plt.title(f"Visualisasi Data untuk {selected_university}")
    plt.xlabel('Semester')
    plt.xticks(rotation=90) #rotasi label sumbu x menjadi vertikal
    plt.ylabel('jumlah')
    plt.legend()

    st.pyplot()