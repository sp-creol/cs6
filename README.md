# cs6
Problem Set for MIT Opencourse cs 6.0001
[Course webpage](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/lecture-slides-code/)
## course directory
- */ps0*: Problem Set 0: *pkgtest.py*,...
- */ps1*: Problem Set 1: *ps1a.py*, *ps1b.py*, *ps1c.py*
- */ps2*: Problem Set 2: *hangman.py*
- */ps3*: Problem Set 3: *ps3.py*
- */ps4*: Problem Set 4: *ps4a.py*, *ps4b.py*, *ps4c.py*

## Problem Set 0
Variables x and y receive input from the user with input(). To make the input into ints that can be used for mathematical operations, input() is surrounded by int() to cast the input to ints. Then, the results of x^y and log base 2 of x are printed out, with the latter using numpy's log2() function.

## Problem Set 1
A) The variables portion_down_payment, current_savings, and r are given set values as floats. The variables annual_salary, portion_saved, and total_cost ask for user input and convert the inputs to floats. The months variable is set to 0, and it counts how many times the loop runs. The loop is a while loop that goes until the savings have reached or surpassed the cost of the down payment, or portion_down_payment * total_cost. Every iteration, the current savings first multiplies by 1 plus a twelfth of the annual rate (for the monthly rate), and then it adds the portion of the monthly salary that is saved, given by portion_saved * (annual_salary/12). After the loop completes, the number of months is printed out.
![ps1a](https://user-images.githubusercontent.com/107879635/175646674-446478a6-4e25-4ca2-b2c3-5f0a59cc905b.png)

B) The code now considers an additional float variable given by user input called semi_annual_raise. Inside the loop, an addition is made after current_savings is manipulated, which checks if the current month is a multiple of 6 using months % 6 == 0. If it is a multiple of 6, the annual salary multiplies by 1 plus the semi-annual raise rate.
![ps1b](https://user-images.githubusercontent.com/107879635/175647386-482ae50f-b85d-4a9f-bc9b-dbb23a993fd4.png)

C) Now, the variables semi_annual_raise, r, portion_down_payment, and total_cost are given set values, and only the original salary requires user input. The code uses a bisection search between low value 0 and high value 10000 to find the best value for portion_saved. A while True loop performs iterations of each guess for portion_saved, and break statements within the loop will terminate the code once a result is reached. The number of iterations is counted with the steps variable. Every iteration, a guess is made using the middle value between the low and high value made as an integer. The code from Part B is then used to test how the guess for portion_saved plays out. One change is that instead of going until the savings reach the down payment cost, the loop goes until 36 months have passed. Then, the difference between the savings and the down payment is calculated. If the absolute value of this difference is below 100, then it is close enough, and the current guess is printed out as the best savings rate, and the number of steps the sort took is printed as well. Otherwise, if the difference is negative and the savings ended up lower than the down payment cost, the low value is set to the current guess. If the diffrerence is positive, the high value is set to the current guess. Then, the sorting loop runs again with new low and high values, and it continues until a guess is reached that is close enough. To account for situations where the down payment will never be reached even at the highest possible rate, the code checks if the guess has reached 9999 or higher (a 100% rate) and stops the code there, printing out that it is not possible to pay the down payment. 9999 was chosen because integers were used for the low and high values, and the guess would always round down to 9999 instead of fully reaching 10000.
![ps1c](https://user-images.githubusercontent.com/107879635/175651444-8e31a7df-be93-4f4c-b7fe-966d368abbbd.png)

## Problem Set 2
1A) For the is_word_guessed function, a for loop iterates over the length of the secret word to look through each individual character. If the character is not found in the list of letters guessed, the function ends and returns False. If the loop completes without any character missing from the list of letters guessed, the function returns True.

1B) For the get_guessed_word function, an empty string variable named result is created. A for loop runs through all the characters in the secret word and sees if they are in the letters guessed. If they have been guessed, the character is added to the end of the result string. Otherwise, "_ " is added. After the loop ends, the final result variable is returned.

1C) For the get_available_letters function, all lowercase letters are put into variable allLetters using string.ascii_lowercase, and an empty string variable named letters is created. A for loop iterates through all the characters in allLetters and looks to see if they have been guessed yet. If a letter has not been guessed, it is added to the end of the letters variable. After the loop is complete, the function returns the letters variable.

2\) The hangman function takes in a string to be the secret word, and while working on it, I called the function with a placeholder word. After I was done, I used randomly selected words. The variable guesses is set to 6 and keeps track of how many guesses the player has left. The list letters_guessed is set up as an empty list. The program tells the player how many letters are in the word using len(secret_word). A while loop runs iterations for every round that passes, and ends when there are zero guesses left. At the start of a round, the program says how many guesses are left and prints out available letters using get_available_letters(letters_guessed). The program then asks for a letter to guess. Variable strikes is set to 3. If the guess is not in the alphabet, has a length that isn't 1, or is already in letters_guessed, strikes goes down by 1 and a warning is given. Once strikes hits 0, the program stops asking again and takes away a guess from the player. If a proper guess is made, the program moves onto the next step and adds the guess to letters_guessed. If the guess is not found in the secret word, it checks if the guess is either a, e, i, o, or u. If the guess is a vowel, 2 guesses are removed; otherwise, 1 is removed. The program tells the player if they guessed right and shows how much of the word has been guessed using get_guessed_word(secret_word,letters_guessed). After each round, the code tests whether the word has been fully guessed using is_word_guessed(secret_word,letters_guessed). If so, the program congratulates the player, calculates the score, and ends. The score is found by creating a list for unique letters and running through each letter in the word. If a letter is not yet in the list, it is added. The score is found by multiplying the number of guesses left by the length of the list. If the player runs out of guesses, the program ends and lets the player know what the word was.
![ps22](https://user-images.githubusercontent.com/107879635/175657865-848eefa2-cbb6-4ebd-a8f1-8f0154f9a04e.png)

3A) For the match_with_gaps function, empty string word is created, and a for loop iterates through each character in my_word. Any character that isn't a space is added to the end of word, creating a string with no spaces. The code checks whether the length of the word matches the length of other_word, and returns False if it doesn't. Then, for every character in word, if it is not an underscore, it is compared to the character at its same location in other_word. If any letter does not match, False is returned. If all letters match, True is returned. The code also checks to make sure a match is not given if an underscored letter has already appeared in the word. If it has already appeared, False is returned.

3B) For the show_possible_matches function, empty string possible_matches is created. The code iterates through every word in wordlist, and calls match_with_gaps() to see if the word matches the inputted word my_word. If it matches, the word is added to the end of possible_matches. After running through all words, if the length of the string created is 0, "No matches found" is printed. Otherwise, the string possible_matches is printed.

3C) The hangman_with_hints function is almost identical to the hangman function, but a new condition is added where the program asks for a letter. If the guess is \*, show_possible_matches(get_guessed_word(secret_word,letters_guessed)) is called to find matching words for the currently guessed letters. \* counts as a valid guess character, so the code moves on to the next round.
![ps23](https://user-images.githubusercontent.com/107879635/175660684-403749d1-2d09-4e1d-8b4c-7c899bd1cb55.png)

## Problem Set 3
1\) The get_word_score function creates variables componentA and componentB for the two parts of the final score. componentA iterates through each letter in the word and adds its corresponding value in the SCRABBLE_LETTER_VALUES list to get a sum of all the letters' scores. componentB uses the expression 7 * len(word) - 3 * (n - len(word)), as given by the problem. If 1 is greater than that value, componentB becomes 1 instead. The product of componentA and componentB is returned.

2\) The update_hand function creates a copy of the hand in a new dictionary called newHand. The code iterates through each letter in the word, making each letter lowercase with str.lower(), and looks for the letter in newHand. If it finds the letter, the number value associated with the letter goes down by 1. If the value gets to 0, the letter is removed from the dictionary entirely. This removes all letters that are used and are in the hand, regardless of whether a valid word is made. At the end, newHand is returned.

3\) The is_valid_word function (without considering changes made to account for wild cards) checks if the given word is inside the valid word list, and if it's not, it returns False. Otherwise, it moves onto a modified version of the code from update_hand, which creates a newHand copy of the hand and takes away letters from the word. Here, if it is ever unable to find a letter in newHand, it returns False, as the hand does not have all the letters to form the word. If it gets through the word and finds every letter in the hand, it returns True; it is a valid word to use.

4\) To account for wild cards, deal_hand needed to give a special * vowel instead of one of its normal vowels. To do this, I added code inside the loop to add vowels which checks if i == num_vowels - 1 and adds * to the hand with a value of 1 in that one case. For all other i values, a normal vowel would be added. This makes it so that the last vowel to be added is always a \*. Inside is_valid_word, a new piece of code runs if there is a * inside the word, replacing the simple check for if the word is in the word list. The code iterates through each vowel in VOWELS and puts it in the place of the * in the word by slicing the word into the slice before the * is found and the slice after the * is found, and then placing the vowel in the middle. If this new word is found inside the word list, the word can pass as a valid word before moving onto checking whether the hand has the letters for the word. If after going through all the vowels, no viable word is found, it returns False. The last change was adding '\*': 0 to SCRABBLE_LETTER_VALUES, to declare * as a zero-point letter.
![ps34](https://user-images.githubusercontent.com/107879635/175832458-556878c1-ea42-46f8-a19d-14ecdecf49be.png)

5\) The play_hand function follows the pseudocode closely. A score variable is initially set to 0, and a while loop goes until calculate_handlen(hand) returns 0, for no more letters in the hand. The program displays the current hand using display_hand(), and then asks for a word. If !! is entered, the program breaks out of the while loop and stops early. Otherwise, is_valid_word() checks if the word is valid, and if so, the points from the word are calculated with get_word_score and added to the total score. If the word is invalid, the program states that the word is invalid. Regardless of whether the word was valid, the hand is updated to take away whatever letters were used. After the while loop is finished, the code checks whether the game ended by running out of letters by seeing if calculate_handlen(hand) returns 0, and if so, it prints that the player ran out of letters. Finally, the program prints the player's total score and returns the score.
![ps35](https://user-images.githubusercontent.com/107879635/175832459-0feb43b5-9cfa-4954-bf52-bfbe4ed904f0.png)

6\) The substitute_hand function creates a copy of hand in newHand, and then sees if the inputted letter is inside the hand. If so, the letter is removed from newHand. Then, a string of all letters called allChoices is made from concatenating VOWELS and CONSONANTS. The code iterates through all the letters in the original hand and removes the letters from allChoices so that they can't be chosen for the new letter. After this, random.choice(allChoices) picks a random letter from the remaining possible choices and adds it to newHand with a value of the difference between the original hand length and the length after the old letter was removed. Finally, newHand is returned. The play_game function asks the player for how many total hands will be played and sets it to variable numHands. It sets up totalScore as 0 and substituteAvailable and replayAvailable as True. For each hand, a hand is dealt with deal_hand(HAND_SIZE) and displayed with display_hand(hand). If substituteAvailable is True, the program asks the player if they'd like to susbtitute a letter. If they answer "yes", substituteAvailable is set to False and substitute_hand() is used to change a letter based on the player's input. Variable score1 is set to the result of play_hand(), which plays with the hand the player has. If replayAvailable is True, the program asks if the player would like to replay the last hand. If they answer "yes", replayAvailable is set to False and another hand is played, this time with the score set to variable score2. After the hand is finished, the code checks whether score1 or score2 is larger, and adds the larger score of the two to the total score. After all the hands are played, the total score is printed for the player.
![ps36](https://user-images.githubusercontent.com/107879635/175832464-a81bd99a-fc9f-4340-9b25-c20f66596d18.png)

## Problem Set 4
A) The get_permutations function calls itself to perform recursion. I followed the suggested approach in the problem set, so the base case occurs when the length of the sequence input is 1. The recursive case creates a list called thisPerms to store all of its possible permutations. The code calls get_permutations on the characters in the sequence without the first letter. For each permutation, the first letter is placed in all possible places; for example, permutation BC will have ABC, BAC, and BCA added to thisPerms. To avoid duplicates, a new list called uniquePerms is created, and every permutation in thisPerms is checked to see if it is already added; if not, it is added to uniquePerms. uniquePerms is then returned. For the base case of a length of 1, the single letter in the sequence is returned. This gets all possible permutations for any length of the original sequence.
![ps4a](https://user-images.githubusercontent.com/107879635/176041176-8e753be5-9ae2-4469-9c42-1d1487c1382a.png)


B1) In the Message class, the \_\_init__ function sets self.message_text to the input for text and sets self.valid_words to all valid words from load_words(WORDLIST_FILENAME). get_message_text simply returns self.message_text, and get_valid_words returns a copy of the valid words list using self.valid_words\[:]. build_shift_dict starts by creating an empty dictionary named dict and creating variables lowercase and uppercase for string.ascii_lowercase and string.ascii_uppercase. For numbers 0 through the length of lowercase (26, for the letters in the alphabet), the dictionary is given keys for the lowercase and uppercase letters matching the number. These keys are given the value of the letter that is a certain distance away using lowercase\[(i+shift) % len(lowercase)] or uppercase\[(i+shift) % len(uppercase)]. The modulo makes it so that if i + shift ends up being a number beyond the alphabet like 30, it will loop back around to the start of the alphabet, so 30 would become 4. After all keys and values are added, the dictionary is returned with all the values that letters will shift to in the encryption. The function apply_shift calls on self.build_shift_dict to get the letters to change to, and it creates empty string newString. For every letter in the message, accessed with self.message_text, the code checks whether the dictionary has a key for it. If so, the value associated with the key is added to newString. If not, the original letter is added. This creates the encrypted string, which is then returned.

B2) In the PlaintextMessage class, the \_\_init__ function calls on the \_\_init__ function from the parent Message class first to set self.message_text and self.valid_words. Then, the new instance variables are set: self.shift is set to shift, self.encryption_dict uses build_shift_dict from the Message class, and self.message_text_encrypted uses apply_shift from the Message class. get_shift returns self.shift, get_encryption_dict returns a copy of self.encryption_dict using .copy(), and get_message_text_encrypted returns self.message_text_encrypted. change_shift calls on the \_\_init__ function using the existing self.message_text value and the new shift value to change the shift value and everything else that will be affected as a result.

B3) In the CiphertextMessage class, \_\_init__ simply calls on the Message class's \_\_init__ function to initialize self.message_text and self.valid_words. The decrypt_message function sets up variables bestMessage, bestScore, and bestShift, as it will use these to keep track of the best decryption it makes. It iterates through all numbers from 0 to 25 with the variable s, and shifts the letters of the message using self.apply_shift(s). Then, wordsList is created by splitting up the message into all its individual words using str.split(). For every word in wordsList that is a valid word according to is_word(), variable score increases by 1. After the score, or number of valid words, is found, it is compared to bestScore. If it is higher than the best score so far, bestScore is set to the new score, bestMessage is set to the message that has the best score, and bestShift is set to the value of s. After going through every shift, the final values of bestShift and bestMessage are returned.

B4)
![ps4b](https://user-images.githubusercontent.com/107879635/176041327-b2f6d586-e194-47a1-9aca-fdd967eb6813.png)

C1) In the SubMessage class, \_\_init__ sets self.message_text to text and self.valid_words to the result of load_words(WORDLIST_FILENAME). get_message_text returns self.message_text, and get_valid_words returns a copy of self.valid_words. build_transpose_dict starts with empty dictionary dict, and for each letter in VOWELS_LOWER and VOWELS_UPPER, the letter is added as a key to dict and its value is set to the corresponding letter in vowels_permutation. For each consonant in CONSONANTS_LOWER and CONSONANTS_UPPER, the key and value are both set to the letter, because they won't change from the encryption. After this, the dictionary is returned. apply_transpose iterates through all the letters in self.message_text, and checks to see if it has a key in a dictionary made by build_transpose_dict. If so, the corresponding value in the dictionary is added to string encrypted. Otherwise, the letter is simply added to encrypted. Finally, encrypted is returned, with all applicable letters transposed.

C2) In the EncryptedSubMessage class, \_\_init__ just calls SubMessage's \_\_init__ function. decrypt_message calls on get_permutations(VOWELS_LOWER) to get all possible ways the vowels can be arranged for encryption. A similar system from CiphertextMessage's decrypt_message function is used to test what decryption results in the best "score", or number of valid words. Here, bestMessage starts off as self.message_text, so that if no message gets a score above 0, the original message is returned. Only bestMessage is returned after this function completes.

C3)
![ps4c](https://user-images.githubusercontent.com/107879635/176043583-701954d9-f866-4069-98eb-d6785761b272.png)
