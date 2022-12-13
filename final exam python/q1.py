com_1 = [
 'Jonn',
 ['Prayag',['Rahi']],
 ['Tom', 'Cindy', 'Prayag']
]
com_2 = [
 'Rahi',
 ['Jonn', ['Tom', 'Cindy']],
 ['Rambo', ['Cindy', ['Rahi', ['Bob', 'Tyler', 'Prayag']]]],
]

def print_tree(company, condition = 0):
    for num in company:

        if type(num) is not list:
            print('    ' * (condition - 1) + '    ' * (condition > 0) + num)
            
        elif type(num) is list:
            print_tree(num, condition + 1)
            
        else:
            print('    ' * condition + '    ' + num)

print_tree(com_1)
print_tree(com_2)
