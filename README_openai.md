docker build -f Dockerfile_openai -t whisper-api-openai .

docker run -p 8000:8000 \
  -e OPENAI_API_KEY=sk-你的金鑰 \
  whisper-api-openai