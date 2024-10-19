#Wpisz tu wartości a, b oraz c, z funkcji kwadratowej. Te wartości są użyte w obliczeniach dalej.
a = 2
b = 2
c = -1
#Komputer sprawdza, czy wszystkie wartości są liczbami, jeżeli tak to oblicza deltę.
import math
if type(a) == int and type(b) == int and type(c) == int:
    delta = b * b - 4 * a * c
    #Na podstawie wartości delty komputer decyduje jakie dalsze kroki podjąć.
    if delta < 0:
        print("Delta wynosi " + str(delta) + " jest to liczba ujemna, dlatego funkcja nie ma miejsc zerowych." )
    elif delta == 0:
        print("Delta wynosi 0.")
        print("Pierwiastek z delty wynosi 0.")
        print("W takim przypadku funkcja ma tylko jedno miejsce zerowe.")
        x0 = -(b) // 2 * a
        print("x0 równa się " + str(x0) + ".")
    elif delta > 0:
        #Komputer sprawdza, czy delta wynosi 1, jeżeli tak to pomija niepotrzebe liczenie pierwiaskta delty i od razu zakłada, że równa się 1.
        if delta == 1:
            print("Delta wynosi 1, od razu widać że pierwiastek z delty też wynosi 1.")
            pierwiastekDelta = math.sqrt(delta)
            x1 = (-b - pierwiastekDelta)/(2 * a)
            x2 = (-b + pierwiastekDelta)/(2 * a)
            print("x1 równa się " + str(x1) + ".")
            print("x2 równa się " + str(x2) + ".")
        else:
            print("Delta wynosi " + str(delta) + ".")
            pierwiastekDelta = math.sqrt(delta)
            print("Pierwiastek z delty wynosi " + str(pierwiastekDelta) + ".")
            x1 = (-b - pierwiastekDelta)/(2 * a)
            x2 = (-b + pierwiastekDelta)/(2 * a)
            print("x1 równa się " + str(x1) + ".")
            print("x2 równa się " + str(x2) + ".")
    else:
        #Nie mam pojęcia w jakiej sytuacji może tutaj się kod zepsuć, ale słyszałem że warto takie rzeczy robić na wszelki wypadek.
        print("Wystąpił jakis straszliwy błąd :(")
else:
    print("Wszystkie wpisane wartości muszą być liczbami!")