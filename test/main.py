from funct import *
import serial
import struct
import time





import tkinter as tk


def update_angle(value):
    """Обновляет метку с текущим значением угла"""
    global val_pitch, val_yaw
    angle_label.config(text=f"Текущий угол roll: {value}°")
    val_pitch = int(value) * 45
    pitch_motor_control(val_pitch, val_yaw)
    return val_pitch


def update_angle2(value):
    """Обновляет метку с текущим значением угла"""
    global val_pitch, val_yaw
    angle_label2.config(text=f"Текущий угол: {value}°")
    val_yaw = int(value) * 45
    pitch_motor_control(val_pitch, val_yaw)
    return val_yaw


def click():
    print(val_yaw, val_pitch)

    pitch_motor_control(val_pitch, val_yaw)
    # yaw_motor_control(val_yaw)


# Создаем главное окно
root = tk.Tk()
root.title("Угловой ползунок")
root.geometry("300x300")
on_motor(11)
global val_pitch, val_yaw
val_pitch, val_yaw = 0, 0
pitch_motor_control(val_pitch, val_yaw)
# Создаем метку для отображения угла
angle_label = tk.Label(root, text="Текущий угол roll: 0°")
angle_label.pack(pady=0)
angle_label2 = tk.Label(root, text="Текущий угол2: 0°")
angle_label2.pack(pady=10)
# Создаем горизонтальный ползунок
angle_slider = tk.Scale(
    root,
    from_=-180,  # Минимальное значение
    to=180,  # Максимальное значение
    orient=tk.HORIZONTAL,  # Ориентация
    length=200,  # Длина ползунка
    command=update_angle2  # Функция обновления
)
angle_slider.pack()
angle_slider2 = tk.Scale(
    root,
    from_=-180,  # Минимальное значение
    to=180,  # Максимальное значение
    orient=tk.HORIZONTAL,  # Ориентация
    length=200,  # Длина ползунка
    command=update_angle  # Функция обновления
)
# Создаем кнопку
button_send = tk.Button(root, text="Send", command=click)
button_send.pack(pady=40)
angle_slider2.pack()

root.mainloop()



