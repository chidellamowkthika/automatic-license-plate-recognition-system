import streamlit as st
from PIL import Image 
import os

st.header("licence number plate recognition system")
src_file=st.file_uploader("upload car image",type=["png","jpg","jpeg"])
def load_image(image_file):
    img=Image.open(image_file)
    return img

if src_file is not None:
    file_details={
        "filename": src_file.name,
        "filetype": src_file.type,
        "filesize": src_file.size
    }
    st.write(file_details)
    st.image(load_image(src_file),width=250)

    with open(os.path.join("inputs","car.jpg"),"wb") as f:
        f.write(src_file.getbuffer())
    
    



