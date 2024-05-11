#Дано целое число N (>0). Найти наибольшее целое число K, квадрат которого не пр
# евосходит N:K в квадрате < N. Функцию из
# влечения квадратного корня не использовать.
N = (input("Введите целое число: "))
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = (input("Введите целое число: "))
print('N = ', N)
K = 1
while K*K <= N:
    K += 1
K -= 1
print("K = {0}, K^2 = {1}, (K+1)^2 = {2}".format(K,K**2,(K+1)**2))