import streamlit
import pandas
import snowflake.connector
streamlit.title('My Mon\'s New Healthy Dinner.')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), [1,2])
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on the page
streamlit.dataframe (fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize (fruityvice response.json())
  return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?') if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
else:
  back from function = get_fruityvice_data(fruit_choice) 
  streamlit.dataframe (back_from_function)
# streamlit.header("Fruityvice Fruit Advice!")

# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe (fruityvice_normalized)
# except URLError as e:
#   streamlit.error()

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# #streamlit.text(fruityvice_response.json())

# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)

# don't run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)

my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe (my_data_row)

fruit_choice1 = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
