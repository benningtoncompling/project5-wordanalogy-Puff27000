# project5-wordanalogy-Puff27000
project5-wordanalogy-Puff27000 created by GitHub Classroom

Accuracy: Oddly enough, Manhattan Distance seemed to work slightly better for me, with the other two similarity metrics 
(Euclidean Distance and Cosine Distance) tied for second. This is not what I might intuitively have predicted. Because the input was pre-normalized, normalizing didn't do anything, so it didn't change the accuracy. I checked my normalization separately on different input data to make sure it was working properly. I would imagine that on previously un-normalized data, the accuracy would have been higher on the un-normalized version than the normalized version. It seems to me that normalization is necessarily losing some information when it brings all the data points onto the unit circle-- one dimension of similarity is effectively lost, even if another dimension of similarity becomes clearer and easier to measure.
One of the biggest factors lowering my accuracy was duplication of word entries. I imagine that, if I adjusted my program to not look for the eact match words for A,B, or C, that my results might be better.

It's impressive how drastically numpy speeds up the code. I haven't spent much time learning about or prioritizing efficient code, and I don't exactly understand how numpy works, but this is one of only a few occasions that the importance of efficient code has made a significant difference, and it gave me a little insight into how important finding the most efficient way to perform a complex or data-intensive task might be in a professional setting (or a personal one... debugging inefficient code takes forEEVER!). I did like getting to write all my functions before realizing that numpy might be a better choice. It helped me understand the math behind each similarity metric much more clearly than if I had implemented only using built-in numpy shortcuts.

The eval was probably (ironically) the most challenging and stressful part of this project for me, perhaps exacerbated by the fact that scoping in Python isn't the easiest. Most of my challenges in this assignment were whitespace challenges, and the eval step was no exception. 

I learned a new element of debugging: checking file size! It should have been an automatic red flag when my output files, despite ostensibly being almost identical to my input files, wouldn’t upload to GitHub. Again, this was a simple scoping issue, but with literally massive results— megabytes instead of kilobytes of data. A lesson well-learned. 
Some new things I learned:
-How to loop through and navigate directories and full file paths in Python. This is a thing I was scared of/ didn’t know I could do. 
Also, makedir is fun! I don’t think I’ve used that before. 
-Numpy refresher! It was super useful in Database Management Systems, but I forgot what it was and how to use it.
-Actually using similarity metrics: very different to actually do it than to look at it in my notes. I also understand linear algebra better because of this than from learning it in math.
