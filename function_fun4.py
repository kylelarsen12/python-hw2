#maximum of 3 numbers
def max_num(num1, num2, num3):
        return max([num1, num2, num3])

#multiply list elements
def mult_list(list):
        if len(list) == 0:
                return 0
        else:
                value = list[0]
                for number in list[1:]:
                        value = value * number
                return value


#recursive reverse string
def rev_string(word, i = 0):
        #base case
        if i == len(word) - 1:
                return word[0]
        #recursive case
        else:
                return word[-1-i] + rev_string(word, i + 1)


#find if number in range
def num_within(test_num, min, max):
        if test_num >= min and test_num <= max:
                return True
        else:
                return False


