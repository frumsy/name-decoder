# name-decoder
Python version of couple-name-decoder

This is a neural net that, when given two names mashed together and a database of names, returns the two original names.

Base training set:
The names are randomly mashed together. Specifically, the first name is randomly truncated from the right, and the second name is randomly truncated from the left. They are then concatenated.

Vowel training set:
The names are concatenated along a vowel.

stoint():
 -converts a string to an integer
 -
 


NN:
feed forward convolutional NN
input:
-age1
-age2
-gender1
 >0/1
-gender2
 >0/1
-mashedname
 >toint(mashedname)

Hidden layer:
 -dense
 -4 nodes

output:
-index1
-index2

errfunction:
111      .5 * .5
110      .9 * .5
101      .8 * .5
100      .3 * .5

Files:

decoder.py:
-loads dataset
-converts strings to number vectors
-loads dataset into numpy arrays:
 >year
 >name
 >gender
 >frequency


