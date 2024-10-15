FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn  # Add this line to install gunicorn
EXPOSE 5000
ENV FLASK_APP=CalorieEstimator.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "CalorieEstimator:app"]