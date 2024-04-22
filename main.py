
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
  {"spanish": "dejar", "english": "to leave"},
  {"spanish": "su", "english": "his/her/your/their"},
  {"spanish": "creer", "english": "to believe"},
  {"spanish": "hablar", "english": "to speak"},
  {"spanish": "nada", "english": "nothing"},
  {"spanish": "menos", "english": "less"},
  {"spanish": "mas", "english": "more"},
  {"spanish": "estar", "english": "to be"},
  {"spanish": "como", "english": "like/as"},
  {"spanish": "tener", "english": "to have"},
  {"spanish": "hacer", "english": "to make"},
  {"spanish": "nuevo", "english": "new"},
  {"spanish": "viejo", "english": "old"},
  {"spanish": "cada", "english": "each"},
  {"spanish": "encontrar", "english": "find"},
  {"spanish": "llevar", "english": "to carry"},
  {"spanish": "ahora", "english": "now"},
  {"spanish": "donde", "english": "where"},
  {"spanish": "bien", "english": "well/good"},
  {"spanish": "parecer", "english": "seem"},
  {"spanish": "cosa", "english": "thing"},
  {"spanish": "dia", "english": "day"},
  {"spanish": "desde", "english": "from"},
  {"spanish": "si", "english": "yes"},
  {"spanish": "llegar", "english": "to arrive"},
  {"spanish": "poco", "english": "little"},
  {"spanish": "tiempo", "english": "time"},
  {"spanish": "desde", "english": "from"},
  {"spanish": "entre", "english": "between"},
  {"spanish": "vez", "english": "time"},
  {"spanish": "sobre", "english": "on"},
  {"spanish": "mi", "english": "my"},
  {"spanish": "dar", "english": "to give"},
  {"spanish": "ese", "english": "that"},
  {"spanish": "este", "english": "this"},
  {"spanish": "ya", "english": "already"},
  {"spanish": "otro", "english": "other"},
  {"spanish": "poder", "english": "can"},
  {"spanish": "no poder", "english": "can't"},
  {"spanish": "alguno", "english": "some"},
  {"spanish": "carro", "english": "car"},
  {"spanish": "perro", "english": "dog"},
  {"spanish": "beber", "english": "to drink"},
  {"spanish": "escuchar", "english": "heard"},
  {"spanish": "hasta", "english": "until"},
  {"spanish": "primero", "english": "first"},
  {"spanish": "segundo", "english": "second"},
  {"spanish": "grande", "english": "big"},
  {"spanish": "small", "english": "pequeno"},
  {"spanish": "gato", "english": "cat"},
  {"spanish": "cosa", "english": "thing"},
  {"spanish": "quedar", "english": "to stay"},
  {"spanish": "cada", "english": "each"},
  {"spanish": "seguir", "english": "continue"},
  {"spanish": "silla", "english": "chair"},
  {"spanish": "mesa", "english": "table"},
  {"spanish": "tambien", "english": "also"},
  {"spanish": "picante", "english": "spicy"},
  {"spanish": "pato", "english": "duck"},
  {"spanish": "cocina", "english": "kitchen"},
  {"spanish": "pollo", "english": "chicken"},
  {"spanish": "cocinar", "english": "to cook"},
  {"spanish": "lavar", "english": "to wash"},
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

# looping over the words.
# having the anser and with strip and lower, the user will not make mistakes of spacing and uppercase.
  for word in words:
      print("What is the English equivalent of '{word['spanish']}'?")
      user_answer = input("add your name: ").strip().lower()
      correct_anser = word['english'].lower()
#if the answer is correct, will say correct or correcto.
#if the answer is incorrect, it will show you the right answer.
      if user_answer == correct_answer:
        print("Correct!!!\n!","Correcto!!"\n!")
        score += 1
      else:
        print("Wrong, try again! The correct answer will be '{word['english']}'.\n)
        

    
    
  


# Welcome coding page!
def main():
  print("Welcome to the learning Spanish tool for beginners EspanolEasy!","Bienvenidos a la herramienta de aprendizaje de Espanol para principiantes EspanolEasy!")
  print("Press enter/return to start learning", "Presiona enter/retornar para comenzar aprendiendo")
  prueba_user(words)
  
  
