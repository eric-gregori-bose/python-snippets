import json
import csv


list_of_states = []
list_of_changes = []

class Process:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Line:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

class GenerateDiagram:
    def __init__(self, doc_name, page_name, title):
        self.rows = []
        self.fields = { 'Id':'',
                        'Name':'',
                        'Shape Library':'',
                        'Page ID':'',
                        'Contained By':'',
                        'Group':'',
                        'Line Source':'',
                        'Line Destination':'',
                        'Source Arrow':'',
                        'Destination Arrow':'',
                        'Status':'',	
                        'Text Area 1':'',
                        'Text Area 2':'' }
        self.pageid = 2
        self.add_row(1,'Document',{'Status':'Draft','Text Area 1':doc_name})
        self.add_row(self.pageid,'Page',{'Text Area 1':page_name})
        self.add_row(3,'Text',{'Group':6,'Shape Library':'Standard','Page ID':self.pageid,'Text Area 1':title})
        self.add_row(4,'Text',{'Group':6,'Shape Library':'Standard','Page ID':self.pageid,'Text Area 1':"Dec 2022"})    
        self.add_row(5,'Group 1',{'Page ID':self.pageid})
        self.add_row(6,'Group 2',{'Page ID':self.pageid,'Group':5,})
        self.id = 7

    def add_row(self, id, name, data):
        self.rows.append({**self.fields, **{'Id':id,'Name':name}, **data})

    def add_process(self, state_name, state_id):
        self.add_row(self.id, 'Process',{'Shape Library':'Data Flow','Page ID':self.pageid,'Text Area 1':state_name,'Text Area 2':state_id})
        self.id = self.id + 1
        
with open('Names.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = output.fields.keys())
    writer.writeheader()
    writer.writerows(output.rows)
