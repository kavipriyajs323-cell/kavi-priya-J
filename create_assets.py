from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "Image"
OUT.mkdir(exist_ok=True)

FONT_CANDIDATES = [
    "C:/Windows/Fonts/georgia.ttf", "C:/Windows/Fonts/times.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
]


def load_font(size):
    for p in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_logo(path, color):
    W, H = 600, 160
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, top = 70, 22
    d.line([(cx, top), (cx, 130)], fill=color, width=6)
    d.line([(cx - 40, top + 16), (cx + 40, top + 16)], fill=color, width=6)
    d.line([(cx - 28, 128), (cx + 28, 128)], fill=color, width=8)
    for sx in (cx - 40, cx + 40):
        d.line([(sx, top + 16), (sx - 16, 80)], fill=color, width=3)
        d.line([(sx, top + 16), (sx + 16, 80)], fill=color, width=3)
        d.pieslice([sx - 20, 62, sx + 20, 98], 0, 180, fill=color)
    d.text((140, 42), "LegalEase", font=load_font(64), fill=color)
    img.save(path)


draw_logo(OUT / "Logo.png", (20, 30, 60, 255))
draw_logo(OUT / "inverseLogo.png", (255, 255, 255, 255))
print("Logos created in", OUT)