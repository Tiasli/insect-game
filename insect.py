class Insect:
    def __init__(self, power, defence, mobility, hp):
        self.power = power
        self.defence = defence
        self.mobility = mobility
        self.hp = hp
    
    def protect(self):
        self.defn += 10
        print("Bugs have chitin exoskeleton : +10 defence")
    
    def antennea(self):
        self.mob += 5
        print("Bugs percieve with compound eyes and smell via receptors on the antennae : +5 mobility")
        

class Flies(Insect):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def flying(self):
        self.mobility += 20
        print("Flies can fly (shocking isnt it) with their two wings : +20 mobility")
    
    def acrobatics(self):
        self.mobility += 10
        print("Flies have organs called halteres that act as rotational movement sensors : +10 mobility")
    
    def diseases(self):
        self.power += 10
        print("Flies are vector to diseases : +10 pow")     
        
class Housefly(Flies):
    pass

class Mosquitos(Flies): 
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def sucking(self):
        self.power += 20
        print("Some flies can suck blood! - +10 power")
        
#-----------------------

class Butterflies(Insect):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def metamorphosis(self):
        self.mobility += 20
        print("Butterflies can metamorphose from larvae, into pupae to a winged adult! : +20 mobility")
     
    def camouflage(self):
        self.defence += 10
        print("Butterflies use camouflage to blend in : +10 defence")

#----------------------

class Hymenoptera(Insect):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def sting(self):
        self.power += 20
        print("It can sting! : +20 power")
        
        
class Bees(Hymenoptera):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def honey(self): 
        print("Bees make honey for : ")
        
    
    
    
        
        
        
    
#----------------------
#The enemy: 

class Hand:
    def __init__(self, power, defence, mobility, hp, insect):
        self.power = power
        self.defence = defence
        self.mobility = mobility
        self.insect = insect
        self.hp = hp
    
    def shoo(self, insect):
        print("The hand seems to not be pleased")
        insect.mob -= 5
    
    def hit(self, insect):
        print("Hand attacks you! Try not to get squashed ")
        
        
    
    
    
        




def main():
    print("Welcome to the fight!!")
    print("Here are todays fighters! : ")
    print("Housefly / Mosquito ")
    user_bug = input("Type your character : ")
    print("A wild hand appears from above. It seems like they try to hit you. How dare they!")

        
        
        

    
if __name__ == "__main__":
    main()