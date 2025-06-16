import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.header("Image Resizer")
uploaded_img=st.file_uploader("Upload/Drag your file here..",type=["jpg","jpeg","png"])

if uploaded_img:

    img=Image.open(uploaded_img)
    array_image=np.array(img)
    st.image(array_image,caption="Original Image",width=100)

    width=st.number_input("enter width",min_value=1,value=array_image.shape[1])
    height=st.number_input("enter height",min_value=1,value=array_image.shape[0])

    flip_value=st.selectbox("Direction",["None","Vertical","Horizontal"])
    if flip_value=="Vertical":
        flip_image=cv2.flip(array_image,0)
        array_image=flip_image
    elif flip_value=="Horizontal":
        flip_image=cv2.flip(array_image,1)
        array_image=flip_image
    st.image(array_image,caption="filped image",width=100)

    if st.button("Resize"):
        resized_img=cv2.resize(array_image,(int(width),int(height)))
        st.image(resized_img,caption="Resized",width=200)

            buff=io.BytesIO()
            image_pil=Image.fromarray(resized_img)
            image_pil.save(buff,format="jpeg")
            st.download_button("Download here",data=buff.getvalue(),mime="image/jpeg",file_name="resized_image_from_jayApp.jpeg")
