
# 100+ most commom spanish words
words = [
  {"spanish": "el", "english": "he"},
  {"spanish": "ella", "english": "she"},
  {"spanish": "que", "english": "that/which (question) /what (question)"},
  {"spanish": "y", "english": "and"},
  {"spanish": "a", "english": "to/at"},
  {"spanish": "de", "english": "of/from"},
  {"spanish": "ser", "english": "to be"},
  {"spanish": "parte", "english": "part"},
  {"spanish": "en", "english": "in/on"},
  {"spanish": "haber", "english": "to be"},
  {"spanish": "no", "english": "not/no"},
  {"spanish": "dejar", "english": "leave"},
  {"spanish": "su", "english": "his/her/your/their"},
  {"spanish": "creer", "english": "believe"},
  {"spanish": "hablar", "english": "speak"},
  {"spanish": "nada", "english": "nothing"},
  {"spanish": "menos", "english": "less"},
  {"spanish": "mas", "english": "more"},
  {"spanish": "estar", "english": "to be"},
  {"spanish": "como", "english": "like/as"},
  {"spanish": "tener", "english": "have"},
  {"spanish": "hacer", "english": "make"},
  {"spanish": "nuevo", "english": "new"},
  {"spanish": "viejo", "english": "old"},
  {"spanish": "cada", "english": "each"},
  {"spanish": "encontrar", "english": "find"},
  {"spanish": "llevar", "english": "carry"},
  {"spanish": "ahora", "english": "now"},
  {"spanish": "donde", "english": "where"},
  {"spanish": "bien", "english": "well/good"},
  {"spanish": "parecer", "english": "seem"},
  {"spanish": "cosa", "english": "thing"},
  {"spanish": "dia", "english": "day"},
  {"spanish": "desde", "english": "from"},
  {"spanish": "si", "english": "yes"},
  {"spanish": "llegar", "english": "arrive"},
  {"spanish": "poco", "english": "little"},
  {"spanish": "tiempo", "english": "time"},
  {"spanish": "desde", "english": "from"},
  {"spanish": "entre", "english": "between"},
  {"spanish": "vez", "english": "time"},
  {"spanish": "sobre", "english": "on"},
  {"spanish": "mi", "english": "my"},
  {"spanish": "dar", "english": "give"},
  {"spanish": "ese", "english": "that"},
  {"spanish": "este", "english": "this"},
  {"spanish": "ya", "english": "already"},
  {"spanish": "otro", "english": "other"},
  {"spanish": "poder", "english": "can"},
  {"spanish": "no poder", "english": "can't"},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
  {"spanish": "", "english": ""},
]
# By using this coding, it will shuffle all the words already placed on top.
def prueba_user(words):
  random.shuffle(words)
  score = 0

#
  for word in words:
    print("What is the English equivalent of '{word['spanish']}'?")
    
  


# Welcome coding page!
def main():
  print("Welcome to the learning Spanish tool for beginners EspanolEasy!","Bienvenidos a la herramienta de aprendizaje de Espanol para principiantes EspanolEasy!")
  print("Press enter/return to start learning", "Presiona enter/retornar para comenzar aprendiendo")
  prueba_user(words)
  
  
