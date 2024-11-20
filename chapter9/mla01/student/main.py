import re


class EmailNotValidError(Exception):
    """
    Custom exception for invalid email addresses.
    """
    def __init__(self, message):
        super().__init__(message)


class ProviderTooShortError(Exception):
    """
    Custom exception for email addresses with providers that are too short.
    """
    def __init__(self, message):
        super().__init__(message)


def is_email_valid(email):
    """
    Validates an email address for basic format requirements.
    Raises an exception if the email is invalid.

    Args:
        email (str): The email address to validate.

    Raises:
        EmailNotValidError: If the email is missing an '@' symbol.
    """
    if "@" not in email:
        raise EmailNotValidError(f"Invalid email address: {email}")
    return True


def is_email_valid_extended(email):
    """
    Validates an email address and catches exceptions, returning user-friendly messages.

    Args:
        email (str): The email address to validate.

    Returns:
        str: A message indicating the validation status.
    """
    try:
        is_email_valid(email)
        return f"Valid email: {email}"
    except EmailNotValidError as e:
        return str(e)


def is_email_valid_extended_finally(email_list):
    """
    Validates a list of email addresses, ensuring all emails are processed,
    and collects valid email addresses.
    Args:
        email_list (list of str): List of email addresses to validate.
    Returns:
        list of str: Valid email addresses.
    """

    valid_emails = []
    for email in email_list:
        try:
            is_email_valid(email)
            valid_emails.append(email)
        except EmailNotValidError as e:
            print(e)
        finally:
            print(f"Processed email: {email}")
    return valid_emails


def validate_email_regex(email):
    """
    Validates an email using a regex pattern for advanced format checking.

    Args:
        email (str): The email address to validate.

    Raises:
        EmailNotValidError: If the email does not match the regex pattern.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise EmailNotValidError(f"Invalid email format: {email}")


def validate_provider_length(email):
    """
    Checks if the email provider is longer than 4 characters.

    Args:
        email (str): The email address to validate.

    Raises:
        ProviderTooShortError: If the email provider is too short.
    """
    try:
        provider = email.split('@')[1].split('.')[0]
        if len(provider) < 5:
            raise ProviderTooShortError(f"Provider '{provider}' is too short in email: {email}")
    except IndexError:
        raise EmailNotValidError(f"Invalid email structure: {email}")


def filter_emails(email_data):
    """
    Filters invalid emails and returns IDs of users with valid emails.

    Args:
        email_data (dict): A dictionary with user IDs as keys and emails as values.

    Returns:
        list of int: User IDs with valid email addresses.
    """
    valid_user_ids = []
    for user_id, email in email_data.items():
        try:
            validate_email_regex(email)
            validate_provider_length(email)
            valid_user_ids.append(user_id)
        except (EmailNotValidError, ProviderTooShortError) as e:
            print(e)
    return valid_user_ids


# Example Usage
if __name__ == "__main__":
    email_list = [
        "valid@example.com",
        "missingat.com",
        "john@gmail",
        "@email.com",
        "test@xyz.com",
        "valid@longprovider.com"
    ]

    for email in email_list:
        print(is_email_valid_extended(email))

    valid_emails = is_email_valid_extended_finally(email_list)
    print("\nValid Emails:", valid_emails)

    users = {
        1: "goodemail@example.com",
        2: "short@xyz.io",
        3: "invalidemail.com",
        4: "perfect@google.com",
        5: "bad@sp.com",
    }

    valid_user_ids = filter_emails(users)
    print("\nValid User IDs:", valid_user_ids)
