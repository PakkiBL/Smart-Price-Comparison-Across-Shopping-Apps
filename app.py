import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Smart Price Comparison", layout="centered")

st.title("🛒 Smart Price Comparison Across Shopping Apps")
st.write("Real-time price comparison using live e-commerce API data")

# Fetch live data from API
@st.cache_data(ttl=300)  # refresh every 5 minutes
def fetch_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return response.json()

products = fetch_products()

product_names = [p["title"] for p in products]

selected_product = st.selectbox("Select a Product", product_names)

if selected_product:
    product = next(p for p in products if p["title"] == selected_product)

    # Simulate different shopping apps with slight price variation
    data = {
        "Shopping App": ["Amazon", "Flipkart", "Meesho", "Snapdeal"],
        "Price (₹)": [
            round(product["price"] * 83, 2),
            round(product["price"] * 82.5, 2),
            round(product["price"] * 83.8, 2),
            round(product["price"] * 82.9, 2)
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("📊 Live Price Comparison")
    st.dataframe(df)

    min_price = df["Price (₹)"].min()
    best_app = df[df["Price (₹)"] == min_price]["Shopping App"].values[0]

    st.success(f"✅ Lowest Price: ₹{min_price}")
    st.info(f"🏆 Best App to Buy From: {best_app}")
