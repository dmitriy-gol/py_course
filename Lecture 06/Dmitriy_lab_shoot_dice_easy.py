# v 1.0
import random
comp_result = random.randint(1,4)

# v 1.1
# import random as r
# comp_result = r.randint(1,4)

# v 1.2
# from random import randint
# comp_result = randint(1,4)

# v 1.3
# from random import randint as r
# comp_result = r(1,4)


user_result = int(input("Put 1 2 or 3 to play the dice --> "))

win_or_not = 'are you winning son?' \
    if user_result == comp_result else 'are you lose son?'
print(win_or_not)