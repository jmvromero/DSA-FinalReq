import csv

with open('studentDetails.csv', 'w', newline='') as fileForStudentDetails:
    writer = csv.writer(fileForStudentDetails)
    writer.writerow(['Serial', 'Student ID', 'Name', 'College', 'Department', 'Level', 'Degree', 'Major', 'Minor', 'Terms'])
    writer.writerow(['1','2324001','Julia-Ann Christian Lasala','College of Engineering','COE Department 1','U','BS','COED1MajorCpE1','COED1MinorCpE1','2'])
    writer.writerow(['2','2324001','Julia-Ann Christian Lasala','College of Engineering','COEDepartmentM1','G','M','COEDM1MajorCpE1','COEDM1MinorCpE1','2'])
    writer.writerow(['3','2324001','Julia-Ann Christian Lasala','College of Engineering','COEDepartmentD1','G','D','COEDD1MajorCpE1','COEDD1MinorCpE1','2'])
    writer.writerow(['4','2324021','John Michael Vincent Romero','College of Engineering','COEDepartment1','U','BS','COED1MajorCpE1','COED1MinorCpE1','2'])
    writer.writerow(['5','2324021','John Michael Vincent Romero','College of Engineering','COEDepartmentM1','G','M','COEDM1MajorCpE1','COEDM1MinorCpE1','2'])
    writer.writerow(['6','2324065','Dan Gabriel Lettac','College of Engineering','COEDepartmentM1','G','M','COEDM1MajorCpE1','COEDM1MinorCpE1','2'])
    writer.writerow(['7','2324112','Gerald Lopez','College of Engineering','COEDepartmentM1','U','BS','COED1MajorCpE1','COED1MinorCpE1','2'])
    writer.writerow(['8','2324112','Gerald Lopez','College of Engineering','COEDepartmentD1','G','D','COEDD1MajorCpE1','COEDD1MinorCpE1','2'])

with open('2324001.csv', 'w', newline='') as fileForTranscript:
    writer = csv.writer(fileForTranscript)

    #Undergraduate Level
    writer.writerow(['Level','Degree','Term','Course Name','courseID','courseType','creditHours','Grade'])
    writer.writerow(['U','BS','Term 1','Computer Engineering 1','CMPE1','Major','3','91'])
    writer.writerow(['U','BS','Term 1','Computer Engineering 2','CMPE2','Major','3','96'])
    writer.writerow(['U','BS','Term 1','Communication 1','C1','Minor','1','90'])
    writer.writerow(['U','BS','Term 2','Computer Engineering 3','CMPE3','Major','1','92'])
    writer.writerow(['U','BS','Term 2','Communication 2','C2','Minor','1','93'])
    writer.writerow(['U','BS','Term 2','Communication 3','C3','Minor','1','90'])

    #Graduate Level
    #Masteral
    writer.writerow(['G','M','Term 1','Computer Engineering M1','CMPEM1','Major','4','85'])
    writer.writerow(['G','M','Term 1','Communication M1','CM1','Minor','2','89'])
    writer.writerow(['G','M','Term 2','Computer Engineering M2','CMPEM2','Major','4','87'])
    writer.writerow(['G','M','Term 2','Communication M2','CM2','Minor','2','82'])
    #Doctoral
    writer.writerow(['G','D','Term 1','Computer Engineering D1','CMPED1','Major','4','90'])
    writer.writerow(['G','D','Term 1','Communication D1','CD1','Minor','2','91'])
    writer.writerow(['G','D','Term 2','Computer Engineering D2','CMPED2','Major','4','94'])
    writer.writerow(['G','D','Term 2','Communication D2','CD2','Minor','2','97'])

with open('2324021.csv', 'w', newline='') as fileForTranscript:
    writer = csv.writer(fileForTranscript)

    #Undergraduate Level
    writer.writerow(['Level','Degree','Term','Course Name','courseID','courseType','creditHours','Grade'])
    writer.writerow(['U','BS','Term 1','Computer Engineering 1','CMPE1','Major','3','94'])
    writer.writerow(['U','BS','Term 1','Computer Engineering 2','CMPE2','Major','3','97'])
    writer.writerow(['U','BS','Term 1','Communication 1','C1','Minor','1','95'])
    writer.writerow(['U','BS','Term 2','Computer Engineering 3','CMPE3','Major','1','85'])
    writer.writerow(['U','BS','Term 2','Communication 2','C2','Minor','1','83'])
    writer.writerow(['U','BS','Term 2','Communication 3','C3','Minor','1','80'])

    #Graduate Level
    #Masteral
    writer.writerow(['G','M','Term 1','Computer Engineering M1','CMPEM1','Major','4','90'])
    writer.writerow(['G','M','Term 1','Communication M1','CM1','Minor','2','84'])
    writer.writerow(['G','M','Term 2','Computer Engineering M2','CMPEM2','Major','4','83'])
    writer.writerow(['G','M','Term 2','Communication M2','CM2','Minor','2','82'])

with open('2324065.csv', 'w', newline='') as fileForTranscript:
    writer = csv.writer(fileForTranscript)

    #Graduate Level
    #Masteral
    writer.writerow(['Level','Degree','Term','Course Name','courseID','courseType','creditHours','Grade'])
    writer.writerow(['G','M','Term 1','Computer Engineering M1','CMPEM1','Major','4','81'])
    writer.writerow(['G','M','Term 1','Communication M1','CM1','Minor','2','97'])
    writer.writerow(['G','M','Term 2','Computer Engineering M2','CMPEM2','Major','4','98'])
    writer.writerow(['G','M','Term 2','Communication M2','CM2','Minor','2','92'])


with open('2324112.csv', 'w', newline='') as fileForTranscript:
    writer = csv.writer(fileForTranscript)

    #Graduate Level
    #Masteral
    writer.writerow(['G','M','Term 1','Computer Engineering M1','CMPEM1','Major','4','88'])
    writer.writerow(['G','M','Term 1','Communication M1','CM1','Minor','2','84'])
    writer.writerow(['G','M','Term 2','Computer Engineering M2','CMPEM2','Major','4','86'])
    writer.writerow(['G','M','Term 2','Communication M2','CM2','Minor','2','92'])
    #Doctoral
    writer.writerow(['G','D','Term 1','Computer Engineering D1','CMPED1','Major','4','93'])
    writer.writerow(['G','D','Term 1','Communication D1','CD1','Minor','2','90'])
    writer.writerow(['G','D','Term 2','Computer Engineering D2','CMPED2','Major','4','81'])
    writer.writerow(['G','D','Term 2','Communication D2','CD2','Minor','2','87'])





