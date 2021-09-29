regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.

P = input()
import re
print(len(re.findall(r'(?=(\d)\d\1)',P)) < 2 and bool(re.match(r'^[1-9][0-9]{5}$',P)))

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)