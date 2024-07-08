import streamlit as st

# Sample data
countries = ["USA", "UK", "Canada", "France", "Germany", "India", "China"]

# Sidebar for filtering
with st.sidebar:
    selected_region = st.selectbox("Filter by Region:", ["All", "North America", "Europe", "Asia"])

# Filter based on user selection
filtered_countries = countries.copy()
if selected_region != "All":
    if selected_region == "North America":
        filtered_countries = [country for country in countries if country in ["USA", "Canada"]]
    elif selected_region == "Europe":
        filtered_countries = [country for country in countries if country in ["UK", "France", "Germany"]]
    elif selected_region == "Asia":
        filtered_countries = [country for country in countries if country in ["India", "China"]]

# Display the filtered list
st.title("List of Countries")
st.write(filtered_countries)
