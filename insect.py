class Insect:
    def __init__(self, power, defence, mobility, hp):
        self.power = power
        self.defence = defence
        self.mobility = mobility
        self.hp = hp
        
    def abilities(self):
        print("=== Insect Abilities ===\n")
        print("1. Protect \n")
        print("2. Antennea\n")
        
    
    def protect(self):
        self.defn += 10
        print("Bugs have chitin exoskeleton : +10 defence")
    
    def antennea(self):
        self.mob += 5
        print("Bugs percieve with compound eyes and smell via receptors on the antennae : +5 mobility")
        

class Flies(Insect):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
        
    def abilities(self):
        super().abilities()
        print("=== Fly Abilities ===\n")
        print("3. Flying \n")
        print("4. Acrobatics\n")
        print("5. Diseases\n")
        
    
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
        
    def abilities(self):
        super().abilities()
        print("=== Mosquito Abilities ===\n")
        print("6. Sucking Blood \n")
       
    def sucking_blood(self):
        self.power += 20
        print("Some flies can suck blood! - +10 power")
        
#-----------------------

class Butterflies(Insect):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
        
    def abilities(self):
        super().abilities()
        print("=== Butterfly Abilities ===\n")
        print("3. Metamorphosis \n")
        print("4. Camouflage\n")
        
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
    
    def abilities(self):
        super().abilities()
        print("=== Hymenoptera (Bees&Ants) Abilities ===\n")
        print("3. Sting \n")
        
    
    def sting(self):
        self.power += 20
        print("It can sting! : +20 power")
        
        
class Bees(Hymenoptera):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
        
    def abilities(self):
        print("=== Bee Abilities ===\n")
        print("4. Honey\n")
        print("5. Flying\n")
        
    
    def honey(self): 
        print("Bees make honey : ")
    
    def flying(self):
        self.mobility += 20
        print("Bees can fly : +20 mobility")
    
        
    
class Ants(Hymenoptera):
    def __init__(self, power, defence, mobility, hp):
        super().__init__(power, defence, mobility, hp)
    
    def abilities(self):
        super().abilities()
        print("=== Fly Abilities ===\n")
        print("4. Colony \n")
        
        
    def colony(self):
        self.power *= 100
        print("Ants live in highly organised colonies with milions of colony members : X100 POWER!")
    
    
    
        
        
        
    
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
        print("Hand attacks you! Try not to get squashed")


def main():
    print("Welcome to the fight!!")
    print("Here are todays fighters! : ")
    print("Housefly / Mosquito / Butterfly / Bee / Ant")

    insect_map = {
        "housefly" : Housefly,
        "mosquito" : Mosquitos,
        "butterfly" : Butterflies,
        "bee" : Bees,
        "ant" : Ants
    }  
    user_ins = input("Type your character : ").lower()
    
    if user_ins in insect_map:
        player = insect_map[user_ins](power=10, defence=5, mobility=5, hp=20)
        print(f"You chose {user_ins}!")
        player.abilities()
    else:
        print("Invalid character! Choose from:", list(insect_map.keys()))
           
        
    
if __name__ == "__main__":
    main()