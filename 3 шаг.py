from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Собери яйца — шаг 3")
root.geometry("800x600")
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.place(x=350, y=100)

bg_image = Image.open("/Users/ivanzilaev/Desktop/ПРОЕКТ/ЕЩЕ фон.png").resize((800, 600), Image.LANCZOS)
background = ImageTk.PhotoImage(bg_image)
canvas.background = background  # Сохраняем ссылку, чтобы не удалилось
canvas.create_image(0, 0, image=background, anchor="nw")

# Игрок-картинка
wolf_right_img = Image.open("/Users/ivanzilaev/Desktop/ПРОЕКТ/правоверх.png").resize((250, 340), Image.LANCZOS)
wolf_left_img = Image.open("/Users/ivanzilaev/Desktop/ПРОЕКТ/левоверх.png").resize((250, 340), Image.LANCZOS)

wolf_right = ImageTk.PhotoImage(wolf_right_img)
wolf_left = ImageTk.PhotoImage(wolf_left_img)

canvas.wolf_right = wolf_right
canvas.wolf_left = wolf_left

player_x = 450
player_y = 550
player_image = canvas.create_image(player_x, player_y, image=wolf_right)

# Очки
score = 0
score_text = canvas.create_text(10, 10, anchor="nw", text="Очки: 0", font=("PIXY", 26))
speed_point = 3


# Класс яйца
class Egg:
    def __init__(self):
        self.size = 20
        self.x = random.randint(20, 780)
        self.y = 0
        self.speed = random.randint(3, 6)
        self.oval = canvas.create_oval(
            self.x, self.y - 10, self.x + self.size, self.y + self.size,
            fill="#F0EAD6"
        )

    def move(self):
        canvas.move(self.oval, 0, self.speed)
        coords = canvas.bbox(self.oval)
        player_coords = canvas.bbox(player_image)

        # Столкновение с игроком
        if coords and player_coords:
            if (coords[2] >= player_coords[0] and
                    coords[0] <= player_coords[2] and
                    coords[3] >= player_coords[1] and
                    coords[1] <= player_coords[3]):
                global score
                global speed_point
                score += 1
                speed_point += 1
                canvas.itemconfig(score_text, text=f"Очки: {score}")
                self.reset()
                return

        # Упало мимо
        if coords[3] >= 600:
            speed_point -= 1
            self.reset()

    def reset(self):
        global score
        self.x = random.randint(20, 780)
        self.y = 0
        self.speed = random.randint(speed_point, speed_point + 3)
        canvas.coords(self.oval, self.x, self.y - 10, self.x + self.size, self.y + self.size)


# Создаем список яиц
eggs = [Egg() for i in range(2)]  # можно увеличить число


# Игровой цикл
def game_loop():
    for egg in eggs:
        egg.move()
    root.after(30, game_loop)


# Управление
def move_player(event):
    global player_x
    if event.keysym in ["a", "Left"]:
        if player_x > 40:
            player_x -= 20
            canvas.move(player_image, -20, 0)
            canvas.itemconfig(player_image, image=wolf_left)  # поворот влево
    elif event.keysym in ["d", "Right"]:
        if player_x < 760:
            player_x += 20
            canvas.move(player_image, 20, 0)
            canvas.itemconfig(player_image, image=wolf_right)


root.bind("<KeyPress>", move_player)
game_loop()
root.mainloop()

хуек немытый ты прав
