#!/usr/bin/env python3
"""Compose the Nov 18 2026 news poster: masthead + hero triptych + headline ticker.
Output: entry.png at 1024x1024, <= 1 MiB (palette-quantized PNG if needed)."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(HERE, "media-generation-news-20261118-hero-0-ebd2041b-3604-4142-afa2-d180b5460672.webp")
OUT = os.path.join(HERE, "entry.png")

NAVY = (10, 18, 30)
CREAM = (238, 226, 199)
GOLD = (201, 162, 75)
RED = (178, 58, 44)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

W = 1024
img = Image.new("RGB", (W, W), NAVY)
d = ImageDraw.Draw(img)

def centered(text, y, font, fill, tracking=0):
    if tracking:
        x = (W - sum(d.textlength(ch, font=font) + tracking for ch in text) + tracking) / 2
        for ch in text:
            d.text((x, y), ch, font=font, fill=fill)
            x += d.textlength(ch, font=font) + tracking
    else:
        d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)

# Masthead
centered("THE WORLD IN ONE DAY", 26, ImageFont.truetype(SERIF_B, 54), CREAM, tracking=2)
d.line([(48, 100), (W - 48, 100)], fill=GOLD, width=2)
centered("WEDNESDAY · 18 NOVEMBER 2026", 110, ImageFont.truetype(SANS_B, 21), GOLD, tracking=4)
d.line([(48, 142), (W - 48, 142)], fill=GOLD, width=2)

# Hero: crop the square art to 1024x600, anchored slightly above center
hero = Image.open(HERO).convert("RGB")
hw, hh = hero.size
crop_h = int(hw * 600 / 1024)
top = int((hh - crop_h) * 0.38)
hero = hero.crop((0, top, hw, top + crop_h)).resize((1024, 600), Image.LANCZOS)
img.paste(hero, (0, 152))

# Headline
centered("THREE FLAGS, ONE TABLE —", 766, ImageFont.truetype(SERIF_B, 40), CREAM)
centered("WAR AT THE EDGES", 812, ImageFont.truetype(SERIF_B, 40), RED)
d.line([(48, 868), (W - 48, 868)], fill=GOLD, width=2)

# Ticker: the day's five stories
lines = [
    "SHENZHEN — TRUMP, XI & PUTIN OPEN THE FIRST TRILATERAL SUMMIT",
    "GULF — IRANIAN DRONES AT KUWAIT & BAHRAIN AFTER U.S. STRIKE ON QESHM",
    "CRIMEA — KERCH BRIDGE HIT AGAIN; A ROAD SPAN COLLAPSES",
    "WASHINGTON — PELTOLA FLIPS ALASKA; THE SENATE GOES 56–44",
    "MARKETS — ANTHROPIC'S $81.3B RAISE, THE LARGEST OFFERING ON RECORD",
]
f = ImageFont.truetype(SANS_B, 20)
y = 882
for ln in lines:
    centered(ln, y, f, CREAM)
    y += 27

img.save(OUT)
size = os.path.getsize(OUT)
print("saved", OUT, size, "bytes")
if size > 1024 * 1024:
    q = img.quantize(colors=256, method=Image.MEDIANCUT)
    q.save(OUT, optimize=True)
    print("quantized ->", os.path.getsize(OUT), "bytes")
