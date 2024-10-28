"""Making Tea For a Big Party"""

__author__: str = "730752946"


def main_planner (guests: int) -> None:
    """
    A central definition that takes all of the other definition together and 
    makes something that with one input gives us a lot of info. Cost, teabags, and treats.
    """
    print("A Cozy Tea Party for " + str(guests)+ " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(int(treats(people=guests))))
   #I put the int because the example had treats as an int instead of a float
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))))
   #I needed to make tea_count/treat_count the return value of both the treat and tea definitions, so I did it like this.
   #This will mean that the definitions will save the value and then feed it into the definition of cost.


def tea_bags (people: int) -> int:
    """the number of guests at the tea party to figure out how much tea we need."""
    teabags: int = people * 2
    return(teabags)  

def treats (people: int) -> int:
    """This definition is to find how many treats there are depending on how many teas."""
#takes the return value of tea_bags and makes it a varable that can be used to calculate treats as a variable.
    teabags: int = tea_bags(people=people)
    treats: int = teabags * 1.5
    return(treats)

def cost (tea_count: int, treat_count: int) -> float:
    """This definition is to find the cost of both treats and tea combined"""
#takes the variables of how much treats and teas we need and converts it to the cost it will take.
    Teacost = tea_count * 0.5
#The teacost is the amount of tea times 0.5 and treatcost is similar but with 0.75
    Treatcost = treat_count * 0.75
    cost: float = Teacost + Treatcost
    #I added them together so that it would give me the total cost of both treats and teabags
    return(cost)


if __name__== "__main__":
    main_planner(guests=int(input("How many guests are attending your party?")))




 
