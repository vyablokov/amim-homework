#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt


def zero_probability_calculation(coefficiency_probabilty):
    zero_p = 0
    sum_coef = 0
    for i in range(len(coefficiency_probabilty)):
        sum_coef += coefficiency_probabilty[i]
    zero_p = 1/sum_coef
    return zero_p


def is_probability_correct(failure_probability_real, 
                           failure_probability_required):
   if failure_probability_real > failure_probability_required:
       return False
   return True


def probability_calculation(zero_probability, coefficiency_probabilty):
    cur_p = []
    for i in range(len(coefficiency_probabilty)):
        cur_p.append(zero_probability * coefficiency_probabilty[i])
    return cur_p


def efficiency_calculation(probablity):
    efficiency = 0
    for i in range(len(probablity)):
        efficiency += i * probablity[i]
        
    return efficiency


def efficiency_calculation_with_query(probablity):
    efficiency = 0
    for i in range(len(probablity)):
        if i == (len(probablity) - 1):
            efficiency += (i-1) * probablity[i]
            continue
        efficiency += i * probablity[i]
        
    return efficiency


def probability_coefficient_calculation(a, n):
    probability_coefficients = []
    for i in range(n+1):
        probability_coefficients.append(
            function_coefficient_calculaton(a, i))
    return probability_coefficients
    

def solution_without_query(p, k, n, a, p_required):
    coef_p = probability_coefficient_calculation(a, n) 
    zero_p = zero_probability_calculation(coef_p)
    cur_p = probability_calculation(zero_p, coef_p)
    
    p.append(cur_p[n])
    k.append(efficiency_calculation(cur_p))
    if is_probability_correct(p[n], p_required):
        return True
    
    return False


def function_coefficient_calculaton(a, n):
    return math.pow(a, n)/math.factorial(n)
    
    
def solution_with_query(q, a, k, n):
    coef_p = probability_coefficient_calculation(a, n) 
    # print(coef_p)
    for i in range(n+1):
        # Предельный стационарный режим
        if i <= a:
            continue
        alpha = a/i
        
        if math.fabs(1-alpha) < 0.1:
            continue
        cur_coef_p = coef_p[0:i+1]+[coef_p[i]*(alpha/(1-alpha))]
        zero_p = zero_probability_calculation(cur_coef_p)
        
        cur_p = probability_calculation(zero_p, cur_coef_p)
        
        k.append(efficiency_calculation_with_query(cur_p))
        q.append(alpha*zero_p*coef_p[i]/math.pow(1-alpha, 2))


def main(p_required, a):
    p = []  # Вероятность отказа
    k = []  # Среднее число занятых каналов
    k_query = []  # Среднее число занятых каналов с очередью
    q = []  # Средняя длина очереди
    k_avg = []  # Среднее относительное число занятых каналов
    n = 0

    while True:
        is_ok = solution_without_query(p, k, n, a, p_required)
        if is_ok:
            break    
        n += 1

    for i in range(len(k)):
        if i == 0:
            k_avg.append(0)
            continue
        k_avg.append(k[i]/i)

    print('СМО без очереди:')
    print('Для {0:d} каналов вероятность отказа равна {1:.3f} ( < {2:.3f}).'.format(n, p[n], p_required))
    print('При этом в среднем занято {0:.2f} каналов (или {1:.1f}%).'.format(k[n], k_avg[n]*100))

    solution_with_query(q, a, k_query, n)

    print('\nСМО с очередью:')
    print('Cредняя длина очереди равна {1:.3f}.'.format(n, q[len(q)-1]))
    print('Среднее число занятых каналов равно {0:.2f}.'.format(k_query[len(k_query)-1]))

    plt.plot(p, label="Вероятность отказа")
    plt.plot(k, label="Среднее число занятых каналов")
    plt.plot(range(n-len(q)+1, n+1), q, label="Средняя длина очереди")
    plt.plot(range(n-len(k_query)+1, n+1), k_query, label="Среднее число занятых каналов с очередью")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1)
    plt.show()

l = 1.0 / 3.0
m = 1.0 / 14.0
a = l/m

main(0.01, a)
