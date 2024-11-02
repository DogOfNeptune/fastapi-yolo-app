from ultralytics import YOLO
from PIL import Image  

# Define a class to handle YOLOv8 model operations
class model_yolo8:
    # Initialize the model with a specified path and optional dataset YAML configuration
    def __init__(self, model_path: str, dataset_yaml: str = None):
        self.model = YOLO(model_path)  # Load the YOLO model from the given path
        self.dataset_yaml = dataset_yaml  # Optional YAML configuration for dataset

    # Alternative constructor (note: this will override the previous __init__ if left as-is)
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)  # Load the YOLO model from the given path

    # Train the model with specified parameters
    def train(self, device: str, epochs=80, imgsz=800, batch=16, workers=4):
        # Start model training with the given configuration parameters
        self.model.train(dataset_yaml=self.dataset_yaml, imgsz=imgsz, batch=batch, epochs=epochs, workers=workers, device=device)

    # Evaluate the model and return the evaluation metrics
    def evaluate(self):
        metrics = self.model.val()  # Run model validation
        return metrics  # Return evaluation metrics

    # Save the model to a specified path
    def save(self, save_path: str):
        self.model.save(save_path)  # Save model weights to the specified path

    # Perform prediction on a given image and return the results
    def predict(self, image: Image):
        results = self.model(image)  # Run the model on the input image
        return results  # Return the prediction results
