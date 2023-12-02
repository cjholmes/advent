
def first_digit(str):
    for i in str:
        try:
            if type(int(i)) == int:
                return i
        
        except TypeError:
            continue
        except ValueError:
            continue
        
def last_digit(str):
    for i in reversed(str):
        try:
            if type(int(i)) == int:
                return i
        
        except TypeError:
            continue
        except ValueError:
            continue

def sum(cali, sum = 0):
    with open(cali) as file:
        for line in file:
            count = 0
            for i in line.strip():
                try:
                    if type(int(i)) == int:
                        count += 1
        
                except ValueError:
                    continue
            if count == 1:
                num = int(first_digit(line))
                sum += (num * 11)
            else:
                first = int(first_digit(line))
                last = int(last_digit(line))
                sum += (first * 10 + last)
            
    return sum

def main():
    answer = sum("calibrations.txt")
    print(answer)
    
main()

