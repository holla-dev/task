from typing import Type


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name 
        self.age = age 
        self.tracks = tracks
        self.score = score


    def change_name(self,name):
        self.name = name 
        print(name)

    
    def change_age(self,age):
        self.age = int(age)
        print(str(age) + " years old")

    def add_track(self,track):
        self.track = track
        print(track)
        print(self.tracks + [self.track])

    def get_score(self):
        print(float(self.score))



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
