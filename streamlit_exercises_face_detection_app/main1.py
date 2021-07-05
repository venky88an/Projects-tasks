import streamlit as st
from PIL import Image
import cv2
from matplotlib import pyplot as plt
uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg', "jpg", "tiff"])

if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)

image_file=uploaded_file

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img

img1 = load_image(image_file)
st.image(img1)