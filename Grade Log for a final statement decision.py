# -*- coding: utf-8 -*-
"""Yüzük_Kardeşliği_Project_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14KmNcHTmpza8Q6ceymy8qRbIquqRI1ST
"""

import sqlite3 as sql
import numpy as np
import pandas as pd

# Empty value lists
course_names=[]
student_names=[]
student_surnames=[]
student_numbers=[]
student_grades=[]
student_letter_grades=[]
student_statements=[]



# Connect database
grade_database=sql.connect('grade_database.db')

# Create cursor
cursor=grade_database.cursor()

# Create Table
cursor.execute("CREATE TABLE IF NOT EXISTS 'Grade System'('Course' TEXT,'Name' TEXT,'Surname' TEXT,'Student Number' INTEGER,'Grade' INTEGER)")

# Commit comment
grade_database.commit()

print("The database connection is successful, and Grade Table is created!")

# Creating sql table to store data
sql_create_table="CREATE TABLE IF NOT EXISTS 'Grade System'('Course' TEXT,'Name' TEXT,'Surname' TEXT,'Student Number' INTEGER,'Grade' INTEGER)"
cursor.execute(sql_create_table)





# Class for exception in course_grade 
class P1(Exception): 
  pass

# Class for course definition
class course: 
  def __init__(self, course_name):
    while(True):
      try:
        self.course_name = input("State course name: ")
        if self.course_name.isalpha()==True:
          course_names.append(self.course_name)
        if self.course_name.isalpha()==False:
          raise P1
        else:
          break    
      except P1:
        print("You must enter a valid course name! Please, try again...")
  def __str__(self):
    return (self.course_name + ' is selected.')

# Class for student name
class student_name: 
  def __init__(self, name): #Function to enter student name as strings
    while(True):
      try:
        self.name=input("State student's name: ")
        if self.name.isalpha()==True:
          student_names.append(self.name)
        if self.name.isalpha()==False:
            raise P1
        else:
            break
      except P1:
        print("You must enter a valid statement! Please, try again...") 
  def __str__(self):
    return 

# Class for student surname
class student_surname: 
  def __init__(self, surname): #Function to enter student name as strings
    while(True):
      try:
        self.surname=input("State student's surname: ")
        if self.surname.isalpha()==True:
          student_surnames.append(self.surname)
        if self.surname.isalpha()==False:
            raise P1
        else:
            break 
      except P1:
        print("You must enter a valid statement! Please, try again...")
  def __str__(self):
    return      
        
# Class for student number
class student_id: 
  def __init__(self, student_number): #Function to enter student number as integer
    while(True):
      try:        
        self.student_number=input("State student's number: ")
        if self.student_number.isnumeric()==True:
          student_numbers.append(self.student_number)
        if self.student_number.isnumeric()==False:
            raise P1
        else:
            break    
      except P1:
        print("You must enter a valid statement! Please, try again...")   
  def __str__(self):
    return 


# Class for student grade with exceptions
class course_grade: 
  def __init__(self, student_grade):
    while(True):
      try:
        self.student_grade=int(input("Please, enter the grade of student: "))
        if self.student_grade>0 and self.student_grade<=100:
          student_grades.append(self.student_grade)
        if self.student_grade<0 or self.student_grade>100:
          raise P1
        else:
          break
      except P1:
        print("Grade must be between 0-100")
      except:
        print("Grade must be an integer")    
    print("Student grade has been recorded.")





print ("Welcome to the Yüzük Kardeşliği grade system.")

def Menu():
  while True:
    course_selection=course(course_name=" ")
    name_input=student_name(name=" ")
    surname_input=student_surname(surname=" ")
    student_id_input=student_id(student_number=" ")   
    student_grade=course_grade(" ")

    check = input("Do you want to quit or start again? Enter Y to restart or another key to end: ")
    if check.upper() == "Y": #go back to the top
      continue
    else:
      break
        
  # Inserting data into sqlite query 
  sql_list="""
  INSERT INTO 'Grade System' VALUES(?,?,?,?,?)
  """
  merged_list=[[a, b, c, d, e] for a, b, c, d, e in zip(course_names, student_names, student_surnames, student_numbers, student_grades)]
  cursor.executemany(sql_list, merged_list)
  
  print(merged_list)

  # Read sqlite query results into a pandas DataFrame
  df = pd.read_sql_query("SELECT * from 'Grade System'", grade_database)

  # Verify that result of SQL query is stored in the dataframe
  print(df)

 
  # converting grades into letters and deciding final grade statement 
  statement1='Pass' # Final grade statements
  statement2='Fail'

  i=df['Grade'].tolist() 
  for grade in i:
    if grade<=100 and grade>=90:
      print('Final grade is A,', statement1)
      student_letter_grades.append('A')
      student_statements.append(statement1)
    elif grade<=89 and grade>=80:
      print('Final grade is B,', statement1)
      student_letter_grades.append('B')
      student_statements.append(statement1)
    elif grade<=79 and grade>=70:
      print('Final grade is C,', statement1)
      student_letter_grades.append('C')
      student_statements.append(statement1)        
    elif grade<=69 and grade>=60:
      print('Final grade is D,', statement1)
      student_letter_grades.append('D')
      student_statements.append(statement1) 
    elif grade<=59 and grade>=50:
      print('Final grade is E,', statement1)
      student_letter_grades.append('E')
      student_statements.append(statement1) 
    else:
      print('Final grade is F,', statement2)
      student_letter_grades.append('F')
      student_statements.append(statement2)
      
    
  grade_database.close()

  result_data = { 
    "Course": course_names,
    "Name": student_names,
    "Surname": student_surnames,
    "Student Number":student_numbers,
    "Grade":student_grades,
    "Final Grade":student_letter_grades,
    "Statement":student_statements
    }

  
  result = pd.DataFrame(result_data)
  print(result)


  result.to_excel('Project1.xlsx', sheet_name='sheet1', index = False)





Menu()
print ("All data is reported and documented in the Grade System Table! Many thanks for your collaboration!")