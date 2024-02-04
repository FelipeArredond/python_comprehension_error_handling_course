import matplotlib.pyplot as plt

def generate_bar_chart():
    labels = ['a', 'b', 'c']
    values = [100, 200, 120]
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar_chaart.png')

if __name__ == '__main__':
    generate_bar_chart()