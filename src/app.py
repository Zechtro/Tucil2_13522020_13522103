import flet as ft
import flet.canvas as cv
import math
import time

def main(page: ft.Page):
    page.title = "Bézier Curve"
    app_h = 700
    app_w = 1300
    page.window_height = app_h
    page.window_width = app_w
    page.window_resizable = False
    
    # Fonts
    page.fonts = {
        "Railinc" : "/fonts/Raillinc.otf",
    }
    
    # Initiate Variable
    num_of_iteration = [0]
    
    process_time = [0]
    
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
        color="#6B728E"
    )
    
    result_circle = []
    paint_result_circle = ft.Paint(
        style=ft.PaintingStyle.FILL,
        stroke_width=1,
        color="#000000"
    )
    
    cartesian_line_canvas = []
    cartesian_line_result_canvas = []
    paint_cartesian_line_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=0.3,
        color="#45474B"
    )
    
    cartesian_text_number_canvas = []
    cartesian_text_number_result_canvas = []
    paint_cartesian_text_number_canvas = ft.Paint(
        style=ft.PaintingStyle.STROKE,
        stroke_width=1,
        color="#45474B"
    )
    
    initial_canvas_axis = []
    initial_canvas_ordinat = []
    
    coordinate_points = []
    initial_points = []    
    visualization_speed = [0]
    
    listview_controls = [
        ft.Container(
            margin=ft.margin.only(top=10),
            content=ft.Text("Result Point",text_align="CENTER",size=12, font_family="Railinc")
        ),
        ft.Divider(color="#000000")
    ]
        
    # Implementation
    def resetPath():
        makeListEmpty(canvas_path)
        makeListEmpty(result_path)
        makeListEmpty(result_circle)
        process_time[0] = 0
        makeListEmpty(cartesian_line_result_canvas)
        makeListEmpty(cartesian_text_number_result_canvas)
        makeListEmpty(listview_controls)
        listview_controls.append(
            ft.Container(
                margin=ft.margin.only(top=10),
                content=ft.Text("Result Point",text_align="CENTER",size=15, font_family="Railinc")
            )
        )
        listview_controls.append(
            ft.Divider(color="#000000")
        )
        
    def resetInitial():
        makeListEmpty(initial_points)
        makeListEmpty(coordinate_points)
        makeListEmpty(initial_circle)
        makeListEmpty(cartesian_line_canvas)
        makeListEmpty(cartesian_text_number_canvas)
        makeListEmpty(initial_canvas_axis)
        makeListEmpty(initial_canvas_ordinat)
        process_time[0] = 0
        range_x[0] = 0
        range_y[0] = 0
    
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
        s = 5
        initial_circle.append(cv.Path.Oval(p[0]-(0.5*s),p[1]-(0.5*s),s,s))
        page.update()
        
    def insertToPathResultCircle(p):
        s = 5
        result_circle.append(cv.Path.Oval(p[0]-(0.5*s),p[1]-(0.5*s),s,s))
        page.update()
        
    def insertToPathCartesianLineCanvas(ps):
        if(ps[1] == "m"):
            cartesian_line_canvas.append(cv.Path.MoveTo(ps[0][0],ps[0][1]))
        else:
            cartesian_line_canvas.append(cv.Path.LineTo(ps[0][0],ps[0][1]))
        page.update()
        
    def insertToPathCartesianLineResultCanvas(ps):
        if(ps[1] == "m"):
            cartesian_line_result_canvas.append(cv.Path.MoveTo(ps[0][0],ps[0][1]))
        else:
            cartesian_line_result_canvas.append(cv.Path.LineTo(ps[0][0],ps[0][1]))
        page.update()
        
    def insertToPathCartesianTextNumberCanvas(ps):
        cartesian_text_number_canvas.append(
            cv.Text(
                ps[0][0]-5,
                ps[0][1]-5,
                ps[1],
                ft.TextStyle(size=ps[2]),
            )
        )
        page.update()
        
    def insertToPathCartesianTextNumberResultCanvas(ps):
        t = cv.Text(
                ps[0][0]-5,
                ps[0][1]-5,
                ps[1],
                ft.TextStyle(size=ps[2]),
            )
        if(t not in cartesian_text_number_result_canvas and t not in cartesian_text_number_canvas):
            cartesian_text_number_result_canvas.append(t)
        page.update()
        
    def insertToListView(p):
        if(str(p[0]) == "process time"):
            listview_controls.append(
                ft.Container(
                    margin=ft.margin.only(left=15),
                    content=ft.Column(
                        controls=[
                            ft.Text("Process time (Netto): " + str(p[1]*1000) + " ms",size=12,color="#000000", weight=800,font_family="Railinc"),
                            ft.Text(" ",size=5,color="#000000"),
                        ]
                    )
                )
            )
        else:
            listview_controls.append(
                ft.Container(
                    margin=ft.margin.only(left=15),
                    content=ft.Column(
                        controls=[
                            ft.Text(str(len(listview_controls)-1)+ ". " + str(p),size=12,color="#000000"),
                            ft.Text(" ",size=5,color="#000000"),
                        ]
                    )
                )
            )
        page.update()
    
    def initCoordinate_to_canvasCoordinate(p):
        min_y = min([point[1] for point in initial_points])
        min_x = min([point[0] for point in initial_points])
        if(range_y[0] > range_x[0]):
            coordinate_multiplier = float((app_h*0.85)/range_y[0])
            y = (app_h*0.85) - ((p[1]-min_y)*coordinate_multiplier)
            x = p[0]*coordinate_multiplier + (float(((app_h*0.85)-(range_x[0]*coordinate_multiplier))/2)-(min_x*coordinate_multiplier))
        else:
            coordinate_multiplier = float((app_h*0.85)/range_x[0])
            x = (p[0]-min_x)*coordinate_multiplier
            y = (app_h*0.85)-(p[1]*coordinate_multiplier + (float(((app_h*0.85)-(range_y[0]*coordinate_multiplier))/2)-(min_y*coordinate_multiplier)))
        return (x,y)
    
    def getMidPoint(p1,p2):
        x = float((p1[0]+p2[0])/2 )
        y = float((p1[1]+p2[1])/2)
        pout = (x,y)
        return pout
    
    def BezierN_process_time(points, iterasi, iterasiMax):
        if (iterasi >= iterasiMax):
            return []
        else:
            q = points
            left = [q[0]]
            right = [q[-1]]
            while len(q) > 1:
                temp = q
                q = [getMidPoint(temp[i], temp[i+1]) for i in range(len(temp)-1)]
                
                left.append(q[0])
                right.append(q[-1])
            right.reverse()
            if iterasi == 0:
                iterasi += 1
                output = [points[0]] + BezierN_process_time(left, iterasi, iterasiMax)
                return  output + [left[-1]] + BezierN_process_time(right, iterasi, iterasiMax) + [points[-1]]
            else:
                iterasi += 1
                output = BezierN_process_time(left, iterasi, iterasiMax)
                return output + [left[-1]] + BezierN_process_time(right, iterasi, iterasiMax)
            
    def BezierN(points, iterasi, iterasiMax):
        if(iterasi == 0):
            insertToPathResultCircle(initCoordinate_to_canvasCoordinate(points[0]))
            insertToListView(points[0])
        offset=5
        if (iterasi >= iterasiMax):
            return []
        else:
            q = points
            left = [q[0]]
            right = [q[-1]]
            while len(q) > 1:
                temp = q
                q = [getMidPoint(temp[i], temp[i+1]) for i in range(len(temp)-1)]
                left.append(q[0])
                right.append(q[-1])
                for i in range(len(temp)):
                    if(i == 0):
                        insertToPath((initCoordinate_to_canvasCoordinate(temp[0]),"m"))
                    else:
                        insertToPath((initCoordinate_to_canvasCoordinate(temp[i]),"l"))
            right.reverse()
            canvas_point = initCoordinate_to_canvasCoordinate(q[0])
            if(iterasi == iterasiMax-1):
                
                insertToPathResultCircle(canvas_point)
                
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85-offset),"m"))
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85+offset),"l"))
                insertToPathCartesianTextNumberResultCanvas(((canvas_point[0],0+app_h*0.85+offset+15),str(round(q[0][0],2)),8))
                
                insertToPathCartesianLineResultCanvas(((0-offset,canvas_point[1]),"m"))
                insertToPathCartesianLineResultCanvas(((0+offset,canvas_point[1]),"l"))
                insertToPathCartesianTextNumberResultCanvas(((0-offset-15,canvas_point[1]),str(round(q[0][1],2)),8))
                
                insertToPathResult((initCoordinate_to_canvasCoordinate(points[0]),"m"))
                insertToPathResult((canvas_point,"l"))
                insertToPathResult((initCoordinate_to_canvasCoordinate(points[-1]),"l"))
            elif(iterasi < iterasiMax-1):
                insertToPath((initCoordinate_to_canvasCoordinate(points[0]),"m"))
                insertToPath((canvas_point,"l"))
                insertToPath((initCoordinate_to_canvasCoordinate(points[-1]),"l"))
                
            if iterasi == 0:
                iterasi += 1
                
                output = [points[0]]
                
                output += BezierN(left, iterasi, iterasiMax)
                
                insertToListView(left[-1])
                
                canvas_point = initCoordinate_to_canvasCoordinate(left[-1])
                insertToPathResultCircle(canvas_point)
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85-offset),"m"))
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85+offset),"l"))
                insertToPathCartesianTextNumberResultCanvas(((canvas_point[0],0+app_h*0.85+offset+15),str(round(left[-1][0],2)),8))
                
                insertToPathCartesianLineResultCanvas(((0-offset,canvas_point[1]),"m"))
                insertToPathCartesianLineResultCanvas(((0+offset,canvas_point[1]),"l"))
                insertToPathCartesianTextNumberResultCanvas(((0-offset-15,canvas_point[1]),str(round(left[-1][1],2)),8))
                
                output += [left[-1]]
                
                output += BezierN(right, iterasi, iterasiMax)
                
                output += [points[-1]]
                
                insertToPathResultCircle(initCoordinate_to_canvasCoordinate(points[-1]))
                insertToListView(points[-1])
                return output
            
            else:
                iterasi += 1
                output = BezierN(left, iterasi, iterasiMax)
                
                insertToListView(left[-1])
                
                canvas_point = initCoordinate_to_canvasCoordinate(left[-1])
                insertToPathResultCircle(canvas_point)
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85-offset),"m"))
                insertToPathCartesianLineResultCanvas(((canvas_point[0],0+app_h*0.85+offset),"l"))
                insertToPathCartesianTextNumberResultCanvas(((canvas_point[0],0+app_h*0.85+offset+15),str(round(left[-1][0],2)),8))
                
                insertToPathCartesianLineResultCanvas(((0-offset,canvas_point[1]),"m"))
                insertToPathCartesianLineResultCanvas(((0+offset,canvas_point[1]),"l"))
                insertToPathCartesianTextNumberResultCanvas(((0-offset-15,canvas_point[1]),str(round(left[-1][1],2)),8))
                
                output += [left[-1]]
                
                output += BezierN(right, iterasi, iterasiMax)
                
                return output
    
    def buttonVisualizeClicked(e):
        resetPath()
        e.control.visible = False
        BezierN(initial_points,0,num_of_iteration[0])
        startT = time.time()
        BezierN_process_time(initial_points,0,num_of_iteration[0])
        endT = time.time()
        process_time[0] = endT-startT
        insertToListView(("process time",endT-startT))
        e.control.visible = True
        page.update()
    
    buttonVisualize = ft.ElevatedButton(
        style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: "#FFFFFF",
                    ft.MaterialState.HOVERED: "#000000",
                    ft.MaterialState.DISABLED: "#000000",
                },
                bgcolor={ft.MaterialState.DEFAULT: "#000000",
                         ft.MaterialState.HOVERED: "#FFFFFF",
                         ft.MaterialState.DISABLED: "#FFFFFF"
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
        content=ft.Text("Visualize!",size=15,font_family="Railinc")
    )
    
    def inputChanged(e):
        resetInitial()
        resetPath()
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
                        try:
                            x = float(point[0])
                            y = float(point[1])
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
                # Draw Axis and Ordinat line
                insertToPathCartesianLineCanvas(((0,0),"m"))
                insertToPathCartesianLineCanvas(((0,0+app_h*0.85),"l"))
                insertToPathCartesianLineCanvas(((0+app_h*0.85,0+app_h*0.85),"l"))
                # Draw Circle (Dot)
                for i in range(len(coordinate_points)):
                    point = coordinate_points[i]
                    insertToPathCircle(point)
                    offset = 5
                    if(point[0] not in initial_canvas_axis):
                        insertToPathCartesianLineCanvas(((point[0],0+app_h*0.85-offset),"m"))
                        insertToPathCartesianLineCanvas(((point[0],0+app_h*0.85+offset),"l"))
                        insertToPathCartesianTextNumberCanvas(((point[0],0+app_h*0.85+offset+15),str(round(initial_points[i][0],2)),8))
                        initial_canvas_axis.append(point[0])
                    if(point[1] not in initial_canvas_ordinat):
                        insertToPathCartesianLineCanvas(((0-offset,point[1]),"m"))
                        insertToPathCartesianLineCanvas(((0+offset,point[1]),"l"))
                        insertToPathCartesianTextNumberCanvas(((0-offset-15,point[1]),str(round(initial_points[i][1],2)),8))
                        initial_canvas_ordinat.append(point[1])                    
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
        height=app_h*0.92,
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
                                        margin=ft.margin.only(left=20,bottom=20),
                                        content=ft.Column(
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    cartesian_line_canvas,
                                                                    paint=paint_cartesian_line_canvas
                                                                )
                                                            ],
                                                            width=float("inf"),
                                                            expand=True,
                                                        ),
                                                        cv.Canvas(
                                                            [
                                                                cv.Path(
                                                                    cartesian_line_result_canvas,
                                                                    paint=paint_cartesian_line_canvas
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
                                                        cv.Canvas(
                                                            cartesian_text_number_canvas
                                                        ),
                                                        cv.Canvas(
                                                            cartesian_text_number_result_canvas
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
                                                    width=app_w*0.18,
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
                                        margin=ft.margin.only(top=10,bottom=10),
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
                                                    divisions=100,
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
                                    ),
                                    # ListView
                                    ft.Container(
                                        width=0.25*app_w,
                                        height=app_h*0.3,
                                        border=ft.border.all(2, "#000000"),
                                        border_radius=15,
                                        content=ft.ListView(
                                            auto_scroll=True,
                                            controls=listview_controls,
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


        
    