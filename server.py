from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import io
# import spacy
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


PATH = r'C:\Users\utkar\Desktop\autobots-b\Garnishment_Database.json'


def startupCheck():
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        with io.open(PATH, 'w') as db_file:
            db_file.write(json.dumps({}))
# from spacy import displacy
# nlp = spacy.load("en_core_web_trf")

# def labels():
#     return {
#         "PERSON":True,
#         "NORP":False,
#         "FAC":False,
#         "ORG":True,
#         "GPE":False,
#         "LOC":False,
#         "PRODUCT":True,
#         "EVENT":False,
#         "WORK_OF_ART":False,
#         "LAW":True,
#         "LANGUAGE":False,
#         "DATE":False,
#         "TIME":False,
#         "PERCENT":False,
#         "MONEY":True,
#         "QUANTITY":False,
#         "ORDINAL":False,
#         "CARDINAL":False
#     }
    
def get_questions():
    return [
        'What is the Customer id of record on whom garnishment notice has been raised?',
        'What is the Legal name of record on whom garnishment notice has been raised?',
        'What is the account number of record on whom garnishment notice has been raised?',
        'What is the Garnishment Status of garnishment notice raised?',
        'What is the Garnishment Type of garnishment notice raised?',
        'What is the Garnishment Amount of garnishment notice raised?',
        'What are the Garnishment Details of garnishment notice raised?',
        'What are the Court Details of raised garnishment notice?',
        
        'What is the Customer id?',
        'What is the Legal name?',
        'What is the account number?',
        'What is the Garnishment Status?',
        'What is the Garnishment Type?',
        'What is the Garnishment Amount?',
        'What are the Garnishment Details?',
        'Which are the Court Details?'  ,
        
        'What is Customer id?',
        'What is Legal name?',
        'What is account number?',
        'What is Garnishment Status?',
        'What is Garnishment Type?',
        'What is Garnishment Amount?',
        'What are Garnishment Details?',
        'Which Court?'
    ]

def insighter(body):
    text = body['text']
    text = text.encode('utf-8').decode('unicode-escape')
    text = text.replace('\r\n', '. ').replace('\r','. ').replace('\n','. ')
#     doc = nlp(text)
#     print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#     print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    # Find named entities, phrases and concepts
#     for entity in doc.ents:
#         print(entity.text, entity.label_)
#     displacy.render(doc, style="dep", jupyter=True)
#     displacy.render(doc, style="ent", jupyter=True)
#     client_name = ""
    
    response = {}
    question_answer_mapping = {}
    questions = get_questions();
    for question in questions:
        QA_input = {
            'question': question,
            'context': text
        }
#         {'score': 0.9427658319473267, 'start': 1047, 'end': 1053, 'answer': '7500$.'}
        res = nlp(QA_input)
        print(res)
        question_answer_mapping[question] = res
    
    for index in range(0,8):
        q1= questions[index]
        q2=questions[index+8]
        q3=questions[index+8*2]
        
        if question_answer_mapping[q1]['score'] >= question_answer_mapping[q2]['score'] and  question_answer_mapping[q1]['score'] >= question_answer_mapping[q3]['score']:
            response[index] = question_answer_mapping[q1]
        elif question_answer_mapping[q2]['score'] >= question_answer_mapping[q3]['score']:
             response[index] = question_answer_mapping[q2]
        else:
            response[index] = question_answer_mapping[q3]
    # Writing to sample.json
    customer_id = response.get(0)
    key = customer_id["answer"]
    json_object = {key : response}
    print(json_object)
    with open(r'C:\Users\utkar\Desktop\autobots-b\Garnishment_Database.json', "w") as outfile:
        outfile.write(json.dumps(json_object))        
    return response


class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        response_data = {'message': 'Hello World'}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
    def do_POST(self):
        if self.path == '/greet':
            self.handle_greet()
        elif self.path == '/echo':
            self.handle_echo()
        elif self.path == '/insight':
            self.handle_insighter()
        else:
            self.send_error(404)
            
    def handle_greet(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request_data = json.loads(body)
        response_data = {'message': 'Hello, ' + request_data['name']}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        
    def handle_echo(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request_data = json.loads(body)
        response_data = request_data
        self.send_response(200) 
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def handle_insighter(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request_data = json.loads(body)
        response_data = insighter(request_data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))
        
def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    startupCheck()
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server listening on port {port}")
    httpd.serve_forever()
    
run()