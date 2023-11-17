import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset (pastikan path file sesuai dengan lokasi dataset)
d = "day.csv"
dataset = pd.read_csv(d)

# Bagian untuk menampilkan visualisasi
st.title("Bike Sharing Data Analysis Dashboard")

# Visualisasi 1: Tren Peminjaman Berdasarkan Musim
st.subheader("Tren Peminjaman Berdasarkan Musim")
avg_rentals_season = dataset.groupby("season")["cnt"].mean()
st.bar_chart(avg_rentals_season)

# Visualisasi 2: Tren Peminjaman Berdasarkan Hari dalam Seminggu
st.subheader("Tren Peminjaman Berdasarkan Hari dalam Seminggu")
avg_rentals_weekday = dataset.groupby("weekday")["cnt"].mean()
st.bar_chart(avg_rentals_weekday)

# Visualisasi 3: Peminjaman Berdasarkan Kondisi Cuaca
st.subheader("Peminjaman Berdasarkan Kondisi Cuaca")
avg_rentals_weather = dataset.groupby("weathersit")["cnt"].mean()
st.bar_chart(avg_rentals_weather)


# METODE CLUSTERING


# Fungsi untuk membuat kategori suhu
def categorize_temp(temp):
    if temp * 41 < 10:
        return "Cold"
    elif temp * 41 >= 10 and temp * 41 < 25:
        return "Moderate"
    else:
        return "Hot"


# Menambahkan kolom kategori suhu ke dalam dataset
dataset["temp_category"] = dataset["temp"].apply(categorize_temp)

# Visualisasi 4: Scatter Plot Berdasarkan Kategori Suhu
st.subheader("Peminjaman Berdasarkan Kategori Suhu")
plt.figure(figsize=(8, 6))

# Scatter plot untuk setiap kategori suhu
for category in dataset["temp_category"].unique():
    temp_subset = dataset[dataset["temp_category"] == category]
    plt.scatter(temp_subset["temp"], temp_subset["cnt"], label=category)

plt.xlabel("Temperature")
plt.ylabel("Count of Rentals")
plt.title("Scatter Plot of Rentals based on Temperature Categories")
plt.legend()
st.pyplot(plt)  # Menampilkan scatter plot di dashboard


# Menjalankan dashboard
if __name__ == "__main__":
    st.write()
