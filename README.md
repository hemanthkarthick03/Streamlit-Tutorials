# Streamlit Tutorial
Creating a comprehensive Markdown page with Streamlit tutorials and code examples can help you get started with Streamlit effectively. Here's a step-by-step guide along with examples:

## Introduction
Streamlit is an open-source app framework for Machine Learning and Data Science teams. It turns data scripts into shareable web apps in minutes. 

## Installation
To install Streamlit, use pip:
```bash
pip install streamlit
```

## Basic Usage
Create a new Python file `app.py` and add the following code:
```python
import streamlit as st

st.title('Hello, Streamlit!')
st.write('Welcome to your first Streamlit app.')
```

Run the app using the following command:
```bash
streamlit run app.py
```

## Displaying Text
Streamlit provides various functions to display text.

### Title
```python
st.title('This is a title')
```

### Header
```python
st.header('This is a header')
```

### Subheader
```python
st.subheader('This is a subheader')
```

### Markdown
```python
st.markdown('This is **markdown** text')
```

### Write
```python
st.write('This is a write statement')
```

## Displaying Data
You can display data using several Streamlit functions.

### DataFrame
```python
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(df)
```

### Table
```python
st.table(df)
```

### JSON
```python
st.json({'name': 'John', 'age': 30})
```

## Widgets
Streamlit provides interactive widgets to make your app dynamic.

### Button
```python
if st.button('Say hello'):
    st.write('Hello!')
```

### Checkbox
```python
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
```

### Radio Buttons
```python
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
```

### Selectbox
```python
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
```

### Slider
```python
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

## Media
Streamlit can display various types of media.

### Image
```python
from PIL import Image

image = Image.open('path/to/image.jpg')
st.image(image, caption='Sunrise', use_column_width=True)
```

### Video
```python
video_file = open('path/to/video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
```

### Audio
```python
audio_file = open('path/to/audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
```

## Layout
Streamlit offers ways to control the layout of your app.

### Sidebar
```python
st.sidebar.title('Sidebar Title')
st.sidebar.write('Sidebar content')
```

### Columns
```python
col1, col2, col3 = st.columns(3)
col1.write('Column 1')
col2.write('Column 2')
col3.write('Column 3')
```

### Expander
```python
with st.expander("See explanation"):
    st.write("Here is the hidden content")
```

## Example App: Iris Dataset
Here's a complete example using the Iris dataset.

```python
import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Iris Dataset Viewer')

@st.cache
def load_data():
    return sns.load_dataset('iris')

df = load_data()

st.write("Here's the Iris dataset:")
st.dataframe(df)

st.write("Summary statistics:")
st.write(df.describe())

species = st.selectbox('Select species', df['species'].unique())
filtered_df = df[df['species'] == species]
st.write(f"Data for {species}:")
st.dataframe(filtered_df)
```

## Conclusion
This tutorial covered the basics of Streamlit, including text and data display, interactive widgets, and media display. With these tools, you can start building interactive web apps for your data projects.

For more information, visit the [Streamlit documentation](https://docs.streamlit.io/).
```

Save the above content as `Streamlit_Tutorial.md`. This file includes basic Streamlit functions with examples and explanations to get you started.
