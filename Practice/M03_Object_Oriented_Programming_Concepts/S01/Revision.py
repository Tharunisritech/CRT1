# single inheritance
class King:
    def rule(self):
        print("Ruling the kingdom")

class Prince(King):  # Single Inheritance
    pass

p = Prince()
p.rule()  # Inherits rule() from King

# Multilevel Inheritance
class King:
    def rule(self):
        print("Ruling the kingdom")

class Prince(King):  # Single Inheritance
    pass

p = Prince()
p.rule()  # Inherits rule() from King

# Multiple Inheritance
class King:
    def RoyalBloodline(self):
        print("Lineage of Kings")

class Queen:
    def DiplomaticSkills(self):
        print("Master of Diplomacy")

class Princess(King, Queen):  # Multiple Inheritance
    pass

p = Princess()
p.RoyalBloodline()
p.DiplomaticSkills()

# Hierarchical Inheritance
class King:
    def royal_title(self):
        print("Your Royal Highness")

class Prince(King):  # First derived class
    pass

class Princess(King):  # Second derived class
    pass

prince = Prince()
princess = Princess()
prince.royal_title()
princess.royal_title()

#Hybrid Inheritance
class Monarch:
    def crown(self):
        print("Wearing the royal crown")

# Hierarchical Part: Prince and Princess both inherit from Monarch
class Prince(Monarch):
    def sword_skills(self):
        print("Swordsmanship")

class Princess(Monarch):
    def archery_skills(self):
        print("Archery")


class RoyalChild(Prince, Princess):  # Hybrid Inheritance
    pass

c = RoyalChild()
c.crown()           # Inherited from Monarch via Prince/Princess
c.sword_skills()    # Inherited from Prince
c.archery_skills()  # Inherited from Princess
