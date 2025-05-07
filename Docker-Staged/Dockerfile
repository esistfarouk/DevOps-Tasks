FROM python:3.9-alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.9-alpine AS runtime

WORKDIR /app

# Copy the built dependencies from the backend-builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

# Copy the application code from the backend-builder stage
COPY --from=builder /app /app

EXPOSE 8000

CMD ["python", "app/main.py"]