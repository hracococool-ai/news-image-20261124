#!/usr/bin/env python3
"""Draft infographic for make.fun news-image-20261124.
Deterministic: same input -> same PNG bytes (fixed text, no timestamps in image).
1024x1024, PNG, < 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
BG = (250, 248, 243)
NAVY = (16, 42, 67)
ACCENT = (198, 40, 40)
INK = (30, 30, 30)
MUTED = (90, 90, 90)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(size, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT_R, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 150], fill=NAVY)
d.text((36, 28), "THE WORLD IN ONE IMAGE", font=font(44, True), fill=(255, 255, 255))
d.text((36, 88), "Tuesday 24 November 2026  |  Six stories that defined the day", font=font(24), fill=(200, 210, 220))
d.rectangle([0, 150, W, 158], fill=ACCENT)

panels = [
    ("1  TECH", (0, 120, 90), "NVIDIA BRINGS BACK HUANG",
     "Nvidia reinstates Jensen Huang as CEO after Trump intervened. US stocks surge as AI shares rebound.",
     "Japan Times / Straits Times"),
    ("2  WAR AT SEA", (140, 60, 30), "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
     "Kyiv says sea drones sank a Russian warship near Libya, widening the war.",
     "Japan Times"),
    ("3  SPACE", (40, 80, 140), "NUCLEAR SPACE WEAPON FEAR",
     "Allies warn Russia may launch a nuclear-armed satellite next month. NATO vows to defend space.",
     "Japan Times / Straits Times"),
    ("4  DISASTER", (170, 80, 0), "24 KILLED IN INDONESIA FACTORY FIRE",
     "A factory fire in Indonesia kills 24 people, one of the day's deadliest accidents.",
     "Qatar Tribune"),
    ("5  EUROPE", (0, 100, 100), "BOMB THREATS HIT GERMAN SCHOOLS",
     "Hundreds of schools across Germany receive bomb threats. Denmark moves to ban phones in schools.",
     "Qatar Tribune / Guanghua Daily"),
    ("6  SPORT", (0, 130, 60), "2031 WOMEN'S WORLD CUP HOSTS NAMED",
     "USA, Mexico, Costa Rica and Jamaica will host the 2031 Women's World Cup; the UK hosts 2035.",
     "Japan Times / Straits Times"),
]

# 2 columns x 3 rows
margin, gap = 28, 20
pw = (W - 2 * margin - gap) // 2
ph = 250
top0 = 182
for i, (tag, color, title, body, src) in enumerate(panels):
    col, row = i % 2, i // 2
    x = margin + col * (pw + gap)
    y = top0 + row * (ph + gap)
    d.rounded_rectangle([x, y, x + pw, y + ph], radius=14, fill=(255, 255, 255), outline=(220, 220, 220), width=2)
    d.rectangle([x, y, x + 10, y + ph], fill=color)
    d.text((x + 28, y + 18), tag, font=font(20, True), fill=color)
    # title wrapped
    ty = y + 48
    for line in textwrap.wrap(title, width=24):
        d.text((x + 28, ty), line, font=font(26, True), fill=INK)
        ty += 32
    # body wrapped
    by = ty + 12
    for line in textwrap.wrap(body, width=34):
        d.text((x + 28, by), line, font=font(21), fill=(60, 60, 60))
        by += 27
    d.text((x + 28, y + ph - 32), "Source: " + src, font=font(17), fill=MUTED)

# Footer
d.text((36, 985), "24 November 2026  |  Sources: Japan Times, Straits Times, Qatar Tribune, Manila Times",
       font=font(17), fill=MUTED)

out = "/home/hatch/workspace/makefun/news-image-20261124/entry.png"
img.save(out, "PNG", optimize=True)
print(out)
