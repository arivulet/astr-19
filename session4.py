def main():
    class HammerheadShark:
        def __init__(self, armLen, legLen, numEye, tail, fur):
            self.armLen = armLen
            self.legLen = legLen
            self.numEye = numEye
            self.tail = tail
            self.fur = fur

        def printinfo(self):
            print("My favorite animal is the hammerhead shark!")
            print(f"The hammerhead shark has no arms, but its pectoral (frontal swimming) fins are {self.armLen} inches long!")
            print(f"The hammerhead shark has no legs either, but its pelvic (bottom of its belly) fins are {self.legLen} inches long!")
            print(f"The hammerhead shark has {self.numEye} eyes!")
            print(f"True or False? The hammerhead shark has a tail: {self.tail}")
            print(f"True or False? The hammerhead shark has fur: {self.fur}")

    myFav = HammerheadShark(21, 6, 2, True, False)
            
    myFav.printinfo()

main()