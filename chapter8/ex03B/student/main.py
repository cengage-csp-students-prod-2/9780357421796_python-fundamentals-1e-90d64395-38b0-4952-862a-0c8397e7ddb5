# Write your function here

import string

def resources_scanner(package):
    """
    This function takes a package (module) as input and prints out the names
    of all the resources (attributes, methods, classes) defined in that package.
    
    :param package: The package/module whose resources we want to list.
    """
    resources = dir(package)
    for resource in resources:
        print(resource)

if __name__ == '__main__':
    import math
    resources_scanner(math)
