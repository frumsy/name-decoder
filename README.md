# name-decoder
Python version of couple-name-decoder

This is a neural net that, when given two names mashed together and a database of names, returns the two original names.

Base training set:
The names are randomly mashed together. Specifically, the first name is randomly truncated from the right, and the second name is randomly truncated from the left. They are then concatenated.

Vowel training set:
The names are concatenated along a vowel.



Files:

decoder.py:
-loads dataset
-converts strings to number vectors
-loads dataset into numpy arrays:
 >year
 >name
 >gender
 >frequency
   
NN.py:
 -creates the NN with Keras
 -trains it on our data
