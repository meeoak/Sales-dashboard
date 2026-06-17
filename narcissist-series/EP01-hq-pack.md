# EP01 고품질 제작 팩 — 러브바밍 (한국어 Brian 톤 · 사례 재구성)

> 목표: 아래 에셋 + 턴키 설정으로 **폴리시드 MP4** 완성. 9:16 · ≈58초.
> 동봉 파일: `EP01.srt`(자막), `EP01-love-bombing.md`(대본/SSML/설명란/QA), `EP01-final-cut.html`(타이밍·낭독 미리보기).

## 1) 에셋 매니페스트 (Canva 생성 완료)
| 용도 | 편집 링크(영구) | PNG(만료 ~12–24h) |
|---|---|---|
| 표지/썸네일 | https://www.canva.com/d/UA6xttYZaWzLJIS | [download](https://export-download.canva.com/3DYaI/DAHMy23DYaI/-1/0/0001-4034606016611282703.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260616%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260616T105958Z&X-Amz-Expires=65039&X-Amz-Signature=6dd4a69b8e48f7e287d52330f1da246d09c0771b54081cfde5137bc0355b614b&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2017%20Jun%202026%2005%3A03%3A57%20GMT) |
| S1 따뜻한 시작 (0–6s) | https://www.canva.com/d/ePUICH8BR7Xf-9q | export job 25a33746 |
| S2 러브바밍 과잉 (6–18s) | https://www.canva.com/d/X7O41xwSC-YR4T2 | export job 76e77b77 |
| S3 전환·차가움 (18–33s) | https://www.canva.com/d/oxwnB88htFiUod9 | export job 26e88e0d |
| S4 깨달음·실루엣 (33–48s) | https://www.canva.com/d/2W5idYKq3gtDqV5 | export job 5b94dcdd |
| S5 희망·빛 (48–58s) | https://www.canva.com/d/aDe5ZQGcX9hA4QA | export job fd892a42 |
> PNG 직링크는 만료되므로, 각 편집 링크에서 본인 계정으로 저장 후 "공유→다운로드(PNG)"가 가장 안전. 텍스트가 끼었으면 편집에서 제거.

## 2) 음성 (Brian 톤) — 플랫폼별 턴키

### A. Microsoft Azure TTS (가장 정밀, SSML 그대로)
- 보이스: `ko-KR-InJoonNeural`(남성) 또는 `ko-KR-HyunsuMultilingualNeural`
- `EP01-love-bombing.md`의 SSML 블록 그대로 사용(rate -8% · pitch -2st · break 포함). MP3 24kHz↑로 내보내기.

### B. ElevenLabs (자연스러움)
- 모델: Multilingual v2 (또는 v3). Voice Library에서 **Korean + male + deep/calm** 오디션 후 선택.
- 세팅: Stability 55–60 · Similarity 80 · Style 0–15 · Speaker Boost ON · Speed ~0.9
- 입력: 아래 일반 텍스트(문장 사이 `<break time="0.6s"/>` 또는 줄바꿈으로 호흡).
```
처음 한 달은… 완벽했습니다. 그 사람은, 그게 사랑이라고 믿게 만들었죠.
매일 아침과 밤, 연락이 끊이지 않았습니다. 잦은 선물. 그리고 며칠 만에 — "넌 내 운명이야." 모든 것이 빠르고, 강렬했습니다.
그런데… 어느 순간부터, '완벽하다'던 바로 그 모습들을, 그 사람은 문제 삼기 시작했습니다. 칭찬이 비난으로 바뀌는 데에는… 오래 걸리지 않았습니다.
이건 빠른 사랑이 아니었습니다. '러브바밍'이라 불리는 패턴이었죠. 과한 애정으로 빠르게 의존하게 만든 뒤, 주도권을 가져가는 방식. 사랑은 속도가 아니라 — 일관성으로 증명됩니다.
혹시 지금, 비슷한 신호를 느끼고 있다면 — 그건 당신의 잘못이 아닙니다.
```

### C. Naver CLOVA Voice / Dubbing (한국어 발음 강점)
- **차분한 톤의 남성 내레이터** 보이스 오디션 후 선택. 속도 -10%, 톤 -1~-2.
- 문장별로 끊어 입력하고 사이에 정지(쉼) 추가. 상업 라이선스 플랜 사용.

> 공통: 깊은 저음 · 느린 속도 · 평탄한 감정 = Brian 느낌. 결과 길이가 58초와 다르면 4)에서 싱크 조정.

## 3) 음악 & SFX
- 음원(무료·상업 가능): **YouTube 오디오 보관함**("sad piano", "emotional ambient", "reflective cinematic") · **Pixabay Music** · **Uppbeat**. 단조·인스트루멘털·70–90 BPM.
- 큐 시트: 0:00 잔잔 → **0:18 단조로 전환(텐션)** → 0:33 고조 유지 → **0:48 부드럽게 해소**.
- SFX: S1–S2 알림음 몇 번 · 0:18 낮은 임팩트 톤 1회 · S3–S4 빗소리 앰비언스(약하게).
- 라우드니스: 내레이션 ≈ -16 LUFS, 음악은 그 아래 -20~-22 LUFS(덕킹), 최종 통합 ≈ -14 LUFS.

## 4) CapCut 고품질 조립
1. 새 프로젝트 1080×1920 · 30fps(또는 60).
2. 이미지 5장 타임라인 배치: S1 0–6 / S2 6–18 / S3 18–33 / S4 33–48 / S5 48–58. 각 장 **느린 줌(100→110%)**.
3. 0:18에 **따뜻→차가움 색 전환**(필터/온도). S1–S2 웜, S3–S4 쿨, S5 다시 웜.
4. 음성 MP3를 0:00에 임포트.
5. **자막: `EP01.srt` 임포트.** 굵은 흰색 + 검정 외곽선/그림자, 하단 15%, 세이프영역. (음성 길이가 다르면 자동자막으로 재생성해 싱크.)
6. 오버레이: 0:00–0:08 상단 "사례 재구성 · 특정 인물과 무관" · 0:53–0:58 하단 "여성긴급전화 1366 · 자살예방 109" + 구독/다음편 엔드카드.
7. 음악 트랙 추가(덕킹) + SFX.
8. 내보내기: 1080×1920 · H.264 · 30fps · 비트레이트 "높음"(≈16–20Mbps). 썸네일은 표지 PNG 사용.

## 5) 싱크 팁
TTS 길이가 58초와 다르면: (a) 이미지 컷 지점을 음성에 맞춰 이동, 또는 (b) `EP01.srt` 타임코드를 실제 음성에 맞게 재조정(CapCut 자동자막이 가장 빠름).

## 6) 업로드 전 QA
- [ ] 음성-자막 싱크 OK · 가독성 OK · 라우드니스 ≈ -14 LUFS
- [ ] 첫 3초 "완벽했다→반전" 약속 회수
- [ ] 색 전환(웜→쿨→웜)이 감정선과 일치
- [ ] **AI 콘텐츠 라벨 ON** · "사례 재구성" 고지 · 도움 자원 자막
- [ ] 얼굴/실존 브랜드/실명 없음 · 음원·이미지 라이선스 OK
- [ ] 9:16 · 45–60초 · 표지 PNG 썸네일 적용
- [ ] 먼저 비공개 업로드로 점검 후 공개
