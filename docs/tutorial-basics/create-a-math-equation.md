# Math equations
Mathematical equations can be rendered using KaTeX.

Let $f\colon[a,b]\to\R$ be Riemann integrable. Let $F\colon[a,b]\to\R$ be
$F(x)=\int_{a}^{x} f(t)\,dt$. Then $F$ is continuous, and at all $x$ such that
$f$ is continuous at $x$, $F$ is differentiable at $x$ with $F'(x)=f(x)$.

$$
I = \int_0^{2\pi} \sin(x)\,dx \tag{1}
$$


$$
f(x) = \int_{-\infty}^\infty
    \hat f(\xi)\,e^{2 \pi i \xi x}
    \,d\xi
$$


### Math notation

Math expressions can be added using the [KaTeX notation](https://khan.github.io/KaTeX/). To add an inline equation, wrap the expression in `$EXPRESSION$`, eg. `$\sqrt{3x-1}+(1+x)^2$`. $\sqrt{3x-1}+(1+x)^2$ To create an expression block, wrap it as follow:

	$$
	EXPRESSION
	$$

For example:

	$$
	f(x) = \int_{-\infty}^\infty
		\hat f(\xi)\,e^{2 \pi i \xi x}
		\,d\xi
	$$

Here is an example with the Markdown and rendered result side by side:


