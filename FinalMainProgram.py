#This work done by Group 7
#Romero, John Michael Vincent P., 2021-08078-MN-0, 40%
#Lasala, Julia-Ann Christian R., 2021-08057-MN-0, 20%
#Lettac, Dan Gabriel R., 2021-08058-MN-0, 20%
#Lopez, Gerald V., 2021-08059-MN-0, 20%


#os module for clearing the details
import os
#sys module for exit application
import sys
#time module for sleep function
import time
#datetime module for recording the current time and date.
import datetime
#numpy module for reading csv file
import numpy as np


def startFeature():
    # List For Student Details
    tempList = []
    filtered_List = []

    # List for recording time.
    listForTime = []

    # Level - Student Details 
    listU = []
    listG = []
    # Degree
    listM = []
    listD = []

    # List for recording the maximum and minimum grade per level and degree.
    listMaxGrade = []
    listMinGrade = []
    listMinGradeG = []
    listMaxGradeG = []
    listMaxGradeM = []
    listMinGradeM = []
    listMaxGradeD = []
    listMinGradeD = []

    # Variables that are needed to pass to toher functions.
    degree = ""

    # These variables are needed in statistics and transcript
    overallAverage = ""
    averageTerm1 = ""
    averageTerm2 = ""
    maxGrade = ""
    minGrade = ""
    allCourses = ""

    overallAverageM = ""
    averageTerm1M = ""
    averageTerm2M = ""
    maxGradeM = ""
    minGradeM = ""
    allCoursesM = ""

    overallAverageD = ""
    averageTerm1D = ""
    averageTerm2D = ""
    maxGradeD = ""
    minGradeD = ""
    allCoursesD = ""

    overallAverageG = ""
    averageTerm1G = ""
    averageTerm2G = ""
    maxGradeG = ""
    minGradeG = ""
    allCoursesG = ""

    # Full
    # List for generating all courses in different level and degree
    allCoursesTerm1 = []
    allCoursesTerm2 = []

    allCoursesTerm1M = []
    allCoursesTerm2M = []

    allCoursesTerm1D = []
    allCoursesTerm2D = []

    allCoursesTerm1G = []
    allCoursesTerm2G = []

    # Major
    # List for generating all courses in major for all different level and degree
    allCoursesMajorTerm1 = []
    allCoursesMajorTerm2 = []
    majorAverageTerm1 = ""
    majorAverageTerm2 = ""

    allCoursesMajorTerm1M = []
    allCoursesMajorTerm2M = []
    majorAverageTerm1M = ""
    majorAverageTerm2M = ""

    allCoursesMajorTerm1D = []
    allCoursesMajorTerm2D = []
    majorAverageTerm1D = ""
    majorAverageTerm2D = ""

    allCoursesMajorTerm1G = []
    allCoursesMajorTerm2G = []
    majorAverageTerm1G = ""
    majorAverageTerm2G = ""

    # Minor
    # List for generating all courses in minor for all different level and degree
    allCoursesMinorTerm1 = []
    allCoursesMinorTerm2 = []
    minorAverageTerm1 = ""
    minorAverageTerm2 = ""

    allCoursesMinorTerm1M = []
    allCoursesMinorTerm2M = []
    minorAverageTerm1M = ""
    minorAverageTerm2M = ""

    allCoursesMinorTerm1D = []
    allCoursesMinorTerm2D = []
    minorAverageTerm1D = ""
    minorAverageTerm2D = ""

    allCoursesMinorTerm1G = []
    allCoursesMinorTerm2G = []
    minorAverageTerm1G = ""
    minorAverageTerm2G = ""

    # List for the details in stdID csv file.
    arrTranscript = []

    # List for generating the details from reading the csv file named "studentDetails.csv".
    studentDetails = np.loadtxt("studentDetails.csv", delimiter=",", dtype=str, skiprows=1)

    # MMove the details from the arr to another list.
    for i in studentDetails:
        tempList.append(i)

    # This is where the displaying of text starts. This will inform the users that they entered the program.
    print("\nStudent Transcript Generation System")

    # The program will ask user to input his or her level to show specific details based on the level and degree.
    level = input("Please select Student level (U, G, B): ")

    # Conditions for levels.
    if level == "U":
        degree = "BS"
    if level == "G" or level == "B":
        degree = input("Please select degree (M, D, B0): ")
    if level not in ["U", "G", "B"]:
        print("Invalid Level/Degree. Please try again.")
        startFeature()

    # Input variable for Student ID. This is where the user inputs his or her Student ID.
    studentID = input("Enter your Student ID (Ex. 2324001): ")

    # Condition for Student ID
    if studentID not in [eachSTDID[1] for eachSTDID in tempList]:
        print("\nInvalid Student ID. Please try again.")
        startFeature()

    if studentID in [eachSTDID[1] for eachSTDID in tempList]:
        arrTranscript = np.loadtxt(f'{studentID}.csv', delimiter=",", dtype=str, skiprows=1)

    # Condition for Level. This is where the sorting of specific details starts.
    # The inputted level and degree are the basis of displaying specific details.
    # Level U and G and Degree is not equal to B0.
    if (level == "U" or level == "G") and degree != "B0":
        try:
            # Filter the rows based on student level, degree and student ID
            filtered_List = [row for row in tempList if row[5] == level and row[6] == degree and row[1] == studentID]
            # Transcript
            # To get the specific details for Graduate and Undergraduate Level in transcript csv file, we use list comprehension.
            # U / G
            filtered_ListTranscript = [row for row in arrTranscript if row[0] == level and row[1] == degree]
            filtered_ListTerm1 = [row for row in arrTranscript if row[0] == level and row[1] == degree and row[2] == "Term 1"]
            filtered_ListTerm2 = [row for row in arrTranscript if row[0] == level and row[1] == degree and row[2] == "Term 2"]
            allGrades = [int(eachGrade[7]) for eachGrade in filtered_ListTranscript]
            maxGrade = str(max(allGrades))
            minGrade = str(min(allGrades))
            searchIndexMaxGrade = [maxGrade in eachElem for eachElem in filtered_ListTranscript].index(True)
            searchIndexMinGrade = [minGrade in eachElem for eachElem in filtered_ListTranscript].index(True)
            allCourses = [eachCourse[3] for eachCourse in filtered_ListTranscript]
            for i in filtered_ListTranscript[searchIndexMaxGrade]:
                listMaxGrade.append(i)
            for i in filtered_ListTranscript[searchIndexMinGrade]:
                listMinGrade.append(i)

            # Full Transcript
            # We also use here list comprehension to get the all courses, grades, and average for terms 1 and 2.
            allCoursesTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                            filtered_ListTerm1]
            allCoursesTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                            filtered_ListTerm2]
            allGradesTerm1 = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1]
            allGradesTerm2 = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2]
            averageTerm1 = sum(allGradesTerm1) / len(allGradesTerm1)
            averageTerm2 = sum(allGradesTerm2) / len(allGradesTerm2)
            overallAverage = sum(allGrades) / len(allGrades)

            # Major Transcript
            # Generating the details for major transcript.
            filtered_ListMajorTerm1 = [row for row in arrTranscript if
                                    row[0] == level and row[1] == degree and row[2] == "Term 1" and row[5] == "Major"]
            filtered_ListMajorTerm2 = [row for row in arrTranscript if
                                    row[0] == level and row[1] == degree and row[2] == "Term 2" and row[5] == "Major"]
            allCoursesMajorTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm1]
            allCoursesMajorTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm2]
            allGradesTerm1Major = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1]
            allGradesTerm2Major = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2]
            majorAverageTerm1 = sum(allGradesTerm1Major) / len(allGradesTerm1Major)
            majorAverageTerm2 = sum(allGradesTerm2Major) / len(allGradesTerm2Major)

            # Minor Transcript
            # Generating the details for minor transcript.
            filtered_ListMinorTerm1 = [row for row in arrTranscript if
                                    row[0] == level and row[1] == degree and row[2] == "Term 1" and row[5] == "Minor"]
            filtered_ListMinorTerm2 = [row for row in arrTranscript if
                                    row[0] == level and row[1] == degree and row[2] == "Term 2" and row[5] == "Minor"]
            allCoursesMinorTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm1]
            allCoursesMinorTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm2]
            allGradesTerm1Minor = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1]
            allGradesTerm2Minor = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2]
            minorAverageTerm1 = sum(allGradesTerm1Minor) / len(allGradesTerm1Minor)
            minorAverageTerm2 = sum(allGradesTerm2Minor) / len(allGradesTerm2Minor)

        except ValueError:
            print("\nInvalid Data. Please try again.")
            startFeature()


       
    # Level G and Degree B0.
    if level == "G" and degree == "B0":
        try:
             # Student Details
            filtered_List = [row for row in tempList if
                            row[5] == level and (row[6] == "M" or row[6] == "D") and row[1] == studentID]

            # Transcript
            # Masteral
            filtered_ListM = [row for row in arrTranscript if row[0] == level and row[1] == "M"]
            filtered_ListTerm1M = [row for row in arrTranscript if row[0] == level and row[1] == "M" and row[2] == "Term 1"]
            filtered_ListTerm2M = [row for row in arrTranscript if row[0] == level and row[1] == "M" and row[2] == "Term 2"]
            allGradesM = [int(eachGrade[7]) for eachGrade in filtered_ListM]
            maxGradeM = str(max(allGradesM))
            minGradeM = str(min(allGradesM))
            searchIndexMaxGradeM = [maxGradeM in eachElem for eachElem in filtered_ListM].index(True)
            searchIndexMinGradeM = [minGradeM in eachElem for eachElem in filtered_ListM].index(True)
            allCoursesM = [eachCourse[3] for eachCourse in filtered_ListM]
            for i in filtered_ListM[searchIndexMaxGradeM]:
                listMaxGradeM.append(i)
            for i in filtered_ListM[searchIndexMinGradeM]:
                listMinGradeM.append(i)

            # Full
            allCoursesTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                filtered_ListTerm1M]
            allCoursesTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                filtered_ListTerm2M]
            allGradesTerm1M = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1M]
            allGradesTerm2M = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2M]
            averageTerm1M = sum(allGradesTerm1M) / len(allGradesTerm1M)
            averageTerm2M = sum(allGradesTerm2M) / len(allGradesTerm2M)
            overallAverageM = sum(allGradesM) / len(allGradesM)

            # Major
            filtered_ListMajorTerm1M = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "M" and row[2] == "Term 1" and row[5] == "Major"]
            filtered_ListMajorTerm2M = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "M" and row[2] == "Term 2" and row[5] == "Major"]
            allCoursesMajorTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm1M]
            allCoursesMajorTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm2M]
            allGradesTerm1MajorM = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1M]
            allGradesTerm2MajorM = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2M]
            majorAverageTerm1M = sum(allGradesTerm1MajorM) / len(allGradesTerm1MajorM)
            majorAverageTerm2M = sum(allGradesTerm2MajorM) / len(allGradesTerm2MajorM)

            # Minor
            filtered_ListMinorTerm1M = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "M" and row[2] == "Term 1" and row[5] == "Minor"]
            filtered_ListMinorTerm2M = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "M" and row[2] == "Term 2" and row[5] == "Minor"]
            allCoursesMinorTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm1M]
            allCoursesMinorTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm2M]
            allGradesTerm1MinorM = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1M]
            allGradesTerm2MinorM = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2M]
            minorAverageTerm1M = sum(allGradesTerm1MinorM) / len(allGradesTerm1MinorM)
            minorAverageTerm2M = sum(allGradesTerm2MinorM) / len(allGradesTerm2MinorM)

            # Doctoral
            # Transcript
            filtered_ListD = [row for row in arrTranscript if row[0] == level and row[1] == "D"]
            filtered_ListTerm1D = [row for row in arrTranscript if row[0] == level and row[1] == "D" and row[2] == "Term 1"]
            filtered_ListTerm2D = [row for row in arrTranscript if row[0] == level and row[1] == "D" and row[2] == "Term 2"]
            allGradesD = [int(eachGrade[7]) for eachGrade in filtered_ListD]
            maxGradeD = str(max(allGradesD))
            minGradeD = str(min(allGradesD))
            searchIndexMaxGradeD = [maxGradeD in eachElem for eachElem in filtered_ListD].index(True)
            searchIndexMinGradeD = [minGradeD in eachElem for eachElem in filtered_ListD].index(True)
            allCoursesD = [eachCourse[3] for eachCourse in filtered_ListD]
            for i in filtered_ListD[searchIndexMaxGradeD]:
                listMaxGradeD.append(i)
            for i in filtered_ListD[searchIndexMinGradeD]:
                listMinGradeD.append(i)

            # Full
            allCoursesTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                filtered_ListTerm1D]
            allCoursesTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                filtered_ListTerm2D]
            allGradesTerm1D = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1D]
            allGradesTerm2D = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2D]
            averageTerm1D = sum(allGradesTerm1D) / len(allGradesTerm1D)
            averageTerm2D = sum(allGradesTerm2D) / len(allGradesTerm2D)
            overallAverageD = sum(allGradesD) / len(allGradesD)

            # Major
            filtered_ListMajorTerm1D = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "D" and row[2] == "Term 1" and row[5] == "Major"]
            filtered_ListMajorTerm2D = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "D" and row[2] == "Term 2" and row[5] == "Major"]
            allCoursesMajorTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm1D]
            allCoursesMajorTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMajorTerm2D]
            allGradesTerm1MajorD = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1D]
            allGradesTerm2MajorD = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2D]
            majorAverageTerm1D = sum(allGradesTerm1MajorD) / len(allGradesTerm1MajorD)
            majorAverageTerm2D = sum(allGradesTerm2MajorD) / len(allGradesTerm2MajorD)

            # Minor
            filtered_ListMinorTerm1D = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "D" and row[2] == "Term 1" and row[5] == "Minor"]
            filtered_ListMinorTerm2D = [row for row in arrTranscript if
                                        row[0] == level and row[1] == "D" and row[2] == "Term 2" and row[5] == "Minor"]
            allCoursesMinorTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm1D]
            allCoursesMinorTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm2D]
            allGradesTerm1MinorD = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1D]
            allGradesTerm2MinorD = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2D]
            minorAverageTerm1D = sum(allGradesTerm1MinorD) / len(allGradesTerm1MinorD)
            minorAverageTerm2D = sum(allGradesTerm2MinorD) / len(allGradesTerm2MinorD)
        except ValueError:
            print("\nInvalid data. Please try again.")
            startFeature()
        

    # Level B
    if level == "B":
        try:
            #Student Details
            filtered_List = [row for row in tempList if (row[5] == "U" and row[6] == "BS" and row[1] == studentID) or (
                row[5] == "G" and (row[6] == "M" or row[6] == "D") and row[1] == studentID)]
            
            #Transcript
            #Level U
            filtered_ListTranscript = [row for row in arrTranscript if row[0] == "U"]
            filtered_ListTerm1 = [row for row in arrTranscript if row[0] == "U" and row[2] == "Term 1"]
            filtered_ListTerm2 = [row for row in arrTranscript if row[0] == "U" and row[2] == "Term 2"]
            allGrades = [int(eachGrade[7]) for eachGrade in filtered_ListTranscript]
            maxGrade = str(max(allGrades))
            minGrade = str(min(allGrades))

            searchIndexMaxGrade = [maxGrade in eachElem for eachElem in filtered_ListTranscript].index(True)
            searchIndexMinGrade = [minGrade in eachElem for eachElem in filtered_ListTranscript].index(True)
            allCourses = [eachCourse[3] for eachCourse in filtered_ListTranscript]
            for i in filtered_ListTranscript[searchIndexMaxGrade]:
                listMaxGrade.append(i)
            for i in filtered_ListTranscript[searchIndexMinGrade]:
                listMinGrade.append(i)

            # Full
            allCoursesTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                            filtered_ListTerm1]
            allCoursesTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                            filtered_ListTerm2]
            allGradesTerm1 = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1]
            allGradesTerm2 = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2]
            averageTerm1 = sum(allGradesTerm1) / len(allGradesTerm1)
            averageTerm2 = sum(allGradesTerm2) / len(allGradesTerm2)
            overallAverage = sum(allGrades) / len(allGrades)

            # Major
            filtered_ListMajorTerm1 = [row for row in arrTranscript if
                                    row[0] == "U" and row[2] == "Term 1" and row[5] == "Major"]
            filtered_ListMajorTerm2 = [row for row in arrTranscript if
                                    row[0] == "U" and row[2] == "Term 2" and row[5] == "Major"]
            allCoursesMajorTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm1]
            allCoursesMajorTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm2]
            allGradesTerm1Major = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1]
            allGradesTerm2Major = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2]
            majorAverageTerm1 = sum(allGradesTerm1Major) / len(allGradesTerm1Major)
            majorAverageTerm2 = sum(allGradesTerm2Major) / len(allGradesTerm2Major)

            # Minor
            filtered_ListMinorTerm1 = [row for row in arrTranscript if
                                    row[0] == "U" and row[2] == "Term 1" and row[5] == "Minor"]
            filtered_ListMinorTerm2 = [row for row in arrTranscript if
                                    row[0] == "U" and row[2] == "Term 2" and row[5] == "Minor"]
            allCoursesMinorTerm1 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm1]
            allCoursesMinorTerm2 = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListMinorTerm2]
            allGradesTerm1Minor = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1]
            allGradesTerm2Minor = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2]
            minorAverageTerm1 = sum(allGradesTerm1Minor) / len(allGradesTerm1Minor)
            minorAverageTerm2 = sum(allGradesTerm2Minor) / len(allGradesTerm2Minor)

            # For Masteral  or Doctoral Degree
            if degree == "M" or degree == "D":
                # Graduate Level
                filtered_ListG = [row for row in arrTranscript if row[1] == degree]
                filtered_ListTerm1G = [row for row in arrTranscript if row[1] == degree and row[2] == "Term 1"]
                filtered_ListTerm2G = [row for row in arrTranscript if row[1] == degree and row[2] == "Term 2"]
                allGradesG = [int(eachGrade[7]) for eachGrade in filtered_ListG]
                maxGradeG = str(max(allGradesG))
                minGradeG = str(min(allGradesG))
                searchIndexMaxGradeG = [maxGradeG in eachElem for eachElem in filtered_ListG].index(True)
                searchIndexMinGradeG = [minGradeG in eachElem for eachElem in filtered_ListG].index(True)
                allCoursesG = [eachCourse[3] for eachCourse in filtered_ListG]
                for i in filtered_ListG[searchIndexMaxGradeG]:
                    listMaxGradeG.append(i)
                for i in filtered_ListG[searchIndexMinGradeG]:
                    listMinGradeG.append(i)

                # Full
                allCoursesTerm1G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm1G]
                allCoursesTerm2G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm2G]
                allGradesTerm1G = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1G]
                allGradesTerm2G = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2G]
                averageTerm1G = sum(allGradesTerm1G) / len(allGradesTerm1G)
                averageTerm2G = sum(allGradesTerm2G) / len(allGradesTerm2G)
                overallAverageG = sum(allGradesG) / len(allGradesG)

                # Major
                filtered_ListMajorTerm1G = [row for row in arrTranscript if
                                            row[1] == degree and row[2] == "Term 1" and row[5] == "Major"]
                filtered_ListMajorTerm2G = [row for row in arrTranscript if
                                            row[1] == degree and row[2] == "Term 2" and row[5] == "Major"]
                allCoursesMajorTerm1G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm1G]
                allCoursesMajorTerm2G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm2G]
                allGradesTerm1MajorG = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1G]
                allGradesTerm2MajorG = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2G]
                majorAverageTerm1G = sum(allGradesTerm1MajorG) / len(allGradesTerm1MajorG)
                majorAverageTerm2G = sum(allGradesTerm2MajorG) / len(allGradesTerm2MajorG)

                # Minor
                filtered_ListMinorTerm1G = [row for row in arrTranscript if
                                            row[1] == degree and row[2] == "Term 1" and row[5] == "Minor"]
                filtered_ListMinorTerm2G = [row for row in arrTranscript if
                                            row[1] == degree and row[2] == "Term 2" and row[5] == "Minor"]
                allCoursesMinorTerm1G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm1G]
                allCoursesMinorTerm2G = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm2G]
                allGradesTerm1MinorG = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1G]
                allGradesTerm2MinorG = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2G]
                minorAverageTerm1G = sum(allGradesTerm1MinorG) / len(allGradesTerm1MinorG)
                minorAverageTerm2G = sum(allGradesTerm2MinorG) / len(allGradesTerm2MinorG)

            # For B0 degree under Level B.
            if degree == "B0":
                # Masteral
                filtered_ListM = [row for row in arrTranscript if row[0] == "G" and row[1] == "M"]
                filtered_ListTerm1M = [row for row in arrTranscript if
                                    row[0] == "G" and row[1] == "M" and row[2] == "Term 1"]
                filtered_ListTerm2M = [row for row in arrTranscript if
                                    row[0] == "G" and row[1] == "M" and row[2] == "Term 2"]
                allGradesM = [int(eachGrade[7]) for eachGrade in filtered_ListM]
                maxGradeM = str(max(allGradesM))
                minGradeM = str(min(allGradesM))
                searchIndexMaxGradeM = [maxGradeM in eachElem for eachElem in filtered_ListM].index(True)
                searchIndexMinGradeM = [minGradeM in eachElem for eachElem in filtered_ListM].index(True)
                allCoursesM = [eachCourse[3] for eachCourse in filtered_ListM]
                for i in filtered_ListM[searchIndexMaxGradeM]:
                    listMaxGradeM.append(i)
                for i in filtered_ListM[searchIndexMinGradeM]:
                    listMinGradeM.append(i)

                # Full
                allCoursesTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm1M]
                allCoursesTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm2M]
                allGradesTerm1M = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1M]
                allGradesTerm2M = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2M]
                averageTerm1M = sum(allGradesTerm1M) / len(allGradesTerm1M)
                averageTerm2M = sum(allGradesTerm2M) / len(allGradesTerm2M)
                overallAverageM = sum(allGradesM) / len(allGradesM)

                # Major
                filtered_ListMajorTerm1M = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "M" and row[2] == "Term 1" and row[5] == "Major"]
                filtered_ListMajorTerm2M = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "M" and row[2] == "Term 2" and row[5] == "Major"]
                allCoursesMajorTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm1M]
                allCoursesMajorTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm2M]
                allGradesTerm1MajorM = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1M]
                allGradesTerm2MajorM = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2M]
                majorAverageTerm1M = sum(allGradesTerm1MajorM) / len(allGradesTerm1MajorM)
                majorAverageTerm2M = sum(allGradesTerm2MajorM) / len(allGradesTerm2MajorM)

                # Minor
                filtered_ListMinorTerm1M = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "M" and row[2] == "Term 1" and row[5] == "Minor"]
                filtered_ListMinorTerm2M = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "M" and row[2] == "Term 2" and row[5] == "Minor"]
                allCoursesMinorTerm1M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm1M]
                allCoursesMinorTerm2M = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm2M]
                allGradesTerm1MinorM = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1M]
                allGradesTerm2MinorM = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2M]
                minorAverageTerm1M = sum(allGradesTerm1MinorM) / len(allGradesTerm1MinorM)
                minorAverageTerm2M = sum(allGradesTerm2MinorM) / len(allGradesTerm2MinorM)

                # Doctoral
                filtered_ListD = [row for row in arrTranscript if row[0] == "G" and row[1] == "D"]
                filtered_ListTerm1D = [row for row in arrTranscript if
                                    row[0] == "G" and row[1] == "D" and row[2] == "Term 1"]
                filtered_ListTerm2D = [row for row in arrTranscript if
                                    row[0] == "G" and row[1] == "D" and row[2] == "Term 2"]
                allGradesD = [int(eachGrade[7]) for eachGrade in filtered_ListD]
                maxGradeD = str(max(allGradesD))
                minGradeD = str(min(allGradesD))
                searchIndexMaxGradeD = [maxGradeD in eachElem for eachElem in filtered_ListD].index(True)
                searchIndexMinGradeD = [minGradeD in eachElem for eachElem in filtered_ListD].index(True)
                allCoursesD = [eachCourse[3] for eachCourse in filtered_ListD]
                for i in filtered_ListD[searchIndexMaxGradeD]:
                    listMaxGradeD.append(i)
                for i in filtered_ListD[searchIndexMinGradeD]:
                    listMinGradeD.append(i)

                # Full
                allCoursesTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm1D]
                allCoursesTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                    filtered_ListTerm2D]
                allGradesTerm1D = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm1D]
                allGradesTerm2D = [(int(eachGrade[7])) for eachGrade in filtered_ListTerm2D]
                averageTerm1D = sum(allGradesTerm1D) / len(allGradesTerm1D)
                averageTerm2D = sum(allGradesTerm2D) / len(allGradesTerm2D)
                overallAverageD = sum(allGradesD) / len(allGradesD)

                # Major
                filtered_ListMajorTerm1D = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "D" and row[2] == "Term 1" and row[5] == "Major"]
                filtered_ListMajorTerm2D = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "D" and row[2] == "Term 2" and row[5] == "Major"]
                allCoursesMajorTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm1D]
                allCoursesMajorTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMajorTerm2D]
                allGradesTerm1MajorD = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm1D]
                allGradesTerm2MajorD = [int(eachGrade[7]) for eachGrade in filtered_ListMajorTerm2D]
                majorAverageTerm1D = sum(allGradesTerm1MajorD) / len(allGradesTerm1MajorD)
                majorAverageTerm2D = sum(allGradesTerm2MajorD) / len(allGradesTerm2MajorD)

                # Minor
                filtered_ListMinorTerm1D = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "D" and row[2] == "Term 1" and row[5] == "Minor"]
                filtered_ListMinorTerm2D = [row for row in arrTranscript if
                                            row[0] == "G" and row[1] == "D" and row[2] == "Term 2" and row[5] == "Minor"]
                allCoursesMinorTerm1D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm1D]
                allCoursesMinorTerm2D = [(eachCourse[4], eachCourse[3], eachCourse[6], eachCourse[7]) for eachCourse in
                                        filtered_ListMinorTerm2D]
                allGradesTerm1MinorD = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm1D]
                allGradesTerm2MinorD = [int(eachGrade[7]) for eachGrade in filtered_ListMinorTerm2D]
                minorAverageTerm1D = sum(allGradesTerm1MinorD) / len(allGradesTerm1MinorD)
                minorAverageTerm2D = sum(allGradesTerm2MinorD) / len(allGradesTerm2MinorD)
        except ValueError:
            print("\nInvalid data. Please try again.")
            startFeature()

    # Checking if the inputted level and degree are valid by checking the length or content of the filtered list for Student Details.
    if len(filtered_List) == 0:
        print("No records found for the given input.")
        startFeature()
    # If there are records in the list, it will proceed to the other functions. Sorting Details - Sleep Function - Menu Function.
    else:
        sortingDetails(level, degree, studentID, filtered_List, listU, listG, listM, listD)
        sleepFunctionForMainMenu()
        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD, overallAverage,
                    averageTerm1,
                    averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade, allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)


# This function is responsible for sleep function in the program.
def sleepFunction():
    # We print this to inform the user that the program will automatically redirect to the main menu.
    print("\nRedirecting you to the menu window. . . . .")
    time.sleep(5)        
    os.system('cls' if os.name == 'nt' else 'clear')
    # We use sleep function from time module to delay the flashing of Main Menu.
    time.sleep(5)
    print("Welcome to the menu window")
    
def sleepFunctionForMainMenu():
    # We print this to inform the user that the program will automatically redirect to the main menu.
    print("\nRedirecting you to the menu window. . . . .")
    time.sleep(3)        
    # We use sleep function from time module to delay the flashing of Main Menu
    print("Welcome to the menu window")


# This function is for sorting the details that will be displayed in the detailsFeature Function.
def sortingDetails(level, degree, studentID, filtered_List, listU, listG, listM, listD):
    # If condition for each level.
    # Level U and Degree BS
    if level == "U" and degree == "BS":
        if studentID in (eachElem for eachSublist in filtered_List for eachElem in eachSublist):
            searchDetailIndex = [studentID in eachElem for eachElem in filtered_List].index(True)
            for i in filtered_List[searchDetailIndex]:
                listU.append(i)

            # We print this to inform the user that the studentID is found.
            print("\nYour data has been found!")
            #print(listU)
        else:
            print("\nInvalid Student ID, Level, or Degree. Try again.")
            startFeature()

    # Level G and Degree M or D
    if level == "G" and (degree == "M" or degree == "D"):
        if studentID in (eachElem for eachSublist in filtered_List for eachElem in eachSublist):
            searchDetailIndexMD = [studentID and degree in eachElem for eachElem in filtered_List].index(True)
            for i in filtered_List[searchDetailIndexMD]:
                listG.append(i)
            # We print this to inform the user that the studentID is found.
            print("\nYour data has been found!")
            #print(listG)
        else:
            print("\nInvalid Student ID, Level, or Degree. Try again.")
            startFeature()

    # Level G and Degree B0
    if level == "G" and degree == "B0":
        if studentID in (eachElem for eachSublist in filtered_List for eachElem in eachSublist):
            searchDetailIndexM = [studentID and "M" in eachElem for eachElem in filtered_List].index(True)
            searchDetailIndexD = [studentID and "D" in eachElem for eachElem in filtered_List].index(True)
            for i in filtered_List[searchDetailIndexM]:
                listM.append(i)
            for i in filtered_List[searchDetailIndexD]:
                listD.append(i)
            # We print this to inform the user that the studentID is found.
            print("\nYour data has been found!")
            #print(listM)
            #print(listD)
        else:
            print("\nInvalid Student ID, Level, or Degree. Try again.")
            startFeature()

    # Level B and not Degree B0
    if level == "B" and (degree != "B0"):
        if studentID in (eachElem for eachSublist in filtered_List for eachElem in eachSublist):
            searchDetailIndexU = [studentID and "U" in eachElem for eachElem in filtered_List].index(True)
            searchDetailIndexG = [studentID and degree in eachElem for eachElem in filtered_List].index(True)
            for i in filtered_List[searchDetailIndexU]:
                listU.append(i)
            for i in filtered_List[searchDetailIndexG]:
                listG.append(i)
            # We print this to inform the user that the studentID is found.
            print("Your data has been found!")
            #print(listU)
            #print(listG)

    # Level B and Degree B0
    if level == "B" and (degree == "B0"):
        if studentID in (eachElem for eachSublist in filtered_List for eachElem in eachSublist):
            searchDetailIndexU = [studentID and "U" in eachElem for eachElem in filtered_List].index(True)
            searchDetailIndexM = [studentID and "M" in eachElem for eachElem in filtered_List].index(True)
            searchDetailIndexD = [studentID and "D" in eachElem for eachElem in filtered_List].index(True)

            for i in filtered_List[searchDetailIndexU]:
                listU.append(i)
            for i in filtered_List[searchDetailIndexM]:
                listM.append(i)
            for i in filtered_List[searchDetailIndexD]:
                listD.append(i)
            # We print this to inform the user that the studentID is found.
            print("\nYour data has been found!")
            #print(listU)
            #print(listM)
            #print(listD)


# This is where the other functions can be chosen. Also, this function shows the printing of the Main Menu of the program.
def menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD,
                overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade, allCourses,
                overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                allCoursesM,
                overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                allCoursesD,
                overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                allCoursesG,
                allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G):
                
    # Printing of Main Menu.
    print("\nStudent Transcript Generation System")
    print("=============================================")
    print("1. Student details")
    print("2. Statistics")
    print("3. Transcript based on major courses")
    print("4. Transcript based on minor courses")
    print("5. Full transcript")
    print("6. Previous transcript requests")
    print("7. Select another student")
    print("8. Terminate the system")
    print("=============================================")
    selected = input("Enter Your Feature: ")

    # Condition for each item.
    if selected not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Wrong input. Please try again.")
        startFeature()

    if selected == "1":
        detailsFeatures(level, degree, listU, listG, listM, listD)
        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD, overallAverage,
                    averageTerm1,
                    averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade, allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "2":
        statisticsFeature(level, degree, studentID, overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade,
                          allCourses, listMaxGrade, listMinGrade, overallAverageM, averageTerm1M, averageTerm2M,
                          maxGradeM, minGradeM, listMaxGradeM, listMinGradeM, allCoursesM, overallAverageD,
                          averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD, allCoursesD,
                          overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG,
                          listMinGradeG, allCoursesG)
        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD, overallAverage,
                    averageTerm1,
                    averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade, allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "3":
        majorTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD,
                               allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                               allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                               allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                               allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G)

        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD,
                    overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade,
                    allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "4":
        minorTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD,
                               allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                               allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                               allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                               allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G)

        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD,
                    overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade,
                    allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "5":
        fullTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD,
                              allCoursesTerm1, allCoursesTerm2, averageTerm1, averageTerm2, overallAverage,
                              allCoursesTerm1M, allCoursesTerm2M, averageTerm1M, averageTerm2M, overallAverageM,
                              allCoursesTerm1D, allCoursesTerm2D, averageTerm1D, averageTerm2D, overallAverageD,
                              allCoursesTerm1G, allCoursesTerm2G, averageTerm1G, averageTerm2G, overallAverageG,
                              majorAverageTerm1, majorAverageTerm2, minorAverageTerm1, minorAverageTerm2,
                              majorAverageTerm1M, majorAverageTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                              majorAverageTerm1D, majorAverageTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                              majorAverageTerm1G, majorAverageTerm2G, minorAverageTerm1G, minorAverageTerm2G)

        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD,
                    overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade,
                    allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "6":
        previousRequestFeature(listForTime, studentID)
        menuFeature(level, degree, studentID, listForTime, filtered_List, listU, listG, listM, listD,
                    overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade, listMaxGrade, listMinGrade,
                    allCourses,
                    overallAverageM, averageTerm1M, averageTerm2M, maxGradeM, minGradeM, listMaxGradeM, listMinGradeM,
                    allCoursesM,
                    overallAverageD, averageTerm1D, averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD,
                    allCoursesD,
                    overallAverageG, averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG,
                    allCoursesG,
                    allCoursesMajorTerm1, allCoursesMajorTerm2, majorAverageTerm1, majorAverageTerm2,
                    allCoursesMajorTerm1M, allCoursesMajorTerm2M, majorAverageTerm1M, majorAverageTerm2M,
                    allCoursesMajorTerm1D, allCoursesMajorTerm2D, majorAverageTerm1D, majorAverageTerm2D,
                    allCoursesMajorTerm1G, allCoursesMajorTerm2G, majorAverageTerm1G, majorAverageTerm2G,
                    allCoursesMinorTerm1, allCoursesMinorTerm2, minorAverageTerm1, minorAverageTerm2,
                    allCoursesMinorTerm1M, allCoursesMinorTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                    allCoursesMinorTerm1D, allCoursesMinorTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                    allCoursesMinorTerm1G, allCoursesMinorTerm2G, minorAverageTerm1G, minorAverageTerm2G,
                    allCoursesTerm1, allCoursesTerm2, allCoursesTerm1M, allCoursesTerm2M, allCoursesTerm1D,
                    allCoursesTerm2D, allCoursesTerm1G, allCoursesTerm2G)

    if selected == "7":
        newStudentFeature()

    if selected == "8":
        terminateFeature()
        
        
    sleepFunction()


# Show the details of student based on the inputted Level, Degree, and Student ID.
def detailsFeatures(level, degree, listU, listG, listM, listD):
    if level == "U":
        print("\nStudent Details")
        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print("Name:", name)
        print("ID:", stdID)
        print("Levels:", levels2)
        print("College:", college)
        print("Department:", department)
        print("Number of terms:", terms)

        # Store the details in a file
        with open("{}details.txt".format(stdID), "w") as file:
            file.write("Name: {}\n".format(name))
            file.write("ID: {}\n".format(stdID))
            file.write("Levels: {}\n".format(levels2))
            file.write("College: {}\n".format(college))
            file.write("Department: {}\n".format(department))
            file.write("Number of terms: {}\n".format(terms))

    if level == "G" and (degree == "M" or degree == "D"):
        print("\nStudent Details")
        name = listG[2]
        stdID = listG[1]
        levels2 = listG[5]
        terms = listG[9]
        college = listG[3]
        department = listG[4]

        # Show the details on the screen
        print("Name:", name)
        print("ID:", stdID)
        print("Levels:", levels2)
        print("College:", college)
        print("Department:", department)
        print("Number of terms:", terms)

        # Store the details in a file
        with open("{}details.txt".format(stdID), "w") as file:
            file.write("Name: {}\n".format(name))
            file.write("ID: {}\n".format(stdID))
            file.write("Levels: {}\n".format(levels2))
            file.write("College: {}\n".format(college))
            file.write("Department: {}\n".format(department))
            file.write("Number of terms: {}\n".format(terms))

    if level == "G" and degree == "B0":
        print("\nStudent Details")
        name = listM[2]
        stdID = listM[1]
        levels2 = listM[5]
        degree2 = listM[6] + "/" + "" + listD[6]
        terms = listM[9]
        college = listM[3]
        department = listM[4]

        # Show the details on the screen
        print("Name:", name)
        print("ID:", stdID)
        print("Level(s):", levels2)
        print("Degree(s):", degree2)
        print("College:", college)
        print("Department:", department)
        print("Number of terms:", terms)

        # Store the details in a file
        with open("{}details.txt".format(stdID), "w") as file:
            file.write("Name: {}\n".format(name))
            file.write("ID: {}\n".format(stdID))
            file.write("Level(s): {}\n".format(levels2))
            file.write("Degree(s):{}\n".format(degree2))
            file.write("College: {}\n".format(college))
            file.write("Department: {}\n".format(department))
            file.write("Number of terms: {}\n".format(terms))

    if level == "B" and (degree == "M" or degree == "D"):
        print("\nStudent Details")
        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5] + "/" + listG[5]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print("Name:", name)
        print("ID:", stdID)
        print("Levels:", levels2)
        print("College:", college)
        print("Department:", department)
        print("Number of terms:", terms)

        # Store the details in a file
        with open("{}details.txt".format(stdID), "w") as file:
            file.write("Name: {}\n".format(name))
            file.write("ID: {}\n".format(stdID))
            file.write("Levels: {}\n".format(levels2))
            file.write("College: {}\n".format(college))
            file.write("Department: {}\n".format(department))
            file.write("Number of terms: {}\n".format(terms))

    if level == "B" and (degree == "B0"):
        print("\nStudent Details")
        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5] + "/" + listM[5]
        degree2 = listM[6] + "/" + listD[6]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print("Name:", name)
        print("ID:", stdID)
        print("Level(s):", levels2)
        print("Degree(s):", degree2)
        print("College:", college)
        print("Department:", department)
        print("Number of terms:", terms)

        # Store the details in a file
        with open("{}details.txt".format(stdID), "w") as file:
            file.write("Name: {}\n".format(name))
            file.write("ID: {}\n".format(stdID))
            file.write("Level(s): {}\n".format(levels2))
            file.write("Degree(s): {}\n".format(degree2))
            file.write("College: {}\n".format(college))
            file.write("Department: {}\n".format(department))
            file.write("Number of terms: {}\n".format(terms))


    sleepFunction()



def statisticsFeature(level, degree, studentID, overallAverage, averageTerm1, averageTerm2, maxGrade, minGrade,
                      allCourses, listMaxGrade, listMinGrade, overallAverageM, averageTerm1M, averageTerm2M, maxGradeM,
                      minGradeM, listMaxGradeM, listMinGradeM, allCoursesM, overallAverageD, averageTerm1D,
                      averageTerm2D, maxGradeD, minGradeD, listMaxGradeD, listMinGradeD, allCoursesD, overallAverageG,
                      averageTerm1G, averageTerm2G, maxGradeG, minGradeG, listMaxGradeG, listMinGradeG, allCoursesG):
    if level == "U" and degree == "BS":
        print("\n=============================================")
        print("********     Undergraduate Level     ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverage)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1)}")
        print(f"Term 2:  {round(averageTerm2)}")
        print(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}")

        if len(allCourses) != len(set(allCourses)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        with open("{}statistics.txt".format(studentID), "w") as file:
            file.write("\n=============================================\n")
            file.write("\n=============================================\n")
            file.write("********     Undergraduate Level     ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor)for all terms: {round(overallAverage)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1)}\n")
            file.write(f"Term 2:  {round(averageTerm2)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}\n")

            if len(allCourses) != len(set(allCourses)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

    if level == "G" and (degree == "M" or degree == "D"):
        print("\n=============================================")
        print(f"********      Graduate {degree} Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverage)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1)}")
        print(f"Term 2:  {round(averageTerm2)}")
        print(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}")
        if len(allCourses) != len(set(allCourses)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        with open("{}statistics.txt".format(studentID), "w") as file:
            file.write("\n=============================================\n")
            file.write(f"********      Graduate {degree} Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverage)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1)}\n")
            file.write(f"Term 2:  {round(averageTerm2)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}\n")

            if len(allCourses) != len(set(allCourses)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

    if level == "G" and degree == "B0":
        print("\n=============================================")
        print("********      Graduate M Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverageM)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1M)}")
        print(f"Term 2:  {round(averageTerm2M)}")
        print(f"Maximum grade(s) and in which term(s): {maxGradeM} - {listMaxGradeM[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGradeM} - {listMinGradeM[2]}")

        if len(allCoursesM) != len(set(allCoursesM)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        print("\n=============================================")
        print("********      Graduate D Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverageD)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1D)}")
        print(f"Term 2:  {round(averageTerm2D)}")
        print(f"Maximum grade(s) and in which term(s): {maxGradeD} - {listMaxGradeD[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGradeD} - {listMinGradeD[2]}")

        if len(allCoursesD) != len(set(allCoursesD)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        with open("{}statistics.txt".format(studentID), "w") as file:
            file.write("\n=============================================\n")
            file.write("********      Graduate M Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverageM)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1M)}\n")
            file.write(f"Term 2:  {round(averageTerm2M)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGradeM} - {listMaxGradeM[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGradeM} - {listMinGradeM[2]}\n")

            if len(allCoursesM) != len(set(allCoursesM)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

            file.write("\n=============================================\n")
            file.write("********      Graduate D Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverageD)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1D)}\n")
            file.write(f"Term 2:  {round(averageTerm2D)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGradeD} - {listMaxGradeD[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGradeD} - {listMinGradeD[2]}\n")

            if len(allCoursesD) != len(set(allCoursesD)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

    if level == "B" and (degree == "M" or degree == "D"):
        print("\n=============================================")
        print("********     Undergraduate Level     ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverage)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1)}")
        print(f"Term 2:  {round(averageTerm2)}")
        print(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}")

        if len(allCourses) != len(set(allCourses)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        print("\n=============================================")
        print(f"********      Graduate {degree} Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverageG)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1G)}")
        print(f"Term 2:  {round(averageTerm2G)}")
        print(f"Maximum grade(s) and in which term(s): {maxGradeG} - {listMaxGradeG[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGradeG} - {listMinGradeG[2]}")

        if len(allCoursesG) != len(set(allCoursesG)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        with open("{}statistics.txt".format(studentID), "w") as file:
            file.write("\n=============================================\n")
            file.write("\n=============================================\n")
            file.write("********     Undergraduate Level     ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor)for all terms: {round(overallAverage)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1)}\n")
            file.write(f"Term 2:  {round(averageTerm2)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}\n")

            if len(allCourses) != len(set(allCourses)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

            file.write("\n=============================================\n")
            file.write(f"********      Graduate {degree} Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverageG)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1G)}\n")
            file.write(f"Term 2:  {round(averageTerm2G)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGradeG} - {listMaxGradeG[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGradeG} - {listMinGradeG[2]}\n")

            if len(allCoursesG) != len(set(allCoursesG)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

    if level == "B" and degree == "B0":
        print("\n=============================================")
        print("********     Undergraduate Level     ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverage)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1)}")
        print(f"Term 2:  {round(averageTerm2)}")
        print(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}")

        if len(allCourses) != len(set(allCourses)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        print("\n=============================================")
        print("********      Graduate M Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverageM)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1M)}")
        print(f"Term 2:  {round(averageTerm2M)}")
        print(f"Maximum grade(s) and in which term(s): {maxGradeM} - {listMaxGradeM[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGradeM} - {listMinGradeM[2]}")

        if len(allCoursesM) != len(set(allCoursesM)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        print("\n=============================================")
        print("********      Graduate D Level       ********")
        print("=============================================")
        print(f'Overall average (major and minor) for all terms: {round(overallAverageD)}')
        print("Average (major and minor) of each term: ")
        print(f"Term 1: {round(averageTerm1D)}")
        print(f"Term 2:  {round(averageTerm2D)}")
        print(f"Maximum grade(s) and in which term(s): {maxGradeD} - {listMaxGradeD[2]}")
        print(f"Minimum grade(s) and in which term(s): {minGradeD} - {listMinGradeD[2]}")

        if len(allCoursesD) != len(set(allCoursesD)):
            print("Do you have any repeated course(s): Yes")
        else:
            print("Do you have any repeated course(s): No")

        with open("{}statistics.txt".format(studentID), "w") as file:
            file.write("\n=============================================\n")
            file.write("********     Undergraduate Level     ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor)for all terms: {round(overallAverage)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1)}\n")
            file.write(f"Term 2:  {round(averageTerm2)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGrade} - {listMaxGrade[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGrade} - {listMinGrade[2]}\n")

            if len(allCourses) != len(set(allCourses)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

            file.write("\n=============================================\n")
            file.write("********      Graduate M Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverageM)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1M)}\n")
            file.write(f"Term 2:  {round(averageTerm2M)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGradeM} - {listMaxGradeM[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGradeM} - {listMinGradeM[2]}\n")

            if len(allCoursesM) != len(set(allCoursesM)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")

            file.write("\n=============================================\n")
            file.write("********      Graduate D Level       ********\n")
            file.write("=============================================\n")
            file.write(f'Overall average (major and minor) for all terms: {round(overallAverageD)}\n')
            file.write("Average (major and minor) of each term: \n")
            file.write(f"Term 1: {round(averageTerm1D)}\n")
            file.write(f"Term 2:  {round(averageTerm2D)}\n")
            file.write(f"Maximum grade(s) and in which term(s): {maxGradeD} - {listMaxGradeD[2]}\n")
            file.write(f"Minimum grade(s) and in which term(s): {minGradeD} - {listMinGradeD[2]}\n")

            if len(allCoursesD) != len(set(allCoursesD)):
                file.write("Do you have any repeated course(s): Yes\n")
            else:
                file.write("Do you have any repeated course(s): No\n")
                

    sleepFunction()


def majorTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD, allCoursesMajorTerm1,
                           allCoursesMajorTerm2,
                           majorAverageTerm1, majorAverageTerm2, allCoursesMajorTerm1M, allCoursesMajorTerm2M,
                           majorAverageTerm1M, majorAverageTerm2M, allCoursesMajorTerm1D, allCoursesMajorTerm2D,
                           majorAverageTerm1D, majorAverageTerm2D, allCoursesMajorTerm1G, allCoursesMajorTerm2G,
                           majorAverageTerm1G, majorAverageTerm2G):
    
    current_time = datetime.datetime.now()
    majorTime = "Major"
    formatted_date = current_time.strftime("%Y-%m-%d")
    formatted_time = current_time.strftime("%H:%M:%S")

    temp_ListTime = [majorTime, formatted_date, formatted_time]

    listForTime.append(temp_ListTime)

    if (level == "U" or level == "G") and (degree == "BS" or degree == "M" or degree == "D"):

        name = ""
        stdID = ""
        levels2 = ""
        major = ""
        minor = ""
        terms = ""
        college = ""
        department = ""

        if level == "U" and degree == "BS":
            name = listU[2]
            stdID = listU[1]
            levels2 = listU[5]
            major = listU[7]
            minor = listU[8]
            terms = listU[9]
            college = listU[3]
            department = listU[4]

        if level == "G" and (degree == "M" or degree == "G"):
            name = listG[2]
            stdID = listG[1]
            levels2 = listG[5]
            major = listG[7]
            minor = listG[8]
            terms = listG[9]
            college = listG[3]
            department = listG[4]

        # Show the details on the screen
        print(f"\nStudent Details - Level {levels2} {degree}")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1)}' + f'                      Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2)}' + f'                      Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {level}          ***********")
        print("====================================================================")

        # Store the details in a file
        with open("{}MajorTranscript.txt".format(stdID), "w") as file:
            file.write("Student Details\n")
            file.write(f'Name: {name}' + f'        Student ID: {stdID}\n')
            file.write(f'College: {college}' + f'         Department: {department}\n')
            file.write(f'Major: {major}' + f'                   Minor: {minor}\n')
            file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMajorTerm1:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm1)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMajorTerm2:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm2)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********          End of Transcript Level {level}           ***********\n")
            file.write("====================================================================\n")

    if level == "G" and degree == "B0":
        # Access the details from the List that we generate in the startFeature to show the student details.
        # This is for Masteral Degree
        nameM = listM[2]
        stdIDM = listM[1]
        levels2M = listM[5]
        majorM = listM[7]
        minorM = listM[8]
        termsM = listM[9]
        collegeM = listM[3]
        departmentM = listM[4]

        # This is for Doctoral Degree
        nameD = listD[2]
        stdIDD = listD[1]
        levels2D = listD[5]
        majorD = listD[7]
        minorD = listD[8]
        termsD = listD[9]
        collegeD = listD[3]
        departmentD = listD[4]

        # Show the details on the screen
        print("\nStudent Details - Level G (M)")
        print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
        print(f'College: {collegeM}' + f'         Department: {departmentM}')
        print(f'Major: {majorM}' + f'                   Minor: {minorM}')
        print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm1M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1M)}' + f'                      Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm2M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2M)}' + f'                      Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}')
        print("====================================================================")
        print(f"***********        End of Transcript Level {level} - M            ***********")
        print("====================================================================")

        # Show the details on the screen
        # For Graduate Level and Doctorate Degree
        print("\nStudent Details - Level G (D)")
        print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
        print(f'College: {collegeD}' + f'         Department: {departmentD}')
        print(f'Major: {majorD}' + f'                   Minor: {minorD}')
        print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm1D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1D)}' + f'                      Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm2D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2D)}' + f'                      Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}')
        print("====================================================================")
        print("***********        End of Transcript Level {level} - D            ***********")
        print("====================================================================")

        # Store the details in a file
        with open("{}MajorTranscript.txt".format(stdIDM), "w") as file:
            file.write("\nStudent Details - Level G (M)\n")
            file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
            file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
            file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
            file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMajorTerm1M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm1M)}' + f'                     Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMajorTerm2M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm2M)}' + f'                     Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {level} - M         ***********\n")
            file.write("====================================================================\n")

            file.write("\nStudent Details - Level G (D)\n")
            file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
            file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
            file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
            file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm1D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm1D)}' + f'                     Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMajorTerm2D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(majorAverageTerm2D)}' + f'                     Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {level} - D        ***********\n")
            file.write("====================================================================\n")

    if level == "B":
        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5]
        major = listU[7]
        minor = listU[8]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print("\nStudent Details - Level U (BS)")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1)}' + f'                      Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMajorTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2)}' + f'                      Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {levels2}          ***********")
        print("====================================================================")

        if degree == "M" or degree == "D":
            nameG = listG[2]
            stdIDG = listG[1]
            levels2G = listG[5]
            majorG = listG[7]
            minorG = listG[8]
            termsG = listG[9]
            collegeG = listG[3]
            departmentG = listG[4]

            print(f"\nStudent Details - Level G ({degree}) ")
            print(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
            print(f'College: {collegeG}' + f'         Department: {departmentG}')
            print(f'Major: {majorG}' + f'                   Minor: {minorG}')
            print(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm1G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1G)}' + f'                      Overall Average: {round((majorAverageTerm1G + majorAverageTerm2G) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm2G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2G)}' + f'                      Overall Average:{round((majorAverageTerm1G + majorAverageTerm2G) / 2)}')
            print("====================================================================")
            print(f"***********           End of Transcript Level {levels2G}          ***********")
            print("====================================================================")

            with open("{}MajorTranscript.txt".format(stdID), "w") as file:
                file.write("\nStudent Details - Level U (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}\n')
                file.write(f'College: {college}' + f'         Department: {department}\n')
                file.write(f'Major: {major}' + f'                   Minor: {minor}\n')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm1)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm2)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********          End of Transcript Level {levels2}           ***********\n")
                file.write("====================================================================\n")

                file.write(f"\nStudent Details - Level G ({degree}) ")
                file.write(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
                file.write(f'College: {collegeG}' + f'         Department: {departmentG}')
                file.write(f'Major: {majorG}' + f'                   Minor: {minorG}')
                file.write(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade")
                for course in allCoursesMajorTerm1G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1G)}' + f'                      Overall Average: {round((majorAverageTerm1G + majorAverageTerm2G) / 2)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade")
                for course in allCoursesMajorTerm2G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2G)}' + f'                      Overall Average:{round((majorAverageTerm1G + majorAverageTerm2G) / 2)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {levels2G}          ***********")
                file.write("====================================================================")

        if degree == "B0":
            # This is for Masteral Degree
            nameM = listM[2]
            stdIDM = listM[1]
            levels2M = listM[5]
            majorM = listM[7]
            minorM = listM[8]
            termsM = listM[9]
            collegeM = listM[3]
            departmentM = listM[4]

            # This is for Doctoral Degree
            nameD = listD[2]
            stdIDD = listD[1]
            levels2D = listD[5]
            majorD = listD[7]
            minorD = listD[8]
            termsD = listD[9]
            collegeD = listD[3]
            departmentD = listD[4]

            # Show the details on the screen
            print("\nStudent Details - Level G (M)")
            print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
            print(f'College: {collegeM}' + f'         Department: {departmentM}')
            print(f'Major: {majorM}' + f'                   Minor: {minorM}')
            print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm1M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1M)}' + f'                      Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm2M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2M)}' + f'                      Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2M} - M            ***********")
            print("====================================================================")

            # Show the details on the screen
            # For Graduate Level and Doctorate Degree
            print("\nStudent Details - Level G (D)")
            print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
            print(f'College: {collegeD}' + f'         Department: {departmentD}')
            print(f'Major: {majorD}' + f'                   Minor: {minorD}')
            print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm1D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1D)}' + f'                      Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade")
            for course in allCoursesMajorTerm2D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2D)}' + f'                      Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2D} - D            ***********")
            print("====================================================================")

            with open("{}MajorTranscript.txt".format(stdID), "w") as file:
                file.write("\nStudent Details - Level U (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}\n')
                file.write(f'College: {college}' + f'         Department: {department}\n')
                file.write(f'Major: {major}' + f'                   Minor: {minor}\n')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm1)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm2)}' + f'                     Overall Average: {round((majorAverageTerm1 + majorAverageTerm2) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********          End of Transcript Level {levels2}           ***********\n")
                file.write("====================================================================\n")

                file.write("\nStudent Details - Level G (M)\n")
                file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
                file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
                file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
                file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm1M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm1M)}' + f'                     Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm2M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm2M)}' + f'                     Overall Average: {round((majorAverageTerm1M + majorAverageTerm2M) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2M} - M         ***********\n")
                file.write("====================================================================\n")

                file.write("\nStudent Details - Level G (D)\n")
                file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
                file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
                file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
                file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm1D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm1D)}' + f'                     Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMajorTerm2D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(majorAverageTerm2D)}' + f'                     Overall Average: {round((majorAverageTerm1D + majorAverageTerm2D) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2D} - D        ***********\n")
                file.write("====================================================================\n")


    sleepFunction()


def minorTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD, allCoursesMinorTerm1,
                           allCoursesMinorTerm2,
                           minorAverageTerm1, minorAverageTerm2, allCoursesMinorTerm1M, allCoursesMinorTerm2M,
                           minorAverageTerm1M, minorAverageTerm2M, allCoursesMinorTerm1D, allCoursesMinorTerm2D,
                           minorAverageTerm1D, minorAverageTerm2D, allCoursesMinorTerm1G, allCoursesMinorTerm2G,
                           minorAverageTerm1G, minorAverageTerm2G):
    current_time = datetime.datetime.now()
    minorTime = "Minor"
    formatted_date = current_time.strftime("%Y-%m-%d")
    formatted_time = current_time.strftime("%H:%M:%S")

    temp_ListTime = [minorTime, formatted_date, formatted_time]

    listForTime.append(temp_ListTime)

    if (level == "U" or level == "G") and (degree == "BS" or degree == "M" or degree == "D"):

        name = ""
        stdID = ""
        levels2 = ""
        major = ""
        minor = ""
        terms = ""
        college = ""
        department = ""

        if level == "U" and degree == "BS":
            name = listU[2]
            stdID = listU[1]
            levels2 = listU[5]
            major = listU[7]
            minor = listU[8]
            terms = listU[9]
            college = listU[3]
            department = listU[4]

        if level == "G" and (degree == "M" or degree == "G"):
            name = listG[2]
            stdID = listG[1]
            levels2 = listG[5]
            major = listG[7]
            minor = listG[8]
            terms = listG[9]
            college = listG[3]
            department = listG[4]

        # Show the details on the screen
        print(f"\nStudent Details - Level {levels2} ({degree})")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMinorTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Minor Average = {round(minorAverageTerm1)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade")
        for course in allCoursesMinorTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Minor Average = {round(minorAverageTerm2)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {level}          ***********")
        print("====================================================================")

        # Store the details in a file
        with open("{}MinorTranscript.txt".format(stdID), "w") as file:
            file.write(f"Student Details- Level {levels2} {degree}\n")
            file.write(f'Name: {name}' + f'        Student ID: {stdID}\n')
            file.write(f'College: {college}' + f'         Department: {department}\n')
            file.write(f'Major: {major}' + f'                   Minor: {minor}\n')
            file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm1)}' + f'                     Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm2)}' + f'                     Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********          End of Transcript Level {level}           ***********\n")
            file.write("====================================================================\n")

    if level == "G" and degree == "B0":
        # Access the details from the List that we generate in the startFeature to show the student details.
        # This is for Masteral Degree
        nameM = listM[2]
        stdIDM = listM[1]
        levels2M = listM[5]
        majorM = listM[7]
        minorM = listM[8]
        termsM = listM[9]
        collegeM = listM[3]
        departmentM = listM[4]

        # This is for Doctoral Degree
        nameD = listD[2]
        stdIDD = listD[1]
        levels2D = listD[5]
        majorD = listD[7]
        minorD = listD[8]
        termsD = listD[9]
        collegeD = listD[3]
        departmentD = listD[4]

        # Show the details on the screen
        print("\nStudent Details - Level G (M)")
        print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
        print(f'College: {collegeM}' + f'         Department: {departmentM}')
        print(f'Major: {majorM}' + f'                   Minor: {minorM}')
        print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm1M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm1M)}' + f'                      Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm2M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm2M)}' + f'                      Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}')
        print("====================================================================")
        print(f"***********        End of Transcript Level {levels2M} - M            ***********")
        print("====================================================================")

        # Show the details on the screen
        # For Graduate Level and Doctorate Degree
        print("\nStudent Details - Level G (D)")
        print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
        print(f'College: {collegeD}' + f'         Department: {departmentD}')
        print(f'Major: {majorD}' + f'                   Minor: {minorD}')
        print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm1D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm1D)}' + f'                      Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm2D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm2D)}' + f'                      Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}')
        print("====================================================================")
        print(f"***********        End of Transcript Level {levels2D} - D            ***********")
        print("====================================================================")

        # Store the details in a file
        with open("{}MinorTranscript.txt".format(stdIDM), "w") as file:
            file.write("\nStudent Details - Level G (M)\n")
            file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
            file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
            file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
            file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm1M)}' + f'                     Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm2M)}' + f'                     Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {levels2M} - M         ***********\n")
            file.write("====================================================================\n")

            file.write("\nStudent Details - Level G (D)\n")
            file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
            file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
            file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
            file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm1D)}' + f'                     Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'\nMajor Average = {round(minorAverageTerm2D)}' + f'                     Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}\n')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {levels2D} - D        ***********\n")
            file.write("====================================================================\n")

    if level == "B":

        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5]
        major = listU[7]
        minor = listU[8]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print(f"\nStudent Details - Level {levels2} (BS)")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm1)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesMinorTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(minorAverageTerm2)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {levels2}          ***********")
        print("====================================================================")

        if degree == "M" or degree == "D":

            nameG = listG[2]
            stdIDG = listG[1]
            levels2G = listG[5]
            majorG = listG[7]
            minorG = listG[8]
            termsG = listG[9]
            collegeG = listG[3]
            departmentG = listG[4]

            print(f"\nStudent Details - Level G ({degree}) ")
            print(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
            print(f'College: {collegeG}' + f'         Department: {departmentG}')
            print(f'Major: {majorG}' + f'                   Minor: {minorG}')
            print(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm1G)}' + f'                      Overall Average: {round((minorAverageTerm1G + minorAverageTerm2G) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm2G)}' + f'                      Overall Average:{round((minorAverageTerm1G + minorAverageTerm2G) / 2)}')
            print("====================================================================")
            print(f"***********           End of Transcript Level {levels2G}          ***********")
            print("====================================================================")

            with open("{}MinorTranscript.txt".format(stdID), "w") as file:
                file.write(f"\nStudent Details - Level {levels2} (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}')
                file.write(f'College: {college}' + f'         Department: {department}')
                file.write(f'Major: {major}' + f'                   Minor: {minor}')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm1)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm2)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {levels2}          ***********")
                file.write("====================================================================")

                file.write(f"\nStudent Details - Level G ({degree}) ")
                file.write(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
                file.write(f'College: {collegeG}' + f'         Department: {departmentG}')
                file.write(f'Major: {majorG}' + f'                   Minor: {minorG}')
                file.write(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm1G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm1G)}' + f'                      Overall Average: {round((minorAverageTerm1G + minorAverageTerm2G) / 2)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm2G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm2G)}' + f'                      Overall Average:{round((minorAverageTerm1G + minorAverageTerm2G) / 2)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {levels2G}          ***********")
                file.write("====================================================================")

        if degree == "B0":
            # This is for Masteral Degree
            nameM = listM[2]
            stdIDM = listM[1]
            levels2M = listM[5]
            majorM = listM[7]
            minorM = listM[8]
            termsM = listM[9]
            collegeM = listM[3]
            departmentM = listM[4]

            # This is for Doctoral Degree
            nameD = listD[2]
            stdIDD = listD[1]
            levels2D = listD[5]
            majorD = listD[7]
            minorD = listD[8]
            termsD = listD[9]
            collegeD = listD[3]
            departmentD = listD[4]

            # Show the details on the screen
            print("\nStudent Details - Level G (M)")
            print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
            print(f'College: {collegeM}' + f'         Department: {departmentM}')
            print(f'Major: {majorM}' + f'                   Minor: {minorM}')
            print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm1M)}' + f'                      Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm2M)}' + f'                      Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2M} - M            ***********")
            print("====================================================================")

            # Show the details on the screen
            # For Graduate Level and Doctorate Degree
            print("\nStudent Details - Level G (D)")
            print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
            print(f'College: {collegeD}' + f'         Department: {departmentD}')
            print(f'Major: {majorD}' + f'                   Minor: {minorD}')
            print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm1D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm1D)}' + f'                      Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesMinorTerm2D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(minorAverageTerm2D)}' + f'                      Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2D} - D            ***********")
            print("====================================================================")

            with open("{}MinorTranscript.txt".format(stdID), "w") as file:
                file.write(f"\nStudent Details - Level {levels2} (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}')
                file.write(f'College: {college}' + f'         Department: {department}')
                file.write(f'Major: {major}' + f'                   Minor: {minor}')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm1)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(minorAverageTerm2)}' + f'                      Overall Average: {round((minorAverageTerm1 + minorAverageTerm2) / 2)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {levels2}          ***********")
                file.write("====================================================================")

                file.write("\nStudent Details - Level G (M)\n")
                file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
                file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
                file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
                file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm1M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(minorAverageTerm1M)}' + f'                     Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm2M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(minorAverageTerm2M)}' + f'                     Overall Average: {round((minorAverageTerm1M + minorAverageTerm2M) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2M} - M         ***********\n")
                file.write("====================================================================\n")

                file.write("\nStudent Details - Level G (D)\n")
                file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
                file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
                file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
                file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm1D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(minorAverageTerm1D)}' + f'                     Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesMinorTerm2D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'\nMajor Average = {round(minorAverageTerm2D)}' + f'                     Overall Average: {round((minorAverageTerm1D + minorAverageTerm2D) / 2)}\n')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2D} - D        ***********\n")
                file.write("====================================================================\n")
    
    
    sleepFunction()

def fullTranscriptFeature(level, degree, listForTime, listU, listG, listM, listD,
                          allCoursesTerm1, allCoursesTerm2, averageTerm1, averageTerm2, overallAverage,
                          allCoursesTerm1M, allCoursesTerm2M, averageTerm1M, averageTerm2M, overallAverageM,
                          allCoursesTerm1D, allCoursesTerm2D, averageTerm1D, averageTerm2D, overallAverageD,
                          allCoursesTerm1G, allCoursesTerm2G, averageTerm1G, averageTerm2G, overallAverageG,
                          majorAverageTerm1, majorAverageTerm2, minorAverageTerm1, minorAverageTerm2,
                          majorAverageTerm1M, majorAverageTerm2M, minorAverageTerm1M, minorAverageTerm2M,
                          majorAverageTerm1D, majorAverageTerm2D, minorAverageTerm1D, minorAverageTerm2D,
                          majorAverageTerm1G, majorAverageTerm2G, minorAverageTerm1G, minorAverageTerm2G):
    current_time = datetime.datetime.now()
    fullTime = "Full"
    formatted_date = current_time.strftime("%Y-%m-%d")
    formatted_time = current_time.strftime("%H:%M:%S")

    temp_ListTime = [fullTime, formatted_date, formatted_time]

    listForTime.append(temp_ListTime)

    if (level == "U" or level == "G") and (degree == "BS" or degree == "M" or degree == "D"):

        name = ""
        stdID = ""
        levels2 = ""
        major = ""
        minor = ""
        terms = ""
        college = ""
        department = ""

        if level == "U" and degree == "BS":
            name = listU[2]
            stdID = listU[1]
            levels2 = listU[5]
            major = listU[7]
            minor = listU[8]
            terms = listU[9]
            college = listU[3]
            department = listU[4]

        if level == "G" and (degree == "M" or degree == "G"):
            name = listG[2]
            stdID = listG[1]
            levels2 = listG[5]
            major = listG[7]
            minor = listG[8]
            terms = listG[9]
            college = listG[3]
            department = listG[4]

        # Show the details on the screen
        print(f"\nStudent Details - Level {levels2} {degree}")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1)}' + f'                      Minor Average: {round(minorAverageTerm1)}')
        print(
            f'Term Average = {round(averageTerm1)}' + f'                       Overall Average: {round(overallAverage)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2)}' + f'                      Minor Average: {round(minorAverageTerm2)}')
        print(
            f'Term Average = {round(averageTerm2)}' + f'                       Overall Average: {round(overallAverage)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {level}          ***********")
        print("====================================================================")

        with open("{}FullTranscript.txt".format(stdID), "w") as file:
            # Show the details on the screen
            file.write(f"\nStudent Details - Level {levels2} {degree}")
            file.write(f'Name: {name}' + f'        Student ID: {stdID}')
            file.write(f'College: {college}' + f'         Department: {department}')
            file.write(f'Major: {major}' + f'                   Minor: {minor}')
            file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
            file.write("====================================================================")
            file.write("***********                    Term 1                    ***********")
            file.write("====================================================================")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1:
                file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm1)}' + f'                      Minor Average: {round(minorAverageTerm1)}')
            file.write(
                f'Term Average = {round(averageTerm1)}' + f'                       Overall Average: {round(overallAverage)}')
            file.write("====================================================================")
            file.write("***********                    Term 2                    ***********")
            file.write("====================================================================")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2:
                file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm2)}' + f'                      Minor Average: {round(minorAverageTerm2)}')
            file.write(
                f'Term Average = {round(averageTerm2)}' + f'                       Overall Average: {round(overallAverage)}')
            file.write("====================================================================")
            file.write(f"***********           End of Transcript Level {level}          ***********")
            file.write("====================================================================")

    if level == "G" and degree == "B0":
        # Access the details from the List that we generate in the startFeature to show the student details.
        # This is for Masteral Degree
        nameM = listM[2]
        stdIDM = listM[1]
        levels2M = listM[5]
        majorM = listM[7]
        minorM = listM[8]
        termsM = listM[9]
        collegeM = listM[3]
        departmentM = listM[4]

        # This is for Doctoral Degree
        nameD = listD[2]
        stdIDD = listD[1]
        levels2D = listD[5]
        majorD = listD[7]
        minorD = listD[8]
        termsD = listD[9]
        collegeD = listD[3]
        departmentD = listD[4]

        # Show the details on the screen
        print("\nStudent Details - Level G (M)")
        print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
        print(f'College: {collegeM}' + f'         Department: {departmentM}')
        print(f'Major: {majorM}' + f'                   Minor: {minorM}')
        print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm1M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1M)}' + f'                      Minor Average: {round(minorAverageTerm1M)}')
        print(
            f'Term Average = {round(averageTerm1M)}' + f'                       Overall Average: {round(overallAverageM)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm2M:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2M)}' + f'                      Minor Average: {round(minorAverageTerm2M)}')
        print(
            f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
        print("====================================================================")
        print(f"***********        End of Transcript Level {levels2M} - M            ***********")
        print("====================================================================")

        # Show the details on the screen
        # For Graduate Level and Doctorate Degree
        print("\nStudent Details - Level G (D)")
        print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
        print(f'College: {collegeD}' + f'         Department: {departmentD}')
        print(f'Major: {majorD}' + f'                   Minor: {minorD}')
        print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm1D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1D)}' + f'                      Minor Average: {round(minorAverageTerm1D)}')
        print(
            f'Term Average = {round(averageTerm1D)}' + f'                       Overall Average: {round(overallAverageD)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm2D:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2D)}' + f'                      Minor Average: {round(minorAverageTerm2D)}')
        print(
            f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
        print("====================================================================")
        print(f"***********        End of Transcript Level {levels2D} - D            ***********")
        print("====================================================================")

        # Store the details in a file
        with open("{}FullTranscript.txt".format(stdIDM), "w") as file:
            file.write("\nStudent Details - Level G (M)\n")
            file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
            file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
            file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
            file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm1M)}' + f'                      Minor Average: {round(minorAverageTerm1M)}')
            file.write(
                f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2M:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm2M)}' + f'                      Minor Average: {round(minorAverageTerm2M)}')
            file.write(
                f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {levels2M} - M         ***********\n")
            file.write("====================================================================\n")

            file.write("\nStudent Details - Level G (D)\n")
            file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
            file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
            file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
            file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
            file.write("====================================================================\n")
            file.write("***********                    Term 1                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm1D)}' + f'                      Minor Average: {round(minorAverageTerm1D)}')
            file.write(
                f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
            file.write("====================================================================\n")
            file.write("***********                    Term 2                    ***********\n")
            file.write("====================================================================\n")
            file.write("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2D:
                file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
            file.write(
                f'Major Average = {round(majorAverageTerm2D)}' + f'                      Minor Average: {round(minorAverageTerm2D)}')
            file.write(
                f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
            file.write("====================================================================\n")
            file.write(f"***********        End of Transcript Level {levels2D} - D        ***********\n")
            file.write("====================================================================\n")

    if level == "B":
        name = listU[2]
        stdID = listU[1]
        levels2 = listU[5]
        major = listU[7]
        minor = listU[8]
        terms = listU[9]
        college = listU[3]
        department = listU[4]

        # Show the details on the screen
        print(f"\nStudent Details - Level {levels2} (BS)")
        print(f'Name: {name}' + f'        Student ID: {stdID}')
        print(f'College: {college}' + f'         Department: {department}')
        print(f'Major: {major}' + f'                   Minor: {minor}')
        print(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
        print("====================================================================")
        print("***********                    Term 1                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm1:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm1)}' + f'                      Minor Average: {round(minorAverageTerm1)}')
        print(
            f'Term Average = {round(averageTerm1)}' + f'                       Overall Average: {round(overallAverage)}')
        print("====================================================================")
        print("***********                    Term 2                    ***********")
        print("====================================================================")
        print("Course ID          Course Name          Credit Hours          Grade\n")
        for course in allCoursesTerm2:
            print("{:<13} {:<30} {:<18} {:<5}".format(*course))
        print(
            f'Major Average = {round(majorAverageTerm2)}' + f'                      Minor Average: {round(minorAverageTerm2)}')
        print(
            f'Term Average = {round(averageTerm2)}' + f'                       Overall Average: {round(overallAverage)}')
        print("====================================================================")
        print(f"***********           End of Transcript Level {level}          ***********")
        print("====================================================================")

        if degree == "M" or degree == "D":
            nameG = listG[2]
            stdIDG = listG[1]
            levels2G = listG[5]
            majorG = listG[7]
            minorG = listG[8]
            termsG = listG[9]
            collegeG = listG[3]
            departmentG = listG[4]

            # Show the details on the screen
            # For Graduate Level and Doctorate Degree
            print(f"\nStudent Details - Level {levels2G} ({degree})")
            print(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
            print(f'College: {collegeG}' + f'         Department: {departmentG}')
            print(f'Major: {majorG}' + f'                   Minor: {minorG}')
            print(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1G)}' + f'                      Minor Average: {round(minorAverageTerm1G)}')
            print(
                f'Term Average = {round(averageTerm1G)}' + f'                       Overall Average: {round(overallAverageG)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2G:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2G)}' + f'                      Minor Average: {round(minorAverageTerm2G)}')
            print(
                f'Term Average = {round(averageTerm2G)}' + f'                       Overall Average: {round(overallAverageG)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2G} - D            ***********")
            print("====================================================================")

            with open("{}FullTranscript.txt".format(stdID), "w") as file:
                # Show the details on the screen
                file.write(f"\nStudent Details - Level {levels2} (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}')
                file.write(f'College: {college}' + f'         Department: {department}')
                file.write(f'Major: {major}' + f'                   Minor: {minor}')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1)}' + f'                      Minor Average: {round(minorAverageTerm1)}')
                file.write(
                    f'Term Average = {round(averageTerm1)}' + f'                       Overall Average: {round(overallAverage)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2)}' + f'                      Minor Average: {round(minorAverageTerm2)}')
                file.write(
                    f'Term Average = {round(averageTerm2)}' + f'                       Overall Average: {round(overallAverage)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {level}          ***********")
                file.write("====================================================================")

                # For Graduate Level and Doctorate Degree
                file.write(f"\nStudent Details - Level {levels2G} ({degree})")
                file.write(f'Name: {nameG}' + f'        Student ID: {stdIDG}')
                file.write(f'College: {collegeG}' + f'         Department: {departmentG}')
                file.write(f'Major: {majorG}' + f'                   Minor: {minorG}')
                file.write(f'Levels: {levels2G}' + f'                               Number of Terms: {termsG}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm1G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1G)}' + f'                      Minor Average: {round(minorAverageTerm1G)}')
                file.write(
                    f'Term Average = {round(averageTerm1G)}' + f'                       Overall Average: {round(overallAverageG)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm2G:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2G)}' + f'                      Minor Average: {round(minorAverageTerm2G)}')
                file.write(
                    f'Term Average = {round(averageTerm2G)}' + f'                       Overall Average: {round(overallAverageG)}')
                file.write("====================================================================")
                file.write(f"***********        End of Transcript Level {levels2G} - D            ***********")
                file.write("====================================================================")

        if degree == "B0":
            # Access the details from the List that we generate in the startFeature to show the student details.
            # This is for Masteral Degree
            nameM = listM[2]
            stdIDM = listM[1]
            levels2M = listM[5]
            majorM = listM[7]
            minorM = listM[8]
            termsM = listM[9]
            collegeM = listM[3]
            departmentM = listM[4]

            # This is for Doctoral Degree
            nameD = listD[2]
            stdIDD = listD[1]
            levels2D = listD[5]
            majorD = listD[7]
            minorD = listD[8]
            termsD = listD[9]
            collegeD = listD[3]
            departmentD = listD[4]

            # Show the details on the screen
            print("\nStudent Details - Level G (M)")
            print(f'Name: {nameM}' + f'        Student ID: {stdIDM}')
            print(f'College: {collegeM}' + f'         Department: {departmentM}')
            print(f'Major: {majorM}' + f'                   Minor: {minorM}')
            print(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1M)}' + f'                      Minor Average: {round(minorAverageTerm1M)}')
            print(
                f'Term Average = {round(averageTerm1M)}' + f'                       Overall Average: {round(overallAverageM)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2M:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2M)}' + f'                      Minor Average: {round(minorAverageTerm2M)}')
            print(
                f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2M} - M            ***********")
            print("====================================================================")

            # Show the details on the screen
            # For Graduate Level and Doctorate Degree
            print("\nStudent Details - Level G (D)")
            print(f'Name: {nameD}' + f'        Student ID: {stdIDD}')
            print(f'College: {collegeD}' + f'         Department: {departmentD}')
            print(f'Major: {majorD}' + f'                   Minor: {minorD}')
            print(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}')
            print("====================================================================")
            print("***********                    Term 1                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm1D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm1D)}' + f'                      Minor Average: {round(minorAverageTerm1D)}')
            print(
                f'Term Average = {round(averageTerm1D)}' + f'                       Overall Average: {round(overallAverageD)}')
            print("====================================================================")
            print("***********                    Term 2                    ***********")
            print("====================================================================")
            print("Course ID          Course Name          Credit Hours          Grade\n")
            for course in allCoursesTerm2D:
                print("{:<13} {:<30} {:<18} {:<5}".format(*course))
            print(
                f'Major Average = {round(majorAverageTerm2D)}' + f'                      Minor Average: {round(minorAverageTerm2D)}')
            print(
                f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
            print("====================================================================")
            print(f"***********        End of Transcript Level {levels2D} - D            ***********")
            print("====================================================================")

            with open("{}FullTranscript.txt".format(stdID), "w") as file:
                # Show the details on the screen
                file.write(f"\nStudent Details - Level {levels2} (BS)")
                file.write(f'Name: {name}' + f'        Student ID: {stdID}')
                file.write(f'College: {college}' + f'         Department: {department}')
                file.write(f'Major: {major}' + f'                   Minor: {minor}')
                file.write(f'Levels: {levels2}' + f'                               Number of Terms: {terms}')
                file.write("====================================================================")
                file.write("***********                    Term 1                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm1:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1)}' + f'                      Minor Average: {round(minorAverageTerm1)}')
                file.write(
                    f'Term Average = {round(averageTerm1)}' + f'                       Overall Average: {round(overallAverage)}')
                file.write("====================================================================")
                file.write("***********                    Term 2                    ***********")
                file.write("====================================================================")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm2:
                    file.write("{:<13} {:<30} {:<18} {:<5}".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2)}' + f'                      Minor Average: {round(minorAverageTerm2)}')
                file.write(
                    f'Term Average = {round(averageTerm2)}' + f'                       Overall Average: {round(overallAverage)}')
                file.write("====================================================================")
                file.write(f"***********           End of Transcript Level {level}          ***********")
                file.write("====================================================================")

                file.write("\nStudent Details - Level G (M)\n")
                file.write(f'Name: {nameM}' + f'        Student ID: {stdIDM}\n')
                file.write(f'College: {collegeM}' + f'         Department: {departmentM}\n')
                file.write(f'Major: {majorM}' + f'                   Minor: {minorM}\n')
                file.write(f'Levels: {levels2M}' + f'                               Number of Terms: {termsM}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm1M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1M)}' + f'                      Minor Average: {round(minorAverageTerm1M)}')
                file.write(
                    f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm2M:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2M)}' + f'                      Minor Average: {round(minorAverageTerm2M)}')
                file.write(
                    f'Term Average = {round(averageTerm2M)}' + f'                       Overall Average: {round(overallAverageM)}')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2M} - M         ***********\n")
                file.write("====================================================================\n")

                file.write("\nStudent Details - Level G (D)\n")
                file.write(f'Name: {nameD}' + f'        Student ID: {stdIDD}\n')
                file.write(f'College: {collegeD}' + f'         Department: {departmentD}\n')
                file.write(f'Major: {majorD}' + f'                   Minor: {minorD}\n')
                file.write(f'Levels: {levels2D}' + f'                               Number of Terms: {termsD}\n')
                file.write("====================================================================\n")
                file.write("***********                    Term 1                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm1D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm1D)}' + f'                      Minor Average: {round(minorAverageTerm1D)}')
                file.write(
                    f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
                file.write("====================================================================\n")
                file.write("***********                    Term 2                    ***********\n")
                file.write("====================================================================\n")
                file.write("Course ID          Course Name          Credit Hours          Grade\n")
                for course in allCoursesTerm2D:
                    file.write("{:<13} {:<30} {:<18} {:<5}\n".format(*course))
                file.write(
                    f'Major Average = {round(majorAverageTerm2D)}' + f'                      Minor Average: {round(minorAverageTerm2D)}')
                file.write(
                    f'Term Average = {round(averageTerm2D)}' + f'                       Overall Average: {round(overallAverageD)}')
                file.write("====================================================================\n")
                file.write(f"***********        End of Transcript Level {levels2D} - D        ***********\n")
                file.write("====================================================================\n")


    sleepFunction()


def previousRequestFeature(listForTime, studentID):
    listForTimeSorted = [(eachDatetime[0], eachDatetime[1], eachDatetime[2]) for eachDatetime in listForTime]
    #print(listForTimeSorted)
    print("\nRequest               Date               Time")
    print("==============================================")
    for eachDatetime in listForTimeSorted:
        print("{:<18} {:<18} {:<18}".format(*eachDatetime))

    with open("{}PreviousRequests.txt".format(studentID), "w") as file:
        file.write("\nRequest               Date               Time\n")
        file.write("==============================================")
        for eachDatetime in listForTimeSorted:
            file.write("\n{:<18} {:<18} {:<18}\n".format(*eachDatetime))
            
    sleepFunction()


def newStudentFeature():
    print("Redirecting you to the main program.")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    # python = sys.executable
    # os.execl(python, python, *sys.argv
    time.sleep(3)
    print("Welcome to the main program.")
    startFeature()


def terminateFeature():
    sys.exit()


startFeature()
