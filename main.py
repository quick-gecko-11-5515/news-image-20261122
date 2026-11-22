"""Copy the bundled entry.png to the output directory for the make.fun news-image bounty.

Copies entry.png to /output by default, or to the directory given as the first
command-line argument.
"""

from pathlib import Path
import shutil
import sys


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
