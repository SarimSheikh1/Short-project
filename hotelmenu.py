import streamlit as st

menu = {
    '🍕 Pizza': 800,
    '🍔 Burger': 300,
    '🍜 Noodles': 200,
    '🥤 Coke': 100,
    '💧 Water': 50,
    '🍵 Tea': 60,
    '☕ Coffee': 130,
    '🍟 Fries': 200,
    '🥪 Sandwich': 350,
    '🥚 Egg': 100,
    '🍝 Pasta': 350,
    '🥗 Salad': 180,
    '🌯 Chicken Wrap': 250,
    '🧄 Garlic Bread': 150,
    '🍦 Ice Cream': 90,
    '🍫 Chocolate Cake': 150,
    '🍗 Grilled Chicken': 400,
    '🐟 Fish and Chips': 750,
    '🌮 Tacos': 320,
    '🥟 Spring Rolls': 140,
    '🧀 Nachos': 180,
    '🥛 Milkshake': 200,
    '🧁 Muffin': 100,
    '🥤 Smoothie': 150,
    '🍩 Donut': 80,
}

st.title("🍽️ Welcome to Sarim Sheikh Hotel")
st.write("Here's our menu:\n")

# Display the menu items with emojis
for item, price in menu.items():
    st.write(f"{item}: {price} 💸")

order_total = 0

# Input for first item
item_1 = st.text_input("Enter the name of the item you want to order 🍽️:")

if st.button("🛒 Add First Item"):
    if item_1 in menu:
        order_total += menu[item_1]
        st.write(f"✅ Your item **{item_1}** has been added to your order")
    else:
        st.write(f"❌ Sorry, **{item_1}** is not available in our menu")

# Option to add another item
if st.checkbox("🛒 Do you want to add another item?"):
    item_2 = st.text_input("Enter the name of the second item 🍽️:")

    if st.button("🛒 Add Second Item"):
        if item_2 in menu:
            order_total += menu[item_2]
            st.write(f"✅ Your item **{item_2}** has been added to your order")
        else:
            st.write(f"❌ Sorry, **{item_2}** is not available in our menu")

# Display the total bill with emojis
st.write(f"💰 Your total bill amount to be paid is: **{order_total}** 💵")
