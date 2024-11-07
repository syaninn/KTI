import streamlit as st

# Fungsi untuk menghitung IMT
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Fungsi untuk menentukan kategori IMT
def bmi_category(bmi):
    if bmi < 18.5:
        return "Kekurangan Berat Badan"
    elif 18.5 <= bmi < 24.9:
        return "Berat Badan Ideal"
    elif 25 <= bmi < 29.9:
        return "Kelebihan Berat Badan"
    else:
        return "Kegemukan"

# Judul aplikasi
st.title("Aplikasi Pemantau Berat Badan")

# Input data dari pengguna
name = st.text_input("Nama:")
date = st.date_input("Tanggal:")
initial_weight = st.number_input("Berat Badan Awal (kg):", min_value=0.0, step=0.1)
initial_height = st.number_input("Tinggi Badan Awal (m):", min_value=0.0, step=0.01)

# Ketika tombol ditekan
if st.button("Hitung"):
    if name and initial_weight > 0 and initial_height > 0:
        bmi = calculate_bmi(initial_weight, initial_height)
        category = bmi_category(bmi)

        st.write(f"Nama: {name}")
        st.write(f"Tanggal: {date}")
        st.write(f"Berat Badan Awal: {initial_weight} kg")
        st.write(f"Tinggi Badan Awal: {initial_height} m")
        st.write(f"Indeks Massa Tubuh (IMT): {bmi:.2f}")
        st.write(f"Kategori: {category}")
    else:
        st.warning("Silakan masukkan semua data yang diperlukan.")

# Menjalankan aplikasi dengan perintah: streamlit run nama_file.py