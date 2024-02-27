import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Рисуем комнату
room = patches.Rectangle((0, 0), 10, 10, linewidth=1, edgecolor='black', facecolor='lightgrey')
ax.add_patch(room)

# Рисуем лестницу
stairs = patches.Rectangle((7, 0), 3, 5, linewidth=1, edgecolor='black', facecolor='grey')
ax.add_patch(stairs)

# Устанавливаем пределы осей для создания видимости сверху
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Располагаем камеру сверху в углу
camera = patches.Circle((9, 9), 0.3, edgecolor='black', facecolor='red')
ax.add_patch(camera)

plt.axis('equal')
plt.axis('off')
plt.show()
