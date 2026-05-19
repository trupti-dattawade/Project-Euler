'''
The nth term of the sequence of triangle numbers is given 
by, tn=1/2*n*(n+1) ; so the first ten triangle numbers are:
1,3,6,10,15,21,28,36,45,55,...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is  19+11+25=55 = t_10 . If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import math

def is_triangle_number(n: int) -> bool:
    x = int((math.sqrt(8*n + 1) - 1) / 2)
    return x * (x + 1) // 2 == n


def word_value(word: str) -> int:
    return sum(ord(c) - ord('A') + 1 for c in word)


def count_triangle_words(filename: str) -> int:
    with open(filename) as f:
        words = f.read().replace('"', '').split(',')

    count = 0
    for w in words:
        if is_triangle_number(word_value(w)):
            count += 1

    return count


if __name__ == "__main__":
    print(count_triangle_words("words.txt"))