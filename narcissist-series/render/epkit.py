"""EP01 렌더 공용 모듈: 장면/자막 데이터 + 슬라이드 렌더 + ffmpeg 합치기.
make_animatic.py(플레이스홀더 그라데이션)와 build_final.py(실제 이미지+음성)가 공유."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")

# (텍스트, 장면 index 0..4, 시작초, 끝초)  -- EP01.srt 와 동일 타임라인
CAPTIONS = [
    ("처음 한 달은… 완벽했습니다.", 0, 0.0, 3.2),
    ("그 사람은, 그게 사랑이라고 믿게 만들었죠.", 0, 3.2, 6.0),
    ("매일 아침과 밤, 연락이 끊이지 않았습니다.", 1, 6.0, 10.5),
    ('잦은 선물. 그리고 며칠 만에 — "넌 내 운명이야."', 1, 10.5, 14.5),
    ("모든 것이 빠르고, 강렬했습니다.", 1, 14.5, 18.0),
    ("그런데… 어느 순간부터,", 2, 18.0, 22.5),
    ("'완벽하다'던 바로 그 모습들을 — 문제 삼기 시작했습니다.", 2, 22.5, 27.5),
    ("칭찬이 비난으로 바뀌는 데에는… 오래 걸리지 않았습니다.", 2, 27.5, 32.5),
    ("이건 빠른 사랑이 아니었습니다. '러브바밍'이라는 패턴이었죠.", 3, 32.5, 37.5),
    ("과한 애정으로 의존하게 만든 뒤, 주도권을 가져가는 방식.", 3, 37.5, 43.0),
    ("사랑은 속도가 아니라 — 일관성으로 증명됩니다.", 3, 43.0, 48.0),
    ("혹시 지금, 비슷한 신호를 느끼고 있다면 —", 4, 48.0, 53.5),
    ("그건 당신의 잘못이 아닙니다.", 4, 53.5, 58.5),
]

SCENES = [
    ((58, 42, 26), (201, 138, 60),  "S1 · 따뜻한 시작"),
    ((66, 42, 22), (217, 154, 74),  "S2 · 러브바밍 (과잉 애정)"),
    ((42, 47, 58), (106, 122, 140), "S3 · 전환 (칭찬→비난)"),
    ((17, 22, 31), (47, 74, 99),    "S4 · 깨달음 · '러브바밍'"),
    ((26, 20, 16), (207, 147, 80),  "S5 · 당신 잘못이 아닙니다"),
]

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/opentype/unifont/unifont.otf",
]

def font(size):
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def gradient(top, bottom):
    img = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            # 단어 자체가 너무 길면 글자 단위로 분해
            if draw.textlength(w, font=fnt) > max_w:
                buf = ""
                for ch in w:
                    if draw.textlength(buf + ch, font=fnt) <= max_w:
                        buf += ch
                    else:
                        lines.append(buf); buf = ch
                cur = buf
            else:
                cur = w
    if cur:
        lines.append(cur)
    return lines

def chip(draw, xy, text, fnt, pad=10, bg=(0, 0, 0, 140), fg=(255, 255, 255)):
    x, y = xy
    tw = draw.textlength(text, font=fnt)
    th = fnt.size + 6
    draw.rounded_rectangle([x, y, x + tw + pad * 2, y + th + pad], radius=8, fill=bg)
    draw.text((x + pad, y + pad // 2), text, font=fnt, fill=fg)

def render_slide(bg, idx):
    """bg: RGB 배경 이미지(장면), idx: CAPTIONS 인덱스 → 슬라이드 이미지 반환"""
    text, sc, *_ = CAPTIONS[idx]
    img = bg.convert("RGBA")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # 하단 가독성용 그라데이션 박스
    d.rectangle([0, int(H * 0.60), W, H], fill=(0, 0, 0, 90))
    # 장면 라벨
    f_sc = font(34)
    sl = SCENES[sc][2]
    d.text(((W - d.textlength(sl, font=f_sc)) / 2, int(H * 0.40)), sl, font=f_sc, fill=(255, 255, 255, 150))
    # 자막
    f_cap = font(62)
    lines = wrap(d, text, f_cap, W - 160)
    lh = f_cap.size + 18
    total = lh * len(lines)
    y = int(H * 0.74) - total // 2
    for ln in lines:
        x = (W - d.textlength(ln, font=f_cap)) / 2
        d.text((x, y), ln, font=f_cap, fill=(255, 255, 255, 255),
               stroke_width=5, stroke_fill=(0, 0, 0, 255))
        y += lh
    # 좌상단 재구성 라벨(첫 2컷) / 우상단 AI 배지(상시)
    if idx < 2:
        chip(d, (40, 40), "사례 재구성 · 특정 인물과 무관", font(26))
    badge = "AI"
    fb = font(30)
    chip(d, (W - 40 - draw_w(d, badge, fb) - 20, 40), badge, fb, bg=(255, 255, 255, 60))
    # 도움 자막(S5)
    if sc == 4:
        fh = font(30)
        ht = "도움이 필요하면 · 여성긴급전화 1366 · 자살예방 109"
        chip(d, ((W - draw_w(d, ht, fh) - 20) / 2, int(H * 0.88)), ht, fh, bg=(120, 60, 20, 170))
    return Image.alpha_composite(img, ov).convert("RGB")

def draw_w(d, text, fnt):
    return d.textlength(text, font=fnt)

def ffmpeg_bin():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()

def concat_to_video(slide_paths, out_path, fps=30):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    listf = os.path.join(BUILD, "concat.txt")
    with open(listf, "w", encoding="utf-8") as f:
        for p, (_, _, s, e) in zip(slide_paths, CAPTIONS):
            f.write(f"file '{p}'\n")
            f.write(f"duration {round(e - s, 3)}\n")
        f.write(f"file '{slide_paths[-1]}'\n")  # concat demuxer 마지막 프레임 보정
    cmd = [ffmpeg_bin(), "-y", "-f", "concat", "-safe", "0", "-i", listf,
           "-vf", f"fps={fps},format=yuv420p,scale={W}:{H}",
           "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", out_path]
    subprocess.run(cmd, check=True, capture_output=True)
    return out_path

def kenburns_concat(slide_paths, out_path, fps=30):
    """각 슬라이드를 느린 줌(켄번스) 클립으로 만든 뒤 이어붙인다. 무음 비디오."""
    os.makedirs(BUILD, exist_ok=True)
    clips = []
    for p, (_, _, s, e) in zip(slide_paths, CAPTIONS):
        dur = max(0.2, round(e - s, 3)); frames = max(1, int(dur * fps))
        c = p + ".clip.mp4"
        vf = (f"scale={W*2}:{H*2},zoompan=z='min(zoom+0.0008,1.10)':"
              f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={fps},"
              f"format=yuv420p")
        subprocess.run([ffmpeg_bin(), "-y", "-loop", "1", "-i", p, "-t", str(dur),
                        "-vf", vf, "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", c],
                       check=True, capture_output=True)
        clips.append(c)
    listf = os.path.join(BUILD, "clips.txt")
    with open(listf, "w", encoding="utf-8") as f:
        for c in clips:
            f.write(f"file '{c}'\n")
    subprocess.run([ffmpeg_bin(), "-y", "-f", "concat", "-safe", "0", "-i", listf,
                    "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart", out_path], check=True, capture_output=True)
    return out_path
