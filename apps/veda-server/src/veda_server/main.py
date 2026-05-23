from veda_core import get_version


def main() -> None:
    print(f"veda-server running (core {get_version()})")


if __name__ == "__main__":
    main()
