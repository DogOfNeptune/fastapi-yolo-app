class Config:
    # Path to the YOLOv8 model file
    MODEL_PATH = "model/yolov8.pt"
    
    # Server configuration
    HOST = "127.0.0.1"  # Server host address
    PORT = 8000  # Server port

    # Directory for serving static files, such as HTML, CSS, and JavaScript
    STATIC_FILES_DIR = "frontend"  

    # Directories for training and validation data
    TRAIN_IMAGES_DIR = 'data/datasets/images/train/'  # Directory for training images
    VAL_IMAGES_DIR = 'data/datasets/images/val/'      # Directory for validation images
    TRAIN_LABELS_DIR = 'data/datasets/labels/train/'  # Directory for training labels
    VAL_LABELS_DIR = 'data/datasets/labels/val/'      # Directory for validation labe
    
    # Directory for yaml files
    YAML_DIR = 'data/dataset.yaml'  # Directory for yaml files
    
    # Directory for index.html file
    INDEX_HTML_DIR = 'frontend/index.html'  # Directory for index.html file