# Image Processing Suite 🖼️

A comprehensive, interactive web application built with **Streamlit** and **OpenCV** that demonstrates essential Image Processing techniques. The application allows users to upload custom images and apply a wide array of transformations across multiple foundational sub-fields of computer vision.

---

## 🚀 Key Modules & Features

The suite is logically structured into six core operational modules:

### 1. Point Operations
Implements pixel-level arithmetic adjustments to alter contrast and brightness:
* **Addition & Subtraction:** Modifies image intensity values globally using configurable scalar values.
* **Division:** Globally scales down pixel values to darken or compress dynamic range.
* **Complement:** Performs a bitwise inversion (`NOT` operation) to generate the photographic negative of the image.

### 2. Histogram & Color Image Operations
Deals with spatial color tracking and enhancement:
* **Color Modifications:** Specialized channels adjustments such as increasing red intensity, removing red fully, or swapping the Red and Green channels entirely.
* **Grayscale Conversion:** Transforms native RGB images into single-channel luminance arrays.
* **Histogram Stretching & Equalization:** Automatically stretches or contrast-balances intensity distributions over the full 8-bit dynamic range.

### 3. Segmentation & Edge Detection
Features regional separation and edge extraction algorithms:
* **Thresholding Suites:** Includes manual Global Thresholding (fixed boundary at 127), automated data-driven **Otsu's Thresholding**, and spatially local **Adaptive Thresholding**.
* **Sobel Edge Detection:** Computes spatial gradients on both the horizontal (X) and vertical (Y) axes to isolate continuous object boundaries.

### 4. Neighborhood Operations (Filters)
Applies local spatial convolutions via structural windows:
* **Linear Filters:** Implements standard smoothing via an **Average Filter** box kernel and high-pass spatial sharpening using a **Laplacian Filter** kernel.
* **Non-Linear Filters:** Standard neighborhood sort filters including **Minimum**, **Maximum**, and native **Median** blurring, alongside a custom discrete local **Mode Filter**.

### 5. Image Restoration
Targeted at reconstructing structural components degraded by synthetic or natural artifacts:
* Alleviates **Salt and Pepper noise** utilizing precise spatial Adaptive Outlier methods, box blurring, or targeted median smoothing blocks.
* Counteracts **Gaussian noise** distribution envelopes using specialized Gaussian filtering kernels.

### 6. Mathematical Morphology
Advanced shape-based pixel transformations working over grayscale structural layouts:
* Native erosion, dilation, and structural opening passes.
* Dedicated **Boundary Extraction** sub-modes capable of rendering internal boundaries, external boundary margins, or full morphological gradients.

---

## 🛠️ Project Structure

The project relies on a modular architecture separating the Streamlit interface logic from backend algorithmic execution:
* `main.py` - The core Streamlit interface script handling UI components, image uploading layout, and dynamic visualization modules.
* `operations.py` - Core point processing arithmetic methods.
* `histogram.py` - Color operations, contrast stretching, and histogram equalization logic.
* `my_segmentation.py` - Binarization models (Global, Otsu, Adaptive) and gradient edge extractors.
* `filters.py` - Spatial linear and non-linear neighborhood convolution kernels.
* `Image_restoration.py` - Noise cancellation wrappers and mathematical morphological structures.

---

## 📦 Prerequisites & Installation

To run this application locally on your machine, follow these setup steps:

### 1. Install Dependencies
Make sure you have Python installed, then run the following command to install the required libraries:
```bash
pip install streamlit opencv-python numpy pandas scipy pillow
