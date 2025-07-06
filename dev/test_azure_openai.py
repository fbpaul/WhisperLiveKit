import requests
import os

# ==== 替換為你的 Azure OpenAI 設定 ====
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "https://your-resource.openai.azure.com")
AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY", "your-api-key")
AZURE_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "your-deployment-name")
AZURE_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION", "2023-12-01-preview")

# ==== 測試音訊檔（確保存在） ====
AUDIO_FILE_PATH = "test.m4a"  # 可為 .mp3, .m4a, .webm, .mp4, .mpeg, .mpga, .wav

if not os.path.exists(AUDIO_FILE_PATH):
    raise FileNotFoundError(f"找不到音訊檔：{AUDIO_FILE_PATH}")

# ==== 發送請求 ====
url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT_NAME}/audio/transcriptions?api-version={AZURE_API_VERSION}"

headers = {
    "api-key": AZURE_OPENAI_API_KEY,
}

files = {
    "file": (os.path.basename(AUDIO_FILE_PATH), open(AUDIO_FILE_PATH, "rb"), "audio/wav"),
    "model": (None, "whisper-1"),
    "language": (None, "en"),  # 或 "zh"、"auto"
}

response = requests.post(url, headers=headers, files=files)

# ==== 顯示結果 ====
if response.status_code == 200:
    print("✅ 成功！轉錄結果：")
    print(response.json()["text"])
else:
    print(f"❌ 發生錯誤！HTTP {response.status_code}")
    print(response.text)
