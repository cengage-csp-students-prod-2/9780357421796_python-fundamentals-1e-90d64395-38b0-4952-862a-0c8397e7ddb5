# Write your function here

import string  # Replace with any package you want to inspect

def resources_scanner(package):
    """
    This function takes a package (module) as input and prints out the names
    of all the resources (attributes, methods, classes) defined in that package.
    
    :param package: The package/module whose resources we want to list.
    """
    # Get the list of resources in the package using dir()
    resources = dir(package)
    
    # Loop through the resources and print them
    for resource in resources:
        print(resource)

# Example usage:
if __name__ == '__main__':
    import string  # You can replace this with any module you are interested in.
    
    # Call the function with the string module (or any module/package)
    resources_scanner(string)
