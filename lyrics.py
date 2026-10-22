import sys
import os
from time sleep
import time

# Đảm bảo mã hóa đầu ra luôn là UTF-8 (đặc biệt quan trọng trên GitHub Codespaces/Linux/Git Bash)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Kích hoạt ANSI Color Code nếu chạy trên Windows Git Bash
os.system('')

def printlyrics():
    lyrics = [
        ("\nCó phải anh đã cứu thế giới ở một cuộc đời trước đây", 0.07, 0.1),
        ("Nên là em mới bước tới dịu dàng ta nắm tay", 0.07, 0.2),
        ("Đi qua bão giông - đang cuộn xoay - những tâm tư bủa vây ", 0.08, 0.2),
        ("Người đã vì anh mà ôm lấy", 0.07, 0.08),
        ("Và giờ thì cả thế giới của anh đang ở đây", 0.08, 0.1),
        ("Là người con gái đứng trước mắt anh lúc này", 0.07, 0.5),
        ("Dường như chính anh đang nằm mơ", 0.08, 0.1),
        ("Có đâu ngờ mình may mắn đến", 0.09, 0.3),
        ("Nhường này", 0.07, 0.5)
    ]
    
    color_stops = [
        (46, 204, 113),
        (241, 196, 15),
        (230, 126, 34),
        (231, 76, 60),
        (155, 89, 182),
        (52, 152, 219)
    ]

    def get_rgb_color(ratio):
        if ratio <= 0:
            return color_stops[0]
        if ratio >= 1:
            return color_stops[-1]
        scaled = ratio * (len(color_stops) - 1)
        idx = int(scaled)
        frac = scaled - idx
        c1 = color_stops[idx]
        c2 = color_stops[idx + 1]
        r = int(c1[0] + (c2[0] - c1[0]) * frac)
        g = int(c1[1] + (c2[1] - c1[1]) * frac)
        b = int(c1[2] + (c2[2] - c1[2]) * frac)
        return (r, g, b)

    for text, delay, wait in lyrics:
        length = len(text)
        for i, char in enumerate(text):
            ratio = i / (length - 1) if length > 1 else 0
            r, g, b = get_rgb_color(ratio)
            # Dùng ANSI escape RGB 24-bit
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            sys.stdout.flush()
            sleep(delay)
        print()
        sleep(wait)

if __name__ == "__main__":
    time.sleep(1)
    printlyrics()
