# Functions

<!-- 
Note from Charlotte, July 29:
This was adapted from the COMP1631 tutorial. I made a few changes to the wording, and there are probably other things that could be changed. For Q1, I haven't been great about the terminology of "formal parameters" vs "actual parameters", so I changed it to say "function arguments" and "(formal) parameters". Also, Q3 originally said to "draw a picture of memory and show how it changes as the program executes", but this is also not wording that I have used in class.

I had an idea for an alternative activity that I think could be fun, but needs more work to flesh out:
- Get students into ~4 groups
- Each student implements (on the whiteboard) a different function that makes up part of a complete function
- Students call other functions by writing arguments on a piece of paper, then passing it to the next group, who executes their function line by line and passes back the return value

The goal of this activity would be to illustrate:
- When calling a function, you need to know
  - Function name
  - Number and type of arguments
  - Return data type
- When calling a function you do not need to know:
  - Function implementation
  - Parameter names
- When implementing a function you need to decide:
  - Name, number and type of parameters
  - Algorithm to implement
  - What to return
- When implementing a function you do not need to know:
  - The variable names of the arguments passed
  - The variable name assigned to the return value (if any)
-->

1. Identify the following items in the program shown below:

    1. function definition(s)
    2. function implementation(s)
    3. function call(s)
    4. function argument(s)
    5. (formal) parameter(s)
    6. local variables(s)

    ```python
    def test(a: int, b: int, c: int) -> None:
        print(a, b, c)

    def main() -> None:
        a = 1
        b = 2
        c = 3
        test(a, b, c)
        test(b, a, c + 7)

    main()
    ```

2. Fill in the table below with the values of the parameters `a`, `b`, and `c` *inside* the `test` function for each of the two function calls:

    | Call to `test` | `a` | `b` | `c` |
    | -------------- | --- | --- | --- |
    | First call     |     |     |     |
    | Second call    |     |     |     |

3. By hand, trace each of the following programs. Show the intermediate values assigned to each variable in `main` and `display`, then write the program output.
   
   ```python
    def display(a: int, b: int) -> None:
        c = 2 * a + b
        print (a, b, c)
    
    def main() -> None:
        n = 3
        display(5, n)
        display(n, n)
        display(n * n, 12)

    main()
    ```

    ```python        
    def silly(a: int, b: int, c: int) -> int:
        c = a + b
        b = c
        a = 2.0 * a
        d = int(a + b + c)
        print(a, b, c, d)
        return d


    def main() -> None:
        a = 10
        b = 2
        c = 3
        d = 4
        print(a, b, c, d)
        d = silly(b, a, c)
        print(a, b, c, d)

    main()
    ```

4. Design a function to compute the annual rate of inflation. The function is passed two prices for the same item: the price one year ago and the price today. The inflation rate is returned as a floating point number (for example, 0.053 to mean 5.3%).
    
    1. Ensure you understand the problem.
    2. Develop an *algorithm* to solve the problem in pseudocode.
    3. Write the function definition.
    4. Write a short segment of code which illustrates how the function could be used to display the rate of inflation, given that a hot dog cost $0.75 last year and $1.25 today. Write the result to the user as a percentage.

5. By following a similar approach as above, design a function which, given three sides of a triangle $a$ $b$ and $c$, computes the area of the triangle. The area can be calculated using Heron's formula:
    
    $$A = \sqrt{s(s - a)(s - b)(s - c)}$$
    
    where $s$ is the semiperimeter of the triangle:
    
    $$s = \frac{a + b + c}{2}$$