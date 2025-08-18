# 1) Base Python image
FROM python:3.11-slim

# 2) Work directory inside the container
WORKDIR /app

# 3) Speed/behavior envs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# 4) OS packages (compiler etc.) then clean up to keep image small
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5) Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy your project files
COPY . .

# 7) Start server: Daphne (ASGI) for Django Channels/WebSockets
# Tell Render what port this container listens on
# Tell Render which port we listen on
# 7) Start server: Daphne (ASGI) for Django Channels/WebSockets
EXPOSE 10000

# Run migrations + collectstatic before starting Daphne
CMD ["sh", "-c", "cd atomxAI && \
  python manage.py migrate && \
  python manage.py collectstatic --noinput && \
  daphne -b 0.0.0.0 -p ${PORT:-10000} atomxAI.asgi:application"]
