import io
from fastapi import HTTPException
from fastapi import UploadFile
from PIL import Image
import cv2
from backend.core.PredictionResponse import PredictionResponse
from model.model_yolo8 import model_yolo8

# Define a handler class for processing uploaded images using YOLOv8
class ImageHandler:
    # Initialize with a YOLO model instance
    def __init__(self, model: model_yolo8):
        self.model = model

    # Asynchronous method to process an uploaded image file
    async def process_image(self, file: UploadFile):
        # Check if the uploaded file is an image
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Invalid file type")  # Raise error for non-image files
        
        # Read the image data from the file
        image_bytes = await file.read()
        
        # Open the image using PIL for further processing
        image = Image.open(io.BytesIO(image_bytes))
        
        # Perform object detection with the YOLO model
        results = self.model.predict(image)  # Predict objects in the image
        output_image_np = results[0].plot()  # Generate output image with detections drawn

        # Convert the image from BGR to RGB format if needed
        output_image_np = cv2.cvtColor(output_image_np, cv2.COLOR_BGR2RGB)

        # Convert the NumPy array back to a PIL image format
        output_image = Image.fromarray(output_image_np)

        # Save the processed image to an in-memory bytes buffer as PNG
        output_image_bytes = io.BytesIO()
        output_image.save(output_image_bytes, format='PNG')  # Save in PNG format
        output_image_bytes.seek(0)  # Reset buffer position to start

        # Return a PredictionResponse object with the processed image bytes
        return PredictionResponse(output_image_bytes.getvalue())