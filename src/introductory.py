"""A tiny CLI for a repository with unnecessarily high ambitions."""

import argparse


def build_message(name: str = "INTRODUCTORY.exe") -> str:
    """Return the demo's welcome message."""
    return (
        f"{name} — booting the ambition engine...\n"
        "Mission: turn confusion into a well-organized repository.\n"
        "Confidence: 100%\n"
        "Evidence: README.md\n"
        "Remember: if it works, write a test. If it doesn't, write a better error message."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="A tiny demo with a suspiciously large README.")
    parser.add_argument("--name", default="INTRODUCTORY.exe", help="Name shown in the greeting")
    args = parser.parse_args()
    print(build_message(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
