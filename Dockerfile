FROM python:3.9-alpine@sha256:c549d512f8a56f7dbf15032c0b21799f022118d4b72542b8d85e2eae350cfcd7
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN adduser -D user
USER user
CMD ["python", "app.py"]
