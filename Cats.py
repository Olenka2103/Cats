from http.client import responses
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url) # делаем запрос по этой ссылке и то, что получим положим в переменную
        response.raise_for_status() # обработка исключений - если будет какая то ошибка, тут эту ошибку получим
        image_data = BytesIO(response.content) # сама картинка будет преобразована с помощью байтс ио
        img = Image.open(image_data)# имэдж дата открываем с пом библ пиллоу и кладём в переменную локальную
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # форматируем картинку что бы изображение всегда было одинакового формата и не страдало качество
        return ImageTk.PhotoImage(img) # функция вернёт картинку и мы её положим в пер где эта функция вызвана
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None # обязательно вернём результат, если всё хорошо - картинка, если ошибка - текст ошибки в консоль


def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel() # открываем новое окно
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img) # прописываем что она именно в этом окне, по умолчанию открылась бы в главном
        label.pack()
        label.image = img


def exit():
    window.destroy() #окно будет закрыто, программа завершится

window = Tk()
window.title('Cats')
window.geometry('600x520')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()

main_menu = Menu(window)
window.config(menu=main_menu)

filemenu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='файл', menu=filemenu)
filemenu.add_command(label='Обновить изображение', command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=exit)


# label = Label()
# label.pack()

# upd_button = Button(text='Обновить картинку', command=set_image, bg='#6b4294', fg='#dad0e4')
# upd_button.pack()

url = 'https://cataas.com/cat'

open_new_window()

window.mainloop()
