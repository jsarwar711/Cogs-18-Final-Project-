from chatbot1 import *
def my_test():
    treatment_list = ['Consult a doctor and ask about treatment options', 'Take prescribed medication', 
                  'If feeling depressed, talk to someone', 'Psychiatric therapy', 'Vocational rehabilitation', 
                  'Family therapy', 'Hospitalization', 
                 'Electroconvulsive therapy']   
    
    Medications = {1: 'Name: Seroquel, Price = $11', 2: 'Name: Abilify, Price = $18', 3: 'Name: Zyprexa, Price = $13',
               4: 'Name: Prochlorperazine , Price = $12', 5:'Name: Latuda, Price = $1,219', 
               6:'Name: Geodon, Price = $31', 7:'Name: Invega, Price = $242', 8:'Name: Perphenazine, Price = $23', 
               9:'Name: Molindone, Price = $89'
}
    
assert (treatment_options() in treatment_list)
assert isinstance(treatment_list, list)
assert isinstance(treatment_list[0], str)
assert len(treatment_list) == 8
assert isinstance(Medications, dict)
assert len(Medications) == 9

