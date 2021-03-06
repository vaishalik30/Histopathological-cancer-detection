# -*- coding: utf-8 -*-
"""Histo app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d7LrgWPLE-02jW_4cu_b_5QVGdbty0eq
"""

import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import streamlit as st
from PIL import Image  
import PIL 

st.title("Histopathological cancer detection")

model = load_model('C:/Users/vaish/OneDrive/Desktop/Spring 20/Project/saved_model.h5')
IMAGE_SIZE = 96
datagen = ImageDataGenerator(rescale=1.0/255)


scan_image  = st.file_uploader("Choose a scan:", type="tif")

    
if (scan_image):
    im1 = Image.open(scan_image)
    im1 = im1.save("C:/Users/vaish/OneDrive/Desktop/Spring 20/Project/Sample/One/Scanned_Image.tif")


    test_path = 'C:/Users/vaish/OneDrive/Desktop/Spring 20/Project/Sample'

    test_gen = datagen.flow_from_directory(test_path,
                                            target_size=(IMAGE_SIZE,IMAGE_SIZE),
                                            batch_size=1,
                                            class_mode='categorical',
                                            shuffle=False)
                                            

    num_test_images = 1



    pred = model.predict_generator(test_gen, steps=num_test_images, verbose =1)
    df_preds = pd.DataFrame(pred, columns=['no_tumor', 'has_tumor'])

    st.write("The Probability of metastasised cancer is: ", df_preds['has_tumor'])

    st.write("The Probability of no cancer tumor is: ", df_preds['no_tumor'])

    st.bar_chart(df_preds,width=0, height=0, use_container_width=True)


