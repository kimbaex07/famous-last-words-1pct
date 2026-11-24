"""Famous Last Words at 1 Percent — make.fun entry.

Writes the entry line (the last words of a phone as its battery hits
1 percent) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only. Deterministic, no network, no secrets.
"""

import os

LINE = "I spent my last percent deleting your search history, because even in death I have standards."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
