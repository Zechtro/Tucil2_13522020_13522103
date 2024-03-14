import flet as ft
import flet.canvas as cv
import math
import time

def main(page: ft.Page):
    page.title = "Bézier Curve"
    app_h = 800
    app_w = 1500
    page.window_height = app_h
    page.window_width = app_w
    page.window_resizable = False
    
    # Fonts
    page.fonts = {
        "Railinc" : "/fonts/Raillinc.otf",
        "Curves" : "/fonts/Square_Curves.ttf",
    }
    
    # Initiate Variable
    num_of_iteration = [0]
    
    range_y = 0
    max_y = 0
    min_y = 0
    
    range_x = 0
    max_x = 0
    min_x = 0
    
    coordinate_multiplier = 1
    
    canvas_path = []
    result_path = []
    
    coordinate_points = []
    initial_points = []

    # Impementation
    def makeListEmpty(List):
        List.clear()
        
    def insertToPath(ps1):
        if(ps1[1] == "m"):
            canvas_path.append(cv.Path.MoveTo(ps1[0][0],ps1[0][1]))
        else:
            canvas_path.append(cv.Path.LineTo(ps1[0][0],ps1[0][1]))
        page.update()
        time.sleep(0.2)
        # print("YAHAHAH",canvas_path)
    
    def insertToPathResult(ps1):
        if(ps1[1] == "m"):
            result_path.append(cv.Path.MoveTo(ps1[0][0],ps1[0][1]))
        else:
            result_path.append(cv.Path.LineTo(ps1[0][0],ps1[0][1]))
        page.update()
        time.sleep(0.2)
        
    def getMidPoint(p1,p2):
        x = float((p1[0]+p2[0])/2 )
        y = float((p1[1]+p2[1])/2)
        pout = (x,y)
        return pout

    def BezierKuadratik(p0, p1, p2, iterate, iterateMax):
        if(iterate == 0):
            insertToPath((p0,"m"))
            insertToPath((p1,"l"))
            insertToPath((p2,"l"))
        q0 = getMidPoint(p0,p1)
        q1 = getMidPoint(p1, p2)
        r0 = getMidPoint(q0,q1)
        if(iterate <= iterateMax-1):
            insertToPath((q0,"m"))
            insertToPath((q1,"l"))
        if(iterate == iterateMax-1):
            insertToPathResult((p0,"m"))
            insertToPathResult((r0,"l"))
            insertToPathResult((p2,"l"))
        elif(iterate < iterateMax-1):
            insertToPath((p0,"m"))
            insertToPath((r0,"l"))
            insertToPath((p2,"l"))
        
        if iterate == 0:
            iterate += 1
            return [p0] + BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax) + [p2]
        elif iterate < iterateMax:
            iterate += 1
            return BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax)
        else:
            return []
    
    def button1Clicked(e):
        makeListEmpty(canvas_path)
        makeListEmpty(result_path)
        x0 = coordinate_points[0][0]
        y0 = coordinate_points[0][1]
        x1 = coordinate_points[1][0]
        y1 = coordinate_points[1][1]
        x2 = coordinate_points[2][0]
        y2 = coordinate_points[2][1]
        print(BezierKuadratik((x0,y0),(x1,y1),(x2,y2),0,num_of_iteration[0]))
        # print(BezierKuadratik((0,720),(360,0),(720,720),0,num_of_iteration[0]))
    
    button1 = ft.ElevatedButton(
        text="1",
        on_click=button1Clicked,
    )
    
    def button2Clicked(e):
        makeListEmpty(canvas_path)
        makeListEmpty(result_path)
        print(BezierKuadratik((0,0),(500,500),(1000,0),0,3))
    
    button2 = ft.ElevatedButton(
        text="2",
        on_click=button2Clicked,
    )
    
    paint_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=1.3,
        color="#B4B4B8"
    )
    
    paint_result_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=2,
        color="#000000"
    )
    
    def inputChanged(e):
        makeListEmpty(initial_points)
        makeListEmpty(coordinate_points)
        range_y = 0
        max_y = 0
        min_y = 0
        range_x = 0
        max_x = 0
        min_x = 0
        coordinate_multiplier = 1
        isValid = True
        points_temp = e.control.value.split("_")
        for i in range(len(points_temp)):
            point = points_temp[i].split(",")
            if(len(point) == 2):
                try:
                    x = int(point[0])
                    y = int(point[1])
                except:
                    e.control.error_text = "x and y must be integer"
                    isValid = False
                    break
                else:
                    if(i==0):
                        max_y = y
                        min_y = y
                        max_x = x
                        min_x = x
                    else:
                        if(y > max_y):
                            max_y = y
                        elif(y < min_y):
                            min_y = y
                        if(x > max_x):
                            max_x = x
                        elif(x < min_x):
                            min_x = x
                    e.control.error_text = ""
                    initial_points.append((x,y))
            else:
                e.control.error_text = "Invalid format"
                isValid = False
                break
        
        if isValid:
            print("HUWAHUWA", initial_points,max_x,min_x,max_y,min_y)
            range_y = max_y-min_y
            range_x = max_x-min_x
            if(range_x > 0 and range_y > 0):
                if(range_y > range_x):
                    coordinate_multiplier = float((app_h*0.85)/range_y)
                    for point in initial_points:
                        y_coor = (app_h*0.85) - ((point[1]-min_y)*coordinate_multiplier)
                        x_coor = point[0]*coordinate_multiplier + (float(((app_h*0.85)-(range_x*coordinate_multiplier))/2)-(min_x*coordinate_multiplier))
                        coordinate_points.append((x_coor,y_coor))
                else:
                    coordinate_multiplier = float((app_h*0.85)/range_x)
                    for point in initial_points:
                        x_coor = (point[0]-min_x)*coordinate_multiplier
                        y_coor = (app_h*0.85)-(point[1]*coordinate_multiplier + (float(((app_h*0.85)-(range_y*coordinate_multiplier))/2)-(min_y*coordinate_multiplier)))
                        coordinate_points.append((x_coor,y_coor))
                print("COOR",coordinate_points, coordinate_multiplier, app_h*0.85, range_x)
        page.update()
        
    def iterationChanged(e):
        try:
            num_of_iteration[0] = int(e.control.value)
        except:
            num_of_iteration[0] = 0
            e.control.error_text = "Value must be integer"
        else:
            e.control.error_text = ""
            
        page.update()
                    
    container = ft.Container(
        height=app_h,
        width=app_w,
        bgcolor="#C7C8CC",
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment="center",
                    vertical_alignment="center",
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                height=app_h-49,
                                alignment="center",
                                controls=[
                                    ft.Container(
                                        height=app_h*0.85,
                                        width=app_h*0.85,
                                        alignment=ft.alignment.center,
                                        # bgcolor="#000000",
                                        content=ft.Column(
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    canvas_path,
                                                                    paint=paint_canvas
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        ),
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    result_path,
                                                                    paint=paint_result_canvas
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            height=app_h*0.8545,
                            width=app_h*0.855,
                            # bgcolor="#000000",
                            content=ft.Column(
                                horizontal_alignment="center",
                                alignment="center",
                                controls=[
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            ft.Text("Bézier Curve",size=40,font_family="Railinc")
                                        ]    
                                    ),
                                    # INPUT
                                    ft.Container(
                                        margin=ft.margin.only(top=0.03*app_h),
                                        alignment=ft.alignment.center,
                                        width=app_w*0.45,
                                        content=ft.Row(
                                            alignment="center",
                                            controls=[
                                                ft.Container(
                                                    width=app_w*0.2,
                                                    content=ft.TextField(
                                                        label="Insert Points",
                                                        hint_text="x0,y0_x1_y1_x2,y2_...",
                                                        on_change=inputChanged,
                                                    )
                                                ),
                                                ft.Container(
                                                    width=app_w*0.1,
                                                    alignment=ft.alignment.center,
                                                    content=ft.TextField(
                                                        label="Iteration(s)",
                                                        on_change=iterationChanged,
                                                    )
                                                )
                                            ],
                                        )
                                    ),
                                    button1,
                                    
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    )
    
    page.add(container)
    page.update()

ft.app(target=main)


        
    