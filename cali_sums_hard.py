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
    pattern = r'(?:one|two|three|four|five|six|seven|eight|nine|\d)'
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
    pattern = r'(?:one|two|three|four|five|six|seven|eight|nine|\d)'
    matches = re.findall(pattern, s, re.IGNORECASE)

    if matches:
        last_match = matches[-1]

        if last_match.isdigit() or last_match.lower() in word_to_number_mapping:
            return word_to_number(last_match.lower())
        else:
            return last_match
    else:
        return None
    
def only_one(str):
    pattern = r'(?:one|two|three|four|five|six|seven|eight|nine|\d)'
    matches = re.findall(pattern, str, re.IGNORECASE)
    if len(matches) == 1:
        return True
    return False

def edgecase(str):
    pattern = r'(?:oneight|twone|threeight|fiveight|sevenine|eightwo|nineight|)'
    bitches = re.findall(pattern,str,re.IGNORECASE)
    case = bitches[0]
    if len(bitches) != 0:
        if case == "oneight":
            return [True,18]
        elif case == "twone":
            return [True,21]
        elif case == "threeight":
            return [True,38]
        elif case == "fiveight":
            return [True,58]
        elif case == "sevenine":
            return [True,79]
        elif case == "eightwo":
            return [True,82]
        elif case == "nineight":
            return [True,98]
        else:
            return [None, None]

def sum(cali, sum = 0):
    with open(cali) as file:
        for line in file:
            line = line.strip()
            edge = edgecase(line)
            if edge[0] == True:
                sum += edge[1]
            elif only_one(line) == True:
                sum += (int(ff_digit(line)) * 11)
            else:
                first = int(ff_digit(line))
                last = int(fl_digit(line))
                sum += (first * 10 + last)
        return sum
    
def main():
    print(sum("calibrations.txt"))

main()


