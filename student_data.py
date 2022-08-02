import pandas as pd
import numpy as np
import json

user_name = input('Hello! My name is Philip Promise, What is your name?\n')

def get_data():
    print('\nHello {}, Welcome To RESULT LODGE\n'.format(user_name))
    print('*************************************************************************************************\n')
    print('{}, on RESULT LODGE there are three tables. Based on the score for each student, data entry will go into the following tables'.format(user_name))
    print('--Best Student  | score = 70 - 100\n')
    print('--Average Student  | score = 45 - 69\n')
    print('--Dull Student  | score = 0 - 44\n')

    proceed = ['C','c']
    while True:
        proceeds = input('if you understand and you choose to continue press "C" else please exit the program now\n').lower()
        if proceeds in proceed:
            print('Lets enter student details')
            return
        else: 
            print("Incorrect input! Try again..\n")

def input_data():

    
    #Dictionary
    best_student = {}
    average_student = {}
    dull_student = {}
    
    while True:
        x = input("\nHow many number of student details do you want to input?")
        try:
            x = int(x)
        except ValueError:
            print("\nInvalid Input! Please enter an integer number. How many number of student details do you want to input?")
            continue
        
        for i in range(x):
            student_full_name = input("Enter student's fullname: ")
            student_score = int(input("Enter student's score: "))
            if student_score >= 0 and student_score <= 44:
                dull_student[student_full_name] = student_score 
            elif student_score >= 45 and student_score <= 69:
                average_student[student_full_name] = student_score
            elif student_score >= 70 and student_score <= 100:
                best_student[student_full_name] = student_score
            else:
                print("Please choose a score from 0 - 100.")
            print('\nData Upload Successful!')

            BS = pd.DataFrame.from_dict(best_student, orient='index').reset_index()
            AS = pd.DataFrame.from_dict(average_student, orient='index').reset_index()
            DS = pd.DataFrame.from_dict(dull_student,  orient='index').reset_index()

        view_choices = ['BS', 'AS', 'DS']
        while True:
            view_choice = input('If you want to view Best Student data enter "BS" \n, For Average Student data enter "AS" and for Dull Student data enter "DS": ').upper()
            if view_choice == 'BS':
                print('\nThese are the data information for Best Student')
                display(BS.rename(columns= {'index': 'Student Name', 0: 'Score'}))
                break
            elif view_choice == 'AS':
                print('\nThese are the data information for Average Student')
                display(AS.rename(columns= {'index': 'Student Name', 0: 'Score'}))
                break
            elif view_choice == 'DS':
                print('\nThese are the data information for Dull Student')
                display(DS.rename(columns= {'index': 'Student Name', 0: 'Score'}))
                break
            if view_choice != view_choices:
                print('Incorrect input! Please choose "BS" - Best Student, "AS" - Average Student and "DS" - Dull Student ..: \n')
                continue
            else:
                break

def main():
   
        get_data()
        input_data()

result = main()
print(result)