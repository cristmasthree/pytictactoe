#Written by Ege Emir Özkan in Cem Kurt's Computer
import random
import os

print("XOX'e hoj geldiniz")
rows = {1:" ", 2:" ", 3:" ",
        4:" ", 5:" ", 6:" ",
        7:" ", 8:" ", 9:" "}
usedrows = []
Turn = 0
def respond():
  global rows
  global usedrows
  selected = random.randint(1, 10)
  if usedrows.count(selected) != 0:
    selected = random.randint(1, 10)
  elif usedrows.count(selected) == 0:
    usedrows.append(selected)
    rows[selected] = "O"
def draw(rows):
  output = """
   [{}] [{}] [{}]
   [{}] [{}] [{}]
   [{}] [{}] [{}]
  """.format(rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8], rows[9])
  print(output)
while Turn <= 9:
  draw(rows)
  input_ = input("Bir numara girin: ")
  input_ = int(input_)
  if input_ in usedrows:
    print("unable to")
  else:
    rows[input_] = "X"
  draw(rows)
  respond()
  Turn += 1
  os.system("cls")

    
