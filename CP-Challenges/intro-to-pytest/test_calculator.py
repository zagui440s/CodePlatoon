import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_subtract():
    assert calculator.calculate(2,3, "subtract") == -1

def test_multiply():
    assert calculator.calculate(10, 2, "multiply") == 20

def test_divide():
    assert calculator.calculate(6, 3, "divide") == 2

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(monkeypatch,capsys):
    monkeypatch.setattr("sys.argv", ["calculator.py", "10", "2", "multiply"])
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: 20.0\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios

