import uvicorn  
from fastapi import FastAPI  
from fastapi.staticfiles import StaticFiles  
from backend.api.endpoints import router  
from Config import Config  

# Define a class to handle the FastAPI application setup and running
class FastAPIApp:
    # Initialize the FastAPI application and set up routes
    def __init__(self):
        self.app = FastAPI()  # Create a FastAPI instance
        self.setup_routes()  # Set up application routes

    # Method to configure application routes
    def setup_routes(self):
        # Mount a static files directory to serve frontend files
        self.app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

        # Include the API router for defining endpoint routes
        self.app.include_router(router)

    # Method to run the application with specified host and port
    def run(self, host=Config.HOST, port=Config.PORT):
        uvicorn.run(self.app, host=host, port=port)  # Run the FastAPI app with Uvicorn
