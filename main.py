from ursina import *

app = Ursina()

# --- СЛОЙ 1: ГЛАВНОЕ МЕНЮ (Список игр) ---
main_menu = Entity(parent=camera.ui)

title_main = Text(text='MINI ROBLOX', origin=(0, 0), position=(0, 0.4), scale=2.5, color=color.orange, parent=main_menu)

def open_game_page():
    main_menu.enabled = False      # Скрываем главное меню
    game_page.enabled = True       # Показываем страницу плейса

# Кнопка выбора нашей "Беты игры" в списке
beta_game_btn = Button(
    text='Бета игра (Плейс #1)',
    color=color.azure,
    scale=(0.5, 0.1),
    position=(0, 0.1),
    parent=main_menu,
    on_click=open_game_page
)


# --- СЛОЙ 2: СТРАНИЦА ОПИСАНИЯ ПЛЕЙСА (Как в Roblox) ---
game_page = Entity(parent=camera.ui, enabled=False)

# Название плейса вверху
game_title_text = Text(text='БЕТА ИГРА', origin=(0, 0), position=(0, 0.35), scale=2, color=color.yellow, parent=game_page)

# Ник создателя сервера
creator_text = Text(text='Создатель: YouDeveloper', origin=(0, 0), position=(0, 0.25), scale=1, color=color.light_gray, parent=game_page)

# Описание игры
desc_text = Text(text='Добро пожаловать в первую тестовую игру!\nИсследуйте мир и тестируйте механику.', origin=(0, 0), position=(0, 0.1), scale=1, color=color.white, parent=game_page)

def start_actual_game():
    game_page.enabled = False    # Скрываем страницу плейса
    game_world.enabled = True    # Включаем 3D-мир

# Большая зеленая кнопка «ИГРАТЬ» (Play)
play_game_btn = Button(
    text='ИГРАТЬ',
    color=color.green,
    scale=(0.4, 0.12),
    position=(0, -0.1),
    parent=game_page,
    on_click=start_actual_game
)

def back_to_main():
    game_page.enabled = False
    main_menu.enabled = True

# Кнопка «Назад»
back_btn = Button(
    text='Назад',
    color=color.red,
    scale=(0.3, 0.08),
    position=(0, -0.3),
    parent=game_page,
    on_click=back_to_main
)


# --- СЛОЙ 3: САМ 3D-МИР (ИГРА) ---
game_world = Entity(enabled=False)

player = Entity(model='cube', color=color.red, scale=(1, 2, 1), position=(0, 1, 0), parent=game_world)
ground = Entity(model='plane', color=color.green, scale=(30, 1, 30), texture='white_cube', parent=game_world)

hud_text = Text(text='W, A, S,D - Бегать\nНажмите ESC для выхода', position=(-0.85, 0.45), scale=1, parent=game_world)

# Логика движения игрока
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