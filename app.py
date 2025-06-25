import streamlit as st
import pandas as pd
import joblib  # atau gunakan pickle sesuai model Anda

# Load model yang sudah dilatih sebelumnya
# Pastikan file model.pkl ini ada di repo GitHub Anda
model = joblib.load("model.pkl")  # Ganti dengan nama file model Anda

# Judul Aplikasi
st.title("Prediksi Income Berdasarkan Usia dan Pengalaman")

# Input dari user
st.subheader("Masukkan Data:")
new_age = st.number_input("Usia (Age)", min_value=0.0, format="%.1f")
new_experience = st.number_input("Pengalaman (Experience)", min_value=0.0, format="%.1f")

# Tombol prediksi
if st.button("Prediksi Income"):
    try:
        # Membuat DataFrame dari input
        new_data_df = pd.DataFrame([[new_age, new_experience]], columns=['Age', 'Experience'])

        # Melakukan prediksi
        predicted_income = model.predict(new_data_df)

        # Menampilkan hasil
        st.success(f"Untuk Usia = {new_age} dan Pengalaman = {new_experience} tahun:")
        st.write(f"💰 **Prediksi Income:** ${predicted_income[0][0]:,.2f}")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
