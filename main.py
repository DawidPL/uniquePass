from tkinter import *
import random
import string

def description():
    print("""         Witaj w programie. Odpowiednie hasło to niezwykle ważna rzecz podczas korzystania 
         z internetu. Powinno być trudne lub wręcz nawet niemożliwe do złamania. 
         Niestety wiele osób obawiając się, że je zapomną stosują najgorsze możliwe
         typy haseł: daty urodzenia i imiona lub ich kombinacje.
         Generator pozwoli Ci utworzyć odpowiednio mocne hasło korzystając z Twoich
         propozycji i sugestii co ma się w nim znaleźć """)

class PasswordProgram:
    def __init__(self):
        self._root = Tk()
        self._root.title("Hasło")
        self._topFrame = Frame(self._root)
        self._topFrame.grid(row=0, column=0)
    def startProgram(self):
        button1 = Button(self._topFrame, text="Kliknij aby rozpocząć program", command=self.choiceButtons, bg="#53536d", fg="#e0abdd")
        button1.grid(row=0)
        self._root.mainloop()
    def choiceButtons(self):
        button1 = Button(self._topFrame, text="Wygeneruj hasło automatycznie", command=self.password_main_question, bg="#53536d", fg="#e0abdd")
        button2 = Button(self._topFrame, text="Ustaw parametry dla hasła", command=self.password_main_parameters, bg="#53536d", fg="#e0abdd")
        button1.grid(row=0)
        button2.grid(row=0, column=1)
    '''def passwordTypeButtons(self):
        button1 = Button(self._topFrame, text="Nie do złamania", command=self.unbreak_password, bg="#53536d", fg="#e0abdd")
        button2 = Button(self._topFrame, text="Bardzo silne", command=self.strong_password, bg="#53536d", fg="#e0abdd")
        button3 = Button(self._topFrame, text="silne", command=self.normal_password, bg="#53536d", fg="#e0abdd")
        entry_1 = Entry(self._root)
        #text = tk.StringVar()
        #entry = tk.Entry(window, width=40, textvariable=text)
        #text.set()
        entry_1.grid(row=1)
        button1.grid(row=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)'''
    def password_main_parameters(self):
        button1 = Button(self._topFrame, text="Jakie litery chcesz mieć w haśle?")
        button2 = Button(self._topFrame, text="Jakie liczby chcesz mieć w haśle?")
        button3 = Button(self._topFrame, text="Jakie znaki specjalne chcesz mieć w haśle?")
        entry_1 = Entry(self._root)
        entry_2 = Entry(self._root)
        entry_3 = Entry(self._root)
        button1.grid(row=2)
        entry_1.grid(row=2, column=1)
        button2.grid(row=3)
        entry_2.grid(row=3, column=1)
        button3.grid(row=4)
        entry_3.grid(row=4, column=1)

    def password_main_question(self):
        print("Wybierz jakie chcesz mieć hasło :")
        button1 = Button(self._topFrame, text="Nie do złamania", command=self.unbreak_password, bg="#53536d", fg="#e0abdd")
        button2 = Button(self._topFrame, text="Bardzo silne", command=self.strong_password, bg="#53536d", fg="#e0abdd")
        button3 = Button(self._topFrame, text="silne", command=self.normal_password, bg="#53536d", fg="#e0abdd")
        entry_1 = Entry(self._root)
        # text = tk.StringVar()
        # entry = tk.Entry(window, width=40, textvariable=text)
        # text.set()
        entry_1.grid(row=1)
        button1.grid(row=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)

    # Functions to generates a random password
    def unbreak_password(self):

        random_choice = random.choice(string.ascii_letters + string.digits + string.punctuation)
        number = 0
        x = ''
        while number != 15:
            number += 1
            x += random_choice
            random_choice = random.choice(string.ascii_letters + string.digits + string.punctuation)
        return x

    def strong_password(self):
        random_choice = random.choice(string.ascii_letters + string.digits)
        number = 0
        x = ''
        while number != 15:
            number += 1
            x += random_choice
            random_choice = random.choice(string.ascii_letters + string.digits)
        return x

    def normal_password(self):
        random_choice = random.choice(string.ascii_letters + string.digits)
        number = 0
        x = ''
        while number != 8:
            number += 1
            x += random_choice
            random_choice = random.choice(string.ascii_letters + string.digits)
        return x

pwProgram = PasswordProgram()
if __name__ == '__main__':
    pwProgram = PasswordProgram()
    pwProgram.startProgram()


description()
pwProgram.startProgram()