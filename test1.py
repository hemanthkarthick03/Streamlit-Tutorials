import matplotlib
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time 

# Title
st.title("This is the App Title")  # Capitalized for clarity

# Subheader and Caption
st.subheader("This is the Subheader")

# Markdown (Header corrected to Markdown format)
st.markdown("This is the Markdown Header")  # Correctly uses markdown

# Text with Write Function
st.write("This is the write")  # Use st.write for general text

st.caption("This is the Caption")

# LaTeX Equation
st.latex(r"""a + a r^1 + a r^2 + a r^3""")  # Corrected spacing for exponent

code = """
def check_positive_negative(number):
  #Checks if a number is positive, negative, or zero.
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

# Example usage with user input
user_number = st.number_input("Enter a number:", min_value=float('-inf'), max_value=float('inf'))
result = check_positive_negative(user_number)
st.write(f"The number {user_number} is {result}.")
"""

st.code(code, language="python")  # Specify language for syntax highlighting


# Image (Assuming "kid.jpg" is in the same directory)
st.image("kid.jpg", width=300)  # Corrected width for image

# No return statement needed in Streamlit apps


# Checkbox
selected_anime = st.multiselect("Select your favorite anime:", ('One Piece', 'Naruto', 'Bleach'))

if selected_anime:
  st.write(f"You selected these anime: {', '.join(selected_anime)}")  # Join selected options with comma and space
is_checked = st.checkbox('Yes')
if is_checked:
    st.write("You checked the checkbox!")

# Button
clicked = st.button('Click')
if clicked:
    st.write("You clicked the button!")

# Radio Button
gender_radio = st.radio("Pick your gender:", ('Male', 'Female'))
st.write("You selected:", gender_radio)

# Selectbox
gender_select = st.selectbox("Pick your gender:", ('Male', 'Female'))
st.write("You selected:", gender_select)

# Multiselect
selected_planets = st.multiselect('Choose a planet (or planets)', ('Jupiter', 'Mars', 'Neptune'))
st.write("You selected:", selected_planets)

# Select Slider
mark_select_slider = st.select_slider("Pick a mark:", ('Ugly', 'Bad', 'Good', 'Excellent'))
st.write("You selected:", mark_select_slider)

# Slider
number_slider = st.slider("Pick a number:", 0, 50)
st.write("You selected:", number_slider)

# User Input Elements
number = st.number_input('Pick a number', min_value=0, max_value=10)
email = st.text_input('Email address')
travel_date = st.date_input('Travelling date')
school_time = st.time_input('School time')
description = st.text_area('Description')
photo = st.file_uploader('Upload a photo')
favorite_color = st.color_picker('Choose your favorite color')

# Display user input (optional)
if number is not None:  # Check if user entered a value
    st.write(f"You picked the number: {number}")
if email:
    st.write(f"Your email address: {email}")
if travel_date:
    st.write(f"Your travel date: {travel_date}")
if school_time:
    st.write(f"Your school time: {school_time}")
if description:
    st.write(f"Description: {description}")
if photo is not None:
    st.write(f"Photo uploaded: {photo.name}")  # Access file name
if favorite_color:
    st.write(f"Your favorite color: {favorite_color}")

st.balloons()  # Show celebratory balloons (optional)

with st.spinner('Wait for it...'):  # Show a loading spinner
    st.progress(10)  # Update progress bar to 10%
    time.sleep(10)  # Simulate a 10-second long process

# Code to execute after the wait
st.success("Done!")  # Display success message (optional)

import streamlit as st

# Success Message
st.success("You did it!")

# Error Message
st.error("Error")  # Typo corrected to "error"

# Warning Message
st.warning("Warning")  # Typo corrected to "warning"

# Informational Message
st.info("It's easy to build a Streamlit app")

# # Exception Handling (Simulating an Error)
# try:
#   raise RuntimeError("RuntimeError exception")  # Simulate an error
# except RuntimeError as e:
#   st.exception(e)  # Display the exception with st.exception


def generate_histogram(mean=1, std=2, num_samples=20, bins=15):
  """Generates a random normal distribution and creates a histogram."""
  rand = np.random.normal(mean, std, size=num_samples)
  fig, ax = plt.subplots()
  ax.hist(rand, bins=bins)
  return fig

# User input options (optional)
mean = st.sidebar.number_input("Mean (μ)",value=1.0)
std = st.sidebar.number_input("Standard Deviation (σ)", min_value=0.0, value=2.0)
num_samples = st.sidebar.number_input("Number of Samples", min_value=1, value=20)
bins = st.sidebar.number_input("Number of Bins in Histogram", min_value=1, value=15)

# Generate and display the histogram
fig = generate_histogram(mean, std, num_samples, bins)
st.pyplot(fig)

df = pd.DataFrame(
    np.random.randn(10, 2),  # Generate random data (10 rows, 2 columns)
    columns=['x', 'y']        # Assign column names 'x' and 'y'
)

st.line_chart(df)  # Display the line chart using the DataFrame

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

st.bar_chart(df)

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

st.area_chart(df)

df = pd.DataFrame(
    np.random.randn(500, 3),
    columns=['x', 'y', 'z']
)

c = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y',
    size='z',
    color='z',
    tooltip=['x', 'y', 'z']
)

st.altair_chart(c, use_container_width=True)

import streamlit as stimport graphviz as graphvizst.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')