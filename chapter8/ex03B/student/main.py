# Write your function here

import string 
myStuff = []

class MethodPackage:
    def __init__(self, package):
        self.package = package

    def resources_scanner(self):
        # Print the available resources in the package
        print(dir(self.package))

    def print_resources_scanner(self):
        # Iterate over the string or package and append to myStuff
        for p in self.package:
            myStuff.append(p)
            print(p, myStuff)

# Create an instance of MethodPackage with the string module
myPack = MethodPackage(string)
myPack.resources_scanner()  # Print resources of the string module
myPack.print_resources_scanner()  # Process the string module

if __name__ == '__main__':
    myPack = MethodPackage(string)
    myPack.resources_scanner()  # Print resources of the string module
    myPack.print_resources_scanner()  # Process the string module