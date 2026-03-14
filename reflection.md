# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

  Summary:-------------------------------------------------------------------------------
    Refactor game logic and fix bugs: 
    - Moved check_guess function to logic_utils.py and updated its logic.
    - Corrected hint messages for high/low guesses.
    - Implemented new game logic to reset history and attempts.
    - Added regression tests to ensure hints are accurate and game resets function correctly.
  --------------------------------------------------------------------------------------

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  --------------------------------------------------------------------------------------

Bug 1: The hints were backward. When I entered a number greater than the secret number, the hint said "enter a higher number". When I entered a number lower than the secret number, the hint said "enter a lower number". 

Bug 2: After I guessed the number correctly, when I click on "New game", it gives me a new secret number. However, it stays at the same output of "You won" when I enter a new guess. It doesn't reset the history and number of attempts.

Bug 3: The number of attempts for the easy level is smaller than that for the normal level. Easy level is supposed to give us more attempts to guess.

Bug 4: Before the game begins, the user didn't make any guesses yet. But, the number of attempts allowed on the left panel doesn't match what it says at the top of the game. It is supposed to show the same value.
    Ex) for easy level: left panel => 6 but to user, it says 5. 

    --------------------------------------------------------------------------------------

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

-----------------------------------------------------------------------------------------
- Used Copilot
- Correct: 
    I used Copilot in Agent Mode to help me fix the check_guess function. I used the following prompt: "Move the check_guess function to logic_utils.py, update the logic to fix the high/low bug, and update the import in app.py. Add a comment next to where you made the Import". Then, it asked me to keep/undo the changes it made. 
    
    They were all correct, so I kept them. I also asked it to generate a specific pytest case in test/test_game_logic.py that specifically targets the bug that was just fixed. I ran the test case in the terminal and also ran the game. Both ran correctly.

- Incorrect:
    I used Copilot in Agent Mode to help me fix the new game logic. I used the following prompt: "#codebase FIXME: Logic breaks here #Handle new game logic - the secret is generated but the history and attempts are not reset. Add comment next to where you fixed it."
    
    Something it did wrong was that it added code to generate the new secret from the current difficulty range instead of always using 1 to 100. I still wanted it to make the secret between 1 and 100. Also, it didn't change the value for the number of attempts. The number of attempts should be reset. 
    
    So, I entered another prompt: "I still want the new secret number to be between 1 and 100. Reset the num of attempts to be equal to those under each difficulty level depending on which one the user selects."
    Now, the code successfully worked after I validated all the changes AI made.

--------------------------------------------------------------------------------------

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--------------------------------------------------------------------------------------
  1. I asked Copilot to generate a specific test case in the test_game_logic.py to make sure the bug was actually fixed. When I tested it in the terminal, all test cases ran correctly.
  2. I used pytest (ran it in the terminal) and also tested it manually by going through each line of code to understand what was happening.
  3. Yes, AI helped me to design test cases for both cases. But I verified that they were correct and actually checking the logic.

--------------------------------------------------------------------------------------

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--------------------------------------------------------------------------------------
  Basically, whenever we enter streamlit run fileName.py in the terminal, it erases all the previous history of the game and reads the file from the start to end and displays an app version of the current python file.
  So, it resets the file and updates the app version so that the user can play the game based on the current updates.
--------------------------------------------------------------------------------------

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--------------------------------------------------------------------------------------

I always used to validate the AI generated code thinking that AI would be correct. However in this assignment, I understood that AI can and might make mistakes. So, it is important that we verify those changes. I also liked the Generate Commit Message of the Git. It will be useful to look back at if I forget what I did.
One strategy I want to reuse in future labs/projects is having AI generate test cases, adding comments (like FIXME and FIX) and also the Generating a commit message for Git.

--------------------------------------------------------------------------------------