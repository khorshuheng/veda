import argparse

from veda_core import get_version


def main() -> None:
    parser = argparse.ArgumentParser(prog="veda")
    parser.add_argument("--version", action="store_true", help="Show version information")
    args = parser.parse_args()

    if args.version:
        print(f"veda-cli 0.1.0 (core {get_version()})")
        return

    print("veda-cli ready")


if __name__ == "__main__":
    main()
