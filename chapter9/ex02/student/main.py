# Use the function return to create an error

import string

def createError():
    dinning = dict(
        name="Johnny's Restaurant",
        location="Times Square"
    )
    print(f"I went to eat at {dinning['name']} yesterday in {dinning['location']}.")  # Fixed the key to 'location'

    f = string.ascii_letters  # Corrected the typo
    print(f)
    return


# Use this code to test your function
if __name__ == '__main__':
    createError()

