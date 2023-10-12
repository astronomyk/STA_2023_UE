import numpy as np
import scipy as sp
import pandas as pd
import astropy

from astropy import units as u
from matplotlib import pyplot as plt


def load():
    edmond = pd.read_csv('./U2_2016_EU_world.csv', sep=',')
    edmond = edmond[edmond['_stream'].isin(['_J8_GEM', '_J8_PER', '_J8_QUA', '_J8_LYR'])]
    mag = edmond['_amag']


    colours = list(map(lambda x: ord(x[4]) - ord(x[5]), list(edmond['_stream'])))
    plt.scatter(edmond['_amag'], edmond['_H2'], s=1 * np.exp(-mag / 5), c=colours)
    plt.ylim(60, 120)
    plt.savefig('out.pdf')

    plt.scatter(edmond['_ra_o'], edmond['_dc_o'], c=edmond['_sol'])
    plt.ylim(None, None)
    plt.savefig('radiant.pdf')


load()