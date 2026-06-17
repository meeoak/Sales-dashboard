# EP01 테스트 제작 키트 — 러브바밍 (한국어 Brian 톤 · 사례 재구성)

> 목표: 이 키트로 **15~20분 안에 테스트용 쇼츠 1편** 완성. 9:16 · ≈58초.
> 동봉: `EP01.srt`(자막), `EP01-animatic.html`(타이밍 미리보기). 대본/SSML/설명란/QA는 `EP01-love-bombing.md`.

## 0) 준비물
- TTS 도구(택1): Naver CLOVA Voice·Dubbing / ElevenLabs / MS Azure(`ko-KR-InJoonNeural`)
- 이미지 생성(택1): Midjourney / Flux / Ideogram / Canva
- 편집기: CapCut(무료, 9:16·자막·오디오 임포트 지원)
- 음원: 편집기/플랫폼의 **로열티 프리·상업용** 라이브러리

## 1) 음성 만들기 (Brian 톤)
- `EP01-love-bombing.md`의 SSML 블록을 TTS에 입력(또는 보이스 대본 + rate↓·pitch↓·평탄 설정).
- 깊고 차분한 남성, 느린 속도. MP3로 내보내기(≈58초).

## 2) 이미지 5장 만들기 (페이스리스 · 9:16 · 얼굴/실존 브랜드 없음)
공통 네거티브: `no faces, no real person, no brand logos, no readable text, no watermark`
- **S1 (0–6s):** `cozy warm-lit cafe table, two coffee cups, soft bokeh, a phone glowing with many message notifications, golden warm tones, vertical 9:16, photoreal, no faces`
- **S2 (6–18s):** `an overflowing bouquet of red roses and gift boxes on a table, a phone full of affectionate message bubbles, warm abundant golden light, vertical 9:16, no faces, no readable text`
- **S3 (18–33s):** `same cafe but cold blue tones, wilting roses, rain on the window, a dim phone with a harsh grey message bubble, melancholic, vertical 9:16, no faces, no readable text`
- **S4 (33–48s):** `a lone unidentifiable silhouette sitting by a rainy window at night, cold blue moody light, reflective, empty space for text, vertical 9:16`
- **S5 (48–58s):** `a small warm light returning in a dark room, open window at dawn, soft hopeful glow, calm, vertical 9:16, no faces`
- 사실적 AI 이미지이므로 업로드 시 **AI 라벨 ON**.

## 3) 조립 (CapCut 기준)
1. 새 프로젝트 → 9:16, 1080×1920.
2. 이미지 5장을 타임코드대로 배치(각 장 느린 줌=Ken Burns). 색이 따뜻함→차가움→희망으로 흐르게.
3. 1)의 음성 MP3를 0:00에 임포트.
4. **자막: `EP01.srt` 임포트**(CapCut: 자막→가져오기) 또는 자동자막 후 교정. 스타일: 굵은 흰색·하단·외곽선.
5. 0:00~0:08 상단에 작은 라벨 카드 **"사례 재구성 · 특정 인물과 무관"**.
6. 로열티 프리 음악 추가(내레이션 대비 -16~-18dB). **0:18에 단조로 전환**, **0:48에 부드럽게 풀어주기**.
7. SFX: 초반 알림음 몇 번, 0:18 전환에 낮은 톤 1회, 잔잔한 빗소리 앰비언스(S3).
8. 0:53~0:58 하단에 도움 자막 **"여성긴급전화 1366 · 자살예방 109"** + 구독/다음편 예고.
9. 내보내기: 1080×1920, 30fps, H.264, 고비트레이트.

## 4) 업로드 (테스트는 '비공개' 또는 '일부공개' 권장)
- **AI 콘텐츠 라벨 ON**(합성 음성 + AI 이미지).
- 제목/설명란/해시태그/고정댓글: `EP01-love-bombing.md` 그대로 복사. 설명란에 **재구성 고지** 포함됨.
- 먼저 비공개로 올려 **첫 3초 이탈·가독성·자막 싱크·음량** 체크 → 수정 → 공개.

## 5) 테스트 체크 (이번 편 한정)
- [ ] 음성-자막 싱크 OK / 자막 가독성 OK
- [ ] 첫 3초에 "완벽했다→반전" 약속이 보이는가
- [ ] 색감 전환(따뜻→차가움→희망)이 감정선과 맞는가
- [ ] AI 라벨 ON · 재구성 고지 · 도움 자원 자막 포함
- [ ] 얼굴/실존 브랜드/실명 없음 · 음원 라이선스 OK
- [ ] 길이 ≈45–60초 · 9:16
