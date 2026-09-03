# Calculation of $\pi$ According to the Method of *Archimedes of Syracuse*

## Introduction
Archimedes (287-212 BC), probably one of the most important mathematicians and physicists of antiquity, was concerned not only with the lever laws or buoyancy, for which he became famous, but also with the approximation of $\pi$. It had been known long before him that the unit circle could be approximated by inscribing and circumscribing regular polygons. However, his idea was to narrow down $\pi$ through a transition from a regular $n$-gon to a $2n$-gon.

Through geometric considerations, he found that the circumference $U_{2n}$ of the outer $2n$-gon is given by the harmonic mean of $U_n$ and $u_n$ (circumference of the outer and inner $n$-gon respectively), i.e.
$$U_{2n}=\frac{2 \cdot U_n \cdot u_n}{U_n + u_n}$$

The circumference $u_{2n}$ of the inscribed $2n$-gon results from the geometric mean of the circumference $U_{2n}$ of the outer $2n$-gon and the circumference $u_n$ of the inner $n$-gon:
$$u_{2n}=\sqrt{U_{2n} \cdot u_n}$$

<div align="center">
<img src="mediaFiles/archimedes.png" alt="Test Image" width="90%" name="Archimedes"/>
</div>

<br>

Archimedes began the approximation of $\pi$ with the regular hexagon inscribed in the unit circle. The special thing about the regular hexagon is that

* the inner circumference $u_6=6$ and
* the outer circumference $U_6=4\sqrt{3}$

as can easily be verified.

Archimedes managed to calculate up to the regular 96-gon using this method by approximating the square root with suitable fractions and was thus able to narrow down $\pi$ to
$$3\frac{10}{71} < \pi < 3\frac{1}{7}$$

## Task

Complete the following tasks:

1. Define the variable `N=20` and initialize variables `ua` and `ui` as row vectors of length `N`, which should later contain the approximations for $\pi$.

2. Now implement Archimedes' algorithm, starting from the regular hexagon and executing a total of `N` steps. Store at the `i`-th position of variable `ua` the approximation using the outer $n$-gon in the `i`-th step. The values of the inner $n$-gons should be stored in variable `ui`. Note that you must halve the circumference ($ U = 2 r \pi$, $r=1$) for the $\pi$ approximation, i.e., for example `ui[0] = 3`.

3. Form the arithmetic mean of the values of the outer and inner $n$-gons for each step and store them in variable `m`.

4. Output the value of the last outer and inner $n$-gon, their mean, and the numerical value of $\pi$ with thirteen decimal places each as follows:    
        `Outer:`&nbsp;&nbsp;`"respective value of the approximation"`     
        `Inner:`&nbsp;&nbsp;&nbsp;&nbsp;`"respective value of the approximation"`     
        `Middle:`&nbsp;&nbsp;`"respective value of the approximation"`     
        `Pi:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"respective value of the approximation"`     

5. Create two plots stacked vertically (with subplot). In the first, show how `ui`, `ua`, and `m` converge to $\pi$. The second plot should be semi-logarithmic showing the absolute difference in each case.

6. Add appropriate labels.

## Hints

* Reference plot:

<div align="center">
<img src="mediaFiles/plot.png" alt="Test Image" width="100%" name="Plot"/>
</div>
