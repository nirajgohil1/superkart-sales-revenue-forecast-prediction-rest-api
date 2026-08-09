FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all backend files into the container
COPY . .

# Install dependencies without caching to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Start the API with Gunicorn: 4 workers, bound to port 7860 on all interfaces
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_api"]
