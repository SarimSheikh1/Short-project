import streamlit as st

menu = {
    '1. Pizza 🍕': 800,
    '2. Burger 🍔': 300,
    '3. Noodles 🍜': 200,
    '4. Coke 🥤': 100,
    '5. Water 💧': 50,
    '6. Tea 🍵': 60,
    '7. Coffee ☕': 130,
    '8. Fries 🍟': 200,
    '9. Sandwich 🥪': 350,
    '10. Egg 🥚': 100,
    '11. Pasta 🍝': 350,
    '12. Salad 🥗': 180,
    '13. Chicken Wrap 🌯': 250,
    '14. Garlic Bread 🧄': 150,
    '15. Ice Cream 🍦': 90,
    '16. Chocolate Cake 🍫': 150,
    '17. Grilled Chicken 🍗': 400,
    '18. Fish and Chips 🐟': 750,
    '19. Tacos 🌮': 320,
    '20. Spring Rolls 🥟': 140,
    '21. Nachos 🧀': 180,
    '22. Milkshake 🥛': 200,
    '23. Muffin 🧁': 100,
    '24. Smoothie 🥤': 150,
    '25. Donut 🍩': 80,
}

st.title("🍽️ Welcome to Sarim Sheikh Hotel")
st.write("Here's our menu:\n")

# Display the menu items
for item, price in menu.items():
    st.write(f"{item}: {price} 💸")  # Numbered list of items

# Initialize order totals
if 'order_total' not in st.session_state:
    st.session_state.order_total = 0
if 'first_item_total' not in st.session_state:
    st.session_state.first_item_total = 0
if 'second_item_total' not in st.session_state:
    st.session_state.second_item_total = 0

# Input for first item
item_number = st.number_input("Enter the number of the item you want to order 🍽️:", min_value=1, max_value=len(menu), step=1)

if st.button("🛒 Add First Item"):
    item_name = list(menu.keys())[item_number - 1]  # Get the item name based on the selected number
    st.session_state.first_item_total = menu[item_name]
    st.session_state.order_total += st.session_state.first_item_total
    st.write(f"✅ Your first item **{item_name}** has been added to your order. Price: {st.session_state.first_item_total} 💵")

# Display total for the first item
if st.session_state.first_item_total > 0:
    st.write(f"💰 Total for first item: **{st.session_state.first_item_total}** 💵")

# Option to add another item
if st.checkbox("🛒 Do you want to add another item?"):
    item_number_2 = st.number_input("Enter the number of the second item 🍽️:", min_value=1, max_value=len(menu), step=1)

    if st.button("🛒 Add Second Item"):
        item_name_2 = list(menu.keys())[item_number_2 - 1]  # Get the item name based on the selected number
        st.session_state.second_item_total = menu[item_name_2]
        st.session_state.order_total += st.session_state.second_item_total
        st.write(f"✅ Your second item **{item_name_2}** has been added to your order. Price: {st.session_state.second_item_total} 💵")

# Display total for the second item
if st.session_state.second_item_total > 0:
    st.write(f"💰 Total for second item: **{st.session_state.second_item_total}** 💵")

# Display the overall total bill
st.write(f"💰 Your total bill amount to be paid is: **{st.session_state.order_total}** 💵")

# Thank you message with emojis at the end
st.write("Thank you for your order! 😊🍽️ We hope you enjoy your meal! 🍴✨")
