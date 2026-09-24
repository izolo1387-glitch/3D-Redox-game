from ursina import *

app = Ursina()

# Создаем игрока (кубический персонаж в стиле Roblox)
player = Entity(model='cube', color=color.azure, scale=(1, 2, 1), position=(0, 1, 0))

# Функция для управления с телефона/клавиатуры
def update():
    if held_keys['w']:
        player.z += 5 * time.dt
    if held_keys['s']:
        player.z -= 5 * time.dt
    if held_keys['a']:
        player.x -= 5 * time.dt
    if held_keys['d']:
        player.x += 5 * time.dt

# Земля (платформа, по которой бегаем)
ground = Entity(model='plane', color=color.green, scale=(20, 1, 20), texture='white_cube')

app.run()
