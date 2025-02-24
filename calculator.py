#streamlit run filename with extension
import streamlit as st

st.title('Calculator')
st.markdown("This is a simple calculator")
c1, c2 = st.columns(2)
fnum = c1.number_input("Enter first number", value=0)
snum = c2.number_input("Enter second number", value=0)