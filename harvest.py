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


    #Initialize function & ascribe following attributes - name, melon type, shape, color, the field it came from, & harvester
    #Create a function to determine if item is sellable based on shape rating and color rating
    #Return a list of melon objects



class Melon:
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon instance."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester


    def is_sellable(self): # a melon is able to be sold if both its shape and color ratings are greater than 5, and it didn’t come from field 3, which was found to have poisonous fertilizer planted by a competing melon farm
        """Determine whether this melon can be sold."""

        if self.shape_rating > 5 and self.color_rating >5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types): #  Create a function called make_melons which instantiates the class Melon for each of the above melons. The function should return a list of objects of the class Melon.
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9
    ]

    return melons
    

def get_sellability_report(melons): # Your last task is to write a function, get_sellability_report, which prints out information about each melon that was harvested, and whether or not it is sellable.

# This function should take a list of melon instances as an argument, and return nothing. But, the function will print out who harvested each melon, what field it was harvested from, and whether it is sellable or not. In order to print this report, you’ll access several attributes, and call the is_sellable method on each melon instance.
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        harvested_by = f"Harvested by {melon.harvester}"
        field_num = f"Field #{melon.field}"
        status = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print(f"{harvested_by} from {field_num} {status}")
