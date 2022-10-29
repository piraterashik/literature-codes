# literature-codes
Analyzes and scores the similarity of text samples.  This statistical tool allows one to identify a particular author or style of writing!

Statistical models of text are one way to quantify how similar one piece of text is to another. Such models were used as evidence that the book The Cuckoo’s Calling was written by J. K. Rowling (using the name Robert Galbraith) in the summer of 2013.

The comparative analysis of Rowling’s works used surprisingly simple techniques to model the author’s style. Possible “style signatures” could include:

-The distribution of word lengths in a document – calculating the frequency of words of length one, length two, length three, etc. This is one of the metrics that was used in the Rowling case.
-The distribution of words used by an author – calculating the frequency of each unique word.
-The distribution of word stems used (e.g., “spam” and “spamming” would have the same stem) by an author – calculating the frequency of each unique stem.
-The distribution of sentence lengths used by an author – calculating the frequency of sentences with one word, two words, three words, etc.

Perhaps the most common application of this kind of feature-based text classification is spam detection and filtering.

Features coded to analyze and compare the statistics of models of text:

-word frequencies
-word-length frequencies
-stem frequencies
-frequencies of different sentence lengths
