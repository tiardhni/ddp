import streamlit as st

st.title("ini halaman dashboard!")
st.session_state['Nabung']
st.session_state['Daftar Tugas']

jumlah = 0
for session in st.session_state['Nabung']:
    jumlah += session['nominal']

st.write("Total nominal menabung sebesar", jumlah) 

for session in st.session_state['Daftar Tugas']:
    st.write(session['nama_tugas'])
