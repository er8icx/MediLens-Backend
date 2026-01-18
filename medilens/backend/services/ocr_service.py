import cv2
import pytesseract
import numpy as np


def extract_text_from_image(image_path: str) -> str:
    # 1️⃣ Read image
    image = cv2.imread(image_path)

    if image is None:
        return ""

    # 2️⃣ Resize (helps small text)
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # 3️⃣ Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4️⃣ Denoise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # 5️⃣ Adaptive threshold (VERY IMPORTANT)
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    # 6️⃣ OCR config (text‑focused)
    custom_config = r"--oem 3 --psm 6"

    text = pytesseract.image_to_string(thresh, config=custom_config)

    return text.strip()
