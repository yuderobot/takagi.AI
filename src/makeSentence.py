import markovify
import json

def remover(result):
  # Load banned.json
  json_open = open('data/banned.json', 'r')
  json_load = json.load(json_open)
  for w in json_load['words']:
    result = result.replace(w, '')
  return result

def make_sentence():
    with open("data/model.json", "r") as f:
        textModel = markovify.Text.from_json(f.read())

    while True:
        made = textModel.make_sentence(tries=100)

        if made:
            sentence = "".join(made.split())
            break
    return remover(sentence)