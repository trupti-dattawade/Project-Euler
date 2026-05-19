'''
If the numbers  1 to 5  are written out in words: one, two, three, four, five, then there are 19 letters used in total.

If all the numbers from one to  (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example,  (three hundred and forty-two) contains  letters and  (one hundred and fifteen) contains 23 letters and 115 contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
def number_to_words(n):
    """Convert a number into words (British usage)."""
    if n == 1000:
        return "one thousand"
    
    words = ""
    
    if n >= 100:
        words += number_to_words(n // 100) + " hundred"
        n %= 100
        if n > 0:
            words += " and "
    
    if n >= 20:
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        words += tens[n // 10]
        n %= 10
        if n > 0:
            words += "-"
    
    if n > 0:
        units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                 "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"]
        words += units[n]
    
    return words

if __name__ == "__main__":
    total_letters = sum(len(number_to_words(i).replace(" ", "").replace("-", "")) for i in range(1, 1001))
    print(total_letters)

# Output: 21124