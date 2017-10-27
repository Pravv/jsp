def zad10():
    students = ['Kasia', 'Basia', 'Marek', 'Darek']
    students.append('Józek')
    students.extend(['Ania', 'Basia'])
    sortedStudents = sorted(students)

    print(sortedStudents[3])
    print(sortedStudents[:2])
    print(sortedStudents[-2:])

zad10()