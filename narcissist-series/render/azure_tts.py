"""Azure TTS: EP01.ssml -> EP01-vo.mp3 (ko-KR-InJoonNeural, Brian 톤).
사전: pip install requests
환경변수: AZURE_SPEECH_KEY, AZURE_SPEECH_REGION (예: koreacentral)
실행: python3 azure_tts.py
"""
import os, sys, requests

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ.get("AZURE_SPEECH_KEY")
REGION = os.environ.get("AZURE_SPEECH_REGION", "koreacentral")
if not KEY:
    sys.exit("AZURE_SPEECH_KEY 환경변수를 설정하세요. (Azure Speech 리소스 키)")

with open(os.path.join(HERE, "EP01.ssml"), "rb") as f:
    ssml = f.read()

url = f"https://{REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
headers = {
    "Ocp-Apim-Subscription-Key": KEY,
    "Content-Type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "audio-24khz-160kbitrate-mono-mp3",
    "User-Agent": "ep01-tts",
}
r = requests.post(url, headers=headers, data=ssml, timeout=60)
r.raise_for_status()
out = os.path.join(HERE, "EP01-vo.mp3")
with open(out, "wb") as f:
    f.write(r.content)
print("OK ->", out, f"({len(r.content)} bytes)")
