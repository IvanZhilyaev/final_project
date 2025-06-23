from tkinter import *

# Настройка окна
root = Tk()
root.title("Собери яйца — шаг 1")
root.geometry("800x600")
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Начальные координаты персонажа
player_x = 400
player_y = 550
player_size = 50

# Создаем персонажа (прямоугольник)
player = canvas.create_rectangle(
    player_x - player_size//2, player_y - player_size//2,
    player_x + player_size//2, player_y + player_size//2,
    fill="blue"
)

# Управление
def move_player(event):
    global player_x

    if event.keysym in ["a", "Left", "ф"]:
        if player_x - player_size//2 > 0:
            canvas.move(player, -20, 0)
            player_x -= 20
    elif event.keysym in ["d", "Right", "в"]:
        if player_x + player_size//2 < 800:
            canvas.move(player, 20, 0)
            player_x += 20

# Привязка клавиш
root.bind("<KeyPress>", move_player)

# Запуск
root.mainloop()
