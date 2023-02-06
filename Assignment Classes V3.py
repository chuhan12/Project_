from Project_Group_doctors_class_full import Doctors as Doc
from Project_Group_facilities_class_full import Facilities as Fac
from Project_Group_laboratories_class_full import Laboratories as Lab
from Project_Group_patients_class_full import Patients as Pat 

def mainMenu():
    print()
    print("Main Menu")
    print("0 - Close application")
    print("1 - Doctors")
    print("2 - Facilities")
    print("3 - Laboratories")
    print("4 - Patients")

def patientsMenu():
    print()
    print("Patient Menu")
    print("0 - Return to Main Menu")
    print("1 - Display patient's list")
    print("2 - Search for patient by ID")
    print("3 - Add patient")
    print("4 - Edit patient info")

def doctorsMenu():
    print()
    print("Doctor's Menu")
    print("0 - Return to Main Menu")
    print("1 - Display Doctor's list")
    print("2 - Search for doctor by ID")
    print("3 - Search for doctor by name")
    print("4 - Add doctor")
    print("5 - Edit doctor info") 

def facilitiesMenu():
    print()
    print("Facility Menu")
    print("0 - Return to Main Menu")
    print("1 - Display Facilities list")
    print("2 - Add Facility")

def laboratoriesMenu():
    print()
    print("Laboratory Menu")
    print("0 - Return to Main Menu")
    print("1 - Display laboratories list")
    print("2 - Add laboratory")


def addPatientToList():
    addId = input('Enter Patient ID: ')
    addName = input('Enter Patient name: ')
    addDiagnosis = input('Enter Patient diagnosis: ')
    addGender = input('Enter Patient gender: ')
    addAge = input('Enter Patient age: ')
    addPatient = Pat(addId, addName, addDiagnosis, addGender, addAge)
    return addPatient

def addDoctorToList():
    addDocId = input('Enter Dr ID: ')
    addDocName = input('Enter Dr name: ')
    addSpecialty = input('Enter Dr specialty: ')
    addSchedule = input('Enter Dr schedule: ')
    addquals = input('Enter Dr qualifications: ')
    addRoomNmbr = input('Enter Dr room number: ')
    addDoctor = Doc(addDocId, addDocName, addSpecialty, addSchedule, addquals, addRoomNmbr)
    return addDoctor

def addFacilityToList():
    addFac = input('Enter Facility name: ')
    addFacility = Fac(addFac)
    return addFacility

def addLabToList():
    addLab = input('Enter Lab Name: ')
    addCost = input('Enter Lab Cost: ')
    addLabratory = Lab(addLab, addCost)
    return addLabratory
 

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

def enterLaboratoryInfo():
    labAppend = []
    labName = input('Enter the lab name: ')
    labCost = input ('Enter the lab cost: ')
    newLabInfo = Lab(labName, labCost)
    labAppend.append(newLabInfo)
    return labAppend

def writePatientsListToFile():
    with open('patients.txt','a') as addPatientFile:
                addPatientFile.write(str(addPatientToList()))
                return addPatientFile

def writeFacilitiesListToFile():
    with open('facilities.txt', 'a') as addFacilityFile:
             addFacilityFile.write(str(addFacilityToList()))
             return addFacilityFile

def writeLabsListToFile():
    with open('laboratories.txt', 'a') as addLabsFile:
              addLabsFile.write(str(addLabToList()))
              return addLabsFile

def writeDoctorsListToFile():
    with open('doctors.txt', 'a') as addDocsFile:
              addDocsFile.write(str(addDoctorToList()))
              return addDocsFile



def main():
    print ('\nWelcome to the Alberta Rural Patient Care Management System')
    mainMenu()
    option = int(input("Enter option: "))
    while option >=0 and option <=4:
        match option:
            case 0:
                print('Thank You for using the Alberta Rural Patient Management System, Good Bye!')
                break
            case 1:
                doctorsMenu()
                doctorOption = int(input('Enter option: '))
                if doctorOption ==1:
                    readDoctorsFile()
                elif doctorOption ==2:
                    pass
                elif doctorOption ==3:
                    pass
                elif doctorOption ==4:
                    writeDoctorsListToFile()
                    continue
                elif doctorOption ==5:
                    pass
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
                    readFacilitiesFile()
                elif facilityOption ==2:
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
                    readLaboratoriesFile()
                elif labOption ==2:
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
                    readPatientsFile()
                elif patientOption ==2:
                    pass
                elif patientOption ==3:
                    writePatientsListToFile()
                    continue
                elif patientOption ==4:
                    pass
                elif patientOption == 0:
                    mainMenu()
                    option = int(input("Enter option: "))
                else:
                    print ('Please enter a value between 1-5 or enter 0 to return to main menu')
                    continue

if __name__ == "__main__":
    main()  



