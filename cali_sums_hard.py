import re

word_to_number_mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

def word_to_number(word):
    return word_to_number_mapping.get(word.lower(), word)

def ff_digit(s):
    pattern = r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d+)'
    digits = re.search(pattern, s, re.IGNORECASE)
    if digits:
        series = digits.group(0)
        if series.lower() in word_to_number_mapping:
            return word_to_number(series.lower())
        else:
            return series
    else:
        return None

def fl_digit(s):
    # Match a combination of words and digits
    pattern = r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d+)'
    matches = re.findall(pattern, s, re.IGNORECASE)

    if matches:
        last_match = matches[-1]

        # Check if the last match is a digit or a word, and convert if necessary
        if last_match.isdigit() or last_match.lower() in word_to_number_mapping:
            return word_to_number(last_match.lower())
        else:
            return last_match
    else:
        return None
    
def sum(cali, sum = 0):
    with open(cali) as file:
        for line in file:
            first = ff_digit(line)
            last = fl_digit(line)
    
def main():
    print(fl_digit("one1twonine8"))

main()


