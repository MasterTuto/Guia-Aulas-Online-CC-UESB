# coding: utf-8

import re

'''
[
  {
      'semester': 'Primeiro Semestre',
      'subjects': [
          {
              'name': 'Algoritmos e Programação I (AP1)',
              'content': {
                  'Recursos em vídeo': [
                      {
                          'title': '1 Evolução das Linguagens [Estudonauta Cursos]',
                          'url': 'https://www.youtube.com/watch?v=VdTRiUe23os'
                      }
                  ]
              }
          }
      ]
  }
]
'''

string = '''''' # insira aqui o conteúdo do README.md, principalmente o conteúdo das aulas em si.

obj = []
currentType = ""

for c in string.split('\n'):
  c = c.strip()

  if c.startswith("###"):
    c_ = c.strip("# ")
    obj.append({"semester": c_, 'subjects': []})

  elif c.startswith("<details><summary>"):
    c_ = re.match(r"<details><summary> ?<b>(.+)</b> ?</summary>", c).groups()[0].strip()
    obj[-1]['subjects'].append({'name': c_, 'content': []})
  
  elif c.startswith("<dt>"):
    c_ = re.match(r'<dt>(.+)</dt>', c).groups()[0].strip()
    currentType = c_
    obj[-1]['subjects'][-1]['content'].append({'type': c_, 'list': []})


  elif c.startswith("<dd>"):
    c_ = re.match(r'<dd><a href="(.+)">(.+)</(a|d)></dd>', c).groups()
    obj[-1]['subjects'][-1]['content'][-1]['list'].append({'title': c_[1], 'url': c_[0]})

import json

a = json.dumps(obj, indent=4, ensure_ascii=False)

with open("output.json", 'w', encoding="utf-8") as f:
  f.write(a)



    

    
    
        
