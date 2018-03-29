"""Application to generate email addresses from a name."""


def create_email(firstname="first", lastname="last"):
    """Create address string."""

    mail_first = str(firstname).lower()
    mail_last = str(lastname).lower()
    mail = "{}.{}@company.com".format(mail_first, mail_last)

    return mail


if __name__ == '__main__':
    mail = create_email('Josh', 'Grant')
    print(mail)
