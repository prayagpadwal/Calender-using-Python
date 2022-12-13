# 10 points: reading file using with syntax 
# 50 points: reading/converting scores with exception handling 
# 30 points: calculating number of tests and grades 
# 10 points: writing file using with syntax 

def find_marks(marks):
    final_marks = ''
    end_marks = 0


    for i in marks:
        end_marks += i

    tests = len(marks)
    average = end_marks/tests

    
    if average >= 90:
        final_marks = 'A'

    elif average >= 80:
        final_marks = 'B'

    elif average >= 70:
        final_marks = 'C'

    elif average >= 60:
        final_marks = 'D'

    else:
        final_marks = 'F'

    return final_marks

def convert_int(str):
    try:
        int(str)

        return True

    except ValueError:

        return False

