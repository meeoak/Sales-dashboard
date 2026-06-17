"""최종 영상 합치기: 실제 장면 이미지 + 음성(+선택 음악) -> EP01-final.mp4
준비:
  render/assets/s1.png ~ s5.png  (Canva 장면 6컷 중 S1~S5 다운로드)
  render/EP01-vo.mp3             (azure_tts.py 결과)
  render/assets/music.mp3        (선택, 로열티 프리)
실행: python3 build_final.py
주의: 음성 길이가 58.5초와 크게 다르면 epkit.CAPTIONS 타임코드를 음성에 맞게 조정.
"""
import os, subprocess
from PIL import Image
from epkit import CAPTIONS, SCENES, BUILD, HERE, W, H, render_slide, kenburns_concat, ffmpeg_bin
import cine

ASSETS = os.path.join(HERE, "assets")

def load_cover(path):
    im = Image.open(path).convert("RGB")
    sw, sh = im.size
    scale = max(W / sw, H / sh)
    im = im.resize((int(sw * scale), int(sh * scale)))
    x = (im.width - W) // 2; y = (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))

# 장면별 실제 이미지 로드 (없으면 안내)
scene_imgs = []
for i in range(5):
    p = os.path.join(ASSETS, f"s{i+1}.png")
    if not os.path.exists(p):
        raise SystemExit(f"이미지가 없습니다: {p}  (Canva에서 S{i+1} 컷을 PNG로 받아 여기에 두세요)")
    scene_imgs.append(cine.treat(load_cover(p)))

os.makedirs(BUILD, exist_ok=True)
slide_paths = []
for i, (_, sc, _, _) in enumerate(CAPTIONS):
    img = render_slide(scene_imgs[sc], i)
    sp = os.path.join(BUILD, f"f{i:02d}.png")
    img.save(sp); slide_paths.append(sp)

silent = os.path.join(BUILD, "silent.mp4")
kenburns_concat(slide_paths, silent)

vo = os.path.join(HERE, "EP01-vo.mp3")
if not os.path.exists(vo):
    raise SystemExit(f"음성이 없습니다: {vo}  (먼저 azure_tts.py 실행)")
music = os.path.join(ASSETS, "music.mp3")
out = os.path.join(HERE, "EP01-final.mp4")
FF = ffmpeg_bin()

if os.path.exists(music):
    cmd = [FF, "-y", "-i", silent, "-i", vo, "-stream_loop", "-1", "-i", music,
           "-filter_complex", "[2:a]volume=0.16[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=3[a]",
           "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
           "-shortest", "-movflags", "+faststart", out]
else:
    cmd = [FF, "-y", "-i", silent, "-i", vo, "-map", "0:v", "-map", "1:a",
           "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
           "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
print("OK ->", out)
