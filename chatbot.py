import random

print("Hello, I am a chatbot 🤖")

while True:
    mood = input("Choose your mood (happy/ok/sad or exit): ").lower()

    if mood == "happy":
        choice = input("Do you want to play a luck game with me 😉? (yes/no): ").lower()

        if choice == "yes":
            print("Take a number between 1-10")

            try:
                user_number = int(input("Which number will you take 😏: "))

                if user_number < 1 or user_number > 10:
                    print("❌ Please choose a number between 1 and 10 only!")
                    continue

                lucky_number = random.randint(1, 10)
                print("My lucky number is:", lucky_number)

                if user_number == lucky_number:
                    print("🎉 WOW! You are super lucky!")
                else:
                    print("😅 Oops! Better luck next time!")

            except ValueError:
                print("❌ Numbers only! No letters or symbols 😅")

        else:
            print("Okay, maybe next time 🙂")

    elif mood == "ok":
        print("Cool 😌 Stay relaxed!")

    elif mood == "sad":
        print("💙 Don’t worry, things will get better!")

    elif mood == "exit":
        print("Bye bye 👋 See you soon!")
        break

    else:
        print("Please enter a valid mood!")
