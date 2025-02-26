import turtle
import math

# Fungsi untuk menggambar satu kelopak bunga
def draw_petal(t, radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)

# Fungsi untuk menggambar bunga
def draw_flower(t, petals, radius):
    for _ in range(petals):
        draw_petal(t, radius)
        t.left(360 / petals)

# Setup turtle
window = turtle.Screen()
window.bgcolor("white")

flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)
flower.color("red")

# Gambar bunga dengan 12 kelopak dan radius 100
draw_flower(flower, 12, 100)

# Sembunyikan turtle setelah selesai
flower.hideturtle()

# Tutup window saat di-klik
window.exitonclick()
