h = 0.1
x = [h * i for i in range(11)]
y = [1/3, 0.20833, 0.14896, 0.13810, 0.16506, 0.22316, 0,30823, 0.41764, 0.54978, 0.70361, 0.87851]

def actual(x):
    return x ** 2 + 1 / 3 * math.e ** (-5 * x)

