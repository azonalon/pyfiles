#!/bin/python
# import matplotlib.pyplot as plt
# import numpy as np
# import scipy.constants
# import scipy.optimize as opt
def plot_config(filetype='png'):
    import matplotlib
    # matplotlib.use('pdf')
    import matplotlib.pyplot
    params = {
        'text.usetex': True,
        'figure.dpi' : 300,
        'savefig.dpi' : 300,
        'savefig.format' : filetype,
        # 'axes.labelsize': 8, # fontsize for x and y labels (was 10)
        # 'axes.titlesize': 8,
        # 'text.fontsize': 8, # was 10
        # 'legend.fontsize': 8, # was 10
        # 'xtick.labelsize': 8,
        # 'ytick.labelsize': 8,
        # 'figure.figsize': [fig_width,fig_height],
        'font.family': 'serif',
        'text.latex.preamble': [r'\usepackage[]{siunitx}'
                                r'\usepackage[]{mhchem}'],
    }
    matplotlib.rcParams.update(params)
    matplotlib.style.use('bmh')
    matplotlib.style.use('seaborn-paper')
    # matplotlib.style.use('seaborn-dark-palette')

    matplotlib.rc('axes', facecolor='white')
    matplotlib.rc('grid', linestyle='-', alpha=0.0)
    # matplotlib.lines.lineStyles
    # markers=[',', '+', '-', '.', 'o', '*']
    # matplotlib.lines.lineMarkers
    # matplotlib.rcParams
