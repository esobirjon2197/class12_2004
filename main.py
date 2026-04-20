# 12-m
class Light:
    def __init__(self, state):
        self.state = state

    def status(self):
        if self.state == True:
            print("Chiroq yoniq")
        elif self.state == False:
            print("Chiroq o'chiq")

l1 = Light(True)

l1.status()
