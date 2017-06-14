from tkinter import *
import time
import turtle
def ejercicio1():
    def triangulo():
        a = int(input('Ingrese la altura del triangulo: '))
        p = int(l*3)
        a = int((l*a)/2)
        print('El perimetro del triangulo es: ',p)
        print('El Area del triangulo es: ',a)
        for x in range (1, n):
            t.forward(l)
            t.left(120)

    def cuadrado():
        p = int(l*4)
        a = int(l**2)
        print('El perimetro del triangulo es: ',p)
        print('El Area del triangulo es: ',a)
        for x in range (1, n):
            t.forward(l)
            t.left(90)
        

    def pentagono():
        m = int(input('Ingrese el apotema del pentagono: '))
        p = int(l*5)
        a = int((p*m)/2)
        for x in range (1, n):
            t.forward(l)
            t.left(72)
        
    
    n = int(input('Indique el numero de lados de la figura\n'+'Por favor el valor ingresado tiene que estar comprendido entre 3 y 5: '))
    if n < 3:
        print('El valor ingresado es menor a 3')
    elif n > 5:
        print('El valor ingresado es mayor a 5')
    elif (n >= 3 & n <= 5):
        l  = int(input('Ingrese la longitud del lado\n'+'La longitud no debe superar las 150 unidades: '))
        if l >150:
            print('La longitud supera las 150 unidades')
        elif l <=150:
            if n == 3:
              triangulo()
            if n == 4:
              cuadrado()
            if n == 5:
              pentagono()

def ejercicio2():
    class Gota:
        def __init__(self, canvas, color, a,b):
            self.canvas = canvas
            self.id = canvas.create_oval(5, 5, 13, 13, fill = color)
            self.canvas.move(self.id, a, b)
        def draw(self, x, y):
            self.canvas.move(self.id, x, y)

    fk = Tk()
    fk.title('Ejercicio2')
    fk.resizable(0, 0)
    fk.wm_attributes("-topmost", 1)
    canvas = Canvas(fk, width=640, height=480, bd=0, highlightthickness=0)
    canvas.pack()
    fk.update()
    gota = Gota(canvas, 'lightblue', 10, 10)
    gota1 = Gota(canvas, 'lightblue', 30, 20)
    gota2 = Gota(canvas, 'lightblue', 50, 30)
    gota3 = Gota(canvas, 'lightblue', 70, 40)
    gota4 = Gota(canvas, 'lightblue', 90, 50)   
    gota5 = Gota(canvas, 'lightblue', 110, 60)
    gota6 = Gota(canvas, 'lightblue', 130, 70)
    gota7 = Gota(canvas, 'lightblue', 150, 80)
    gota8 = Gota(canvas, 'lightblue', 170, 90)
    gota9 = Gota(canvas, 'lightblue', 190, 100)
    gota10 = Gota(canvas, 'lightblue', 210, 10)
    gota11 = Gota(canvas, 'lightblue', 230, 20)
    gota12 = Gota(canvas, 'lightblue', 250, 30)
    gota13 = Gota(canvas, 'lightblue', 270, 40)
    gota14 = Gota(canvas, 'lightblue', 290, 50)
    gota15 = Gota(canvas, 'lightblue', 310, 60)
    gota16 = Gota(canvas, 'lightblue', 330, 70) 
    gota17 = Gota(canvas, 'lightblue', 350, 80)
    gota18 = Gota(canvas, 'lightblue', 370, 90)
    gota19 = Gota(canvas, 'lightblue', 390, 100)

    while 1:
        gota.draw(0, 1)
        gota1.draw(0, 1)
        gota2.draw(0, 1)
        gota3.draw(0, 1)
        gota4.draw(0, 1)
        gota5.draw(0, 1)
        gota6.draw(0, 1)
        gota7.draw(0, 1)
        gota8.draw(0, 1)
        gota9.draw(0, 1)
        gota10.draw(0, 1)
        gota11.draw(0, 1)
        gota12.draw(0, 1)
        gota13.draw(0, 1)
        gota14.draw(0, 1)
        gota15.draw(0, 1)
        gota16.draw(0, 1)
        gota17.draw(0, 1)
        gota18.draw(0, 1)
        gota19.draw(0, 1)
        fk.update_idletasks()
        fk.update()
        time.sleep(0.01)

tk = Tk()
tk.title('Menu')
btn1 = Button(tk, text = 'Ejercicio1', command = ejercicio1)
btn1.pack()
btn2 = Button(tk, text = 'Ejercicio2', command = ejercicio2)
btn2.pack()


    
    

              
              
    
    
