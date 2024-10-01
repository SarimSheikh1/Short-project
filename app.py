import streamlit as st

# Custom CSS to style the font

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&family=Verdana:wght@700&display=swap');
    
    .custom-font {
        font-family: 'Courier Prime', monospace;
        font-size: 20px;
    }
    .title-font {
        font-family: 'Verdana', sans-serif;
        font-size: 28px;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)


# Streamlit inputs with emojis and styled text
st.markdown("<h1 class='title-font'>🏠 Rent Calculator</h1>", unsafe_allow_html=True)

rent = st.number_input("🏡 Enter your hostel/flat Rent", min_value=0)
food = st.number_input("🍽️ Enter the amount of food cost", min_value=0)
electricity_spend = st.number_input("💡 Enter the Total electricity spend", min_value=0)
charge_per_unit = st.number_input("⚡ Enter the charge per unit", min_value=0)
persons = st.number_input("👥 Enter the number of persons living in room/flat", min_value=1)

if st.button('💰 Calculate'):
    # Calculations
    total_bill = electricity_spend * charge_per_unit
    output = (rent + food + total_bill) // persons
    
    # Display result with custom font style
    st.markdown(f"<p class='custom-font'>Each person should pay = 💸 {output}</p>", unsafe_allow_html=True)
