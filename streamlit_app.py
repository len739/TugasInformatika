import streamlit as st

st.title("🎈 halo lino ganteng")
st.write(
   "Ngoding seru bersama Rafalino
   )
st.image("17483129038273881632111553702091.jpg",width=200)

st.title("aplikasi sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganji")
