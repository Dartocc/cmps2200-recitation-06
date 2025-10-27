# CMPS 2200 Recitation 06
## Answers

**Name:**___Darian Tocci______________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
  The recurrence for the work of the recursive algorithm is W(n)=W(n−1)+W(n−2)+O(1)
every call made to fib_recursive(n) makes two recursive calls ,n-1 and n-2, and performs constant additional work.
Solving the reccurence equals W(n)=O(2^n). So the total work grows exponentially with n.

- **3)**
  For the span, only one of the recursive calls can be done in parallel, so S(n)=S(n−1)+O(1). Solving this recurrence equals S(n)=O(n) So we can see that even though the work is exponential, the span is only linear.

- **4)**
  When we look at the counts list after computing fib_recursive(n), we see that the number of times each F_i is computed follows the Fibonacci pattern itself. Specifically, counts[i] equals F_{n−i+1}.
This means smaller Fibonacci numbers are computed many more times than larger ones which shows us a clear sign of repeated work.

- **6)**
  Each Fibonacci number F_i is computed once, since results are stored in the fibs list. W(n)=O(n) Each call depends on the result of the previous ones ,recursive chain depth n,  S(n)=O(n). So the top-down (memoized) version has linear work and linear span.

- **8)**
In the bottom-up version, each Fibonacci number F_i is only computed once and read a constant number of times in order to calculate the next term. W(n)=O(n). Since this version is iterative and all steps are sequential with no recursio , the span is constant S(n)=O(1) So, fib_bottom_up is the most efficient, with linear work and constant span.
