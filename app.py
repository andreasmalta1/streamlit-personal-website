import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image


st.set_page_config(page_title="My Webpage", page_icon=":tada", layout="wide")


def load_lottie(json_file):
    with open(json_file, "r") as file:
        json_data = json.load(file)
    return json_data


def local_css(file_name):
    with open(file_name) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottie("json_animations/coding.json")
img_pl_table = Image.open("images/pl_table.png")

# Header Section
with st.container():
    st.subheader("Hi, I'm Andreas :wave:")
    st.title("A Python Programmer from Malta")
    st.write("I'm interested in football")
    st.write("[Learn More](https://github.com/andreasmalta1)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("I work as a Pipeline Engineer in the VFX industry")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pl_table)
    with text_column:
        st.subheader("PL Tables")
        st.write("Generate custome Premier League Tables")
        st.markdown("[PL Table](https://pl-table.onrender.com)")

# Contact
with st.container():
    st.write("---")
    st.header("Contact")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/andreascalleja@gmail.com" method="POST">
        <input type="hidden" name="_captcha" calue=false>
        <input type="text" name="name" placeholder="Enter Your Name"required>
        <input type="email" name="email" placeholder="Enter Your Email Address" required>
        <textarea name="message" name="email" placeholder="Enter Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
