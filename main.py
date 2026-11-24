# One-word entry: writes the chosen word, and nothing else,
# to the file the grader reads. Fixed text every run:
# no input, no randomness, no network, no environment reads.
from pathlib import Path


def _pick():
    head, tail = "susu", "rrus"
    return "".join((head, tail))


def _check(word):
    ok = 1 <= len(word) <= 24 and word == word.strip()
    ok = ok and all(ch not in word for ch in " \n")
    assert ok
    return word


def _save(word):
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(word, encoding="utf-8")


if __name__ == '__main__':
    _save(_check(_pick()))
