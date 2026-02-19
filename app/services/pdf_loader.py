import fitz
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESUME_PATH = BASE_DIR / "data" / "sandeep_sharma.pdf"


def load_resume_text() -> str:
    if not RESUME_PATH.exists():
        raise FileNotFoundError(f"{RESUME_PATH.name} not found in app/data")

    with fitz.open(RESUME_PATH) as doc:
        pages = [
            page.get_text("text").strip()
            for page in doc
            if page.get_text("text")
        ]

    return "\n".join(pages)
