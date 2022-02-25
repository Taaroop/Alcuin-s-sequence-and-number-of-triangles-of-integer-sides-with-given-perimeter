import matplotlib.pyplot as plt
import math

def triangle_count(n):
    count = 0
    li = []
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                li_2 = [a, b, c]
                li_2 = sorted(li_2)
                if a+b+c == n:
                    if a+b > c and a+c > b and b+c > a:
                        if li_2 not in li:
                            count += 1
                            li.append(li_2)
    return count

def taaroop(n):
    equi = 0
    ordered = ((n-1)*(n-2))/2
    double = (n-1)//2
    if n%3 == 0:
        double -= 1
        equi = 1

    distinct_unordered = (ordered - (3*double) - equi)/6
    total_unordered = distinct_unordered + double + equi
    c_max = math.ceil(n/2)
    sum_a_b = n-c_max
    complement = 0
    for i in range(2, sum_a_b+1):
        complement += i//2
    
    total_final = total_unordered-complement
    return total_final

end = 50
lst_triangle_count = []
lst_taaroop = []
lst_perimeter = []
for n in range(1, end+1):
    lst_triangle_count.append(triangle_count(n))
    lst_taaroop.append(taaroop(n))
    lst_perimeter.append(n)

plt.plot(lst_triangle_count, lst_perimeter)
plt.plot(lst_taaroop, lst_perimeter)
