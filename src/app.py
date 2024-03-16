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
    
    range_x = [0]
    range_y = [0]
    
    canvas_path = []
    paint_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=0.5/(num_of_iteration[0]+1),
        color="#6B728E"
    )
    
    result_path = []
    paint_result_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=1/(num_of_iteration[0]+1),
        color="#000000"
    )
    
    initial_circle = []
    paint_initial_circle = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=1,
        color="#000000"
    )
    
    result_circle = []
    paint_result_circle = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=1,
        color="#000000"
    )
    
    cartesian_canvas = []
    paint_cartesian_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=1,
        color="#000000"
    )
    
    coordinate_points = []
    initial_points = []
    
    visualization_speed = [0]
        
    # Implementation
    def resetPath():
        makeListEmpty(canvas_path)
        makeListEmpty(result_path)
        makeListEmpty(result_circle)
        
    def resetInitial():
        makeListEmpty(initial_points)
        makeListEmpty(coordinate_points)
        makeListEmpty(initial_circle)
    
    def makeListEmpty(List):
        List.clear()
        
    def insertToPath(ps1):
        if(ps1[1] == "m"):
            canvas_path.append(cv.Path.MoveTo(ps1[0][0],ps1[0][1]))
        else:
            canvas_path.append(cv.Path.LineTo(ps1[0][0],ps1[0][1]))
        page.update()
        time.sleep(1-visualization_speed[0])
    
    def insertToPathResult(ps1):
        if(ps1[1] == "m"):
            result_path.append(cv.Path.MoveTo(ps1[0][0],ps1[0][1]))
        else:
            result_path.append(cv.Path.LineTo(ps1[0][0],ps1[0][1]))
        page.update()
        time.sleep(1-visualization_speed[0])
        
    def insertToPathCircle(p):
        s = float(50/(max(range_x[0],range_y[0])))
        s = max(s,5)
        initial_circle.append(cv.Path.Oval(p[0]-(0.5*s),p[1]-(0.5*s),s,s))
        page.update()
        
    def insertToPathResultCircle(p):
        s = float(50/(max(range_x[0],range_y[0])))
        s = max(s,5)
        result_circle.append(cv.Path.Oval(p[0]-(0.5*s),p[1]-(0.5*s),s,s))
        page.update()
        
    def getMidPoint(p1,p2):
        x = float((p1[0]+p2[0])/2 )
        y = float((p1[1]+p2[1])/2)
        pout = (x,y)
        return pout

    # def BezierKuadratik(p0, p1, p2, iterate, iterateMax):
    #     if(iterate == 0):
    #         insertToPath((p0,"m"))
    #         insertToPath((p1,"l"))
    #         insertToPath((p2,"l"))
    #     q0 = getMidPoint(p0,p1)
    #     q1 = getMidPoint(p1, p2)
    #     r0 = getMidPoint(q0,q1)
    #     if(iterate <= iterateMax-1):
    #         insertToPath((q0,"m"))
    #         insertToPath((q1,"l"))
    #     if(iterate == iterateMax-1):
    #         insertToPathResult((p0,"m"))
    #         insertToPathResult((r0,"l"))
    #         insertToPathResult((p2,"l"))
    #     elif(iterate < iterateMax-1):
    #         insertToPath((p0,"m"))
    #         insertToPath((r0,"l"))
    #         insertToPath((p2,"l"))
        
    #     if iterate == 0:
    #         iterate += 1
    #         return [p0] + BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax) + [p2]
    #     elif iterate < iterateMax:
    #         iterate += 1
    #         return BezierKuadratik(p0, q0, r0, iterate, iterateMax) + [r0] + BezierKuadratik(r0, q1, p2, iterate, iterateMax)
    #     else:
    #         return []
    
    # def button1Clicked(e):
    #     x0 = coordinate_points[0][0]
    #     y0 = coordinate_points[0][1]
    #     x1 = coordinate_points[1][0]
    #     y1 = coordinate_points[1][1]
    #     x2 = coordinate_points[2][0]
    #     y2 = coordinate_points[2][1]
    #     makeListEmpty(canvas_path)
    #     makeListEmpty(result_path)
    #     print(BezierKuadratik((x0,y0),(x1,y1),(x2,y2),0,num_of_iteration[0]))
    #     # print(BezierKuadratik((0,720),(360,0),(720,720),0,num_of_iteration[0]))
    
    # button1 = ft.ElevatedButton(
    #     text="1",
    #     on_click=button1Clicked,
    # )
    
    def BezierN(points, iterasi, iterasiMax):
        if (iterasi >= iterasiMax):
            return []
        else:
            q = points
            left = [q[0]]
            right = [q[-1]]
            while len(q) > 1:
                temp = q
                for i in range(len(temp)):
                    if(i == 0):
                        insertToPath((temp[0],"m"))
                    else:
                        insertToPath((temp[i],"l"))
                q = [getMidPoint(temp[i], temp[i+1]) for i in range(len(temp)-1)]
                
                left.append(q[0])
                right.append(q[-1])
            right.reverse()
            if(iterasi == iterasiMax-1):
                insertToPathResultCircle(q[0])
                insertToPathResult((points[0],"m"))
                insertToPathResult((q[0],"l"))
                insertToPathResult((points[-1],"l"))
            elif(iterasi < iterasiMax-1):
                insertToPath((points[0],"m"))
                insertToPath((q[0],"l"))
                insertToPath((points[-1],"l"))
            if iterasi == 0:
                iterasi += 1
                output = [points[0]] + BezierN(left, iterasi, iterasiMax)
                insertToPathResultCircle(left[-1])
                return  output + [left[-1]] + BezierN(right, iterasi, iterasiMax) + [points[-1]]
            else:
                iterasi += 1
                output = BezierN(left, iterasi, iterasiMax)
                insertToPathResultCircle(left[-1])
                return output + [left[-1]] + BezierN(right, iterasi, iterasiMax)
    
    def buttonVisualizeClicked(e):
        resetPath()
        e.control.visible = False
        e.control.disabled = True
        print(BezierN(coordinate_points,0,num_of_iteration[0]))
        e.control.disabled = False
        e.control.visible = True
        page.update()
    
    buttonVisualize = ft.ElevatedButton(
        style=ft.ButtonStyle(
                color={
                    # ft.MaterialState.HOVERED: ft.colors.WHITE,
                    # ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: "#FFFFFF",
                    ft.MaterialState.HOVERED: "#000000",
                },
                bgcolor={ft.MaterialState.DEFAULT: "#000000",
                         ft.MaterialState.HOVERED: "#FFFFFF"
                },
                padding={ft.MaterialState.DEFAULT: 28},
                overlay_color=ft.colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, "#000000"),
                },
            ),
        width=0.15*app_w,
        on_click=buttonVisualizeClicked,
        content=ft.Text("Visualize!",size=17,font_family="Railinc")
    )
    
    def inputChanged(e):
        resetInitial()
        temp_range_y = 0
        max_y = 0
        min_y = 0
        temp_range_x = 0
        max_x = 0
        min_x = 0
        coordinate_multiplier = 1
        isValid = True
        points_temp = e.control.value.split("_")
        n_points = len(points_temp)
        if(n_points < 3):
            e.control.error_text = "A curve consist of minimum 3 control points"
        else:
            for i in range(n_points):
                point = points_temp[i].split(",")
                if(len(point) == 2):
                    try:
                        x = int(point[0])
                        y = int(point[1])
                    except:
                        e.control.error_text = "x and y must be integer"
                        resetInitial()
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
                    resetInitial()
                    isValid = False
                    break
            
            if isValid:
                # print("HUWAHUWA", initial_points,max_x,min_x,max_y,min_y)
                temp_range_y = max_y-min_y
                temp_range_x = max_x-min_x
                if(temp_range_y > temp_range_x):
                    coordinate_multiplier = float((app_h*0.85)/temp_range_y)
                    for point in initial_points:
                        y_coor = (app_h*0.85) - ((point[1]-min_y)*coordinate_multiplier)
                        x_coor = point[0]*coordinate_multiplier + (float(((app_h*0.85)-(temp_range_x*coordinate_multiplier))/2)-(min_x*coordinate_multiplier))
                        coordinate_points.append((x_coor,y_coor))
                else:
                    coordinate_multiplier = float((app_h*0.85)/temp_range_x)
                    for point in initial_points:
                        x_coor = (point[0]-min_x)*coordinate_multiplier
                        y_coor = (app_h*0.85)-(point[1]*coordinate_multiplier + (float(((app_h*0.85)-(temp_range_y*coordinate_multiplier))/2)-(min_y*coordinate_multiplier)))
                        coordinate_points.append((x_coor,y_coor))
                range_y[0] = temp_range_y
                range_x[0] = temp_range_x
                for point in coordinate_points:
                    insertToPathCircle(point)
                print("COOR",coordinate_points, coordinate_multiplier, app_h*0.85, temp_range_x)
                    
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
        
        
    def slider_change(e):
        visualization_speed[0] = e.control.value
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
                                        margin=ft.margin.only(left=150),
                                        content=ft.Column(
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    cartesian_canvas,
                                                                    paint=paint_cartesian_canvas
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        ),
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
                                                        ),
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    initial_circle,
                                                                    paint=paint_initial_circle,
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        ),
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    result_circle,
                                                                    paint=paint_result_circle,
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        ),
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
                                    # TITLE
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
                                    # Button "Visualize!"
                                    ft.Container(
                                        margin=ft.margin.only(top=30,bottom=30),
                                        content=buttonVisualize
                                    ),
                                    # SPEED SLIDER
                                    ft.Container(
                                        width=0.3 * app_w,
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("Visualization Speed",size=15,font_family="Railinc"),          
                                                ft.Slider(
                                                    min=0,
                                                    max =1,
                                                    divisions=10000,
                                                    active_color= "#000000",
                                                    on_change=slider_change
                                                ),
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Text("Slow",size=10,font_family="Railinc")
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text("Fast",size=10,font_family="Railinc")
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                    
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


        
    