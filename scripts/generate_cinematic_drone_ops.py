# -*- coding: utf-8 -*-
"""
Cinematic Croc Sentinel demo — glass UI over real-world backgrounds.
Scenes: alert -> AI dispatch -> dock takeoff -> map route flight ->
live FPV + voice briefs -> auto RTH -> dock land.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
CINE = ROOT / "assets" / "images" / "cinema"
OUT_VID = ROOT / "assets" / "video"
OUT_IMG = ROOT / "assets" / "images"
OUT_VID.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
FPS = 24

# Dashboard-inspired glass palette (from esasecure console)
GLASS = (255, 255, 255, 210)
GLASS_DARK = (15, 23, 42, 200)
BLUE = (37, 99, 235)
BLUE_SOFT = (96, 165, 250)
CYAN = (34, 211, 238)
GREEN = (34, 197, 94)
RED = (239, 68, 68)
ORANGE = (249, 115, 22)
AMBER = (245, 158, 11)
MUTED = (148, 163, 184)
FG = (15, 23, 42)
FG_LIGHT = (248, 250, 252)
LINE = (226, 232, 240)


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


def load_bg(name: str) -> Image.Image:
    path = CINE / name
    img = Image.open(path).convert("RGB")
    img = img.resize((W, H), Image.Resampling.LANCZOS)
    return img


def darken(img: Image.Image, factor: float = 0.55) -> Image.Image:
    return ImageEnhance.Brightness(img).enhance(factor)


def rounded_glass(base: Image.Image, box, fill=(255, 255, 255, 185), outline=(255, 255, 255, 90), radius=22, blur=0):
    """Paste a frosted glass panel onto base (RGB)."""
    x0, y0, x1, y1 = box
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=fill, outline=outline, width=2)
    if blur:
        region = base.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(blur)).convert("RGBA")
        mask = Image.new("L", (x1 - x0, y1 - y0), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, x1 - x0 - 1, y1 - y0 - 1), radius=radius, fill=200)
        overlay.paste(region, (x0, y0), mask)
        d = ImageDraw.Draw(overlay)
        d.rounded_rectangle((x0, y0, x1, y1), radius=radius, outline=outline, width=2)
    out = base.convert("RGBA")
    out = Image.alpha_composite(out, overlay)
    return out.convert("RGB")


def pill(d: ImageDraw.ImageDraw, xy, text, bg=BLUE, fg=FG_LIGHT, pad=18, size=18, bold=True):
    x, y = xy
    f = font(size, bold)
    bbox = d.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.rounded_rectangle((x, y, x + tw + pad * 2, y + th + pad), radius=(th + pad) // 2, fill=bg)
    d.text((x + pad, y + pad // 2), text, fill=fg, font=f)


def voice_toast(base: Image.Image, text: str, sub: str = "", t: float = 0.0) -> Image.Image:
    """Bottom voice brief bar — dashboard style."""
    img = base.convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    y0 = H - 160
    pulse = int(12 + 6 * abs(math.sin(t * math.pi * 2)))
    d.rounded_rectangle((80, y0, W - 80, H - 48), radius=28, fill=(15, 23, 42, 220), outline=(96, 165, 250, 180), width=2)
    # mic icon circle
    cx, cy = 140, y0 + 56
    d.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), fill=(37, 99, 235, 255))
    d.ellipse((cx - pulse // 2, cy - pulse // 2, cx + pulse // 2, cy + pulse // 2), outline=(96, 165, 250, 160), width=2)
    d.text((cx, cy), "AI", fill=FG_LIGHT, font=font(16, True), anchor="mm")
    d.text((200, y0 + 28), "VOICE BRIEF", fill=BLUE_SOFT, font=font(14, True))
    d.text((200, y0 + 54), text, fill=FG_LIGHT, font=font(28, True))
    if sub:
        d.text((200, y0 + 92), sub, fill=MUTED, font=font(18))
    return Image.alpha_composite(img, overlay).convert("RGB")


def header_bar(img: Image.Image, title: str, status: str = "LIVE", clock: str = "00:42:18") -> Image.Image:
    """Top chrome mimicking Croc Sentinel command center."""
    img = rounded_glass(img, (40, 28, W - 40, 110), fill=(255, 255, 255, 200), outline=(255, 255, 255, 120), radius=40)
    d = ImageDraw.Draw(img)
    # logo box
    d.rounded_rectangle((60, 44, 108, 92), radius=12, fill=FG)
    d.text((84, 68), "C", fill=FG_LIGHT, font=font(22, True), anchor="mm")
    d.text((124, 52), "CROC SENTINEL", fill=FG, font=font(22, True))
    d.text((124, 78), "AI-Powered Security Command Center", fill=MUTED, font=font(13))
    d.text((W // 2, 68), title, fill=FG, font=font(20, True), anchor="mm")
    # status pills
    pill(d, (W - 380, 48), clock, bg=(241, 245, 249), fg=FG, size=14, pad=12)
    color = GREEN if status == "LIVE" else AMBER if status == "AI" else BLUE
    pill(d, (W - 200, 48), status, bg=color, fg=FG_LIGHT, size=14, pad=14)
    return img


def lerp(a, b, t):
    return a + (b - a) * t


def bezier(p0, p1, p2, p3, t):
    u = 1 - t
    return (
        u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1],
    )


def draw_map_panel(img: Image.Image, box, progress: float, returning: bool = False, show_route: bool = True):
    """Glass map with city grid + animated drone route."""
    x0, y0, x1, y1 = box
    img = rounded_glass(img, box, fill=(15, 23, 42, 210), outline=(96, 165, 250, 100), radius=24)
    d = ImageDraw.Draw(img)
    # inner map
    mx0, my0, mx1, my1 = x0 + 24, y0 + 56, x1 - 24, y1 - 24
    d.rounded_rectangle((mx0, my0, mx1, my1), radius=16, fill=(8, 14, 28), outline=(51, 65, 85), width=1)
    # streets
    for i in range(1, 8):
        yy = my0 + i * (my1 - my0) // 8
        d.line((mx0 + 10, yy, mx1 - 10, yy), fill=(40, 55, 80), width=2)
    for i in range(1, 10):
        xx = mx0 + i * (mx1 - mx0) // 10
        d.line((xx, my0 + 10, xx, my1 - 10), fill=(40, 55, 80), width=2)

    dock = (mx0 + 90, my1 - 90)
    incident = (mx0 + int((mx1 - mx0) * 0.72), my0 + int((my1 - my0) * 0.28))
    mid1 = (mx0 + (mx1 - mx0) * 0.35, my0 + (my1 - my0) * 0.55)
    mid2 = (mx0 + (mx1 - mx0) * 0.55, my0 + (my1 - my0) * 0.22)

    if show_route:
        # full route path
        pts = []
        for i in range(60):
            t = i / 59
            pts.append(bezier(dock, mid1, mid2, incident, t))
        for i in range(len(pts) - 1):
            d.line([pts[i], pts[i + 1]], fill=(37, 99, 235, 255) if isinstance(BLUE, tuple) else BLUE, width=3)
        # dashed return ghost
        for i in range(0, 60, 2):
            t = i / 59
            p = bezier(incident, mid2, mid1, dock, t)
            d.ellipse((p[0] - 1.5, p[1] - 1.5, p[0] + 1.5, p[1] + 1.5), fill=(34, 211, 238))

    # markers
    d.rounded_rectangle((dock[0] - 34, dock[1] - 18, dock[0] + 34, dock[1] + 18), radius=8, fill=BLUE)
    d.text(dock, "DOCK 3", fill=FG_LIGHT, font=font(12, True), anchor="mm")
    pulse = 10 + int(6 * abs(math.sin(progress * math.pi * 4)))
    d.ellipse((incident[0] - pulse, incident[1] - pulse, incident[0] + pulse, incident[1] + pulse), outline=RED, width=2)
    d.ellipse((incident[0] - 8, incident[1] - 8, incident[0] + 8, incident[1] + 8), fill=RED)
    d.text((incident[0], incident[1] - 28), "INCIDENT", fill=RED, font=font(12, True), anchor="mm")

    # drone position
    t = progress if not returning else progress
    if returning:
        pos = bezier(incident, mid2, mid1, dock, t)
    else:
        pos = bezier(dock, mid1, mid2, incident, t)
    # drone body
    dx, dy = pos
    d.ellipse((dx - 16, dy - 8, dx + 16, dy + 8), fill=CYAN)
    d.ellipse((dx - 30, dy - 3, dx - 16, dy + 3), fill=MUTED)
    d.ellipse((dx + 16, dy - 3, dx + 30, dy + 3), fill=MUTED)
    # trail
    trail_t = max(0, t - 0.08)
    if returning:
        trail = bezier(incident, mid2, mid1, dock, trail_t)
    else:
        trail = bezier(dock, mid1, mid2, incident, trail_t)
    d.line([(trail[0], trail[1]), (dx, dy)], fill=CYAN, width=2)

    d.text((x0 + 36, y0 + 18), "OPS MAP  ·  Live route", fill=FG_LIGHT, font=font(16, True))
    mode = "RTH — auto return" if returning else "AI route — outbound"
    d.text((x1 - 36, y0 + 18), mode, fill=CYAN if returning else BLUE_SOFT, font=font(14, True), anchor="rm")
    return img


def draw_live_feed(img: Image.Image, box, fpv: Image.Image, t: float, recording: bool = True):
    x0, y0, x1, y1 = box
    img = rounded_glass(img, box, fill=(15, 23, 42, 180), outline=(255, 255, 255, 80), radius=24)
    # paste FPV cropped
    fw, fh = x1 - x0 - 28, y1 - y0 - 70
    # subtle motion pan
    ox = int(20 * math.sin(t * 1.2))
    oy = int(12 * math.cos(t * 0.9))
    crop = fpv.resize((fw + 40, fh + 40), Image.Resampling.LANCZOS)
    crop = crop.crop((20 + ox, 20 + oy, 20 + ox + fw, 20 + oy + fh))
    img.paste(crop, (x0 + 14, y0 + 48))
    d = ImageDraw.Draw(img)
    d.text((x0 + 28, y0 + 16), "LIVE VIDEO  ·  Matrice 4TD", fill=FG_LIGHT, font=font(15, True))
    if recording:
        d.ellipse((x1 - 90, y0 + 14, x1 - 74, y0 + 30), fill=RED)
        d.text((x1 - 68, y0 + 14), "REC", fill=RED, font=font(14, True))
    # HUD crosshair
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 + 10
    d.line((cx - 24, cy, cx + 24, cy), fill=(255, 255, 255, 160), width=1)
    d.line((cx, cy - 24, cx, cy + 24), fill=(255, 255, 255, 160), width=1)
    d.text((x0 + 28, y1 - 28), "1080p  ·  12Mbps  ·  latency 180ms", fill=MUTED, font=font(12))
    return img


def draw_side_stats(img: Image.Image, box, alt: float, spd: float, batt: int, phase: str):
    x0, y0, x1, y1 = box
    img = rounded_glass(img, box, fill=(255, 255, 255, 200), outline=(255, 255, 255, 100), radius=22)
    d = ImageDraw.Draw(img)
    d.text((x0 + 24, y0 + 18), "AIRCRAFT TELEMETRY", fill=MUTED, font=font(13, True))
    rows = [
        ("Altitude", f"{alt:.0f} m"),
        ("Speed", f"{spd:.1f} m/s"),
        ("Battery", f"{batt}%"),
        ("Phase", phase),
        ("Link", "Stable"),
        ("AI assist", "ON"),
    ]
    for i, (k, v) in enumerate(rows):
        yy = y0 + 55 + i * 48
        d.text((x0 + 24, yy), k, fill=MUTED, font=font(14))
        color = GREEN if k in ("Link", "AI assist") else (ORANGE if batt < 30 and k == "Battery" else FG)
        d.text((x1 - 24, yy), v, fill=color, font=font(16, True), anchor="rm")
    return img


def scene_hold(frames, n, maker):
    for i in range(n):
        frames.append(maker(i / max(1, n - 1), i))


def build_frames() -> list[Image.Image]:
    city = darken(load_bg("city-night.png"), 0.62)
    dock = darken(load_bg("dock-rooftop.png"), 0.7)
    fpv = load_bg("fpv-street.png")
    ctrl = darken(load_bg("control-room.png"), 0.55)
    dash = None
    dash_path = OUT_IMG / "dash-overview.png"
    if dash_path.exists():
        dash = Image.open(dash_path).convert("RGB")

    frames: list[Image.Image] = []

    # --- 1. Title over city ---
    def title(t, i):
        img = city.copy()
        veil = Image.new("RGBA", (W, H), (10, 16, 32, int(140 + 40 * t)))
        img = Image.alpha_composite(img.convert("RGBA"), veil).convert("RGB")
        d = ImageDraw.Draw(img)
        d.text((W // 2, 400), "CROC SENTINEL", fill=FG_LIGHT, font=font(64, True), anchor="mm")
        d.text((W // 2, 480), "AI Dispatches the Air  ·  Dock returns by itself  ·  Live eyes for the console", fill=MUTED, font=font(24), anchor="mm")
        pill(d, (W // 2 - 160, 540), "Dock 3  ·  Matrice 4D / 4TD", bg=BLUE, fg=FG_LIGHT, size=16, pad=16)
        return img

    scene_hold(frames, int(2.5 * FPS), title)

    # --- 2. Dashboard glass intro ---
    def dash_intro(t, i):
        img = ctrl.copy()
        img = header_bar(img, "Command Center", "LIVE", "00:42:06")
        if dash is not None:
            panel = dash.copy()
            panel.thumbnail((1280, 720), Image.Resampling.LANCZOS)
            px = (W - panel.width) // 2
            py = 160
            img = rounded_glass(img, (px - 16, py - 16, px + panel.width + 16, py + panel.height + 16), fill=(255, 255, 255, 60), radius=28)
            img.paste(panel, (px, py))
        img = voice_toast(img, "Incident score 89 — high.", "AI recommends nearest Dock 3 + ground officer.", t=t)
        return img

    scene_hold(frames, int(3.2 * FPS), dash_intro)

    # --- 3. Dock unlock / takeoff ---
    def takeoff(t, i):
        img = dock.copy()
        img = header_bar(img, "Dock 3 — Auto mission", "AI", "00:42:18")
        d = ImageDraw.Draw(img)
        # glass cards
        img = rounded_glass(img, (60, 160, 520, 520), fill=(255, 255, 255, 210), radius=24)
        d = ImageDraw.Draw(img)
        d.text((90, 190), "AI DISPATCH", fill=BLUE, font=font(14, True))
        d.text((90, 230), "Ready nest selected", fill=FG, font=font(32, True))
        lines = [
            "Hardware: DJI Dock 3",
            "Aircraft: Matrice 4TD (thermal)",
            "Mission: Incident eyes + city grid",
            "Human approval: CONFIRMED",
            "Auto RTH: armed",
        ]
        for j, line in enumerate(lines):
            on = t > j * 0.15
            d.ellipse((100, 300 + j * 36, 114, 314 + j * 36), fill=GREEN if on else LINE)
            d.text((130, 298 + j * 36), line, fill=FG if on else MUTED, font=font(18))
        # lift animation hint
        lift = int(t * 80)
        d.text((W - 200, 900 - lift), "▲ TAKEOFF", fill=CYAN, font=font(22, True), anchor="mm")
        img = voice_toast(img, "Dock unlocked. Matrice 4TD taking off.", "Live video uplink starting.", t=t)
        return img

    scene_hold(frames, int(3.5 * FPS), takeoff)

    # --- 4. Map flight outbound ---
    n_out = int(6.0 * FPS)
    for i in range(n_out):
        t = i / (n_out - 1)
        img = city.copy()
        img = header_bar(img, "City route — outbound", "LIVE", f"00:42:{18 + int(t * 40):02d}")
        img = draw_map_panel(img, (60, 140, 1180, 820), progress=t, returning=False)
        alt = 30 + t * 90
        spd = 4 + t * 10
        batt = 96 - int(t * 8)
        img = draw_side_stats(img, (1220, 140, 1860, 520), alt, spd, batt, "Outbound")
        # mini live feed
        img = draw_live_feed(img, (1220, 540, 1860, 820), fpv, t=t * 3)
        if t < 0.25:
            img = voice_toast(img, "Climbing to patrol height.", "Route locked to incident pin.", t=t)
        elif t < 0.55:
            img = voice_toast(img, "Crossing central grid.", "Console has live eyes.", t=t)
        elif t < 0.85:
            img = voice_toast(img, "Approaching incident zone.", "Thermal assist online.", t=t)
        else:
            img = voice_toast(img, "On station. Holding orbit.", "Ground team two minutes out.", t=t)
        frames.append(img)

    # --- 5. Console watching split ---
    n_watch = int(4.0 * FPS)
    for i in range(n_watch):
        t = i / (n_watch - 1)
        img = ctrl.copy()
        img = header_bar(img, "Console live watch", "LIVE", "00:43:05")
        # large FPV
        img = draw_live_feed(img, (60, 140, 1240, 780), fpv, t=2 + t * 2)
        # right stack
        img = draw_map_panel(img, (1280, 140, 1860, 520), progress=0.95, returning=False, show_route=True)
        img = rounded_glass(img, (1280, 540, 1860, 780), fill=(255, 255, 255, 210), radius=22)
        d = ImageDraw.Draw(img)
        d.text((1310, 565), "VOICE CHANNEL", fill=MUTED, font=font(13, True))
        briefs = [
            "AI: heat signature near north alley",
            "Operator: keep orbit, no drop",
            "AI: ground unit ETA 90 seconds",
            "System: auto RTH window open",
        ]
        for j, b in enumerate(briefs):
            on = t > j * 0.2
            d.text((1310, 610 + j * 38), ("▶ " if on else "· ") + b, fill=FG if on else MUTED, font=font(16))
        img = voice_toast(img, "Voice brief to all responders.", "Thermal tip shared on the incident timeline.", t=t)
        frames.append(img)

    # --- 6. Auto return to home ---
    n_rth = int(5.5 * FPS)
    for i in range(n_rth):
        t = i / (n_rth - 1)
        img = city.copy()
        img = header_bar(img, "Auto return — RTH", "AI", f"00:44:{int(t * 50):02d}")
        img = draw_map_panel(img, (60, 140, 1180, 820), progress=t, returning=True)
        alt = 120 - t * 95
        spd = 12 - t * 4
        batt = 78 - int(t * 6)
        img = draw_side_stats(img, (1220, 140, 1860, 480), alt, max(2, spd), batt, "Auto RTH")
        img = rounded_glass(img, (1220, 500, 1860, 820), fill=(255, 255, 255, 215), radius=22)
        d = ImageDraw.Draw(img)
        d.text((1250, 530), "RETURN PROGRAM", fill=BLUE, font=font(14, True))
        checks = [
            ("Mission complete", t > 0.05),
            ("Safe corridor locked", t > 0.2),
            ("Home dock ready", t > 0.4),
            ("Landing sequence", t > 0.7),
            ("Charge cycle starts", t > 0.9),
        ]
        for j, (label, on) in enumerate(checks):
            d.ellipse((1260, 580 + j * 40, 1278, 598 + j * 40), fill=GREEN if on else LINE)
            d.text((1295, 578 + j * 40), label, fill=FG if on else MUTED, font=font(18))
        if t < 0.4:
            img = voice_toast(img, "AI closing mission. Returning home.", "No pilot stick required for RTH.", t=t)
        elif t < 0.75:
            img = voice_toast(img, "Descending to Dock 3.", "Precision landing unlocked.", t=t)
        else:
            img = voice_toast(img, "Aircraft nested. Charging.", "Ready for the next call.", t=t)
        frames.append(img)

    # --- 7. Dock land close ---
    def land(t, i):
        img = dock.copy()
        img = header_bar(img, "Docked & charging", "LIVE", "00:45:02")
        img = rounded_glass(img, (60, 700, W - 60, 900), fill=(255, 255, 255, 220), radius=28)
        d = ImageDraw.Draw(img)
        d.text((W // 2, 760), "Mission archived on the incident timeline", fill=FG, font=font(28, True), anchor="mm")
        d.text((W // 2, 820), "Live video · voice briefs · route · RTH — all saved", fill=MUTED, font=font(18), anchor="mm")
        img = voice_toast(img, "All clear. Aircraft home.", "Proof package ready for review.", t=t)
        return img

    scene_hold(frames, int(3.0 * FPS), land)

    # --- 8. Closing ---
    def close(t, i):
        img = city.copy()
        veil = Image.new("RGBA", (W, H), (10, 16, 32, 180))
        img = Image.alpha_composite(img.convert("RGBA"), veil).convert("RGB")
        d = ImageDraw.Draw(img)
        d.text((W // 2, 360), "People · AI · Dock drones", fill=FG_LIGHT, font=font(48, True), anchor="mm")
        d.text((W // 2, 440), "One console. Live eyes. Auto return. Full proof.", fill=MUTED, font=font(24), anchor="mm")
        d.text((W // 2, 560), "Croc Nexus AI Technologies  ·  Malaysia", fill=BLUE_SOFT, font=font(20), anchor="mm")
        return img

    scene_hold(frames, int(3.0 * FPS), close)
    return frames


def write_outputs(frames: list[Image.Image]):
    mp4 = OUT_VID / "sentinel-cinematic-drone-ops.mp4"
    gif = OUT_VID / "sentinel-cinematic-drone-ops.gif"
    poster = OUT_IMG / "cinematic-drone-ops-poster.png"

    frames[len(frames) // 3].save(poster, quality=92)

    # GIF subsample for GitHub
    step = max(1, len(frames) // 90)
    gif_frames = [fr.resize((960, 540), Image.Resampling.LANCZOS) for fr in frames[::step]]
    gif_frames[0].save(gif, save_all=True, append_images=gif_frames[1:], duration=int(1000 / 10), loop=0, optimize=True)

    try:
        import imageio.v3 as iio

        arr = [np.asarray(fr.convert("RGB")) for fr in frames]
        iio.imwrite(mp4, arr, fps=FPS, codec="libx264", quality=7)
    except Exception as exc:  # noqa: BLE001
        print("MP4 failed:", exc)
        raise

    print(f"frames={len(frames)} duration~{len(frames)/FPS:.1f}s")
    print("mp4:", mp4, mp4.stat().st_size)
    print("gif:", gif, gif.stat().st_size)
    print("poster:", poster)
    return mp4, gif, poster


if __name__ == "__main__":
    fr = build_frames()
    write_outputs(fr)
