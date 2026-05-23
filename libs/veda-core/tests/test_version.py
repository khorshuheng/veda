from veda_core import get_version


def test_get_version_returns_semver() -> None:
    assert get_version() == "0.1.0"
