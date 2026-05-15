# STUDENT LIFE SIMULATOR

print("🎓 Welcome to Student Life Simulator!")
name = input("Enter your name: ")

energy = 100
money = 500
grades = 50
day = 1

def show_status():
    print("\n📊 STATUS:")
    print("Day:", day)
    print("Energy:", energy)
    print("Money:", money)
    print("Grades:", grades)
    print("-" * 30)

def study():
    global energy, grades
    print("\n📚 You chose to study.")
    hours = int(input("How many hours do you want to study (1-10)? "))
    
    if hours > energy:
        print("⚠️ You are too tired!")
        return
    
    energy -= hours * 5
    grades += hours * 2
    print("✅ You studied well!")

def work():
    global energy, money
    print("\n💼 You chose to work.")
    hours = int(input("How many hours do you want to work (1-10)? "))
    
    if hours > energy:
        print("⚠️ Not enough energy!")
        return
    
    energy -= hours * 4
    money += hours * 50
    print("💰 You earned money!")

def rest():
    global energy
    print("\n😴 You chose to rest.")
    hours = int(input("How many hours do you want to rest (1-10)? "))
    
    energy += hours * 6
    if energy > 100:
        energy = 100
    print("🔋 Energy restored!")

def hangout():
    global energy, money
    print("\n🎉 You chose to hang out with friends.")
    
    if money < 100:
        print("⚠️ Not enough money!")
        return
    
    energy -= 10
    money -= 100
    print("😄 You had fun!")

def exam():
    global grades
    print("\n📝 Exam Day!")
    
    if grades > 80:
        print("🏆 Excellent! You scored A!")
    elif grades > 60:
        print("👍 Good! You scored B!")
    elif grades > 40:
        print("🙂 You passed with C.")
    else:
        print("❌ You failed. Study more next time!")

def random_event():
    global energy, money, grades
    
    print("\n🎲 Random Event!")
    event = int(input("Pick a number (1-3): "))
    
    if event == 1:
        print("💸 Unexpected expense!")
        money -= 100
    elif event == 2:
        print("⚡ Sudden motivation boost!")
        energy += 20
    else:
        print("📖 Surprise quiz!")
        grades += 5

# MAIN GAME LOOP
while day <= 7:
    print("\n🌅 Day", day)
    show_status()
    
    print("Choose your action:")
    print("1. Study 📚")
    print("2. Work 💼")
    print("3. Rest 😴")
    print("4. Hangout 🎉")
    print("5. Skip Day ⏭️")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        study()
    elif choice == "2":
        work()
    elif choice == "3":
        rest()
    elif choice == "4":
        hangout()
    elif choice == "5":
        print("⏭️ You skipped the day.")
    else:
        print("❌ Invalid choice.")
        continue
    
    random_event()
    
    if energy <= 0:
        print("\n💀 You ran out of energy! Game Over.")
        break
    
    if money < 0:
        print("\n💸 You are in debt! Game Over.")
        break
    
    day += 1

# FINAL RESULT
print("\n🎯 FINAL RESULTS:")
show_status()
exam()

print("\n🙏 Thanks for playing,", name)