# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN uv sync --frozen --no-install-project --no-dev

# Add the rest of the project source code and install it
RUN uv sync --frozen --no-dev

# Ensure the virtual environment's bin directory is in the PATH
ENV PATH="/app/.venv/bin:$PATH"

#Expose FastAPI port
EXPOSE 8000

# Run FastAPI with the correct command
ENTRYPOINT ["/app/.venv/bin/uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]