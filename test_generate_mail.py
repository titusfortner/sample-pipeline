from generate_email import create_email


def test_basic():
    expected = "john.smith@company.com"
    actual = create_email("john", "smith")

    assert expected == actual


def test_none():
    expected = "first.last@company.com"
    actual = create_email()

    assert expected == actual


def test_casing():
    expected = "john.smith@company.com"
    actual = create_email("John", "SMITH")

    assert expected == actual
