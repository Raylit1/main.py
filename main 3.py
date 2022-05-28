class Student:
     # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name:str = name #str
        self.age:int = age #int
        self.tracks:list = tracks #list of string 
        self.score:float = score #float

    def change_name(self, name):
        self.name= name
        return str(self.name)

    def change_age(self, age):
        self.age= age
        return int(self.age)

    def add_track(self, track) :
        self.track = track
        return self.track

    def get_score(self):
        return self.score




Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

  
    