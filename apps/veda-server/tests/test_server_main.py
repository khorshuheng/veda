from veda_server.main import main


def test_main_prints_server_status(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "veda-server running (core 0.1.0)"
