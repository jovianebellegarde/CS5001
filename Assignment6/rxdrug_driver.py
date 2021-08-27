'''
CS5001 Fall 2019
HW 6 Programming 1 - RX Driver
Joviane Bellegarde
11/7/19
I was having a lot of trouble with this code. I was not able to get the
drug-drug interactions to work. I have everything up until trying to compare
the drugs that each patient takes and printing out their interactions if
there are any.
'''

from rxdrug import *


def read_file(file_name, mode):
    '''
    function: read_file(file_name, mode)
    parameters: 2 strings, a text file and the mode that is being used
    returns: a nested list from the text file
    '''
    # Going to try to open the file here in this code
    # Initiating an empty list to store the lists of information that is being
    # passed through
    file_list = []

    # Going to try to open the file with the try/except code
    try:

        # Opening the file here in reading mode
        file = open(file_name, mode)

        # Assigning a list of the text from the file
        read_file = file.readlines()

        # This loop strips and splits the file into a list
        for i in read_file:
            stripped_file = i.strip('\n')
            split_file = stripped_file.split('|')
            file_list.append(split_file)
        return file_list
        file.close()
    
    # If there is an error opening the file
    except OSError:
        print('Abort! The file is not opening correctly.')


def main():

    # This code turns the drug file into a drug list
    drug_list = read_file('rxcui_drugs.txt', 'r')

    # Initializing an empty list to put the drug objects in
    drugs = []
    for every_drug in drug_list:

        # Drug object is created here
        drug_object = RxDrug(every_drug[0], every_drug[1])

        # Using the set_description method to add to the drug object
        drug_object.set_description(every_drug[2])

        # Creating a list for the drugs within the drug objects
        drug_interaction = every_drug[3].split(',')

        # Adding the interactions to the drug methods list
        for drug in drug_interaction:
            drug_object.add_interaction(drug)
        drugs.append(drug_object)

    # This code turns the patients file into a list
    patients = read_file('prescriptions.txt', 'r')

    # The patient object is created here
    for every_rx in patients:
        patient_object = Patient(every_rx[0], every_rx[1])

        # The set_prescriptions method is adding the prescriptions to the
        # patient object
        patient_object.set_prescriptions(every_rx[2])

        # The patient drugs is a list within a list with this code
        patient_interactions = every_rx[2].split(',')
        patient = patient_object
        print('Patient Interactions: ', patient_interactions)
        for rxdrug1 in patient_interactions:
            print(rxdrug1, 'rxdrug 1')
            for rxdrug2 in patient_interactions:
                interactions = rxdrug1.prescription[0].check_interactions(rxdrug2.prescription[1])
            print(interactions, 'interactions')
                                                                              
        for interaction in patient_interactions:
        #########    patient_object.(patient_object)
            print('NAME: ', every_rx[0])
            print('INT: ', interaction)
            patient = patient_object
 

    for patient in patients:
        print(patient.prescription[0].check_interactions(patient.prescription[1]))
    

main()
