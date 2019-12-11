# Analysis-of-sorting-algorithms
**Abstract

Analyzing modified versions of two different algorithms. We are investigating the time complex of a modified version of merge sort.

**Theory

Time complex of standard insertion sort in worst case: C(n) = C(1)+((n−1))/2=((n−1)n)/2=(n^2−n)/2

![Ins](/images/ins.png)

Time complex of binary search recursive sort in worst case: C(n/2(k-1) = C(1)+((n−1))/2=((n−1)n)/2=(n^2−n)/2

![Bin](/images/bin.png)

Even though the binary search might only require logarithmic time. The time for the placement would still requirea squared amount of time in the worst case scenario. Hence the worst case and average cost for insertionsort with binary search would still be θ(n^2) but the best case would be Ω(n) because binary search always gets the best case θ(1)and we skip the loop. 

![Bin](/images/theo.png)

**Result

![Ins](/images/1000.png)

![Ins](/images/10000.png)

![Ins](/images/50000.png)

![Ins](/images/100000.png)
