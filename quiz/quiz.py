# -*- coding: utf-8 -*-
"""
@author: Sharath S Hebbar (19GACSE081)
"""


import random

capitals = {
        'Agra': 'TajMahal', 
        'NewDelhi': 'QutubMinar', 
        'Puri': 'SunTemple',
        'Aurangabad': 'Ajanta and Ellora Caves',
        'Chennai': 'CholaTemples', 
        'Mumbai': 'ElephantaCaves',
        'Hyderabad': 'Charminar', 
        'Patna': 'Rani ka vav', 
        'Bubaneshwar': 'Udayagiri caves',
        'Bihar': 'Cooch Behar Palace', 
        'Amritsar': 'Golden Temple', 
        'Jaipur': 'HawaMahal',
        'Karnataka':'Mysuru Palace', 
        'Kolkata': 'Victoria Memorial',
        'UttarPradesh': 'Fatekpursikri', 
        'Vadodara':'Laxmi vilas palace', 
        'Jodhpur': 'Mehrangarh Fort', 
        'Odisha': 'Konark Sun Temple', 
        'Tamil Nadu':'Mahabalipuram', 
        'Tanjevur': 'Brihadeshwara temple', 
        'Madurai': 'MeenakshiAmman Temple', 
        'Pune':'Shaniwar wada', 
        'Goa': 'Basilica of bom jesus', 
        'Kanyakumari': 'Vivekananda Rock', 
        'Lucknow':'Bara Imambara', 
        'Rajastan': 'KumbalgarhFort', 
        'Gujurat': 'Champaner', 
        'Delhi':'Bahai Temple', 
        'Hampi': 'Virupaksha Temple',
        'Junagadh': 'Mahabat Maqbara',
        'Shravanabelagola': 'Gomateshwara statue', 
        'Bijapur': 'GolGumbaz',
        'Bikaner': ' Junagadh Fort',
        'Andra Pradesh': 'Golconda Fort ',
        'Madhya Pradesh': 'Gwalior Fort'
  
        }

quiz_answer_template = '''\
Capitals Quiz Answers #{}

{}
'''

quiz_file_template = '''\
Capitals Quiz #{}
Name:
Date:

Which one of the monument is located in ?
{}
'''

question_template = '''\
Q{} {}?
{}
'''

def create_answer_file(path, question_id, answers):
    with open(path, 'w') as f:
        s = quiz_answer_template.format(question_id, answers)
        f.write(s)

def create_quiz_file(path, question_id, question_and_options):
    with open(path, 'w') as f:
        s = quiz_file_template.format(question_id, question_and_options)
        f.write(s)

def get_quiz(dictionary, n):
    """Based on a dictionary with key and values will return 
      1) Questions with 4 options tab-separated as a string
      2) Correct answers as a string
      """
    output = []

    states = list(dictionary.keys())
    random.shuffle(states)  
    correct_answers = [dictionary.get(i) for i in states]

    for ind, st in enumerate(states[:n], 1):
        d = dictionary.copy()
        correct_answer = d.pop(st)
        incorrect_answers = list(d.values())
        random.shuffle(incorrect_answers)  
        options = [correct_answer] + incorrect_answers[:3]
        random.shuffle(options)
        output.append(question_template.format(ind, st, '\t'.join(options)))

    return '\n'.join(output), '\n'.join(correct_answers)

for quizNum in range(1, 6):
    questions_and_options, answers = get_quiz(capitals, n=35)
    create_quiz_file(f'monumentsquiz{quizNum}.txt', quizNum, questions_and_options)
    create_answer_file(f'monumentsquiz_answers{quizNum}.txt', quizNum, answers)