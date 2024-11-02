# Chose the base image
FROM python:3.10.11

# Set the working directory
WORKDIR /app

# Install dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy the requirements file and install the dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the code, excluding the "data" and file train_YOLO8.ipynb directory
COPY ./backend /app/backend
COPY ./model /app/model
COPY ./frontend /app/frontend
COPY ./main.py /app/main.py
COPY ./Config.py /app/Config.py

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the FastAPI app using main.py
CMD ["python", "main.py"]
