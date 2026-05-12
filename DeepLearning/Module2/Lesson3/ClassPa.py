class parrot:
    def sing(self,song):
        song = "la la la la la"
        return song
    def dance(self):
        print("bam thud bam thud bam")
    def __init__(self, name, age):
        self.name = name
        self.age = age

tim = parrot("Timmy", "5")
print(tim.sing("song"))
print(tim.dance())