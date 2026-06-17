# 낡은 자동차 AI 복원 쇼츠 — 에이전트 MVP

> 목표: "낡은 자동차가 AI로 복원되는 30–45초 세로 쇼츠"를 반복 생산하는 에이전트 파이프라인 MVP + 1편 완성 패키지
> 안전 원칙: 상표/저작권 회피 · AI 합성 라벨 권장 · 수익 보장 0 · 양산(비진정성) 방지(매 회차 변주 + 사람의 큐레이션)

---

## A. MVP 개요 & 파이프라인

핵심 철학(이전 편과 동일): **자동화할 건 '노동(초안·정리·반복)', 사람이 쥘 건 '판단(콘셉트·약속·검수)'.** 편집/렌더 속도보다 콘셉트·훅·검수 시스템이 결과를 가른다.

### 에이전트 체인 (`.claude/agents/`에 설치)
1. **shorts-trend-analyst** — 콘셉트 1개 선정 + 회차별 변주 강제(양산 방지)
2. **shorts-concept-hook** — 첫 3초 훅 / 제목·캡션 / 화면 텍스트 / CTA
3. **restoration-prompt-designer** — BEFORE·AFTER 이미지 + image-to-video 전환 프롬프트 (핵심)
4. **shorts-scriptwriter** — 30–45초 비트시트(샷별 타임코드·텍스트)
5. **shorts-audio-director** — 음악/SFX/비트 동기
6. **shorts-compliance-qa** — 렌더 전 게이트(PASS/HOLD)

### 흐름
```
[1 트렌드/콘셉트] → [2 훅/캡션] → [3 비주얼 프롬프트] → [4 비트시트] → [5 오디오]
        → [6 컴플라이언스 QA: PASS?] → (사람 승인) → 외부 렌더 → 업로드
```

### 외부 렌더 스택 (예시 — 가용성/약관 현행 확인)
- 이미지 생성: Midjourney / Flux / Ideogram / DAL·E 등 (BEFORE·AFTER 동일 구도)
- 이미지→영상: Kling / Runway / Google Veo / Sora / Pika / Luma 등 (전환 클립)
- 조립/자막/오디오: CapCut / Premiere / DaVinci 등 → 9:16 1080×1920 export
- 업로드: AI/합성 콘텐츠 라벨 적용 후 게시
> ※ 완전 무인 자동화도 기술적으로 가능하나, 정책상 "사람의 고유 가치"가 통과 기준이므로 **콘셉트 선택·최종 검수는 사람이** 유지할 것.

---

## B. 1편 완성 패키지 (이번 회차 샘플)

**이번 콘셉트(트렌드 분석가 산출):** 60년대풍 머슬카 · 버려진 헛간 · 좌→우 "복원 스윕" 연출 · 선셋 골드 색감
*(다음 회차 로테이션 예: 50년대 픽업/사막, 70년대 세단/도심 골목, 80년대 스포츠카/지하주차장)*

### 1) 첫 3초 훅
- 화면 텍스트(0~3s): **"이 폐차가… 다시 살아난다"** + 우상단 작은 "AI" 배지
- 비주얼: 녹슨 보닛 클로즈업 → 빠르게 풀샷으로 줌아웃하며 복원된 모습 0.3초 티저 플래시
- 대안 훅: "30초 뒤, 이 차는 새 차가 됩니다" / "버리려던 차, AI로 복원하면?"

### 2) 30–45초 비트시트
| 샷 | 시간 | 화면 | 화면 텍스트 | 오디오 |
|---|---|---|---|---|
| 1 | 0:00–0:03 | 녹슨 보닛 클로즈업 → 풀샷 줌아웃(복원본 0.3s 플래시) | 이 폐차가… 다시 살아난다 | 잔잔 → 텐션 시작 |
| 2 | 0:03–0:10 | 헛간 속 폐차 느린 패닝(먼지·펑크 타이어·바랜 도장) | 1965, 버려진 머슬카 | 빌드업 |
| 3 | 0:10–0:30 | 좌→우 복원 스윕(빛 라인이 지나가며 녹→광택, 타이어 교체, 크롬 광) | 복원 中… | 빌드업 고조 |
| 4 | 0:30–0:40 | 복원 완료 히어로 샷(서서히 회전/로우앵글), 선셋 골드 | 완성 ✨ | 드롭(리빌) |
| 5 | 0:40–0:45 | 전/후 split 0.5s + 첫 컷으로 루프 연결 | 다음엔 어떤 차? 댓글로 | 여운/후렴 |

### 3) 샷 리스트(렌더용)
- IMG-A: BEFORE 폐차(헛간, 풀샷) — 모핑 기준 구도
- IMG-B: AFTER 복원본(동일 구도·동일 각도)
- IMG-C: 훅용 보닛 녹 클로즈업
- VID-1: IMG-A→IMG-B 복원 스윕 i2v(6s)
- VID-2: AFTER 히어로 회전 i2v(4s)

### 4) AI 이미지/비디오 생성 프롬프트
공통 스타일: `photorealistic, cinematic, vertical 9:16, golden hour, shallow depth of field, fictional/generic car design`
공통 네거티브: `no brand logos, no badges, no emblems, no readable license plate, no watermark, no text, no real person, no trademark grille`

- **BEFORE (IMG-A)** — `Photorealistic abandoned 1960s-style muscle car (fictional/generic design) inside a dusty old barn, heavy rust, faded peeling paint, flat cracked tires, cobwebs, dim light beams through wooden planks, vertical 9:16, cinematic. Negative: no brand logos, no badges, no readable plate, no watermark, no text, no real person.`
- **AFTER (IMG-B)** — `The SAME muscle car, SAME camera angle and composition, fully restored: glossy deep-red paint, polished chrome, brand-new tires, spotless, showroom + golden-hour lighting, vertical 9:16, cinematic. Negative: (same as common).`
- **HOOK CLOSE-UP (IMG-C)** — `Extreme macro of a rusted car hood, peeling paint flakes, dramatic light, vertical 9:16. Negative: no logos, no text.`
- **i2v 전환 (VID-1)** — `Start from the rusty car image; a glowing restoration light-sweep moves left to right, transforming rust into glossy paint, replacing flat tires with new ones, chrome polishing in its wake; camera locked/static, subtle dust particles, 6 seconds, smooth morph.`
- **i2v 히어로 (VID-2)** — `Restored car, slow cinematic orbit/low-angle reveal, golden-hour reflections on glossy paint, 4 seconds, static-to-slow push-in.`

### 5) 음악/사운드
- 무드/BPM: 긴장→해방, 90–110 BPM, 빌드업+드롭 1회
- 음원 검색 키워드(플랫폼 라이브러리/로열티 프리): "satisfying transformation", "epic build up reveal", "uplifting cinematic"
- 비트맵: 0–3s 잔잔 / 3–10s 빌드 / 10–30s 텐션 상승 / **30s 드롭=리빌** / 40–45s 후렴 여운
- SFX: 먼지 swoosh, 금속 마찰, 광택 sparkle, 시동음(일반), 셔터음

### 6) 캡션/제목 + 해시태그
- 캡션: **버려진 머슬카, AI로 복원하면? ✨**
- 해시태그: `#shorts #AI복원 #클래식카 #자동차 #카레스토어 #AIart #restoration #satisfying #쇼츠`
- CTA(고정/캡션): "다음엔 어떤 차 복원할까요? 댓글로 골라주세요 🚗"

### 7) 업로드 설정 (중요)
- 규격: 9:16, 1080×1920, 30–45초
- **AI/합성 콘텐츠 라벨**: 이 영상은 사진처럼 리얼한 AI 생성물.
  - 가상의 차량/사건이라 YouTube의 '변형·합성' 의무 공개에 반드시 해당하진 않을 수 있으나, **AI 라벨을 켜는 것이 안전**(크로스 포스팅 시 TikTok/Instagram의 AI 라벨 규정도 충족). 정책 변동되니 공식 도움말 현행 확인.
- 음원: 플랫폼 제공/라이선스 음원만.

### 8) 최종 QA 체크리스트 (렌더 전 게이트)
- [ ] BEFORE/AFTER 구도·각도 동일 (매끄러운 모핑)
- [ ] 실제 브랜드 로고·엠블럼·상표 그릴·번호판·식별 인물·사유지 없음
- [ ] AI/합성 콘텐츠 라벨 적용(또는 적용 예정)
- [ ] 음원 라이선스 안전
- [ ] 워터마크·타 영상 클립 없음
- [ ] 수익 보장·허위·과장 표현 0건
- [ ] 첫 3초에 "복원 전후" 약속 회수
- [ ] 9:16 / 30–45초 / 루프 연결
- [ ] 이번 회차가 직전 회차와 차종·배경·연출·색감이 다른가(양산 방지)
- [ ] 캡션·해시태그·CTA 포함
- 최종 판정: ☐ PASS ☐ HOLD
