import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criação do gráfico
plt.plot(x, y)
plt.title('Gráfico de Seno')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
