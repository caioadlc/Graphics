# Hénon Map
A Study about Chaotic Dynamics developed in the classroom on Introduction to Chaos - 4300320, ministerd by PhD Adriane da Silva Reis.

The Henon Map is a two dimensional attractor defined by a recurrence equation
\begin{equation}
    \begin{cases}
    & x_{i+1}=1-a\cdot x_i^2 + y_i \\ 
    & y_{i+1} = b \cdot x_i
    \end{cases}
\end{equation}

We can represent the last equation in the recurrence in two steps

\begin{equation}
    x_{i+1}=1-a\cdot x_{i} + b\cdot y_{i-1}
\end{equation}