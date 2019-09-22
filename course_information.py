# Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should let the user enter a course number,
# and then it should display the course’s room number, instructor, and meeting time.

import time

course_dict = {'CS101': {'Room': '3004', 'Instructor': 'Haynes', 'Meeting time': '8:00am'},
               'CS102': {'Room': '4501', 'Instructor': 'Alvarado', 'Meeting time': '9:00am'},
               'CS103': {'Room': '6755', 'Instructor': 'Rich', 'Meeting time': '10:00am'},
               'NT110': {'Room': '1244', 'Instructor': 'Burke', 'Meeting time': '11:00am'},
               'CM241': {'Room': '1411', 'Instructor': 'Lee', 'Meeting time': '1:00pm'},
               }


def course_info(course):
    """
    A function to gather and display
    course information stored in dict.
    """
    if course.upper() == course.upper():
        print(f'Course information for {course.upper()} is: ')
        for key, value in course_dict[f'{course.upper()}'].items():
            print(f'\t{key} : {value}')


print('''
Hello! What course information can I provide to you?
Just enter your course number below(type 'quit' to exit).
     ''')

time.sleep(2)

while True:
    user_course = input('\nEnter your course number: ')
    if user_course == 'quit':
        print('Thanks for using this program, goodbye.')
        break
    else:
        try:
            course_info(user_course)
        except KeyError:
            print('\n\tCourse not found, please re-enter your course.\n')
            continue
