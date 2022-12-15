# <2022-12-01 Thu 12:24>
# Saha / Doing Math with Python p. 99
# https://github.com/doingmathwithpython/code/blob/master/chapter4/Chapter4.ipynb

###############################################################################
# ➜  Re68 python --version
# Python 3.10.6

# ➜  Re68 pyenv versions
#   system
# * 3.10.6 (set by /Users/jeffre/.pyenv/version)

# ➜  Re68 python -m venv 68venv

# ➜  Re68 source 68venv/bin/activate
# (68venv) ➜  Re68 python --version
# Python 3.10.6
# (68venv) ➜  Re68 pip --version
# pip 22.2.1 from /Users/jeffre/[...]/Re68/68venv/lib/python3.10/site-packages/pip (python 3.10)
# (68venv) ➜  Re68 pip install sympy
# Collecting sympy
#   Using cached sympy-1.11.1-py3-none-any.whl (6.5 MB)
# Collecting mpmath>=0.19
#   Using cached mpmath-1.2.1-py3-none-any.whl (532 kB)
# Installing collected packages: mpmath, sympy
# Successfully installed mpmath-1.2.1 sympy-1.11.1

# [notice] A new release of pip available: 22.2.1 -> 22.3.1
# [notice] To update, run: pip install --upgrade pip

# (68venv) ➜  Re68
###############################################################################


from sympy import Symbol, pprint, init_printing
def print_series(n, x_value):
    # initialize printing system with
    # reverse order
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
    # evaluate the series at x_value
    series_value = series.subs({x:x_value})
    print('Value of the series at {0}: {1}'.format(x_value, series_value))

if __name__ == '__main__':
    n = input('Enter the number of terms you want in the series: ')
    x_value = input('Enter the value of x at which you want to evaluate the series: ') 
    print_series(int(n), float(x_value))

###############################################################################
# working

def print_series(numberOfPercepts, lifetime):
    series = numberOfPercepts**1

    for i in range(2, lifetime+1):
        series = series + numberOfPercepts**i
    print(series)

###############################################################################
# working

numberOfPercepts = 2
term1 = numberOfPercepts**1
term2 = numberOfPercepts**2
term3 = numberOfPercepts**3
term4 = numberOfPercepts**4

series = term1 + term2 + term3 + term4

print(series)



###############################################################################
# working

numberOfPercepts = 3
term1 = numberOfPercepts**1
term2 = numberOfPercepts**2
term3 = numberOfPercepts**3
term4 = numberOfPercepts**4
term5 = numberOfPercepts**5
term6 = numberOfPercepts**6
term7 = numberOfPercepts**7
term8 = numberOfPercepts**8
term9 = numberOfPercepts**9
term10 = numberOfPercepts**10
term11 = numberOfPercepts**11
term12 = numberOfPercepts**12
term13 = numberOfPercepts**13
term14 = numberOfPercepts**14

series = term1+term2+term3+term4+term5+term6+term7+term8+term9+term10+term11+term12+term13+term14

print(series)

# numberOfPercepts = 2  ...
# In [9]: print(term14)                                                                 │
# 16384


# numberOfPercepts = 3  ...
# In [9]: print(term14)                                                                 │
# 4782969
