# Import the FastAPIApp class from the backend.core.FastAPIApp module
from backend.core.FastAPIApp import FastAPIApp

# Create an instance of the FastAPI application
fastapi_app = FastAPIApp()

# Run the application if this script is executed directly
if __name__ == "__main__":
    fastapi_app.run()