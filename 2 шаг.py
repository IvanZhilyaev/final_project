from tkinter import *
import random

root = Tk()
root.title("Собери яйца — шаг 2")
root.geometry("800x600")
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Игрок
player_x = 400
player_y = 550
player_size = 50
player = canvas.create_rectangle(
    player_x - player_size//2, player_y - player_size//2,
    player_x + player_size//2, player_y + player_size//2,
    fill="blue"
)

# Яйцо
egg_size = 20
egg = canvas.create_oval(0, 0, egg_size, egg_size, fill="#F0EAD6")

# Очки
score = 0
score_text = canvas.create_text(10, 10, anchor="nw", text="Очки: 0", font=("PIXY", 26))

# Двигаем яйцо
def move_egg():
    global score
    canvas.move(egg, 0, 5)  # падение

    egg_coords = canvas.bbox(egg)
    player_coords = canvas.bbox(player)

    if egg_coords and player_coords:
        # Проверка столкновения
        if (egg_coords[2] >= player_coords[0] and
            egg_coords[0] <= player_coords[2] and
            egg_coords[3] >= player_coords[1] and
            egg_coords[1] <= player_coords[3]):
            score += 1
            canvas.itemconfig(score_text, text=f"Очки: {score}")
            reset_egg()
            return

    # Если яйцо упало ниже экрана
    if egg_coords[3] >= 600:
        reset_egg()
        return

    # Повтор движения
    root.after(30, move_egg)

# Перезапуск яйца
def reset_egg():
    x = random.randint(20, 780)
    canvas.coords(egg, x, 0, x + egg_size, egg_size)
    root.after(10, move_egg)

# Управление игроком
def move_player(event):
    global player_x
    if event.keysym in ["a", "Left"]:
        if player_x - player_size//2 > 20:
            canvas.move(player, -20, 0)
            player_x -= 20
    elif event.keysym in ["d", "Right"]:
        if player_x + player_size//2 < 780:
            canvas.move(player, 20, 0)
            player_x += 20

root.bind("<KeyPress>", move_player)
reset_egg()  # запускаем первое падение
root.mainloop()
