# CMPS 2200 Assignment 3
## Answers

**Name:** Daron Lebaredian


Place all written answers from `assignment-03.md` here for easier grading.

1a)

Using a greedy algorithm, you can create an algorithm with a greedy criteron of always using the largest coin domination that is not larger than the remaining N value in dollars, and not in Geometrica currency yet. Also make sure to substact the coin domination's value you pick from the N value each time you pick a coin.

1b)

Given a dollar value N $\in \mathbb{R}$ the largest coin with value g, or coin g, such that g = 2^{i} where i $\in \mathbb{Z}$ and is smaller than N, will be in some optimal solution. By definition of g:

$g \leq N < 2g$

Let's assume there optimial solution O with with the lowest number of that doesn't include coin g. Since the optimial solution doesn't include g, all of the coins', in said solution, values' sum C $\in \mathbb{R}$ must combine must be lower than g, or $2^{i}$, otherwise C > N which would not make O the optimial solution. However since $N \geq g$ the optimal solution O much include some more coins to equal value N. But then this would mean O is not the optimial solution as using smaller valued coin will be less optimal than just using coin g. Therefore coin g much be in the Optimial solution O.

