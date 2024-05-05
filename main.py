
# 100+ most commom spanish words
# when a word has 2 different meanings, I added "[]" and ","
# I found better words to use so I added 30 more words to import

import random

words = [
  {"spanish": "el", "english": "he"},
  {"spanish": "ella", "english": "she"},
  {"spanish": "que", "english": "what"},
  {"spanish": "y", "english": "and"},
  {"spanish": "a", "english": "to"},
  {"spanish": "de", "english": "of or from"},
  {"spanish": "ser", "english": "to be"},
  {"spanish": "parte", "english": "part"},
  {"spanish": "en", "english": "in or on"},
  {"spanish": "haber", "english": "to be"},
  {"spanish": "no", "english": ["not", "no"]},
  {"spanish": "dejar", "english": "leave"},
  {"spanish": "su", "english": "his ,her , your or their"},
  {"spanish": "creer", "english":  "believe"},
  {"spanish": "hablar", "english": "speak"},
  {"spanish": "nada", "english": "nothing"},
  {"spanish": "menos", "english": "less"},
  {"spanish": "mas", "english": "more"},
  {"spanish": "estar", "english": "to be"},
  {"spanish": "como", "english": "like or as"},
  {"spanish": "tener", "english": "have"},
  {"spanish": "hacer", "english":  "make"},
  {"spanish": "nuevo", "english": "new"},
  {"spanish": "viejo", "english": "old"},
  {"spanish": "cada", "english": "each"},
  {"spanish": "encontrar", "english": "find"},
  {"spanish": "llevar", "english":  "carry"},
  {"spanish": "ahora", "english": "now"},
  {"spanish": "donde", "english": "where"},
  {"spanish": "bien", "english": "well or good"},
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
  {"spanish": "dar", "english":  "give"},
  {"spanish": "ese", "english": "that"},
  {"spanish": "este", "english": "this"},
  {"spanish": "ya", "english": "already"},
  {"spanish": "otro", "english": "other"},
  {"spanish": "poder", "english": "can"},
  {"spanish": "no poder", "english": "can't"},
  {"spanish": "alguno", "english": "some"},
  {"spanish": "carro", "english": "car"},
  {"spanish": "perro", "english": "dog"},
  {"spanish": "beber", "english":  "drink"},
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
  {"spanish": "cocinar", "english":  "cook"},
  {"spanish": "lavar", "english": "to wash"},
  {"spanish": "aun", "english": "still"},
  {"spanish": "hombre", "english": "man"},
  {"spanish": "hombres", "english": "men"},
  {"spanish": "mujer", "english": "woman"},
  {"spanish": "mujeres", "english": "women"},
  {"spanish": "pais", "english": "country"},
  {"spanish": "condado", "english": "county"},
  {"spanish": "ciudad", "english": "city"},
  {"spanish": "estado", "english": "state"},
  {"spanish": "capital", "english": "capital"},
  {"spanish": "cosa", "english": "thing"},
  {"spanish": "direccion", "english": "adress"},
  {"spanish": "esos", "english": "those"},
  {"spanish": "estos", "english": "these"},
  {"spanish": "avion", "english": "airplane"},
  {"spanish": "trabajo", "english": "work"},
  {"spanish": "cansado", "english": "tired"},
  {"spanish": "foto", "english": "photo"},
  {"spanish": "mesa", "english": "table"},
  {"spanish": "ventana", "english": "window"},
  {"spanish": "silla", "english": "chair"},
  {"spanish": "doctor", "english": "doctor"},
  {"spanish": "enfermo", "english": "sick"},
  {"spanish": "reloj", "english": "watch"},
  {"spanish": "cuchara", "english": "spoon"},
  {"spanish": "tenedor", "english": "fork"},
  {"spanish": "", "english": ""},
]
# By using this coding, it will shuffle all the words already placed on top.
# I use import to use random properly.
#I organized my code by using the tab bottom.
def quiz_user(words):
    random.shuffle(words)
    score = 0

# looping over the words.
# having the anser and with strip and lower, the user will not make mistakes of spacing and uppercase.
# in order to use '{word['spanish']}'?" properly, I added f in the beginning of ()

    for word in words:
        print(f"What is the English equivalent of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
#if the answer is correct, will say correct or correcto.
#if the answer is incorrect, it will show you the right answer.
        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"Wrong, try again! The correct answer will be '{word['english']}'.\n")
# in order to use {score}/{len(words)}"  properly, I added f in the beginning of ()
            
    print(f"Quiz complete! Your score is:/ Haz completado tu prueba! tu puntuacion es: {score}/{len(words)}")
        


# Welcome coding page.
def main():
    print("Welcome to the learning Spanish tool for beginners EspanolEasy! Bienvenidos a la herramienta de aprendizaje de Espanol para principiantes EspanolEasy!")
    input("Enter to start learning! Comienza aprendiendo!")
    quiz_user(words)
  
if __name__ == "__main__":
    main()
#just texted my code in visual and add I fixed some mistakes.
