############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, first_harvest, code, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.first_harvest = first_harvest
        self.code = code
        self.color = color
        self.is_seedless = is_seedless # may want to have as T/F or boolean?
        self.is_bestseller = is_bestseller # may want to have T/F

    def add_pairing(self, pairing): # melon type behavior - be able to have multiple pairings
        """Add a food pairing to the instance's pairings list."""

        self.pairing.append(pairing) # adding on a new melon! ex) mulk pairs well with mint

    def update_code(self, new_code): # melon behavior - have its reporting code updated
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f"Code updated to {new_code}")


def make_melon_types():
    """Returns a list of current melon types."""

    #Create empty list 
    #Create/add different child classes of all the parent melon with specific attributes
    #Manually add pairing type for each of the child classes
    #Append/add each melon child subclasses to all_melon_types list
    #Return updated list of all_melon_types with all subclasses now included

    all_melon_types = []    

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)   
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types 


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    #Create for loop to iterate through all the melon_types
    #We want to print statement for each melon_type and its pairing together
    #Create another for loop to identify its respective pairing 
    #print the remaining sentence with its pairing type
    #Call the function

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()  

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # create a dictionary of melon type by code
    # create for loop that iterates through melon
    # get melon code
    # return melon type with codes

    melons_by_id = {}
    for melon in melon_types:
        if melon.code not in melons_by_id: # conditional statement for if melon code is not found??
            melons_by_id[melon.code] = melon 

    return melons_by_id


############
# Part 2   # the harvest is here! we need to track each melon that is harvested
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
