import streamlit as st
import numpy as np
from PIL import Image
from Image_restoration import apply_restoration, apply_morphology
import operations as op
import histogram as hs
import my_segmentation as seg
import filters as fl
import cv2
# =========================
st.title("Image Processing 🖼️")
# =========================

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.image(img, caption="Original Image", use_container_width=False)

    # =========================
    module = st.selectbox("Choose Module", [
        "Point Operations",
        "Histogram & Color Image Operations",
        "Segmentation & Edge",
        "Neighborhood Operations",
        "Image Restoration",
        "Mathematical Morphology"
    ])

    result = None

    # =========================
    # OPERATIONS (op)
    # =========================
    if module == "Point Operations":

        option = st.selectbox("Choose Operation", [
            "Addition",
            "Subtraction",
            "Division",
            "Complement"
        ])

        value = st.slider("Value", 1, 100, 50)

        if option == "Addition":
            result = op.addition(img, value)

        elif option == "Subtraction":
            result = op.subtraction(img, value)

        elif option == "Division":
            result = op.division(img, value / 10)

        elif option == "Complement":
            result = op.complement(img)

    # =========================
    # HISTOGRAM (hs)
    # =========================
    elif module == "Histogram & Color Image Operations":

        option = st.selectbox("Choose Operation", [
            "Increase Red",
            "Swap R & G",
            "Remove Red",
            "Gray",
            "Stretch",
            "Equalization"
        ])

        if option == "Increase Red":
            result = hs.increase_red(img)

        elif option == "Swap R & G":
            result = hs.swap_rg(img)

        elif option == "Remove Red":
            result = hs.remove_red(img)

        elif option == "Gray":
            result = hs.to_gray(img)

        elif option == "Stretch":
            result = hs.histogram_stretch(hs.to_gray(img))

        elif option == "Equalization":
            result = hs.histogram_equalization(hs.to_gray(img))

    # =========================
    # SEGMENTATION
    # =========================
    elif module == "Segmentation & Edge":

        option = st.selectbox("Choose Operation", [
            "Global Threshold",
            "Otsu Threshold",
            "Adaptive Threshold",
            "Sobel Edge"
        ])

        if option == "Global Threshold":
            result = seg.global_threshold(img)

        elif option == "Otsu Threshold":
            result = seg.otsu_threshold(img)

        elif option == "Adaptive Threshold":
            result = seg.adaptive_threshold(img)

        elif option == "Sobel Edge":
            result = seg.sobel_edge(img)

    elif module == "Image Restoration":

        img_gray = np.array(image.convert("L"))
        
        noise_type = st.selectbox("Select noise type:", ["Salt and pepper noise", "Gaussian noise"])
        
        if noise_type == "Salt and pepper noise":
            method = st.selectbox("Select filter:", ["Average filter", "Median filter", "An outlier method"])
        else:
            method = st.selectbox("Select filter:", ["Image averaging", "Average filter"])
            
        if st.button("Apply Restoration"):
            result = apply_restoration(img_gray, noise_type, method)        
    elif module == "Mathematical Morphology":
        img_gray = np.array(image.convert("L"))
        
        method = st.selectbox("Select operation:", ["Image dilation", "Image erosion", "Image opening", "Boundary Extraction"])
        
        sub_method = None
        if method == "Boundary Extraction":
            sub_method = st.radio("Select extraction type:", ["Internal boundary", "External boundary", "Morphological gradient"])
        
        if st.button("Apply Morphology"):
            result = apply_morphology(img_gray, method, sub_method)
   
    #--------------FILTERS (Neighborhood Operations)-----------
    elif module == "Neighborhood Operations":
        
        category = st.selectbox("Select Filter Category:", ["Linear Filters", "Non-Linear Filters"])

        if category == "Linear Filters":
            option = st.selectbox("Choose Linear Filter", ["Average", "Laplacian"])
            
            if option == "Average":
                result = fl.avg_filter(img)
            elif option == "Laplacian":
                result = fl.laplacian_filter(img)

        elif category == "Non-Linear Filters":
            option = st.selectbox("Choose Non-Linear Filter", ["Max", "Median", "Min", "Mode"])
            
            if option == "Max":
                result = fl.max_filter(img)
            elif option == "Median":
                result = fl.median_filter(img)
            elif option == "Min":
                result = fl.min_filter(img)
            elif option == "Mode":
                with st.spinner("Processing Mode Filter..."):
                    result = fl.mode_filter(img)

  
    #---------- DISPLAY RESULT (BEFORE / AFTER)-------------
   
    if result is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(img, use_container_width=True)
        with col2:
            st.subheader("Processed Image")
            st.image(result, use_container_width=True)

        st.success("Operation Applied Successfully ✅")