import streamlit as st
from src.ui import render_fraud
st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳", layout="wide")
render_fraud()
