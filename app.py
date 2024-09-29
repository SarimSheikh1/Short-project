import streamlit as st

# Streamlit inputs with emojis
st.title("🏠 Rent Calculator")

rent = st.number_input("🏡 Enter your hostel/flat Rent", min_value=0)
food = st.number_input("🍽️ Enter the amount of food cost", min_value=0)
electricity_spend = st.number_input("💡 Enter the Total electricity spend", min_value=0)
charge_per_unit = st.number_input("⚡ Enter the charge per unit", min_value=0)
persons = st.number_input("👥 Enter the number of persons living in room/flat", min_value=1)

if st.button('💰 Calculate'):
    # Calculations
    total_bill = electricity_spend * charge_per_unit
    output = (rent + food + total_bill) // persons
    
    # Display result with emoji
    st.write(f"Each person should pay = 💸 {output}")
