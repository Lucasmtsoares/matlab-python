#Expresse f(t) = −3.cos(ω0t)+ 4.sen(ω0) como uma única senóide.

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da função
omega_0 = 2 * np.pi  # Frequência angular em radianos por segundo
t = np.linspace(0, 2 * np.pi, 1000)  # Intervalo de tempo de 0 a 2π

# Função original
f_t_original = -3 * np.cos(omega_0 * t) + 4 * np.sin(omega_0 * t)

# Expressão simplificada como uma única senoide
f_t_simplificada = 5 * np.sin(omega_0 * t)

# Plot das duas funções
plt.figure(figsize=(10, 4))
plt.plot(t, f_t_original, label='f(t) = -3cos(ω0t) + 4sin(ω0t)')
plt.plot(t, f_t_simplificada, label='f(t) simplificada = 5sin(ω0t)', linestyle='--')
plt.xlabel('Tempo (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.title('Expressão de f(t) como uma única senoide')
plt.show()
