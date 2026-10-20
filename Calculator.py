import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title(" Calculator")

x = st.number_input("Enter the first number",value=0.0)
y = st.number_input("Enter the Second number",value=0.0)
st.write(f" Addition (x+y): {x+y}")
st.write(f" Subtraction (x-y): {x-y}")
st.write(f" Multiply (x*y): {x*y}")
if y != 0:
    st.write(f"Division (x / y): {x / y}")
else:
    st.warning("Cannot divide by zero!")

