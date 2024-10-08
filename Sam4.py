def update_grades(grades):
    updated_grades = [4 if grade == 3 else grade for grade in grades if grade != 2]
    return updated_grades

grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

updated_list_1 = update_grades(grades_list_1)
updated_list_2 = update_grades(grades_list_2)
updated_list_3 = update_grades(grades_list_3)

print("Обновленный список 1:", updated_list_1)
print("Обновленный список 2:", updated_list_2)
print("Обновленный список 3:", updated_list_3)