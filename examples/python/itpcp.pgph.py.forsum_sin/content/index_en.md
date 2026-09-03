[for]: <https://docs.python.org/3/tutorial/controlflow.html#for-statements> "for"

# Sums and Loops

## Introduction

In this task, we learn how to use for loops to calculate a sum over a mathematical series and display it graphically. Specifically, we look at the Taylor series of the sine and build it up step by step to see how the approximation of the sine develops as we add more and more terms of the series.

## Task

Create a Python script `for_sum_sin` that accomplishes the following
tasks:

1. Create a vector $x$ with $100$ points between $-\pi$ and $\pi$
    and an equally sized vector $y$ with all zeros.

2. Create a figure and plot $y(x)$.

3. Now add in a [for] loop from $n=0$ to $n=6$
    a partial sum $s_n$ of the series for the sine
    $$ s_n(x) = (-1)^n \frac{x^{2n+1}}{(2n+1)!} $$
    to the previous value of $y$ and plot $y(x)$ in the same figure.

4. After the loop, also plot $\sin(x)$ in a different color.

## Hints

* In the plot, you should see the line at zero and
    $$
    \begin{aligned}
    S_0 & = s_0 \\
    S_1 & = s_0 + s_1 \\
    S_2 & = s_0 + s_1 + s_2 \\
        & \vdots
    \end{aligned}
    $$
    Eventually, $S_n(x)$ approaches the sine.

* You will learn other methods to calculate series in a later exercise.
 Here, the goal is only to understand how this is accomplished using a
 [for] loop.
