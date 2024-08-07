FROM python:3.10-slim
LABEL authors="mundiaem"
WORKDIR /app

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

# Expose the application port
EXPOSE 5001

CMD ["python", "app.py"]

