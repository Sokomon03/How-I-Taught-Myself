#The_Guessing_Game

My First Project.

General Description of the project:- "The computer secretly generates a random number, and the user has to guess that number. Unlimited tries. If the guessed number is high, the computer will prompt the user that it is high, and vice versa. If the user is able to guess the number, the game stops there. At the end, the computer provides the number of tries done by the user till they reached the exact number by guessing."

_________________________________________________________________________________________________________________________

The Code:-
```python
import random

print("Welcome to my first python project! The Guessing Game!")

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    
    attempts = attempts + 1
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it in {attempts} tries")
        break
```

_________________________________________________________________________________________________________________________

Overview:-

The project start by importing the library needed for the feature of, computer picking a random number at start.
```python
import random
```
This followed by printing an output to show the title of the game.
```python
print("Welcome to my first python project! The Guessing Game!")
```
The next hurdle was to create a variable which could hold the value of the random function. I mean, well..
```python
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
```
(I am a beginner. So, I'm going to break down this random.randint(x, x+100) function for all of us.)

Generally speaking:- It's a function that tell python to grab a number between x and x+100.

Statistically Speaking:-
```python
# random : Name of the Library
# . (dot) : Tells python to look inside the toolkit
# randint : This is the toolkit. This stands for RANDom and INTeger. You know what an integer is, right?
# (x, x+100) : These are the integer numbers. The boundaries. aka ARGUMENTS! From x to x+100 or anything else, you know the drill.
```
FYI, the '#' is a function used to quote something inside a code. So, that we can write memo notes for our future selves/others to know why we wrote what we wrote. for example...
```python
#it shows like this! and it does not affects the code...and this is called COMMENTING.
```
FYI2.0, remember that indentations are very important in programming languages. python does not want to be messed up around that. I'll tell you the details later. just remember the quote, "a tab a day, keeps the indentationerror away!" 

Well.. Then came the input phase. I have to capture the input of the user, right? He has to type a number.

```python
guess = int(input("Enter your guess: "))
```
Ah! Make sure to add the 'int' here, as the user needs to type a number, not a letter.

Now, the next part comes in 3 stages. I had to change codes as I progressed. As my goal was to understand what I was doing, not just copy-paste inputs to get a good output.
_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________

The Stages:-
_________________________________________________________________________________________________________________________
Phase I: (if, elif, else) functions.
_________________________________________________________________________________________________________________________
General Speaking -> "If the number guess is bigger than the secret number, the computer should print "Too Big", and vice versa. If the user get's it right, the computer should print "You got this! Congrats!"

Statistically Speaking:-
```python
if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("You got it right! Congrats!")
```
So, for now... Let's look at what we've built so far.

The game starts. The computer asks us to guess a number between 1 and 100. It asks us to type the number. We type the number. If it's higher than the secret number picked by the computer, the computer tell us that it's too high, and vice versa. If we guess the right number, the computer congrats us!

Let's see the code and the output for this one.

Code:- Phase 1.

#importing the 'random' library
```python
import random

#printing the first message I want to send as the game starts!
print("Welcome to my first python project! The Guessing Game!")

#giving the value of random.randint to the variable named secret_number
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

#giving the input value entered by the user to the variable 'guess'.
guess = int(input("Enter your guess: "))

#telling the computer that:-
#if the input number stored in the 'guess' variable is 
#greater than the random number, picked and stored in the 'secret_number'
#variable, then they should print the following text and vice versa.
#you know the drill.

if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("You got it right! Congrats!")
```
Output:-
```python
PS C:\Program Files\Microsoft VS Code> & C:\Python314\python.exe "c:/Users/code/python/example.py"
Welcome to my first python project! The Guessing Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 60 (I as a user typed 60 btw)
Too high!
PS C:\Program Files\Microsoft VS Code> 
```
Now,

What happens if the user types something that is not a number between 1 and 100. For example:-
```python
Welcome to my first python project! The Guessing Game!
Im thinking of a number between 1 and 100
Enter your guess: No. I will not enter a number. What will you do? Hmm? Fight Me???
Traceback (most recent call last):
  File "c:/Users/code/python/example.py", line 11, in <module>
    guess = int(input("Enter your guess: "))
ValueError: invalid literal for int() with base 10: "No. I won't enter a number. What will you do? Hmm? Fight Me???"
```
You notice the name of the error? ValueError. This dude shows up when you do not enter the correct value.

Remember that 'int' function I added before the input?? Don't remember? Well, it's not my fault you made your attention span similar to that of a goldfish. Here! This one.
```python
guess = int(input("Enter your guess: "))
```
Here, the int is there to ensure that the value which gets inputed by the user, is an integer. Otherwise, we run into our friendly neighbourhood ValueError!

But, the output looks ugly right now, no? Yes! it does. No matter what you say...

We need to make it so that instead of this ValueError, anything else, like a message shows us telling that 'You have not typed the valid input. Please try again!' or something like that...

That's when Phase II comes in.
_________________________________________________________________________________________________________________________
Phase II (while, try, except, continue, break)
_________________________________________________________________________________________________________________________
General Speaking:- I now want to make it so that if I type the wrong input, it just shows me a message telling me I typed the wrong input. And instead of stopping the game there, it continues and asks for an input again.

Statistically Speaking:-
```python
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
```
Yes! I'll explain it in layman's terms as well, but before that, just look at the output now. Much cleaner.
```python
PS C:\Program Files\Microsoft VS Code> & C:\Python314\python.exe "c:/Users/code/python/example.py"
Welcome to my first python project! The Guessing Game!
Im thinking of a number between 1 and 100
Enter your guess: I love anime/manhwas/mangas/webnovels, but I cannot support them, as I am broke.
That's not a valid number. Try again.
Enter your guess: 
```

Here, We introduce to ourselves, THE LOOPS!! (well, only while loop for now. iykyk!)
```python
while True:
```
This means, if the provided input is correct.
```python

    try:
        guess = int(input("Enter your guess: "))
```
while(as long as) the code stays true, you can try and ask for the input.

And,
```python
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
```
if an exception occurs, (if the user does not type the intended value, then show them the message) and continue. 

BUT!!! 

If we have created a loop by using 'continue', we need to stop the loop by using 'break' at the end of the code too, no?

Well, this function is made just so that our code does not keep itself in a loop even after we provide the correct answer.
```python
        break
```
And, the result from all that is...
```python
Welcome to my first python project! The Guessing Game!
Im thinking of a number between 1 and 100
Enter your guess: I love anime/manhwas/mangas/webnovels, but I cannot support them, as I am broke.
That's not a valid number. Try again.
Enter your guess: 
```
and if the user stays sane, and this time...types the needed output like..
```python
Welcome to my first python project! The Guessing Game!
Im thinking of a number between 1 and 100.
Enter your guess: 8
```
the results should be fine. like..
```python
Enter your guess: 8
Too high!
Enter your guess: 
```
For now, Our code looks like this:-
```python
import random
print("Welcome to my first python project! The Guessing Game!")

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("You got it right! Congrats!")
        break
```
And the output shows like this:-
```python
PS C:\Program Files\Microsoft VS Code> & C:\Python314\python.exe "c:/Users/code/python/example.py"
Welcome to my first python project! The Guessing Game!
I'm thinking of a number between 1 and 100
Enter your guess: Batman!
That's not a valid number. Try again.
Enter your guess: 60
Too low!
Enter your guess: 80
Too high!
Enter your guess: 70
Too low!
Enter your guess: 76
Too high!
Enter your guess: 75
Too high!
Enter your guess: 73
Too high!
Enter your guess: 71
Too low!
Enter your guess: 72
You got it right! Congrats!
PS C:\Program Files\Microsoft VS Code> 
```
Yup! Stage II ends here.
_________________________________________________________________________________________________________________________
Stage III. (add a counter to count the number of tries it took to guess the number!)
_________________________________________________________________________________________________________________________
Changing our code one last time.

Let's see the finished output first this time.

Finished Code:-
```python
import random

print("Welcome to my first python project! The Guessing Game!")

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    
    attempts = attempts + 1
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it in {attempts} tries")
        break
```
Here, notice this guy,
```python
attempts = 0
```
and this dude a well,
```python
    attempts = attempts + 1
```
In the first dude, we are introducing a variable called 'attempts', and we assign it a value of 0. In the second dude, which we introduce inside the loop, we assign the 'attempts' a new value. Which is +1 of the previous attempt.

Understood? No. You didn't. He didn't.

Well, let me make it simpler.

Let's start from the start.
```python
The code gets executed -> It runs -> Game begins. Computer chooses a random number btw 1 and 100 -> computer asks us to choose a number between 1 and 100. We fk it up -> computer gets mad, but still asks us to choose a valid number. This time, out of pity, we choose a random number between 1 and 100. Computer says it's too high. I mean, the number we chose is higher than the secret number. There goes our first attempt. Computer is still asking us to choose the number. This time we choose something else. This time the computer says it's too low. There goes our second attempt.
```
So, basically,
```python
attempts = 0
```
is the counter we set before we try our attempt. As we have assigned the value 0 to it.

and after that, while staying inside the loop, we assign this dude,
```python
    attempts = attempts + 1
```
so, the computer continues to count the number of attempts by adding one per attempt.

Each time we mess up, the while loop restarts, it only 'breaks' if we get our correct try.
_________________________________________________________________________________________________________________________
Stage IV: (f, {}) I know I said that, My bad! I forgot. and now, i'm too lazy to change it all.
_________________________________________________________________________________________________________________________
These guys are needed in a print function to tell us the number of attempts we tried.
```python
    else:
        print(f"You got it in {attempts} tries")
        break
```
So, what we're basically doing here, is bringing the 'attempts' variable which stores the value of the number of tries, inside a print function. And to do that, we need to add a 'f' before the double inverted commas!

Well, we end the loop with a 'break' as well! and TADA!!!

The First Python Project Done!

Let's look at the finished code && the output one last time!
```python
import random

print("Welcome to my first python project! The Guessing Game!")

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    
    attempts = attempts + 1
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it in {attempts} tries")
        break
```
The Output I got after I played the game:-
```python
PS C:\Program Files\Microsoft VS Code> & C:\Python314\python.exe "c:/Users/code/python/example.py"
Welcome to my first python project! The Guessing Game!
I am thinking of a number between 1 and 100.
Enter your guess: Don't wanna
That is not a valid number. Try again.
Enter your guess: 33
Too low!
Enter your guess: 66
Too low!
Enter your guess: 88
Too high!
Enter your guess: 77
Too low!
Enter your guess: 83
Too high!
Enter your guess: 79
Too low!
Enter your guess: 78
Too low!
Enter your guess: 82
Too high!
Enter your guess: 80
Too low!
Enter your guess: 81
You got it in 10 tries
PS C:\Program Files\Microsoft VS Code>
```
Conclusion:-

Here, I learned about:-

1. What libraries are used for (import library).

2. Variables are assigned the values to store them, and they can always be changed. (Variable = a, Variable = b -> then, the value of the variable is b, at first it was a, now it is b.)

3. While loop (try, except, continue and break)

4. we can include a value inside a print function by adding (f) before the ("") and by making the variable inside the {}.

5. Small basic stuff (like {= is an assignment operator, which assigns the value to a variable}, {int is a function which makes sure the input accepted stays an integer}, and so on..)

That's it. I think...
_________________________________________________________________________________________________________________________
Well, there goes my documentation for the first project! Quite unprofessional I dare say.

But, it was as fun as it was exhausting!

See you in my next project {rock, paper, scissors!}.


_________________________________________________________________________________________________________________________
                                                                Until We Meet Again!!!
_________________________________________________________________________________________________________________________