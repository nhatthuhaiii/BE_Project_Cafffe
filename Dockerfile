FROM python:3.10-slim

# Cài đặt biến môi trường tránh hỏi YES/NO trong quá trình cài đặt
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Tạo và chuyển vào thư mục làm việc
WORKDIR /app

# Copy toàn bộ mã nguồn
COPY . .

# Cài đặt dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose cổng cho FastAPI
EXPOSE 80

# Lệnh chạy FastAPI với uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
