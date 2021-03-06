"""
Python Programming For the Absolute Beginner, 3rd Edition
filename: critter_caretaker_v3.py
created on: 03 Jul, 2017
@author: Neil_Crerar

Chapter 8, Challenge 3
Create a 'back door' in the Critter Caretaker program that shows the exact 
values of the objects attributes.  Accomplish this by printing the object when
a secret selection, not listed in the menu, is entered as the users choice. 
(Hint: add the special method __Str__()to the Critter class.)
"""

class Critter(object):
    """
    Create a virtual pet you can feed and play with, but watch out, if it gets
    too bored or hungry it will get mad!
    """    
    
    def __init__(self, name, hunger=0, boredom=0):
        """
        :param name: name assigned to the new critter object
        :param hunger: initial hunger value assigned to critter
        :param boredom: initial boredom value assigned to critter
        """ 
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    

    # Newly added method for Challenge 3    
    def __str__(self):
        """
        :returns: current details for the critter object
        """
        crit_details = "Critter Details\n"
        crit_details += "Name: " + self.name + "\n"
        crit_details += "Hunger: " + str(self.hunger) + "\n"
        crit_details += "Boredom: " + str(self.boredom) + "\n"
        unhappiness = self.hunger + self.boredom
        crit_details += "Unhappiness: " + str(unhappiness) + "\n"
        return crit_details
    
            
    def __pass_time(self):
        """
        Private method to imitate passing of time causing increase in hunger 
        and boredom
        """
        self.hunger += 1
        self.boredom += 1
        
    
    @property
    def mood(self):
        """
        Property that calculates mood of critter based on current hunger and 
        boredom levels
        :returns: the mood calculated for the critter object
        """
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5<= unhappiness <= 10:
            m = "okay"
        elif 11<= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    
    def talk(self):
        """
        Have critter object print name and current mood
        """        
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    
    # Modified to meet challenge 1 criteria
    def eat(self):
        """
        User specified value for how much to feed the critter.  Value entered
        causes a 1:1 drop in hunger level.
        """
        # Try/except for invalid entries
        try:
            food = int(input(
                "How much food do you want to give your critter? (1-3):"))
            if food < 1 or food > 3:
                print("That's not a valid amount to feed your critter!")
            else:   
                print("Brrupp.  Thank you.")
                self.hunger -= food
                if self.hunger < 0:
                    self.hunger = 0
                self.__pass_time()                
        except ValueError:
            print("That was not a valid entry!")

        
    # Modified to meet challenge 1 criteria
    def play(self):
        """
        User specified value for how much to play with the critter.  Value 
        entered causes a 1:1 drop in boredom level.
        """
        # Try/except for invalid entries
        try:
            playtime = int(input("How long do you want to play with your critter? (1-5):"))
            if playtime < 1 or playtime > 5:
                print("That's not a valid amount of time to play with your critter!")
            else:         
                print("Wheee!")
                self.boredom -= playtime
                if self.boredom < 0:
                    self.boredom = 0
                self.__pass_time()
        except ValueError:
            print("That was not a valid entry!")
        
                    
def main():
    """
    Main program menu and control
    """
    crit_name = input("\nWhat do you want to name your critter?: ")
    crit = Critter(crit_name)
    # Game menu an player selection
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
        
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice = input("Choice: ")
        print()
        # Exit program
        if choice == "0":
            print("Good-bye.")
        # Listen to your critter
        elif choice == "1":
            crit.talk()
        # Feed your critter
        elif choice == "2":
            crit.eat()
        # Play with your critter
        elif choice == "3":
            crit.play()
        # Challenge 3 only
        # 'Secret' access to details on the critter
        elif choice == "9":
            print(crit.__str__())    
        # Any other entry
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

                
main()
input("\n\nPress the enter key to exit.")
