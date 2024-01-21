'''
Given the names and grades for each student in a class of N students, store them in 
a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''

def secondLowestGrade(student: list):
    unique_scores = sorted(set(score for name, score in student))
    if len(unique_scores) > 1:
        second_lowest_score = unique_scores[1]
        res = [name for name, score in student if score == second_lowest_score]
    else:
        res = -1
    return sorted(res)

if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    
    print(secondLowestGrade(student))