from veda_cli.main import main


def test_main_with_version_flag_prints_version(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["veda", "--version"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "veda-cli 0.1.0 (core 0.1.0)"


def test_main_without_flags_prints_ready(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["veda"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "veda-cli ready"
