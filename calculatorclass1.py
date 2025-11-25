import streamlit as st

st.title("🧮 Kalkulator Sederhana")

# Input angka
num1 = st.number_input("Masukkan angka pertama:", value=0.0)
num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilihan operasi
operation = st.selectbox(
    "Pilih operasi:",
    ("Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)")
)

# Tombol hitung
if st.button("Hitung"):
    if operation == "Tambah (+)":
        result = num1 + num2
    elif operation == "Kurang (-)":
        result = num1 - num2
    elif operation == "Kali (×)":
        result = num1 * num2
    elif operation == "Bagi (÷)":
        if num2 == 0:
            st.error("Error: Tidak bisa membagi dengan nol!")
            result = None
        else:
            result = num1 / num2
    
    if result is not None:
        st.success(f"Hasil: {result}")
