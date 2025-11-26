# Example Dockerfile base - adapt to your existing Dockerfile
FROM python:3.11-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# run tests during build — will fail build if tests fail
RUN pytest -q

# final image
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /app /app
CMD ["python", "app.py"]   # adapt to your app entrypoint
