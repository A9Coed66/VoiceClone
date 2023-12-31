import matplotlib.pyplot as plt 

def pltSetup(title, xlabel, ylabel, figsize=(10, 6), data=None):
    plt.figure(figsize=figsize)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.plot(data)
    plt.show()