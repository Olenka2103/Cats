from http.client import responses
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url) #делаем запрос по этой ссылке и то, что получим положим в переменную
        response.raise_for_status() #обработка исключений - если будет какая то ошибка, тут эту ошибку получим
        image_data = BytesIO(response.content) #сама картинка будет преобразована с помощью байтс ио
        img = Image.open(image_data) #имэдж дата открываем с пом библ пиллоу и кладём в переменную локальную
        return ImageTk.PhotoImage(img) #функция вернёт картинку и мы её положим в пер где эта функция вызвана
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None #обязательно вернём результат, если всё хорошо - картинка, если ошибка - текст ошибки в консоль


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

upd_button = Button(text='Обновить картинку', command=set_image)
upd_button.pack()

url = 'https://cataas.com/'

set_image()

window.mainloop()
