# Write the TabletCamera class here 

# Write the Facial_recognition class here

# Write the BioTablet class here

# Write an instance of the BioTablet class
    
# Call the scan_face method from the instance

# Print the pixels from the instance

class TabletCamera():
    def __init__(self, pixels):
        self.pixels = pixels
        pass


class Facial_recognition():
    def __init__(self):
        pass

    def scan_face(self):
        print("Scanning Face...")


class BioTablet(TabletCamera, Facial_recognition):
    def __init__(self, mp="12MP"):
        self.mp = mp

if __name__ == '__main__':
    myBioTablet = BioTablet()
    myFC = Facial_recognition()
    myFC.scan_face()
    print(myBioTablet.mp)