import os
import requests
from dotenv import load_dotenv

# === OpenAI API 金鑰 ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("⚠️ 找不到 OPENAI_API_KEY，請確認 .env 是否存在且正確")

# === 選填：測試用的音訊檔（m4a/wav/mp3）===
AUDIO_FILE_PATH = "test.m4a"  # ← 請將這裡換成你的檔案路徑

# === 檢查檔案是否存在 ===
if not os.path.exists(AUDIO_FILE_PATH):
    raise FileNotFoundError(f"音訊檔案不存在：{AUDIO_FILE_PATH}")

# === OpenAI Whisper API 參數 ===
url = "https://api.openai.com/v1/audio/transcriptions"
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}
files = {
    "file": (os.path.basename(AUDIO_FILE_PATH), open(AUDIO_FILE_PATH, "rb"), "audio/m4a"),
    "model": (None, "whisper-1"),
    "language": (None, "zh"),  # 或可指定如 "en", "zh"
}

# === 發送 POST 請求 ===
response = requests.post(url, headers=headers, files=files)

# === 顯示結果 ===
if response.status_code == 200:
    print("✅ 成功！語音辨識結果：")
    print(response.json()["text"])
else:
    print(f"❌ 發生錯誤！HTTP {response.status_code}")
    print(response.text)
