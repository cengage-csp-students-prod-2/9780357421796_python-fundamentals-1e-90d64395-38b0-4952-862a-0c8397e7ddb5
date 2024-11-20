import re


class EmailNotValidError(Exception):
    """
    Custom exception for invalid email addresses.
    """
    def __init__(self, message):
        super().__init__(message)


class ProviderTooShortError(Exception):
    """
    Custom exception for email addresses with short providers.
    """
    def __init__(self, message):
        super().__init__(message)


def is_email_valid(email):
    """
    Validates an email address using regex.

    Args:
        email (str): The email address to validate.

    Raises:
        EmailNotValidError: If the email address does not match the required pattern.

    Returns:
        bool: True if the email is valid.
    """
    # Regex for validating email addresses
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise EmailNotValidError(f"Invalid email address: {email}")
    return True


def is_email_valid_extended(email):
    """
    Validates an email address and handles exceptions gracefully.

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


def is_email_valid_extended_finally(emails):
    """
    Validates a list of email addresses and returns a list of valid ones.

    Args:
        emails (list of str): A list of email addresses to validate.

    Returns:
        list of str: A list of valid email addresses.
    """
    valid_emails = []
    for email in emails:
        try:
            is_email_valid(email)
            valid_emails.append(email)
        except EmailNotValidError as e:
            print(e)
        finally:
            print(f"Processed email: {email}")
    return valid_emails


def validate_provider_length(email):
    """
    Validates the provider length of an email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ProviderTooShortError: If the provider is less than 5 characters.
    """
    try:
        provider = email.split('@')[1].split('.')[0]
        if len(provider) < 5:
            raise ProviderTooShortError(f"Provider '{provider}' is too short in email: {email}")
    except IndexError:
        raise EmailNotValidError(f"Invalid email structure: {email}")


def filter_emails(emails):
    """
    Filters invalid emails and returns the IDs of users with valid emails.

    Args:
        emails (dict): A dictionary of user IDs and email addresses.

    Returns:
        list of int: A list of user IDs with valid email addresses.
    """
    valid_ids = []
    for user_id, email in emails.items():
        try:
            is_email_valid(email)
            validate_provider_length(email)
            valid_ids.append(user_id)
        except (EmailNotValidError, ProviderTooShortError) as e:
            print(e)
    return valid_ids


# Example Usage
if __name__ == "__main__":
    email_list = [
        "valid@example.com",
        "invalidemail.com",
        "john@gmail",
        "@email.com",
        "test@spam.com",
    ]

    # Task 2: Extended validation
    for email in email_list:
        print(is_email_valid_extended(email))

    # Task 3: Finally block
    valid_emails = is_email_valid_extended_finally(email_list)
    print("Valid emails:", valid_emails)

    # Task 4: Advanced validation
    users = {
        1: "validuser@example.com",
        2: "short@xyz.io",
        3: "badformat.com",
        4: "ok@google.com",
        5: "test@sp.com",
    }

    valid_user_ids = filter_emails(users)
    print("Users with valid emails:", valid_user_ids)
