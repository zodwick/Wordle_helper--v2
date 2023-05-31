


<h1 align="center"> Wordle_helper--v2</h1>

This program is a solver for the game Wordle. It takes input parameters representing the greyed-out, yellowed-out, and greened-out letters in the word and provides suggestions for the next word guess.

## Functioning
The program will prompt you to enter the letters in the order they appear in the wordle and the colors in the order they appear.
Use:

- "g" for grey
- "y" for yellow 
- "r" for green.


<h1 align="center">
  
   <img src="https://github.com/zodwick/Wordle_helper--v2/blob/main/screenshots/cli.png" alt="Markdownify" >
<br>
<br>

  <img src="https://github.com/zodwick/Wordle_helper--v2/blob/main/screenshots/wordle_ss.png" alt="Markdownify" >
  <br>
  
</h1>


The program will then provide suggestions for the next word guess based on the given parameters. It uses various filtering algorithms to narrow down the word list and find potential matches.

## How To Use

Make sure you have Python installed on your system.
- Open a terminal or command prompt.
- Navigate to the directory where the code file (wordle_solver.py) is located.
- Run the following command

   ```bash
   python wordle_solver.py
   ```

## Inbuilt functions
The Wordle Solver program includes the following functions:
- containsAll(str, set): Checks if a string contains all the elements in a given set.
- containsAny(str, set): Checks if a string contains any of the elements in a given set.
- pos_check(word, set): Checks if the letters in a word are in the correct positions based on a given set of positions and letters.
- check_individual(word, set): Checks if a specific letter in a word is in the correct position based on a given set of position and letter.
- load(): Loads the word list from a file.
- input_params(grey, yellow, green): Takes user input for the greyed-out, yellowed-out, and greened-out letters and returns the processed parameters.
- find_prime_suggestions(word_list, sorted_letters): Finds prime suggestions for the next word guess based on the given word list and sorted letters.
- suggestions(list): Provides suggestions for the next word guess based on the given list of words.
- suggestions_for_max_info(list, letters): Filters out words that contain letters from the first try and returns suggestions for maximum information.











