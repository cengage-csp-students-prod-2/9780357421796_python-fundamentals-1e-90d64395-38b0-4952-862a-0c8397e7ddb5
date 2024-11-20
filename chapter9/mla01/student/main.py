class EmailNotValidError():
""" Raised when the target email is not valid """
 """
    Custom exception for invalid email addresses.

    Attributes:
        message (str): Description of the error to help with debugging.
"""
    def __init__(self, message):
        super().__init__(message)

def is_email_valid(mailing_list):
    """
      Your docstring documentation starts here.

      For more information on how to proper document your function, please refer to the official PEP8:
       https://www.python.org/dev/peps/pep-0008/#documentation-strings.

   """
   """
    Validates an email address to ensure it contains an '@' symbol.

    Args:
        email (str): The email address to validate.

    Raises:
        EmailNotValidError: If the email address does not contain an '@' symbol.

    Returns:
        bool: True if the email is valid, False otherwise (though this is redundant since it raises an exception).
    """

    if '@' not in email:
        raise EmailNotValidError(f"Invalid email address: {email}. Missing '@' symbol.")
    return True
    

for key, email in  # Loop through the mailing list:

    if '@' not in  # Check if the email contains an @:

        raise  # Raise an EmailNotValidError exception if the @ is not present



def is_email_valid_extended(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """


    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:

        # Loop through the mailing list
        for key, email in # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:


        return # Return a user-friendly message to cast the exception



def is_email_valid_extended_finally(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

    final_users_list = # Array to hold user ids

    # Inserted a try.., except.. block to cast the exception
    try:
        # Loop through the mailing list
        for key, email in  # Your mailing list:


            if '@' in # Check if the @ is present in the email:

                # Append the id of users with valid emails

        else:


            raise # Raises an EmailNotValidError otherwise
    except # Your user-defined exception:

        # Print a user-friendly message to cast the exception
    finally:

        return # Return the id of the users with valid email
