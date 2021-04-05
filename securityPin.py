class securityPin:
    
    
    def pinSet(self):

        oldPin = input("Insert pin: ")
    
    def pinChacker(self, user):
        i = 1
        targetPin = "123"
        while i<4:
            pin = input("Insert pin: ")
            if pin == targetPin:
                print("Correct!")
                break
            else: print("Incorrect! You have {i} tryes from 3.".format(i=i))
            i+=1

