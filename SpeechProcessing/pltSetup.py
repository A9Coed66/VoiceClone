import matplotlib.pyplot as plt 

def pltSetup(title, xlabel, ylabel, data, figsize=(15, 6)):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.figure(figsize=figsize)
    plt.plot(data)
    plt.show()