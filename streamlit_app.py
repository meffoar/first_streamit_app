import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Otameal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Egg')
streamlit.text('🥑🍞 Avacodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_cav("https://uni-lab-files.s3.us.west-2.amaxonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
