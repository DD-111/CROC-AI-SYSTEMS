# -*- coding: utf-8 -*-
"""Generate a clear product demo MP4/GIF for Croc Sentinel + drone response."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT_VID = ROOT / "assets" / "video"
OUT_IMG = ROOT / "assets" / "images"
OUT_VID.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
FPS = 12
BG = (10, 16, 32)
FG = (248, 250, 252)
MUTED = (148, 163, 184)
BLUE = (59, 130, 246)
CYAN = (34, 211, 238)
GREEN = (74, 222, 128)
RED = (248, 113, 113)
ORANGE = (251, 146, 60)
PURPLE = (192, 132, 252)
CARD = (22, 32, 54)
LINE = (51, 65, 85)


def font(size: int, bold: bool = False):
    paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()


def base() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # subtle radial glow
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    for i in range(8):
        r = 80 + i * 60
        c = (14 + i, 24 + i * 2, 48 + i * 3)
        gd.ellipse((W // 2 - r * 2, -r, W // 2 + r * 2, r * 2), fill=c)
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    img = Image.blend(img, glow, 0.35)
    d = ImageDraw.Draw(img)
    return img, d


def badge(d, x, y, text, color=BLUE):
    tw = d.textlength(text, font=font(14, True)) if hasattr(d, "textlength") else len(text) * 8
    d.rounded_rectangle((x, y, x + tw + 24, y + 28), radius=14, fill=color)
    d.text((x + 12, y + 5), text, fill=BG, font=font(14, True))


def scene_title(title: str, subtitle: str = "", hold: float = 2.2) -> list[Image.Image]:
    frames = []
    n = max(1, int(hold * FPS))
    for i in range(n):
        img, d = base()
        alpha = min(1.0, i / max(1, n // 3))
        y_off = int((1 - alpha) * 20)
        d.text((W // 2, 280 + y_off), title, fill=FG, font=font(48, True), anchor="mm")
        if subtitle:
            d.text((W // 2, 350 + y_off), subtitle, fill=MUTED, font=font(22), anchor="mm")
        d.text((W // 2, 660), "Croc Sentinel  ·  Croc Nexus AI Technologies", fill=MUTED, font=font(16), anchor="mm")
        frames.append(img)
    return frames


def scene_dashboard_intro() -> list[Image.Image]:
    """Use real dashboard screenshot if available."""
    frames = []
    shot = OUT_IMG / "dash-overview.png"
    n = int(3.0 * FPS)
    for i in range(n):
        img, d = base()
        d.text((W // 2, 48), "Your real Command Center", fill=FG, font=font(32, True), anchor="mm")
        d.text((W // 2, 88), "www.esasecure.com  ·  AI-Powered Security Command Center", fill=MUTED, font=font(16), anchor="mm")
        if shot.exists():
            raw = Image.open(shot).convert("RGB")
            # fit into box
            box_w, box_h = 1100, 520
            raw.thumbnail((box_w, box_h), Image.Resampling.LANCZOS)
            x = (W - raw.width) // 2
            y = 120
            # soft border
            d.rounded_rectangle((x - 8, y - 8, x + raw.width + 8, y + raw.height + 8), radius=16, outline=BLUE, width=2)
            img.paste(raw, (x, y))
        else:
            d.text((W // 2, H // 2), "Dashboard", fill=MUTED, font=font(28), anchor="mm")
        frames.append(img)
    return frames


def scene_incident_flow() -> list[Image.Image]:
    steps = [
        ("1", "Alarm", "Site sensor triggers", RED),
        ("2", "Alert", "Phone knows in seconds", BLUE),
        ("3", "AI Score", "89 / 100  HIGH", PURPLE),
        ("4", "Decide", "Who goes? What first?", ORANGE),
        ("5", "Dispatch", "People + drone together", CYAN),
        ("6", "Prove", "Full timeline saved", GREEN),
    ]
    frames = []
    for active in range(len(steps)):
        for f in range(int(1.15 * FPS)):
            img, d = base()
            d.text((W // 2, 42), "When something goes wrong", fill=FG, font=font(34, True), anchor="mm")
            d.text((W // 2, 78), "Clear response — people and machines work as one team", fill=MUTED, font=font(18), anchor="mm")
            card_w, card_h = 180, 210
            gap = 18
            total = len(steps) * card_w + (len(steps) - 1) * gap
            x0 = (W - total) // 2
            y = 140
            for i, (num, title, sub, color) in enumerate(steps):
                x = x0 + i * (card_w + gap)
                done = i < active
                on = i == active
                fill = (28, 45, 80) if on else CARD
                outline = color if (on or done) else LINE
                d.rounded_rectangle((x, y, x + card_w, y + card_h), radius=16, fill=fill, outline=outline, width=3 if on else 2)
                d.ellipse((x + 66, y + 22, x + 114, y + 70), fill=color if on else (51, 65, 85))
                d.text((x + 90, y + 46), num, fill=BG if on else FG, font=font(22, True), anchor="mm")
                d.text((x + 90, y + 100), title, fill=FG if on else MUTED, font=font(20, True), anchor="mm")
                # wrap subtitle
                d.text((x + 90, y + 140), sub, fill=MUTED, font=font(13), anchor="mm")
                if done:
                    d.ellipse((x + card_w - 34, y + 12, x + card_w - 10, y + 36), fill=GREEN)
                if on:
                    pulse = int(4 + 3 * math.sin(f / FPS * math.pi * 2))
                    d.rounded_rectangle(
                        (x - pulse, y - pulse, x + card_w + pulse, y + card_h + pulse),
                        radius=16,
                        outline=color,
                        width=2,
                    )
            # progress
            bar_y = 430
            d.rounded_rectangle((120, bar_y, W - 120, bar_y + 12), radius=6, fill=(30, 41, 59))
            frac = (active + f / (1.15 * FPS)) / len(steps)
            d.rounded_rectangle((120, bar_y, 120 + int((W - 240) * frac), bar_y + 12), radius=6, fill=BLUE)
            reason = [
                "North gate after hours — repeated triggers",
                "App push + phone call — AI never blocks the alert",
                "AI: score 89 · reason in plain words",
                "Response plan picks people AND nearest drone dock",
                "Human on ground · drone overhead for eyes",
                "Every second written down for review",
            ][active]
            d.rounded_rectangle((120, 470, W - 120, 560), radius=14, fill=CARD, outline=LINE)
            d.text((W // 2, 500), f"Now: {steps[active][1]}", fill=FG, font=font(22, True), anchor="mm")
            d.text((W // 2, 535), reason, fill=MUTED, font=font(18), anchor="mm")
            d.text((W // 2, 660), "Safety rule: AI can raise urgency — never quietly lower it", fill=MUTED, font=font(14), anchor="mm")
            frames.append(img)
    return frames


def scene_drone_support() -> list[Image.Image]:
    packages = [
        ("DJI Dock 3", "Auto nest / charge / takeoff", "RM 55,140", BLUE),
        ("Matrice 4D", "Day patrol & inspection", "RM 18,180", CYAN),
        ("Matrice 4TD", "Thermal night eyes", "RM 25,740", ORANGE),
    ]
    frames = []
    n = int(5.5 * FPS)
    for f in range(n):
        img, d = base()
        d.text((W // 2, 40), "We support official DJI Dock drones", fill=FG, font=font(34, True), anchor="mm")
        d.text(
            (W // 2, 78),
            "Dock 3 + Matrice 4D / 4TD  ·  AI helps choose who and what flies",
            fill=MUTED,
            font=font(18),
            anchor="mm",
        )
        # drone silhouette animation
        drone_x = 180 + int((f / n) * 920)
        drone_y = 150 + int(12 * math.sin(f / 4))
        d.ellipse((drone_x - 28, drone_y - 10, drone_x + 28, drone_y + 10), fill=CYAN)
        d.ellipse((drone_x - 55, drone_y - 4, drone_x - 30, drone_y + 4), fill=MUTED)
        d.ellipse((drone_x + 30, drone_y - 4, drone_x + 55, drone_y + 4), fill=MUTED)
        d.text((drone_x, drone_y - 28), "AI dispatch", fill=CYAN, font=font(14, True), anchor="mm")

        card_w = 340
        gap = 30
        total = 3 * card_w + 2 * gap
        x0 = (W - total) // 2
        y = 230
        for i, (name, desc, price, color) in enumerate(packages):
            x = x0 + i * (card_w + gap)
            reveal = f > i * 8
            fill = CARD if reveal else (18, 24, 40)
            d.rounded_rectangle((x, y, x + card_w, y + 280), radius=18, fill=fill, outline=color if reveal else LINE, width=3)
            if reveal:
                d.rounded_rectangle((x, y, x + card_w, y + 54), radius=18, fill=color)
                d.rectangle((x, y + 30, x + card_w, y + 54), fill=color)
                d.text((x + card_w // 2, y + 27), name, fill=BG, font=font(22, True), anchor="mm")
                d.text((x + card_w // 2, y + 110), desc, fill=FG, font=font(18), anchor="mm")
                d.text((x + card_w // 2, y + 165), price, fill=color, font=font(28, True), anchor="mm")
                d.text((x + card_w // 2, y + 210), "approx. Malaysia list", fill=MUTED, font=font(13), anchor="mm")
                d.text((x + card_w // 2, y + 245), "Works with Croc Sentinel", fill=GREEN, font=font(14, True), anchor="mm")
        d.text((W // 2, 660), "Hardware package estimate  ·  software + AI coordination by Croc Nexus", fill=MUTED, font=font(14), anchor="mm")
        frames.append(img)
    return frames


def scene_ai_dispatch() -> list[Image.Image]:
    frames = []
    n = int(5.0 * FPS)
    for f in range(n):
        img, d = base()
        d.text((W // 2, 40), "AI-assisted dispatch", fill=FG, font=font(36, True), anchor="mm")
        d.text((W // 2, 80), "Same alarm  →  the right people AND the right aircraft", fill=MUTED, font=font(18), anchor="mm")

        # left: human
        d.rounded_rectangle((80, 140, 560, 560), radius=20, fill=CARD, outline=GREEN, width=3)
        d.text((320, 180), "Ground team", fill=GREEN, font=font(24, True), anchor="mm")
        items_h = [
            "Nearest officer called",
            "Phone + map + reason",
            "Accept → Arrive → Resolve",
            "Human stays in charge",
        ]
        for i, t in enumerate(items_h):
            on = f > 6 + i * 6
            d.ellipse((120, 240 + i * 60, 140, 260 + i * 60), fill=GREEN if on else LINE)
            d.text((160, 250 + i * 60), t, fill=FG if on else MUTED, font=font(18), anchor="lm")

        # right: drone
        d.rounded_rectangle((720, 140, 1200, 560), radius=20, fill=CARD, outline=CYAN, width=3)
        d.text((960, 180), "Air team (Dock 3)", fill=CYAN, font=font(24, True), anchor="mm")
        items_d = [
            "Pick nearest ready dock",
            "Matrice 4D day / 4TD night",
            "City patrol or incident eyes",
            "AI suggests — you approve",
        ]
        for i, t in enumerate(items_d):
            on = f > 10 + i * 6
            d.ellipse((760, 240 + i * 60, 780, 260 + i * 60), fill=CYAN if on else LINE)
            d.text((800, 250 + i * 60), t, fill=FG if on else MUTED, font=font(18), anchor="lm")

        # center arrow pulse
        mid = 0.5 + 0.5 * math.sin(f / 4)
        d.text((W // 2, 350), "< AI >", fill=(int(100 + 100 * mid), 180, 255), font=font(22, True), anchor="mm")
        frames.append(img)
    return frames


def scene_city_patrol() -> list[Image.Image]:
    frames = []
    n = int(5.0 * FPS)
    # simple city map grid
    for f in range(n):
        img, d = base()
        d.text((W // 2, 40), "City patrol + live eyes", fill=FG, font=font(36, True), anchor="mm")
        d.text((W // 2, 80), "Scheduled routes  ·  urgent divert  ·  thermal when needed", fill=MUTED, font=font(18), anchor="mm")

        mx, my, mw, mh = 120, 120, 700, 480
        d.rounded_rectangle((mx, my, mx + mw, my + mh), radius=16, fill=(14, 24, 40), outline=LINE, width=2)
        # streets
        for i in range(1, 6):
            yy = my + i * mh // 6
            d.line((mx + 20, yy, mx + mw - 20, yy), fill=(40, 55, 80), width=2)
        for i in range(1, 5):
            xx = mx + i * mw // 5
            d.line((xx, my + 20, xx, my + mh - 20), fill=(40, 55, 80), width=2)

        # waypoints
        points = [
            (mx + 80, my + 80),
            (mx + 220, my + 160),
            (mx + 380, my + 120),
            (mx + 520, my + 220),
            (mx + 600, my + 340),
            (mx + 420, my + 400),
        ]
        for i in range(len(points) - 1):
            d.line([points[i], points[i + 1]], fill=CYAN, width=3)
        progress = (f / n) * (len(points) - 1)
        idx = int(progress)
        t = progress - idx
        if idx >= len(points) - 1:
            px, py = points[-1]
        else:
            x1, y1 = points[idx]
            x2, y2 = points[idx + 1]
            px = int(x1 + (x2 - x1) * t)
            py = int(y1 + (y2 - y1) * t)
        d.ellipse((px - 12, py - 12, px + 12, py + 12), fill=CYAN, outline=FG, width=2)
        # alarm pin
        ax, ay = mx + 480, my + 280
        d.ellipse((ax - 10, ay - 10, ax + 10, ay + 10), fill=RED)
        d.text((ax, ay - 28), "Incident", fill=RED, font=font(14, True), anchor="mm")

        # dock box
        dx, dy = mx + 100, my + 360
        d.rounded_rectangle((dx - 30, dy - 20, dx + 30, dy + 20), radius=6, fill=BLUE)
        d.text((dx, dy), "Dock 3", fill=FG, font=font(12, True), anchor="mm")

        # right panel
        d.rounded_rectangle((860, 120, 1200, 600), radius=16, fill=CARD, outline=PURPLE, width=2)
        d.text((1030, 160), "Live panel", fill=PURPLE, font=font(22, True), anchor="mm")
        lines = [
            "Route: Central loop",
            "Aircraft: Matrice 4TD",
            "Mode: Thermal assist",
            "AI tip: divert to Incident",
            "ETA to scene: ~90s",
            "Human OK required",
        ]
        for i, line in enumerate(lines):
            on = f > 5 + i * 5
            d.text((880, 220 + i * 50), ("•  " if on else "·  ") + line, fill=FG if on else MUTED, font=font(17), anchor="lm")
        frames.append(img)
    return frames


def scene_closing() -> list[Image.Image]:
    frames = []
    n = int(3.5 * FPS)
    for f in range(n):
        img, d = base()
        d.text((W // 2, 220), "Croc Sentinel", fill=FG, font=font(52, True), anchor="mm")
        d.text((W // 2, 290), "Not just an alarm — a full response system", fill=MUTED, font=font(22), anchor="mm")
        d.text((W // 2, 360), "People · AI · Dock drones · one clear trail", fill=CYAN, font=font(20, True), anchor="mm")
        d.text((W // 2, 450), "Croc Nexus AI Technologies  ·  Malaysia", fill=MUTED, font=font(18), anchor="mm")
        d.text((W // 2, 520), "partnerships@crocnexus.com", fill=GREEN, font=font(18), anchor="mm")
        frames.append(img)
    return frames


def build() -> tuple[Path, Path]:
    frames: list[Image.Image] = []
    frames += scene_title("Croc Sentinel", "Clear response  ·  AI assist  ·  Dock drone ready")
    frames += scene_dashboard_intro()
    frames += scene_incident_flow()
    frames += scene_drone_support()
    frames += scene_ai_dispatch()
    frames += scene_city_patrol()
    frames += scene_closing()

    mp4 = OUT_VID / "sentinel-drone-response-demo.mp4"
    gif = OUT_VID / "sentinel-drone-response-demo.gif"
    poster = OUT_IMG / "drone-response-poster.png"

    # poster = mid frame from drone scene
    poster_frame = frames[len(frames) // 2]
    poster_frame.save(poster, optimize=True)

    # GIF: subsample for size
    gif_frames = frames[::2]
    gif_frames[0].save(
        gif,
        save_all=True,
        append_images=gif_frames[1:],
        duration=int(1000 / (FPS / 2)),
        loop=0,
        optimize=True,
    )

    try:
        import imageio.v3 as iio
        import numpy as np

        arr = [np.asarray(fr.convert("RGB")) for fr in frames]
        iio.imwrite(mp4, arr, fps=FPS, codec="libx264", quality=8)
    except Exception as exc:  # noqa: BLE001
        print("MP4 write via imageio failed:", exc)
        # fallback: write frames as numbered png and instruct
        frame_dir = OUT_VID / "frames_drone"
        frame_dir.mkdir(exist_ok=True)
        for i, fr in enumerate(frames):
            fr.save(frame_dir / f"frame_{i:04d}.png")
        print("Wrote PNG frames only:", frame_dir)

    print(f"frames={len(frames)} mp4={mp4} gif={gif} poster={poster}")
    return mp4, gif


if __name__ == "__main__":
    build()
