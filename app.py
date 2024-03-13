import flet as ft
import flet.canvas as cv
import math

def main(page: ft.Page):
    page.title = "Bézier Curve"
    app_h = 800
    app_w = 1500
    page.window_height = app_h
    page.window_width = app_w
    page.window_resizable = False
    
    # Colors
    
    
    # Fonts
    page.fonts = {
        "Railinc" : "/fonts/Raillinc.otf",
        "Curves" : "/fonts/Square_Curves.ttf",
    }
    
    
    
    
    
    page.update()

ft.app(target=main)

# Initiate Variable
canvas_path = []
p_kontrol_antara = []
p_awal = []
p_akhir = []


# Impementation
def makeListEmpty(List):
    List.clear()
    
def getMidPoint(p1,p2):
    x = float((p1[0]+p2[0])/2 )
    y = float((p1[1]+p2[1])/2)
    pout = (x,y)
    return pout

def BezierKuadratik(p0, p1, p2, iterate, iterateMax):
    q0 = getMidPoint(p0,p1)
    q1 = getMidPoint(p1, p2)
    r0 = getMidPoint(q0,q1)
    if iterate < iterateMax:
        iterate += 1
        BezierKuadratik(p0, q0, p1, iterate, iterateMax)
        BezierKuadratik(p1, q1, p2, iterate, iterateMax)
    else:
        return []
        
    