# Sort Algorithms
Functional code of various sort algorithms, written in Python 3. No special modules are used, thus the code should work out of the box.

#### Organization
Each sort algorithm is saved as a separate file, and each of them are invoked via the main.py file. Additionally, a collection of the utility functions used by more than one sort routine is stored in the `common.py` file.
```buildoutcfg
<algorithm>_sort.py      the sort algorithm
common.py                utilities invoked in more than one algorithm.```
main.py                  the master control file
```

## How to Use
```buildoutcfg
python3 main.py [-d | --descending] [-v | --verbose]
```
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

<table>
<tr>
<td> Algorithm </td>
<td> Description </td>
<td> Time Complexity </td>
<td> Space Complexity </td>
</tr>

<tr>
<td> Bubble Sort </td>
<td> Repeatedly sort adjacent elements, to "bubble" the highest number to the end of the list. </td>
<td> O(n**2) </td>
<td> O(1) </td>
</tr>

<tr>
<td> Counting Sort </td>
<td> Use the count of the occurances of the objects, and stores them in distinct keys. Not meaningful if k >> n </td>
<td> O(n + k) </td>
<td> O(n + k) </td>
</tr>

<tr>
<td> Heap Sort </td>
<td> Using the heap data structure, push the smallest number to the root node.</td>
<td> O(n log(n)) </td>
<td> O(n) </td>
</tr>

<tr>
<td> Insertion Sort </td>
<td> The famed card sorting algorithm. Pick a card at a time, and insert the new card at the appropriate slot. </td>
<td> O(n**2) </td>
<td> O(n) </td>
</tr>

<tr>
<td> Merge Sort </td>
<td> Divide and Conquer technique, to divide lists repeadly into sublists, and then merge them to create a sorted list.  </td>
<td> O(n log(n)) </td>
<td> O(n) </td>
</tr>

<tr>
<td> Quick Sort </td>
<td> Aka the partition-exchange sort.  Partition list against a 'pivot'. One side contains numbers that are lower, while the other contains larger numbers.</td>
<td> O(n**2) ... avg: O(n log(n)) </td>
<td> O(log(n)) </td>
</tr>

<tr>
<td> Radix Sort </td>
<td> Generating keys based on the significant position and value of the digits in a number. </td>
<td> O(n k) </td>
<td> O(n + k) </td>
</tr>

<tr>
<td> Selection Sort </td>
<td> Select the smallest number in a list, and move to a sorted list. </td>
<td> O(n**2) </td>
<td> O(1) </td>
</tr>

</table>
