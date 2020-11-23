#: Länge des Passworts, Großbuchstaben, kleinbuchstaben, Ziffern, Symbole
import pyperclip
import string
import random

def generate_password(length):
  character_pool = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits

  output = ''.join(random.sample(character_pool, k=length))

  return output



def run():
    while True:
        user_input = input("How long should the password be? - ")
        try:
            pw_length = int(user_input)
            pw = generate_password(pw_length)
            pyperclip.copy(pw)
            print(f"""Password: {pw}
It has been copied to the clipboard. ✨
""")
            break
        except ValueError:
            print("Please type in an integer number.")


run()


