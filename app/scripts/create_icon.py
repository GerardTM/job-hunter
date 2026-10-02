from pathlib import Path

from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE = BASE_DIR / "assets" / "icon.png"
OUTPUT = BASE_DIR / "assets" / "icon.ico"


def main() -> None:
    image = Image.open(SOURCE).convert("RGBA")

    image.save(
        OUTPUT,
        format="ICO",
        sizes=[
            (256, 256),
            (128, 128),
            (64, 64),
            (48, 48),
            (32, 32),
            (16, 16),
        ],
    )

    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()