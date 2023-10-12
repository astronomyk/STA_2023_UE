import numpy as np
from matplotlib import pyplot as plt
from astropy.io import ascii, fits

table = fits.getdata("table3.dat.fits", readme="ReadMe.txt")
print(table)
m = table["MH97b"]
m = m[m>0]

x = np.logspace(-1, 2, 50)
y, _ = np.histogram(m, x)

plt.plot(np.log10(x[1:]), np.log10(y), "o")
plt.show()
