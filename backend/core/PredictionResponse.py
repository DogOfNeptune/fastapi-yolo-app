# Define a class for handling prediction responses
class PredictionResponse:
    # Initialize with an image in bytes format
    def __init__(self, image: bytes):
        self.image = image  # Store the image bytes

    # Method to retrieve the image bytes
    def get_image(self):
        return self.image  # Return the image in bytes format
