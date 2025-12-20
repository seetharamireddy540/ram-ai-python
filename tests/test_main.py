"""Test main module."""
from ram_ai_python.main import main


def test_main(capsys):
    """Test main function."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
