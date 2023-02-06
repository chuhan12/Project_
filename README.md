"# hospital-project" 
"# Project_" 
####  This is our code for "Project Classes" 
####  Created by Austin Hilles / Chuhan Wang / Joel Olvera
####  Class 209E - Object Oriented Programming
#### Updated December 12th 2022

#### The code below is incorporated to help the user view specific text files and ammend them or add to them within the program
#### In this scenario you can view, add or append 4 different categories
#### They are Doctor, Facility, Laboratory and Patient
#### It utilizes everything we've learned from the course so far such as Classes,Functions, Calling Functions, Loops
#### Case statements, variables, printing, formatting, case statements and many other things
#### We import 4 classes into this program then use functions to return data

#### Here we import the 4 class programs to use within this main program

#### The first is the doctor class
from Project_Group_doctors_class_full import Doctors as Doc
#### Followed by the facilities class
from Project_Group_facilities_class_full import Facilities as Fac
#### Thirdly we have the laboratories class
from Project_Group_laboratories_class_full import Laboratories as Lab
#### Finally we have the patients class
from Project_Group_patients_class_full import Patients as Pat 

#### Here we define the main menu which will take the user to the particular menus within
#### These are the doctor, facilities, laboratoeies and patients menu
#### When the user is done with the program as a whole they press 0 at this menu to stop the program

def mainMenu():
    print()
    print("Main Menu")
    print("0 - Close application")
    print("1 - Doctors")
    print("2 - Facilities")
    print("3 - Laboratories")
    print("4 - Patients")

#### Here we define the patients menu, pressing 0 will cause the program to go back to the main menu
#### The user can then exit the program or pick a different menu to edit
#### The first option displays the patient list formatted correctly
#### The Second option allows the user to search for specific patients by ID, if none are found it returns an error statement
#### The third option allows the user to add a Patient to the patient.txt file
#### The fourth option allows the user to edit an already created patient

def patientsMenu():
    print()
    print("Patient Menu")
    print("0 - Return to Main Menu")
    print("1 - Display patient's list")
    print("2 - Search for patient by ID")
    print("3 - Add patient")
    print("4 - Edit patient info")

#### Here we define the doctors menu, pressing 0 will cause the program to go back to the main menu
#### The user can then exit the program or pick a different menu to edit
#### The first option displays the doctor list formatted correctly
#### The Second option allows the user to search for specific doctors by ID, if none are found it returns an error statement
#### The third option allows the user to search for specific doctors by name, if none are found it returns an error statement 
#### The fourth option allows the user to add a doctor to the doctor.txt file
#### The fifth option allows the user to edit an already created patient

def doctorsMenu():
    print()
    print("Doctor's Menu")
    print("0 - Return to Main Menu")
    print("1 - Display Doctor's list")
    print("2 - Search for doctor by ID")
    print("3 - Search for doctor by name")
    print("4 - Add doctor")
    print("5 - Edit doctor info") 

#### Here we define the facilities menu, pressing 0 will cause the program to go back to the main menu
#### The user can then exit the program or pick a different menu to edit
#### The first option displays the facilities list formatted correctly
#### the Second option allows the user to add a facility to the facilities.txt file

def facilitiesMenu():
    print()
    print("Facility Menu")
    print("0 - Return to Main Menu")
    print("1 - Display Facilities list")
    print("2 - Add Facility")

#### Here we define the laboratories menu, pressing 0 will cause the program to go back to the main menu
#### The user can then exit the program or pick a different menu to edit
#### The first option displays the laboratories list formatted correctly
#### the Second option allows the user to add a laboratory to the laboratories.txt file

def laboratoriesMenu():
    print()
    print("Laboratory Menu")
    print("0 - Return to Main Menu")
    print("1 - Display laboratories list")
    print("2 - Add laboratory")


#### This function adds the patient to a list which is then used by the writePatientToList function to write it to the patients.txt file
def addPatientToList():
    addId = input('Enter Patient ID: ')
    addName = input('Enter Patient name: ')
    addDiagnosis = input('Enter Patient diagnosis: ')
    addGender = input('Enter Patient gender: ')
    addAge = input('Enter Patient age: ')
    addPatient = Pat(addId, addName, addDiagnosis, addGender, addAge)
    return addPatient

#### This function adds the doctor to a list which is then used by the writeDoctorsToList function to write it to the doctor.txt file
def addDoctorToList():
    addDocId = input('Enter Dr ID: ')
    addDocName = input('Enter Dr name: ')
    addSpecialty = input('Enter Dr specialty: ')
    addSchedule = input('Enter Dr schedule: ')
    addquals = input('Enter Dr qualifications: ')
    addRoomNmbr = input('Enter Dr room number: ')
    addDoctor = Doc(addDocId, addDocName, addSpecialty, addSchedule, addquals, addRoomNmbr)
    return addDoctor

#### This function adds the facility to a list which is then used by the writeFacilitiesToList function to write it to the facilities.txt file
def addFacilityToList():
    addFac = input('Enter Facility name: ')
    addFacility = Fac(addFac)
    return addFacility

#### This function adds the lab to a list which is then used by the writeLabToList function to write it to the laboratories.txt file
def addLabToList():
    addLab = input('Enter Lab Name: ')
    addCost = input('Enter Lab Cost: ')
    addLabratory = Lab(addLab, addCost)
    return addLabratory
 
#### This function reads the patient.txt file into a list to be used by the displayPatientsFile function to display it with proper formatting
def readPatientsFile():
    patientsFile = open('patients.txt','r')
    patientList = []
    for aPatient in patientsFile:
        aPatient = aPatient.rstrip()
        aPatient = aPatient.split('_')
        id = (aPatient[0])
        name = (aPatient[1])
        diagnosis =(aPatient[2])
        gender =(aPatient[3])
        age = (aPatient[4])
        patients = Pat(id,name,diagnosis,gender,age)
        print (patients)
        patientList.append(patients)
    return patientList

#### This function reads the laboratories.txt file into a list to be used by the displayLaboratoriesFile function to display it with proper formatting
def readLaboratoriesFile():
    laboratoriesFile = open('laboratories.txt','r')
    labList = []
    for aLab in laboratoriesFile:
        aLab = aLab.rstrip()
        aLab = aLab.split('_')
        labName = (aLab[0])
        labCost = (aLab[1])
        labs = Lab(labName, labCost)
        print (labs)
        labList.append(labs)
    return labList

#### This function reads the facilities.txt file into a list to be used by the displayFaciltyFile function to display it with proper formatting
def readFacilitiesFile():
    facilityFile = open('facilities.txt','r')
    facList = []
    for aFac in facilityFile:
        aFac = aFac.rstrip()
        aFac = aFac.split('_')
        facilities= (aFac[0])
        Facilities = Fac(facilities)
        print (Facilities)
        facList.append(Facilities)
    return facList

#### This function reads the doctor.txt file into a list to be used by the displayDoctorsFile function to display it with proper formatting
def readDoctorsFile():
    doctorsFile = open('doctors.txt','r')
    doctorList = []
    for aDoctor in doctorsFile:
        aDoctor = aDoctor.rstrip()
        aDoctor = aDoctor.split('_')
        id = (aDoctor[0])
        name = (aDoctor[1])
        speciality =(aDoctor[2])
        schedule =(aDoctor[3])
        qualifications = (aDoctor[4])
        roomNum = (aDoctor[5])
        Doctors = Doc(id,name,speciality,schedule,qualifications,roomNum)
        print(Doctors)
        doctorList.append(Doctors)
    return doctorList

#### This function takes user inputs to ammend an existing patient file from the patients.txt file, its then written to the file.
def enterPatientInfo():
    patientid = input('Enter Patient ID: ')
    PatientAppend = []
    patientName = input('Enter new name: ')
    patientDiagnosis = input('Enter new diagnosis: ')
    patientGender = input('Enter new gender: ')
    patientAge = input('Enter new age: ')
    patient_Info = Pat(patientid, patientName, patientDiagnosis, patientGender, patientAge)
    PatientAppend.append(patient_Info)
    return PatientAppend

#### This function takes user inputs to ammend an existing doctor file from the patients.txt file, its then written to the file.
def enterDrInfo():
    Drid = input('Enter Dr ID: ')
    DoctorAppend = []
    DrName = input('Enter new name: ')
    DrSpecialty = input('Enter new specialty in: ')
    DrSchedule = input('Enter new schedule: ')
    DrQualifications = input('Enter new qualifications: ')
    DrRoomNmbr = input ('Enter new room number: ')
    newDocInfo = Doc(Drid, DrName, DrSpecialty, DrSchedule, DrQualifications, DrRoomNmbr)
    DoctorAppend.append(newDocInfo)
    return DoctorAppend

#### This function takes user inputs to ammend an existing laboratory file from the patients.txt file, its then written to the file.
def enterLaboratoryInfo():
    labAppend = []
    labName = input('Enter the lab name: ')
    labCost = input ('Enter the lab cost: ')
    newLabInfo = Lab(labName, labCost)
    labAppend.append(newLabInfo)
    return labAppend
#### This function takes the addPatientsFile and writes it to the patients.txt file.
def writePatientsListToFile():
    with open('patients.txt','a') as addPatientFile:
                addPatientFile.write(str(addPatientToList()))
                return addPatientFile

#### This function takes the addFacilitiesFile and writes it to the facilities.txt file.
def writeFacilitiesListToFile():
    with open('facilities.txt', 'a') as addFacilityFile:
             addFacilityFile.write(str(addFacilityToList()))
             return addFacilityFile

#### This function takes the addLaboratoriesFile and writes it to the laboratories.txt file.
def writeLabsListToFile():
    with open('laboratories.txt', 'a') as addLabsFile:
              addLabsFile.write(str(addLabToList()))
              return addLabsFile
#### This function takes the addDoctorsFile and writes it to the doctors.txt file.
def writeDoctorsListToFile():
    with open('doctors.txt', 'a') as addDocsFile:
              addDocsFile.write(str(addDoctorToList()))
              return addDocsFile

#### This function searches the list of Doctor objects for a specified doctor ID using the doctor ID that the user enters.
def searchDoctorById():
    doctorsFile = open('doctors.txt','r')
    doctorList = []
    ask = input("Enter the doctor ID: ")
    ask[0]
    for aDoctor in doctorsFile:
        aDoctor = aDoctor.rstrip()
        aDoctor = aDoctor.split('_')
        id = (aDoctor[0])
        name = (aDoctor[1])
        speciality =(aDoctor[2])
        schedule =(aDoctor[3])
        qualifications = (aDoctor[4])
        roomNum = (aDoctor[5])
        Doctors = Doc(id,name,speciality,schedule,qualifications,roomNum)
        doctorList
    if ask != doctorsFile:
        print(Doctors)
        return searchDoctorById

def searchPatientById():
    PatientsFile = open('doctors.txt','r')
    patientList = []
    ask = input("Enter the doctor ID: ")
    ask[0]
    for aPatient in PatientsFile:
        aPatient = aPatient.rstrip()
        aPatient = aPatient.split('_')
        id = (aPatient[0])
        name = (aPatient[1])
        diagnosis =(aPatient[2])
        gender =(aPatient[3])
        age = (aPatient[4])
        PatientID = Doc(id,name,diagnosis,gender,age)
        return patientList
    if ask != PatientsFile:
        print(PatientID)
        return searchDoctorById



#### This is the main function which runs the program as a whole using the above functions and classes
#### Continue statements are used to keep the loop working after inputs are returned
#### If the user inputs 0 on the main menu the program will close
#### Case statements are used based off the user input on the menus above (doctor, lab, facility, patient)

def main():
    print ('\nWelcome to the Alberta Rural Patient Care Management System')
    mainMenu()
    option = int(input("Enter option: "))
    while option >=0 and option <=4:
        match option:
            case 0:
                #### Here the program closes and sends a thank you message to the user if 0 is inputted
                print('Thank You for using the Alberta Rural Patient Management System, Good Bye!')
                break
            case 1:
                doctorsMenu()
                doctorOption = int(input('Enter option: '))
                if doctorOption ==1:
                    print()
                    readDoctorsFile()
                elif doctorOption ==2:
                    print()
                    searchDoctorById()
                elif doctorOption ==3:
                    print()
                    pass
                elif doctorOption ==4:
                    print()
                    writeDoctorsListToFile()
                    continue
                elif doctorOption ==5:
                    enterDrInfo()
                elif doctorOption == 0:
                    mainMenu()
                    option = int(input("Enter option: "))

                else:
                    print ('Please enter a value between 1-5 or enter 0 to return to main menu')
                    continue
            
            case 2:
                facilitiesMenu()
                facilityOption = int(input('Enter option: '))
                if facilityOption ==1:
                    print()
                    readFacilitiesFile()
                elif facilityOption ==2:
                    print()
                    writeFacilitiesListToFile()
                    continue
                elif facilityOption ==0:
                    mainMenu()
                    option = int(input("Enter option: "))
                else:
                    print ('Please enter a value between 1-5 or enter 0 to return to main menu')
                    continue
                    
            case 3:
                laboratoriesMenu()
                labOption = int(input('Enter option: '))
                if labOption ==1:
                    print()
                    readLaboratoriesFile()
                elif labOption ==2:
                    print()
                    writeLabsListToFile()
                    continue
                elif labOption ==0:
                    mainMenu()
                    option = int(input("Enter option: "))
                else:
                    print ('Please enter a value between 1-5 or enter 0 to return to main menu')
                    continue
                
            case 4:
                patientsMenu()
                patientOption = int(input('Enter option: '))
                if patientOption ==1:
                    print()
                    readPatientsFile()
                elif patientOption ==2:
                    print()
                    searchPatientById
                elif patientOption ==3:
                    print()
                    writePatientsListToFile()
                    continue
                elif patientOption ==4:
                    print()
                    enterPatientInfo()
                elif patientOption == 0:
                    mainMenu()
                    option = int(input("Enter option: "))
                else:
                    print ('Please enter a value between 1-5 or enter 0 to return to main menu')
                    continue

#### Here we call the main function so the program can run
if __name__ == "__main__":
    main()  
