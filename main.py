myFavLang = 'C++'
guess = ''
guess_count=0
guess_limit=5
out_of_guess=False
while guess!=myFavLang and not out_of_guess:
    if guess_count<guess_limit:
        guess=input('Guess my favorite programming language= ')
        guess_count+=1
    else:
        out_of_guess=True
if out_of_guess:
    print('You Lose! You were out of guesses.')
else:
    print('YOU WIN!')