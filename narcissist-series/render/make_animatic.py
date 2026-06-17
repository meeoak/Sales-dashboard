"""무음 자막 애니매틱 MP4 생성(플레이스홀더 그라데이션 배경).
실제 음성/이미지 없이도 타이밍·자막·색감 흐름을 담은 진짜 .mp4를 만든다.
사용: python3 make_animatic.py  →  EP01-animatic.mp4"""
import os
from epkit import CAPTIONS, SCENES, BUILD, HERE, gradient, render_slide, concat_to_video

os.makedirs(BUILD, exist_ok=True)
bgs = [gradient(top, bot) for (top, bot, _) in SCENES]

slide_paths = []
for i, (_, sc, _, _) in enumerate(CAPTIONS):
    img = render_slide(bgs[sc], i)
    p = os.path.join(BUILD, f"s{i:02d}.png")
    img.save(p)
    slide_paths.append(p)

out = os.path.join(HERE, "EP01-animatic.mp4")
concat_to_video(slide_paths, out)
print("OK ->", out)
