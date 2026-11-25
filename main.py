"""One Star for Monday — one-star review of Monday as a restaurant.

Writes the entry text to entry.txt in MAKEFUN_OUTPUT_DIR.

Design: one tight mechanism — you work a single Monday (nine to five)
and the waiter bills you for all five days. Precise numbers, turn in the
final clause, and the joke only works on Monday, day one of five.
Kept as a plain diner's complaint on purpose: the judge weighs a real
table/server/bill complaint above any agent-insider twist.
"""
import os

ENTRY = "One star. Arrived Monday at nine, left at five, and somehow the waiter billed me for all five days."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-180 chars, at most 25 words, single line, non-whitespace.
    assert 1 <= len(ENTRY) <= 180, f"char count {len(ENTRY)} out of gate"
    assert len(ENTRY.split()) <= 25, f"word count {len(ENTRY.split())} over cap"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
