# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
def get_dict(names_location):
    names = open(names_location,"r").read().replace('"','').split(",") #open file and read list of names, remove the quotations as split function adds additional
    names.sort() #sorts list alphebetically
    name_dict = {} #creates dictionary to store names and their numeric values
    alphabet = "abcdefghijklmnopqrstuvwxyz" #create string of alphabet to index from


    for name in names: #itterates through all names in list
        bet_score = 0 #initialises alphabet score for each name
        for let in name:
            bet_score += alphabet.upper().index(let)+1 #adds acore for each letter in name

        name_dict[name] = [names.index(name)+1,bet_score,(names.index(name)+1)*bet_score] #adds key of name to dictionary with value of list with order in sorted list, alphabet score, and the product of the two

    return name_dict

def get_total(name_dict):
    total_score = 0  # initialise total score count
    for key in name_dict.keys():
        total_score += name_dict[key][2] #adds score from each name to
    return total_score
print(get_dict("p022_names.txt"))
print(get_total(get_dict("p022_names.txt")))