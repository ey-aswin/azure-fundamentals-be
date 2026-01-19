FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
# --- IGNORE ---
# This file is used to specify files and directories that should be ignored by Git.
# It helps to keep the repository clean by excluding unnecessary files such as      




