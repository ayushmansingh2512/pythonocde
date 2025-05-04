import random

print("🎮 Welcome to Rock, Water, Scissor Game 🎮\n")
print("Here are the instructions:")
print("For 🪨 Rock, press - R")
print("For 💧 Water, press - W")
print("For ✂️ Scissor, press - S")

# Map choices to numbers
choice_dict = {"R": 1, "W": -1, "S": 0}
reverse_dict = {
    1: "🪨 Rock",
    -1: "💧 Water",
    0: "✂️ Scissor"
}

# Computer makes a random choice
computer = random.choice([1, 0, -1])

# User input
your_choice = input("\nEnter your choice: ").upper()

if your_choice not in choice_dict:
    print("❌ Invalid input. Please enter R, W, or S.")
else:
    you = choice_dict[your_choice]

    print(f"\n🧑 You chose: {reverse_dict[you]}")
    print(f"💻 Computer chose: {reverse_dict[computer]}")

    # Determine the winner
    if you == computer:
        print("🤝 It's a tie!")
    elif (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
        print("🎉 You win!")
    else:
        print("😞 Computer wins!")

