import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")

WEB_LOGO_PATH = BASE_DIR / "Image" / "inverseLogo.png"
DOC_LOGO_PATH = BASE_DIR / "Image" / "Logo.png"

COMPANY_FOOTER = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."