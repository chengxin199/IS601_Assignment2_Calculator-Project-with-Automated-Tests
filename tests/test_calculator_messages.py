def test_division_other_value_error(monkeypatch, capsys):
    # Force the division function to raise a ValueError with a different message
    import app.calculator as calc

    def fake_div(a, b):
        raise ValueError("Some other division error")

    # Patch the division function used by the calculator module (it was imported into app.calculator)
    monkeypatch.setattr('app.calculator.division', fake_div)

    # Simulate user input that triggers division and then exit
    inputs = iter(["divide 1 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calc.calculator()
    captured = capsys.readouterr().out
    assert "Some other division error" in captured
