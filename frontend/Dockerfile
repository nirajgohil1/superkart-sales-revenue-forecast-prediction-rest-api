FROM python:3.9-slim

# Working directory inside the container
WORKDIR /app

# Copy frontend files into the container
COPY . .

# Install frontend dependencies
RUN pip3 install -r requirements.txt

# Launch Streamlit on port 8501, reachable externally
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]
