
# Image Processing App - Gaussian Blur with Histogram

This project is part of the course **241-353 ART INTELL ECOSYSTEM MODULE**

This project is an image processing application developed with Streamlit for applying Gaussian Blur and displaying the image's Histogram.

Created by: 6610110341 สุธินันท์ รองพล

## Features

-   **📷 Webcam Capture**: เปิดกล้องและถ่ายรูปแบบ real-time
-   **🌐 Internet URL**: นำเข้าภาพจาก URL บนอินเทอร์เน็ต
-   **📂 File Upload**: อัปโหลดไฟล์ภาพจากอุปกรณ์ (JPG, JPEG, PNG)
-   **🛠️ Gaussian Blur Processing**: ปรับระดับการเบลอภาพด้วย Gaussian Blur
-   **📊 Histogram Visualization**: แสดงกราฟ histogram ของค่าความเข้มของสีในภาพ
-   **Interactive Controls**: ปรับค่า kernel size สำหรับ Gaussian Blur แบบ real-time

## Prerequisites

-   Python 3.8 or higher
-   Poetry (Python dependency management tool)
-   Required libraries: OpenCV, Streamlit, NumPy, Matplotlib

## Installation

### 1. Clone the Repository

Choose either HTTPS or SSH method:

**HTTPS:**

```bash
git clone https://github.com/Suthinxn/streamlit_learn.git

```

**SSH:**

```bash
git clone git@github.com:Suthinxn/streamlit_learn.git

```

### 2. Navigate to Project Directory

```bash
cd image-processing-app

```

### 3. Install Dependencies

```bash
poetry install

```

### 4. Activate Virtual Environment

```bash
poetry shell

```

## Running the Application

### 1. Start the Streamlit Server

```bash
poetry run streamlit run main.py

```

### 2. Access the Application

Open your web browser and navigate to:

```
http://localhost:8XXX/

```

## How to Use

1.  **Select Image Source**: Choose from three options in the sidebar:
    
    -   📷 **Webcam**: Capture image using your camera
    -   🌐 **Internet URL**: Enter a URL to load image from the web
    -   📂 **Upload File**: Upload an image file from your device
2.  **Adjust Blur Settings**: Use the slider in the sidebar to adjust the Gaussian Blur kernel size (1-31, odd numbers only)
    
3.  **View Results**:
    
    -   Original image will be displayed first
    -   Gaussian blurred image will be shown below
    -   Color histogram of the blurred image will be plotted at the bottom

## Project Structure

```
image-processing-app/
│   
├── main.py                                 # Main application file
├── poetry.lock                            # Poetry lock file
├── pyproject.toml                         # Poetry configuration
└── README.md                              # This file

```

## Libraries Used

-   **OpenCV (cv2)**: Image processing operations
-   **Streamlit**: Web application framework
-   **NumPy**: Numerical computations
-   **Matplotlib**: Plotting histograms
-   **urllib**: URL image loading

## Features Explanation

### Gaussian Blur

Gaussian Blur is a image processing technique that reduces image noise and detail by applying a Gaussian function. The kernel size parameter controls the intensity of the blur effect - larger values create more blur.

### Histogram Analysis

The application displays a color histogram showing the distribution of pixel intensities for each color channel (Red, Green, Blue) in the processed image, helping users understand the tonal distribution in their images.

## Development

If you're using an IDE, make sure to select the Python interpreter from the virtual environment created by Poetry.

## Troubleshooting

-   **Port already in use**: If port 8501 is already in use, Streamlit will automatically try to use another available port
-   **Dependencies issues**: Run `poetry install` again to ensure all dependencies are properly installed
-   **Camera access**: Make sure your browser allows camera access for the webcam feature
-   **Image loading errors**: Ensure URLs are accessible and image files are in supported formats (JPG, JPEG, PNG)

## Contributing

1.  Fork the repository
2.  Create a feature branch
3.  Make your changes
4.  Submit a pull request

