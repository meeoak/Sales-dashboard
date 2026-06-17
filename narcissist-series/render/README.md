# EP01 렌더 키트 (자동 파이프라인)

`Sales-dashboard` 샌드박스에서 **EP01-animatic.mp4(무음 자막본)**를 실제로 생성·검증했습니다.
음성과 실제 장면 이미지를 더해 **EP01-final.mp4**까지 한 번에 만드는 스크립트입니다. (CapCut 수작업 대체)

## 구성
- `epkit.py` — 장면/자막 데이터 + 슬라이드 렌더 + ffmpeg 합치기(공용)
- `make_animatic.py` — 무음 자막 애니매틱(EP01-animatic.mp4) 생성 ✅ 검증됨
- `EP01.ssml` — Azure용 SSML (ko-KR-InJoonNeural, Brian 톤)
- `azure_tts.py` — SSML → `EP01-vo.mp3`
- `build_final.py` — 장면 이미지 + 음성(+음악) → `EP01-final.mp4`

## 사전 설치
```
pip install imageio-ffmpeg Pillow requests
```

## 1) 음성 만들기 (Azure)
Azure Portal에서 Speech 리소스 생성 → 키/지역 확인 후:
```
export AZURE_SPEECH_KEY=발급키
export AZURE_SPEECH_REGION=koreacentral
python3 azure_tts.py        # -> EP01-vo.mp3
```
(코드 없이 가려면: Azure Speech Studio → Audio Content Creation → EP01.ssml 붙여넣기 → mp3 내보내기)

## 2) 장면 이미지 준비
Canva 편집 링크에서 S1~S5 컷을 PNG로 받아 `render/assets/`에 저장:
`assets/s1.png … s5.png` (선택: `assets/music.mp3` 로열티 프리 배경음악)

## 3) 최종 영상
```
python3 build_final.py      # -> EP01-final.mp4 (1080x1920, 자막+음성+음악)
```

## 4) 업로드
- **AI 콘텐츠 라벨 ON** · 설명란에 "사례 재구성" 고지 · 도움 자막(1366·109)
- 표지 PNG를 썸네일로 · 먼저 비공개 점검 후 공개

## 타이밍 메모
자막 타임코드는 `epkit.py`의 `CAPTIONS`(=EP01.srt와 동일). 음성 길이가 58.5초와 크게 다르면
`CAPTIONS`의 시작/끝 초를 실제 음성에 맞춰 조정 후 `build_final.py` 재실행.
