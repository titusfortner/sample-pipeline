from subprocess import getoutput

def test_output():
    expected = "josh.grant@company.com"
    actual = getoutput("python generate_email.py")

    assert expected == actual