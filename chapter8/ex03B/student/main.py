# Write your function here

import string 
myStuff = []

class methodPackage():
    def __init__(self, package):
        self.package = package

    def resources_scanner(self, package):
        self.package = package
        print(dir(self.package))

    def print_resources_scanner(self, package):
        self.package = package
        for p in package:
            myStuff.append(p)        
            print (p, myStuff)

"""
myPack = methodPackage('')
myPack.resources_scanner(string)
myPack.print_resources_scanner('')
"""

if __name__ == '__main__':
    import string 
    myPack = methodPackage('')
    myPack.resources_scanner(string)
    myPack.print_resources_scanner('')