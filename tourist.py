import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load hotel data
def load_hotel_data():
    # Simulate loading data from a file; replace this with the path to your CSV
    data = {
        "hotel_name": ["Pearl Continental", "Serena Hotel", "Avari Hotel", "Quetta Serena Hotel", "Movenpick Hotel"],
        "city": ["Karachi", "Islamabad", "Lahore", "Quetta", "Karachi"],
        "latitude": [24.8607, 33.6844, 31.5497, 30.1798, 24.8608],
        "longitude": [67.0011, 73.0479, 74.3436, 66.975, 67.008],
        "price_per_night": [15000, 22000, 16000, 14000, 13000],
        "description": [
            "A luxury hotel in Karachi offering excellent facilities.",
            "A high-end hotel in Islamabad known for its amenities.",
            "A 5-star hotel in Lahore with beautiful views.",
            "A serene hotel in Quetta with a traditional touch.",
            "A comfortable and stylish hotel in Karachi."
        ]
    }
    return pd.DataFrame(data)

# Display map and hotels
def display_map(hotels, selected_city=None):
    # Center map on Pakistan
    map_center = [30.3753, 69.3451]
    m = folium.Map(location=map_center, zoom_start=5)

    # Add hotel markers to the map
    for _, row in hotels.iterrows():
        if selected_city and row['city'] != selected_city:
            continue  # Skip hotels not in the selected city

        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=(
                f"<b>{row['hotel_name']}</b><br>"
                f"City: {row['city']}<br>"
                f"Price: {row['price_per_night']} PKR/night<br>"
                f"{row['description']}"
            ),
            tooltip=row['hotel_name']
        ).add_to(m)

    # Display map in Streamlit
    return st_folium(m, width=700, height=500)

# Main app
def main():
    st.title("Pakistan Tourism - Hotel Finder")
    
    st.write("Explore and book hotels in various cities across Pakistan.")

    # Load data
    hotels = load_hotel_data()

    # Filter by city
    st.sidebar.subheader("Search Hotels")
    city_options = ["All"] + sorted(hotels["city"].unique())
    selected_city = st.sidebar.selectbox("Select a city", city_options)
    filtered_hotels = hotels if selected_city == "All" else hotels[hotels["city"] == selected_city]

    # Display map with filtered hotels
    st.subheader(f"Hotels in {selected_city if selected_city != 'All' else 'Pakistan'}")
    display_map(hotels, selected_city if selected_city != "All" else None)

    # Display hotel booking section
    st.subheader("Book a Hotel")
    selected_hotel = st.selectbox("Choose a hotel", filtered_hotels["hotel_name"].unique())
    hotel_info = filtered_hotels[filtered_hotels["hotel_name"] == selected_hotel].iloc[0]
    
    st.write("### Hotel Details")
    st.write(f"**Name:** {hotel_info['hotel_name']}")
    st.write(f"**City:** {hotel_info['city']}")
    st.write(f"**Price per Night:** {hotel_info['price_per_night']} PKR")
    st.write(f"**Description:** {hotel_info['description']}")

    if st.button("Book Now"):
        st.success(f"Thank you for booking {selected_hotel}!")

if __name__ == "__main__":
    main()
