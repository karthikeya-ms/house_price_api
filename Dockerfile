# Use an official Python runtime as a base image
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy poetry files first (force explicit paths)
COPY ./pyproject.toml ./poetry.lock ./

# Copy the scripts folder
COPY ./scripts ./scripts

# Ensure models directory exists before copying
RUN mkdir -p models
COPY ./models ./models





# Install Poetry and dependencies
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root 

# Expose the FastAPI port
EXPOSE 8000

# Command to start the FastAPI application
CMD ["poetry", "run", "uvicorn", "scripts.api:app", "--host", "0.0.0.0", "--port", "8000"]
