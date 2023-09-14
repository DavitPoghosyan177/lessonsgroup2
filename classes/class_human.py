class Human:
    def __init__(self, name, surname , age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __repr__(self):
        return  self.name +',' + self.surname + ', ' + str(self.age)

human = [
      Human("Kamo" ,  "Ayrumyan" , 27),
      Human("Hovhannes" , "Ter-Hovhannisyan" , 12),
      Human("Bagrad" , "Baxalbashyan" , 46),
      Human("Nahapet" , "Vxkryan" , 22),
      Human("Hmayak", "Petrosyan", 42),
      Human("Narek", "Ispiryan" ,33),
      Human("Pargev", "Berberyan", 59),
      Human("Natali", "Sahakyan", 21),
      Human("Perj", "Proshyan", 24),
      Human("Max", "Avdalyan", 7),
      Human("Gexecik", "Bdoyan", 49),
      Human("Hayrapet", "Partamyan", 64),
      Human("Barsex", "Mutafyan", 64)

]
human.sort(key=lambda a: a.age)
print(human)
