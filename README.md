# Sort Algorithms
Functional code of various sort algorithms, written in Python 3. No special modules are used, thus the code should work out of the box.

Each  
## How to Use
Each sort function takes a standard set of optional arguments
```buildoutcfg
  -h, --help        show this help message and exit
  -v, --verbose     activate verbose print statements
  -d, --descending  sort in descending order
```


For the worst-case scenario, use a fully sorted list, and then sort it in the reverse order.
- E.g. `bubble_sort(bubble_sort(A), True, False)`
- The inner `bubble_sort(A)` routine uses the defaut values for `verbose` and `asc`. Which is False, and True
- Thus, the list will get sorted in the ascending order.
- You can use that output, and feed as the input to the outer sort function, asking it to provide `verbose` output and sort in the `descending` order
- Of course, you can mix and match algorithms too.
## Executive Summary

* Bubble Sort
* Count Sort
* Heap Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Radix Sort
* Selection Sort
