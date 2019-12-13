from newspaper import Article 
import random 
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np 
import warnings

def lem_normal(text):
    """ This is a function that returns lemmatized lower case words after removing punctuation."""
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
               
def greeting(statement):
    """This is a functions that allows the chatbot to recognize lowercase greetings from the user's greeting to return a random 
    greeting from a list."""          
    for word in statement.split():
        if word.lower() in greeting_inputs:
            return random.choice(greeting_response)
    
def response(user_input):
    # user_input = 'What is schizophrenia'
    user_input = user_input.lower()
    ## Print the user's question 
    # print(user_input)
    
    # Set chatbot's response to an empty string 
    bot_response = ''
    
    # Append the user's input to the statement list created above 
    sent_tokens.append(user_input)
    
    # Print sentence list after the user's input 
    # print(sent_tokens)
    
    # Create a TfidfVectorizer Object 
    Tfid_vec = TfidfVectorizer (tokenizer = lem_normal, stop_words = 'english')
    
    # Convert the text to a matrix of term frequency inverse document frequency features 
    tfidf = Tfid_vec.fit_transform(sent_tokens)
    
    # Print the TFIDF features 
    # print(tfidf)
    
    #Get the similarity score 
    values = cosine_similarity(tfidf[-1], tfidf)
    
    ## print similarity scores 
    ## print(values)
    # Get the index of the most similar text based on the user's input 
    """ Use argsort to sort, and use position [-2] because that is the second most similar response
    because the first is the user's original input, which is position [-1]. """
    index = values.argsort()[0][-2]
    
   #Reduce the number of list of the variable value to 1 list 
    flat = values.flatten()
    #Sort the list in ascending order
    flat.sort()
    
    # Get the most similar score to user input 
    similar_score = flat[-2]
    
    # Print similarity score 
    # print(similar_score)
    
    # If the variable similar_score is 0 that means there is no similarity with the user's input and the text 
    if (similar_score == 0):
        bot_response = bot_response + 'Sorry, but I do not understand. Please ask another question.'
    else: 
            bot_response = bot_response + sent_tokens[index] 

    # Print the chatbot's response 
    # print(bot_response)
        
    # Remove the user's input from the sentence tokens list    
    sent_tokens.remove(user_input)

    return bot_response

def symptom_classification(num):
    """ A very simple function that returns a key-value pair for symptoms classfication. """
    return Symptoms.get(num)
Symptoms = {1:  'Delusions: Positive', 2: 'Hallucinations: Positive', 3: 'Disorganized speech: Positive',
               4: 'Disordered behavior: Positive', 5:'Thought disorder: Positive', 
               6:'Alogia(speech poverty): Negative', 7:'Poor attention: Negative', 8:'Social withdrawal: Negative', 
               9:'Attention deficits: Negative'
}

def get_medication(num):
    """ A very simple function that returns a key-value pair for medication and price. """
    return Medications.get(num)
Medications = {1: 'Name: Seroquel, Price = $11', 2: 'Name: Abilify, Price = $18', 3: 'Name: Zyprexa, Price = $13',
               4: 'Name: Prochlorperazine , Price = $12', 5:'Name: Latuda, Price = $1,219', 
               6:'Name: Geodon, Price = $31', 7:'Name: Invega, Price = $242', 8:'Name: Perphenazine, Price = $23', 
               9:'Name: Molindone, Price = $89'
}
                
def treatment_options():
    """ A very simple function that returns a random treatment idea from a list. """
    for i in treatment_list:
        return random.choice(treatment_list)
             
treatment_list = ['Consult a doctor and ask about treatment options', 'Take prescribed medication', 
                  'If feeling depressed, talk to someone', 'Psychiatric therapy', 'Vocational rehabilitation', 
                  'Family therapy', 'Hospitalization', 
                 'Electroconvulsive therapy'] 