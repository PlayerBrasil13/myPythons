from sys import path

path.append('..\\modules')

import modules_and_packages.modules.module as module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

