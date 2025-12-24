
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
WORKDIR /app
COPY requirements.txt .
RUN apt update && apt install -y python3 python3-pip ffmpeg
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD ["python3", "ui/gradio_app.py"]
