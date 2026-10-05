class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "Your age is " + str(self.age) + ". You can attend Ido's birthday in " + str(18 - self.age) + " years."

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(int(age))
        else:
            print("You should send an invite to " + name)

    except UnderAge as e:
        print(e)

def main():
    send_invitation("Talia", 17)
    send_invitation("Dona", 20)
if __name__ == "__main__":
    main()