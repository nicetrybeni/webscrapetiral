class User:
        def __init__(self,firstName,lastName,likesCount,friendsName):
                self.firstName = firstName
                self.lastName = lastName
                self.likesCount = likesCount
                self.friendsNames = friendsName
                print("User created : " + self.firstName)

        def introduce(self):
                print("Hi I am " + self.firstName + " " + self.lastName)

        def fullProfile(self):
                print("Full Name: " + self.firstName + " " + self.lastName)
                print("Likes: " + str(self.likesCount))
                for x in self.friendsNames:
                        print(" -" + x)

userOne = User("Joseph", "Benipayo", 30, ["Duqs", "Lloyd"])
userOne.introduce()
userOne.fullProfile()
