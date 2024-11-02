# FastAPI YOLO App

## Project Description.

A FastAPI-based application for running YOLOv8 image processing with a frontend for visualizing the results. This application uses a pre-trained YOLO model to detect objects in images.

## Folder structure

```plaintext
fastapi-yolo-app/
├── backend/                     # Server-side code
│   ├── api/                     # FastAPI API endpoints
│   │   ├── __init__.py
│   │   └── endpoints.py         # Endpoint definitions for FastAPI
│   └── core/                    # Core configurations
│       ├── __init__.py
│       ├── FastAPIApp.py        # Class to initialize FastAPI app
│       └── PredictionResponse.py # Response schema for predictions
│
├── model/                       # Model and image processing files
│   ├── __init__.py
│   ├── yolov8.pt                # Pre-trained YOLOv8 model
│   ├── model_yolo8.py           # YOLO model loading and usage class
│   └── ImageHandler.py          # Image processing with YOLO
│
├── data/                        # Data and training files
│   ├── datasets/                # Training datasets
│   │   ├── images/              # Images for training
│   │   └── labels/              # Labels for images
│   └── dataset.yaml             # Image annotation file
│
├── frontend/                    # Frontend resources
│   ├── index.html               # Main HTML page
│   ├── script.js                # JavaScript for page functionality
│   └── styles.css               # CSS for page styling
│
├── main.py                      # Main entry point for the app
├── Dockerfile                   # Dockerfile for containerizing the app
├── README.md                    # Project description (this file)
├── requirements.txt             # Project dependencies
├── train_YOLO8.ipynb            # Jupyter notebook for model training
└── Config.py                    # Basic configuration settings for the entire system
```

## How to start a project

1. Install all dependencies from the file `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the server side:

   ```bash
   python backend/main.py
   ```
