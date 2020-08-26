# Quizz
This script turns a text file containing a list of questions (and answers) into an interactive quizz.  

## Format of the question file
The file comprises of several question-answers blocks separated by two newlines. Each block contains the question on the first line and up to 26 answers to choose from, each on its separate line. The first character of each answer line ought to be `+` encoding that the answer is correct, or `-` meaning it's not. Multiple (or none) answers can be correct.  
Example 2 question quizz
```
Question
+ Correct answer.
- Incorrect answer.

Which statement(s) are true?
+ 1 < 2
- Sqrt(2) is rational
+ The set of primes is infinite.
- 2^(2^m) is always prime
```

## Using the quizz
The easiest way to use the quizz is to write the question to a file `data.txt` and call `quizz = Quizz.from_file("data.txt")` followed by `quizz.run()`.
Optionally, one can also shuffle the order of questions and answers by calling `quizz.shuffle()` before running it.  
When multiple answers are correct each must be given in order to get a point. If no answer is correct, empty string or `-` can be provided. Lower as well as upper case is accepted and order of letters doesn't matter.