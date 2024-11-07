# Write your Package class here
class Package:
    items_limit = 6
    def __init__(self, items):
        self.items = items
        if Package.items_limit < self.items:
            print(f"You need to remove {Package.items_limit - self.items} item to continue.")
        else:
            print(f"There are {self.items} items in the package being shipped out.")

# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'
