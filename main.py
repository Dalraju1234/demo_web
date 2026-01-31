import streamlit as st
st.title("ITECH COMPUTERS")
name=st.text_input("Enter Yout Name :")
fname=st.text_input("Enter you Father's Name:")
mname=st.text_input("Enter your Mother's Name:")
addr=st.text_area("Enter you address :")
classdata=st.selectbox("Enter your class",(1,2,3,4,5,6,7,8,9,10))
btn=st.button("Done")
if btn:
    st.markdown(f""" Name of sthe student :{name}

                 fathers Name:{fname}mother name{mname} address:{addr},class :{classdata}""")

