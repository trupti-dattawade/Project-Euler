'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth   3+15+12+9+14 = 53   , is the th name in the list. So, COLIN would obtain a score of  53 * 938 = 49714  .

What is the total of all the name scores in the file?
'''
def name_score(name: str) -> int:
    """Calculate the alphabetical value of a name."""
    return sum(ord(char) - ord('A') + 1 for char in name)

def total_name_scores(filename: str) -> int:
    """Calculate the total of all name scores in the given file."""
    with open(filename, 'r') as file:
        names = file.read().replace('"', '').split(',')
    
    names.sort()
    
    total_score = 0
    for index, name in enumerate(names):
        total_score += (index + 1) * name_score(name)
    
    return total_score
if __name__ == "__main__":
    result = total_name_scores('names.txt')
    print(result)

#=====================================
#output: 871198282
#=====================================