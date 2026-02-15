\# MSCS 532 – Assignment 4  

\## Heap Data Structures: Implementation, Analysis, and Applications



\### Author:

Anushka Nanaware  

MSCS 532 – Algorithms and Data Structures



---



\## Overview



This project implements and analyzes Heap Data Structures, focusing on:



1\. Heapsort algorithm implementation and time complexity analysis.

2\. Empirical comparison between Heapsort, Quicksort, and Merge Sort.

3\. Priority Queue implementation using a binary max-heap.

4\. Analysis of time and space complexities of heap operations.



The theoretical foundation is based on:

Cormen, T. H., Leiserson, C. E., Rivest, R. L., \& Stein, C. (2022). \*Introduction to Algorithms\* (4th ed.). MIT Press.



---



\## Files Included



\- `heapsort.py`  

&nbsp; Implementation of Heapsort algorithm.



\- `comparison.py`  

&nbsp; Empirical performance comparison of Heapsort, Quicksort, and Merge Sort on:

&nbsp; - Random data

&nbsp; - Sorted data

&nbsp; - Reverse-sorted data



\- `priority\_queue.py`  

&nbsp; Binary max-heap based Priority Queue implementation with:

&nbsp; - insert()

&nbsp; - extract\_max()

&nbsp; - increase\_key()

&nbsp; - is\_empty()



\- `report.md`  

&nbsp; Detailed theoretical analysis and discussion.



---



\## How to Run



Navigate to the project folder in Command Prompt:

```bash

cd "C:\\Users\\anush\\OneDrive\\Documents\\ADS532\_Assignment4"

```



Run Heapsort test:

``` bash

python heapsort.py

```



Run empirical comparison:

```bash

python comparison.py

```



Run priority queue test:

```bash

python priority\_queue.py

```





---



\## Summary of Findings



\- Heapsort runs in O(n log n) time in all cases.

\- Quicksort performance depends on pivot selection.

\- Merge Sort maintains stable O(n log n) performance.

\- Binary Heap supports insert and extract operations in O(log n) time.









