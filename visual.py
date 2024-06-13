"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt

def plot_pie_chart(data):

    labels = list(data.keys())
    sizes = list(data.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Reviews by Park")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()
