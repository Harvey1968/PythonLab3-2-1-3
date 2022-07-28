#3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
secret_number = 777

#Below is an example of multi-line printing. 
#You can use triple quotes to print strings on multiple lines in order to make text easier to read, or create a special text-based design.
print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
                 .
                    .
         /^\       .
    /\   "V" 
   /__\   I        O  o
  //..\\\  I       .
  \].`[/  I
  /l\/j\ (]      .  O
 /. ~~ ,\/I          .
 \\\L__j^\/I         o
  \/--v}  I       o   .
  |    |  I   ____________
  |    |  I c(`          ')o
  |    l  I   \. Python ,/
_/j  L l\_!  _//^------^\\\_ 
""") #Art credit - www.asciiart.eu

#User enters an integer number
user_number = int(input("Enter a number: "))

#While loop continues until the number allocated to the 'secret_number' variable is entered
while user_number != secret_number:
    print('\n"Ha ha! You\'re stuck in my loop!"')
    user_number = int(input("Try again: "))
#User finally escapes the secret number game 
print('\n"', user_number, ' already! Well done muggle! You are free now."\n', sep="")