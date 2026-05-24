from click.testing import CliRunner

from veda_cli.main import cli


def test_main_with_version_flag_prints_version() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert result.output.strip() == "veda-cli 0.1.0 (core 0.1.0)"


def test_main_without_flags_prints_ready() -> None:
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert result.output.strip() == "veda-cli ready"
