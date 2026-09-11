```markdown
# 🎲 Guess the Number – Python Game

> **Welcome, code explorer!**  
> This little game is my first venture into Python, and I had a blast building it. 🎉

## Overview
A command‑line game where the computer picks a random number between 1 and 100 and the player tries to guess it. The program validates input, counts attempts, and celebrates when you win.

## Installation
1. **Clone the repository** (or download the folder containing this file).  
   ```bash
   git clone https://github.com/your-username/How-I-Taught-Myself.git
   cd How-I-Taught-Myself/Programming\ Languages/Python/guess-the-number
   ```

2. *(Optional)* **Create a virtual environment** – not required for this script but good practice.  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. No external packages are needed; the only required file is `guess_number.py`.

## Usage
Run the game from the command line:

```bash
python guess_number.py
```

### Sample Session
```text
Welcome to my first python project! The Guessing Game!
I'm thinking of a number between 1 and 100
Enter your guess: hello
That's not a valid number. Try again.
Enter your guess: 60
Too low!
Enter your guess: 85
Too high!
Enter your guess: 73
You got it in 3 tries
```

## How it Works
```python
import random

print("Welcome to my first python project! The Guessing Game!")

secret_number = random.randint(1, 100)   # pick a secret number
print("I'm thinking of a number between 1 and 100")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue          # ask again without counting this as an attempt

    attempts += 1        # increment attempt counter

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it in {attempts} tries")
        break            # exit the loop when the guess is correct
```

- `random.randint(1, 100)` returns an integer **inclusive** of both bounds.  
- The `while True` loop keeps prompting until the correct number is guessed.  
- `try / except ValueError` catches non‑numeric input, displays a friendly message, and repeats the prompt.  
- `attempts += 1` counts only *valid* guesses.  
- An f‑string (`f"…"`) injects the `attempts` variable into the final message.

## What I Learned
- Importing and using Python’s standard library.  
- The importance of **input validation** and exception handling.  
- How loops (`while`) and control statements (`continue`, `break`) shape program flow.  
- Using **f‑strings** for clean, readable output.  
- Adding comments and documentation to make code self‑explanatory.

## Future Improvements
- Add difficulty levels (different number ranges).  
- Implement a maximum number of attempts and reveal the secret number on loss.  
- Store high scores in a JSON file.  
- Build a simple GUI with `tkinter` or a web interface using `Flask`.

---  

## License
This project is licensed under the MIT License – see the [LICENSE](../LICENSE) file for details.
```