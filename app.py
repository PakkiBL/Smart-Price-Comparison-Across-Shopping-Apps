import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Price Comparison", layout="centered")

st.title("🛒 Smart Price Comparison Across Shopping Apps")
st.write("Compare product prices across shopping apps and find the lowest deal.")

# User input
product = st.text_input("Enter Product Name")

if product:
    # Sample price data (demo data)
    data = {
        "Shopping App": ["Amazon", "Flipkart", "Meesho", "Snapdeal"],
        "Price (₹)": [15999, 15499, 16250, 15800]
    }

    df = pd.DataFrame(data)

    # Find lowest price
    min_price = df["Price (₹)"].min()

    st.subheader(f"💡 Price Comparison for: {product}")
    st.dataframe(df)

    st.success(f"✅ Lowest Price Available: ₹{min_price}")

    best_app = df[df["Price (₹)"] == min_price]["Shopping App"].values[0]
    st.info(f"🏆 Best App to Buy From: {best_app}")

else:
    st.warning("Please enter a product name to compare prices.")

