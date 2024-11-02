import io  
from fastapi import APIRouter, UploadFile, File  
from fastapi.responses import StreamingResponse, FileResponse
from Config import Config  
from model.ImageHandler import ImageHandler  
from model.model_yolo8 import model_yolo8

# Create an API router instance
router = APIRouter()

# Initialize YOLO model and image handler
model = model_yolo8(Config.MODEL_PATH)  # Load model from the specified path
image_handler = ImageHandler(model)  # Initialize image handler with the loaded model

# Define an endpoint for image upload and processing
@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Process the uploaded image using ImageHandler
        prediction_response = await image_handler.process_image(file)
        # Return processed image as a PNG streaming response
        return StreamingResponse(io.BytesIO(prediction_response.get_image()), media_type='image/png')
    except Exception as e:
        # Return an error message in case of an exception
        return {"error": str(e)}

# Define an endpoint to serve the main HTML page
@router.get("/")
async def main():
    return FileResponse(Config.INDEX_HTML_DIR)  # Serve the index.html file from the frontend folder
