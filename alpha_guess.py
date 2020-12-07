# On second thought, I don't think I can make this. I'll try though.

alphabet = (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T ,U, V, W, X, Y, Z)
guess_count = 0
guess_limit = 5


def rand_letter():
  randindex = randint(1, 26)
  letter = alphabet[letter - 1]
  return letter

answer = rand_letter()
answer_index = alphabet.index[answer]

try:
	while guess_count < guess_limit:
	       guess = input("Enter a letter: ")
	       guess_count += 1
	       guess_index = alphabet.index[guess.upper]
	if guess.upper == answer:
           print("You got it in " + guess_count + "! Amazing!")
           guessed = True
           break
   elif guess_index > answer_index:
           print("No, no. It came earlier in the alphabet.")
           print("You have " + (guess_limit - guess_count) + " guess(es) remaining.")
   else:
           print("No, no. It came later in the alphabet.")
           print("You have " + (guess_limit - guess_count) + " guess(es) remaining.")
except IndexError:
           print("Come on. Don't be such a killjoy and properly play this game!")

if guessed:
	print("Congratulations! You won the game.")
else:
    print("You lost.")

# Ohh, I did make it! I'll just try and see if there are errors here....
