"""시네마틱 절차적 배경 + '필름 룩' 그레이드.
실사진을 못 받는 샌드박스에서 그라데이션 대비 큰 시각 업그레이드를 만든다.
treat()는 실사진에도 적용 가능 → build_final.py가 Canva 사진에 동일 그레이드를 입힌다."""
import os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from epkit import W, H, SCENES

def _grad(top, bottom):
    top = np.array(top, float); bottom = np.array(bottom, float)
    t = np.linspace(0, 1, H)[:, None, None]
    arr = top[None, None, :] * (1 - t) + bottom[None, None, :] * t
    return np.repeat(arr, W, axis=1)

def _radial(cx, cy, rad):
    ys, xs = np.mgrid[0:H, 0:W]
    d = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2) / rad
    return np.clip(1 - d, 0, 1) ** 1.6

def _bokeh(img, n, palette, smin, smax, amax, seed):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    for _ in range(n):
        r = rnd.randint(smin, smax); x = rnd.randint(0, W); y = rnd.randint(0, int(H * 0.72))
        c = rnd.choice(palette); a = rnd.randint(amax // 3, amax)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(c[0], c[1], c[2], a))
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(rnd.randint(18, 34))))

def _rain(img, n, seed, color=(200, 210, 230)):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    for _ in range(n):
        x = rnd.randint(-40, W); y = rnd.randint(0, H); ln = rnd.randint(28, 86); off = int(ln * 0.18)
        d.line([(x, y), (x - off, y + ln)], fill=(color[0], color[1], color[2], rnd.randint(30, 80)), width=2)
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(0.6)))

def _window(img):
    d = ImageDraw.Draw(img, "RGBA"); m = 70
    d.rectangle([m, int(H * 0.12), W - m, int(H * 0.70)], outline=(14, 17, 25, 225), width=18)
    cx = W // 2; d.line([(cx, int(H * 0.12)), (cx, int(H * 0.70))], fill=(14, 17, 25, 225), width=14)
    cy = int(H * 0.41); d.line([(m, cy), (W - m, cy)], fill=(14, 17, 25, 225), width=14)

def _silhouette(img):
    d = ImageDraw.Draw(img, "RGBA"); cx = int(W * 0.5); base = int(H * 0.70)
    d.ellipse([cx - 120, base - 250, cx + 120, base + 120], fill=(7, 8, 12, 235))
    d.ellipse([cx - 52, base - 350, cx + 52, base - 245], fill=(7, 8, 12, 240))

def _shaft(img):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    d.polygon([(int(W * 0.60), 0), (int(W * 0.93), 0), (int(W * 0.72), H), (int(W * 0.42), H)],
              fill=(255, 210, 150, 60))
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(60)))

def treat(img):
    """비네팅 + 그레인 + 약한 대비. 실사진에도 동일 적용."""
    img = img.convert("RGB").resize((W, H))
    arr = np.asarray(img, float)
    ys, xs = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xs - W / 2) / (W / 2)) ** 2 + ((ys - H / 2) / (H / 2)) ** 2)
    vig = np.clip(1 - 0.55 * np.clip(d - 0.2, 0, 1) ** 2, 0, 1)[:, :, None]
    arr = arr * vig + np.random.normal(0, 5.0, arr.shape)
    arr = (arr - 128) * 1.06 + 128
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))

def cinematic_bg(i):
    top, bottom, _ = SCENES[i]
    arr = _grad(top, bottom)
    glow = {0: ((W * .5, H * .32), (255, 200, 130), .5),
            1: ((W * .5, H * .30), (255, 205, 140), .65),
            2: ((W * .35, H * .30), (150, 175, 200), .35),
            3: ((W * .5, H * .28), (120, 150, 190), .40),
            4: ((W * .72, H * .18), (255, 210, 150), .60)}[i]
    (cx, cy), gcol, gi = glow
    m = _radial(cx, cy, W * 0.9)[:, :, None]
    arr = arr + np.array(gcol, float)[None, None, :] * m * gi
    img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8")).convert("RGBA")
    if i == 0:
        _bokeh(img, 14, [(255, 200, 120), (255, 170, 90), (255, 225, 170)], 30, 90, 110, 10)
    elif i == 1:
        _bokeh(img, 26, [(255, 190, 110), (255, 150, 80), (255, 220, 160), (255, 120, 120)], 26, 96, 130, 21)
    elif i == 2:
        _rain(img, 220, 32); _bokeh(img, 8, [(150, 170, 195)], 30, 70, 60, 33)
    elif i == 3:
        _window(img); _rain(img, 160, 43); _silhouette(img)
    elif i == 4:
        _shaft(img); _bokeh(img, 12, [(255, 205, 150), (255, 180, 110)], 28, 80, 90, 55)
    return treat(img)
