"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) recalling a
childhood memory to /output/entry.txt. Python 3.13 standard library
only, no network at run time.
"""

from pathlib import Path

ENTRY = (
    "At dawn I stood barefoot on the cold kitchen tiles, waiting for "
    "the kettle while my mother hummed a song she never finished."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-280 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be a single sentence"
    )
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    written = output_path.read_text(encoding="utf-8")
    assert written == ENTRY, "written output must match the entry exactly"


if __name__ == "__main__":
    main()
