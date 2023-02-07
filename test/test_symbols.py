from pkg import symbols

def assert_valid_SP500(data):
    assert data is not None
    assert 'Symbol' in data.columns
    symbols_returned = len(data.Symbol)
    assert 490 < symbols_returned < 510  # SP500 shoud return about 500 symbols

def test_grab_from_HTML_file():
    data = symbols.grab_from_HTML_file()
    assert_valid_SP500(data)

def test_grab_SP500_from_wikipedia():
    data = symbols.grab_SP500_from_wikipedia()
    assert_valid_SP500(data)

def test_grab_SP500_from_github_mfs_dataset():
    data = symbols.grab_SP500_from_github_mfs_dataset()
    assert_valid_SP500(data)

