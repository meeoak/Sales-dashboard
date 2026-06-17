"""시네마틱 절차적 배경 + 켄번스 모션 애니매틱(EP01-animatic-v2.mp4, 무음).
그라데이션 대비 큰 시각 업그레이드. 사용: python3 make_animatic_v2.py"""
import os
from epkit import CAPTIONS, BUILD, HERE, render_slide, kenburns_concat
import cine

os.makedirs(BUILD, exist_ok=True)
bgs = [cine.cinematic_bg(i) for i in range(5)]
slides = []
for i, (_, sc, _, _) in enumerate(CAPTIONS):
    img = render_slide(bgs[sc], i)
    p = os.path.join(BUILD, f"v{i:02d}.png")
    img.save(p); slides.append(p)

out = os.path.join(HERE, "EP01-animatic-v2.mp4")
kenburns_concat(slides, out)
print("OK ->", out)
