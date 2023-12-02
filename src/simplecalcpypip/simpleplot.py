import matplotlib.pyplot as plt
import numpy as np

def plot_grafico_linear(x, y, xlabel="X", ylabel="Y", title="Gráfico Linear"):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_dispersao(x, y, xlabel="X", ylabel="Y", title="Gráfico de Dispersão"):
    plt.scatter(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_barra(x, y, xlabel="X", ylabel="Y", title="Gráfico de Barra"):
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_grafico_de_pizza(labels, sizes, title="Gráfico de Pizza"):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Assegura que o gráfico de pizza é desenhado como um círculo.
    plt.title(title)
    plt.show()

#Exemplos de uso:
# x_linear = np.linspace(0, 10, 100)
# y_linear = 2 * x_linear + 5
# plot_grafico_linear(x_linear, y_linear, "X", "Y", "Gráfico Linear")

# x_dispersao = np.random.rand(50)
# y_dispersao = np.random.rand(50)
# plot_grafico_de_dispersao(x_dispersao, y_dispersao, "X", "Y", "Gráfico de Dispersão")

# x_barra = ["Categoria 1", "Categoria 2", "Categoria 3"]
# y_barra = [3, 7, 2]
# plot_grafico_de_barra(x_barra, y_barra, "Categorias", "Valores", "Gráfico de Barra")

# labels_pizza = ["Maçãs", "Bananas", "Pêssegos", "Morangos"]
# sizes_pizza = [30, 45, 15, 10]
# plot_grafico_de_pizza(labels_pizza, sizes_pizza, "Gráfico de Pizza")
