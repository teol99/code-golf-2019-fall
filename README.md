# VandyApps Code Golf Fall 2019

### Overview
This competition focuses on short and succinct code. 
The challenge is to produce answers to the provided problems with as little code as possible.
Your score for each problem will be the file size of your source code for that problem. Your code will not be run. We will assume that your code runs. We will verify the answers your code produces.
However, we will have the 1st, 2nd, and 3rd place contestants run their code live for proof that
it runs and proof that it produces the correct output. Submission input will be released 10 minutes before the end of the competition; example input is supplied in each problem description.
* **The actual code you submit cannot be generated text**
* Your code cannot call any external processes
* Your code must be able to be run independently of any other personal files (i. e. you can use standard libraries and other modules but you can't write code in another file and simply call it in your submission file)

### Submission
You will need to submit the source code for each question.
Fork this GitHub repository, and just copy and paste your repository link [here](https://forms.gle/96cmbriUCYNLfzwE8)
* Each _solution_ file (your actual code) must be in a directory titled `solutions`
* Generate _answer_ files using your solution. The input files are in the `inputs` directory. Each individual input is separated by a newline. Separate your output in the file by newlines.
* Each _answer_ file (your generated answers) must be in a directory titled `answers`
* Each file must have the problem number somewhere in its name
* You should only submit the files we have asked for and nothing else
* There should be no dots ("." charachters) in your filename except before the extension
* The file size of your file will be evaluated with the python function [os.path.getzise](https://docs.python.org/2/library/os.path.html?highlight=os.path.getsize#os.path.getsize) on an Ubuntu OS. Make sure this is not problematic for your source code.
* **you cannot compress your files** you must submit your raw source code

#### Sample Valid Solution Filenames:
* prob_1.py
* prob1.py
* 1.java
* jibberish1jibberish.cpp

#### Sample Invalid Solution Filenames:
* i_dont_contain_a_number.py
* x.java
* get.ridOfThatExtraDot.cpp
* .filename.java

#### Sample Valid Answer Filenames:
* prob_1_out.txt
* prob1.txt
* 1.txt
* whatever1whatever.txt

#### Sample Invalid Answer Filenames:
* i_dont_contain_a_number.py
* x.txt
* get.ridOfThatExtraDot.cpp
* .filename.txt

## Questions

### 1. ASCII Art
#### Generate the following ASCII art:
```
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
```


### 2. Odious Numbers
#### An odious number is a non-negative number that has an odd number of 1s in its binary expansion. Print all the odious numbers from 0 to 50 inclusive, with each number on a new line.

Example Output: 
```
1
2
4
7
8
...
50
```


### 3. Morse Code
#### Write a decoder for Morse Code messages. Letters are separated by one space and words are separated by two spaces. Only A-Z and 0-9 will be included.

Example Input:
```
.... . .-.. .-.. ---  .-- --- .-. .-.. -..
```

Example Output:
```
HELLO WORLD
```


### 4. Bacon's Cipher
#### Bacon’s Cipher tries to hide a word in another message, using the following encoding (B means a letter is capitalized, and A means it is lowercase) Write a decoder for Bacon's Ciper.

Letter  Encoding:
```
A       AAAAA			B       AAAAB		C       AAABA
D       AAABB			E       AABAA		F       AABAB
G       AABBA			H       AABBB		I       ABAAA
J       ABAAB			K       ABABA		L       ABABB
M       ABBAA			N       ABBAB		O       ABBBA
P       ABBBB			Q       BAAAA		R       BAAAB
S       BAABA			T       BAABB		U       BABAA
V       BABAB			W       BABBA		X       BABBB
Y       BBAAA			Z       BBAAB
```

Example Input:
```
thE QUicK broWn FOx JuMPs OVEr ThE LazY DOgS, gaMbOlINg in TH
```

Example Output:
```
HELLOWORLD
```


### 5. Reversed Numbers
#### Given two numbers, return the maximum of the reverse of those numbers. Numbers may positive or negative, and may have a decimal point.

Example Input:
```
133 978
14.7 81.2
-210 -121
```

Example Output:
```
879
7.41
-012
```