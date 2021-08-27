'''
CS5001 Fall 2019
HW 6 Programming 1 - RX Classes
Joviane Bellegarde
11/7/19
'''

class RxDrug:
    '''
    class: this class is for drugs
    parameters: passing in drug information from the main
    returns: information for self
    '''

    def __init__(self, name, rx_ID):
        self.name = name
        self.rx_ID = rx_ID
        self.description  = ''
        self.list_interactions = []

    def add_interaction(self, other_drug):
        # if other_drug is not in our interactions list
        # add other_drug to our interactions list
        if other_drug not in self.list_interactions:
            self.list_interactions.append(other_drug)

    def check_interaction(self, other_drugs):
        # given a list of drugs that possibly interact with us
        # return a list containing the names of the drugs that we
        # actually match with from the list passed in
        new_list = []
        for i in other_drugs:
            if i in self.list_interactions:
                new_list.append(i)
        return new_list

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return(self.name + ' ' + self.rx_ID + ' ' + ' ' + self.description
                + ' ' + str(self.list_interactions))
    

class Patient:
    '''
    class: this class is for patient
    parameters: passing in patient information from the main
    returns: information for self
    '''

    def __init__(self, name, symptom):
        self.name = name
        self.symptom = symptom
        self.prescriptions = []

    def set_prescriptions(self, drug):
        self.prescriptions = drug.split(',')

    def __str__(self):
        return(self.name + ' ' + self.symptom + ' ' + str(self.prescriptions))
