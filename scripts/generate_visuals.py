# -*- coding: utf-8 -*-
"""Generate animated GIF and PNG frames for Croc Sentinel incident flow demo."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_IMG = ROOT / "assets" / "images"
OUT_VID = ROOT / "assets" / "video"
OUT_IMG.mkdir(parents=True, exist_ok=True)
OUT_VID.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
BG = (15, 23, 42)
FG = (248, 250, 252)
MUTED = (148, 163, 184)
ACCENT = (96, 165, 250)
GREEN = (74, 222, 128)
RED = (248, 113, 113)
PURPLE = (192, 132, 252)
ORANGE = (251, 146, 60)

STEPS = [
    ("1", "Something triggers", "Door / panic / sensor", RED),
    ("2", "Phone knows instantly", "App / call / message", ACCENT),
    ("3", "AI judges urgency", "Score + plain reason", PURPLE),
    ("4", "Right steps run", "Fire / SOS / intrusion", GREEN),
    ("5", "Nearest person sent", "On map / timed arrival", ORANGE),
    ("6", "Team for big events", "Roles / adjust live", ACCENT),
    ("7", "Nobody left hanging", "Escalate if no answer", (100, 116, 139)),
    ("8", "Marked resolved", "Done on phone", PURPLE),
    ("9", "Everything saved", "Proof for auditors", GREEN),
]


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_frame(active: int, progress: float) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    title_f = _font(34, True)
    sub_f = _font(18)
    step_f = _font(22, True)
    body_f = _font(16)
    small_f = _font(13)

    d.text((W // 2, 42), "When something goes wrong", fill=FG, font=title_f, anchor="mm")
    d.text((W // 2, 78), "Croc Sentinel - step by step", fill=MUTED, font=sub_f, anchor="mm")

    cols = 5
    pad_x, pad_y = 36, 130
    gap_x, gap_y = 18, 18
    card_w = (W - 2 * pad_x - (cols - 1) * gap_x) // cols
    card_h = 200

    for i, (num, title, sub, color) in enumerate(STEPS):
        row, col = divmod(i, cols)
        x = pad_x + col * (card_w + gap_x)
        y = pad_y + row * (card_h + gap_y)
        is_active = i == active
        is_done = i < active

        fill = (30, 41, 59) if not is_active else (30, 58, 95)
        outline = color if (is_active or is_done) else (71, 85, 105)
        width = 4 if is_active else 2
        d.rounded_rectangle((x, y, x + card_w, y + card_h), radius=14, fill=fill, outline=outline, width=width)

        if is_done:
            d.ellipse((x + card_w - 34, y + 12, x + card_w - 10, y + 36), fill=GREEN)
            d.text((x + card_w - 22, y + 24), "OK", fill=BG, font=small_f, anchor="mm")

        d.ellipse((x + 16, y + 16, x + 52, y + 52), fill=color if is_active else (51, 65, 85))
        d.text((x + 34, y + 34), num, fill=BG if is_active else FG, font=step_f, anchor="mm")
        d.text((x + 16, y + 68), title, fill=FG if is_active else MUTED, font=body_f)
        d.text((x + 16, y + 96), sub, fill=MUTED, font=small_f)

        if is_active:
            pulse = int(8 + 6 * math.sin(progress * math.pi * 2))
            d.rounded_rectangle(
                (x - pulse, y - pulse, x + card_w + pulse, y + card_h + pulse),
                radius=14 + pulse,
                outline=color,
                width=2,
            )

    bar_y = H - 88
    d.rounded_rectangle((80, bar_y, W - 80, bar_y + 14), radius=7, fill=(30, 41, 59))
    frac = (active + progress) / len(STEPS)
    d.rounded_rectangle((80, bar_y, 80 + int((W - 160) * frac), bar_y + 14), radius=7, fill=ACCENT)
    d.text(
        (W // 2, bar_y + 36),
        f"Step {active + 1} of {len(STEPS)}: {STEPS[active][1]}",
        fill=FG,
        font=body_f,
        anchor="mm",
    )
    d.text(
        (W // 2, H - 28),
        "Alert first - people stay in charge - every step saved",
        fill=MUTED,
        font=small_f,
        anchor="mm",
    )
    return img


def make_gif() -> Path:
    frames: list[Image.Image] = []
    for i in range(len(STEPS)):
        for f in range(8):
            frames.append(draw_frame(i, f / 8))
    out = OUT_VID / "incident-flow-demo.gif"
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=450,
        loop=0,
        optimize=True,
    )
    return out


def make_timeline_table() -> Path:
    img = Image.new("RGB", (1400, 900), BG)
    d = ImageDraw.Draw(img)
    title_f = _font(32, True)
    hdr_f = _font(16, True)
    cell_f = _font(14)
    time_f = _font(13, True)

    d.text((700, 40), "Incident flow - visual timeline", fill=FG, font=title_f, anchor="mm")
    d.text((700, 75), "One real-feeling example from trigger to proof", fill=MUTED, font=cell_f, anchor="mm")

    rows = [
        ("10:42:03", "Trigger", "North gate sensor fires", "Device", RED),
        ("10:42:04", "Alert", "Phone + app notified", "Seconds, not minutes", ACCENT),
        ("10:42:05", "Score", "89/100 HIGH - repeated after hours", "AI explains why", PURPLE),
        ("10:42:06", "Call", "On-duty officer rings", "Right person first", ORANGE),
        ("10:42:20", "Escalate", "No answer -> site admin", "Never a dead end", (100, 116, 139)),
        ("10:42:31", "Respond", "Admin sees map + reason", "Heads to gate", GREEN),
        ("10:49:00", "Resolve", "Marked done in app", "Human confirms", PURPLE),
        ("10:49:01", "Proof", "Full timeline saved", "Audit-ready", GREEN),
    ]

    x0, y0, x1 = 60, 110, 1340
    col_w = [140, 120, 520, 420]
    headers = ["Time", "Step", "What happened", "Why it matters"]
    d.rounded_rectangle((x0, y0, x1, y0 + 44), radius=10, fill=(30, 58, 95))
    cx = x0 + 12
    for h, w in zip(headers, col_w):
        d.text((cx, y0 + 22), h, fill=FG, font=hdr_f, anchor="lm")
        cx += w

    y = y0 + 44
    row_h = 86
    for i, (t, step, what, why, color) in enumerate(rows):
        fill = (30, 41, 59) if i % 2 == 0 else (24, 33, 48)
        d.rectangle((x0, y, x1, y + row_h), fill=fill)
        d.line((x0, y + row_h, x1, y + row_h), fill=(51, 65, 85), width=1)
        cx = x0 + 12
        d.text((cx, y + row_h // 2), t, fill=ACCENT, font=time_f, anchor="lm")
        cx += col_w[0]
        d.rounded_rectangle((cx, y + 24, cx + 90, y + 62), radius=8, fill=color)
        d.text((cx + 45, y + 43), step, fill=BG, font=hdr_f, anchor="mm")
        cx += col_w[1]
        d.text((cx, y + row_h // 2), what, fill=FG, font=cell_f, anchor="lm")
        cx += col_w[2]
        d.text((cx, y + row_h // 2), why, fill=MUTED, font=cell_f, anchor="lm")
        y += row_h

    d.rounded_rectangle((x0, y + 16, x1, y + 96), radius=12, outline=GREEN, width=2)
    d.text((x0 + 20, y + 40), "Ordinary alarms stop at step 2.", fill=MUTED, font=cell_f)
    d.text(
        (x0 + 20, y + 68),
        "Croc Sentinel runs the full loop - and saves proof at the end.",
        fill=GREEN,
        font=hdr_f,
    )

    out = OUT_IMG / "incident-timeline-table.png"
    img.save(out, optimize=True)
    return out


def make_journey_cards() -> Path:
    img = Image.new("RGB", (1600, 600), BG)
    d = ImageDraw.Draw(img)
    title_f = _font(30, True)
    card_title = _font(22, True)
    body = _font(15)

    d.text((800, 36), "The full response journey", fill=FG, font=title_f, anchor="mm")

    cards = [
        ("BEFORE", "Are we ready?", ["Response plans set", "Readiness score", "Practice drills"], GREEN),
        (
            "DURING",
            "Who goes? What happens?",
            ["Score + call + dispatch", "Live map + timeline", "Team roles on big events"],
            ACCENT,
        ),
        (
            "AFTER",
            "What really happened?",
            ["Full timeline saved", "Proof of response", "Post-incident review"],
            PURPLE,
        ),
    ]
    cw, ch, gap = 460, 420, 40
    start_x = (1600 - (3 * cw + 2 * gap)) // 2
    y = 100
    for i, (phase, question, bullets, color) in enumerate(cards):
        x = start_x + i * (cw + gap)
        d.rounded_rectangle((x, y, x + cw, y + ch), radius=20, fill=(30, 41, 59), outline=color, width=3)
        d.rounded_rectangle((x, y, x + cw, y + 70), radius=20, fill=color)
        d.rectangle((x, y + 50, x + cw, y + 70), fill=color)
        d.text((x + cw // 2, y + 35), phase, fill=BG, font=card_title, anchor="mm")
        d.text((x + cw // 2, y + 110), question, fill=FG, font=card_title, anchor="mm")
        by = y + 160
        for b in bullets:
            d.ellipse((x + 36, by + 4, x + 48, by + 16), fill=color)
            d.text((x + 60, by), b, fill=MUTED, font=body)
            by += 42
        if i < 2:
            ax = x + cw + 8
            d.polygon(
                [
                    (ax, y + ch // 2),
                    (ax + gap - 16, y + ch // 2 - 16),
                    (ax + gap - 16, y + ch // 2 + 16),
                ],
                fill=MUTED,
            )

    out = OUT_IMG / "journey-before-during-after.png"
    img.save(out, optimize=True)
    return out


if __name__ == "__main__":
    print(f"GIF: {make_gif()}")
    print(f"Timeline table: {make_timeline_table()}")
    print(f"Journey cards: {make_journey_cards()}")
