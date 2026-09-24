from ursina import *

app = Ursina()

# --- МЕНЮ РОБЛОКСА ---
menu_parent = Entity(parent=camera.ui)

# Заголовок меню
title = Text(text='ROBLOX CLONE', origin=(0, 0), position=(0, 0.4), scale=2, color=color.orange, parent=menu_parent)

# Функция запуска первой игры ("Бета игра")
def start_beta_game():
    menu_parent.enabled = False  # Скрываем меню
    game_world.enabled = True    # Показываем 3D-мир
    player.enabled = True
    ground.enabled = True
    info_text.enabled = True

# Кнопка запуска первой игры
play_button = Button(
    text='Бета игра',
    color=color.azure,
    scale=(0.4, 0.1),
    position=(0, 0.1),
    parent=menu_parent,
    on_click=start_beta_game
)

# --- 3D-МИР ИГРЫ (скрыт до нажатия кнопки) ---
game_world = Entity(enabled=False)

# Игрок
player = Entity(model='cube', color=color.red, scale=(1, 2, 1), position=(0, 1, 0), parent=game_world, enabled=False)

# Земля
ground = Entity(model='plane', color=color.green, scale=(30, 1, 30), texture='white_cube', parent=game_world, enabled=False)

# Подсказка в игре
info_text = Text(text='W, A, S, D - Движение\nНажми ESC для выхода', position=(-0.8, 0.45), scale=1, parent=game_world, enabled=False)

# Управление игроком
def update():
    if game_world.enabled:
        if held_keys['w']:
            player.z += 5 * time.dt
        if held_keys['s']:
            player.z -= 5 * time.dt
        if held_keys['a']:
            player.x -= 5 * time.dt
        if held_keys['d']:
            player.x += 5 * time.dt

app.run()
