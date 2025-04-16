# Streamlit App

# modules/libraries 
# print() -> function to display values 

import streamlit 

streamlit.title('My streamlit App')


# Get user input
name = streamlit.text_input("What's your name?")
hobby = streamlit.text_input("What's your favorite hobby?")

# Button to display message
if streamlit.button("Greet Me"):
    streamlit.success(f"Hello, {name}! Have fun with your hobby: {hobby}")

streamlit.header("🍎 Fruit List Viewer")
positions = [1, 2, 3]
fruits = ['mango', 'apple', 'guava', 'pineapple']

if streamlit.button("Show Fruits"):
    for pos, fruit in zip(positions, fruits):
        streamlit.write(f"In position {pos}, we have: {fruit}")
