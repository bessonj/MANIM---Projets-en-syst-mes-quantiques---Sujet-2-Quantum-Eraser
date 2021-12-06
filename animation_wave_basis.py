from manim import *
from manim_physics import *
import numpy as np
from manim.scene.three_d_scene import * 

import sys
sys.setrecursionlimit(10000)

from manim import *

class Oscillating_Arrows_3D(ThreeDScene):
    def construct(self):
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        axes = ThreeDAxes(x_range,y_range,z_range)
        N=15
        amp=2
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)

#        grid = NumberPlane()
#        grid_title = Tex("2D grid", font_size=72)
#        self.add(grid, grid_title)  # Make sure title is on top of grid

        d_i = VGroup()
        for i in range(N):
            d_i.add(Dot([0,i/N*alpha,0],fill_opacity=0.))
        d_fE = VGroup()
        for i in range(N):
            d_fE.add(Dot([0,i/N*alpha,0],fill_opacity=0.,color=BLUE))
        d_fB = VGroup()
        for i in range(N):
            d_fB.add(Dot([i/N*alpha,0,0],fill_opacity=0.,color=YELLOW))
        linesE = VGroup()
        for i in range(N):
            linesE.add(Arrow(d_i[i].get_center(),d_fE[i].get_center(),color=BLUE))
        linesB = VGroup()
        for i in range(N):
            linesB.add(Arrow(d_i[i].get_center(),d_fB[i].get_center(),color=YELLOW))

        t=ValueTracker(0)
        t.set_value(-min_x-14/N*alpha)

        d_i[0].add_updater(lambda z: z.set_y(t.get_value()))
        d_i[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
        d_i[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
        d_i[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))
        d_i[4].add_updater(lambda z: z.set_y(t.get_value()+4/N*alpha))
        d_i[5].add_updater(lambda z: z.set_y(t.get_value()+5/N*alpha))
        d_i[6].add_updater(lambda z: z.set_y(t.get_value()+6/N*alpha))
        d_i[7].add_updater(lambda z: z.set_y(t.get_value()+7/N*alpha))
        d_i[8].add_updater(lambda z: z.set_y(t.get_value()+8/N*alpha))
        d_i[9].add_updater(lambda z: z.set_y(t.get_value()+9/N*alpha))
        d_i[10].add_updater(lambda z: z.set_y(t.get_value()+10/N*alpha))
        d_i[11].add_updater(lambda z: z.set_y(t.get_value()+11/N*alpha))
        d_i[12].add_updater(lambda z: z.set_y(t.get_value()+12/N*alpha))
        d_i[13].add_updater(lambda z: z.set_y(t.get_value()+13/N*alpha))
        d_i[14].add_updater(lambda z: z.set_y(t.get_value()+14/N*alpha))

        d_i[0].set_z(0)
        d_i[1].set_z(0)
        d_i[2].set_z(0)
        d_i[3].set_z(0)
        d_i[4].set_z(0)
        d_i[5].set_z(0)
        d_i[6].set_z(0)
        d_i[7].set_z(0)
        d_i[8].set_z(0)
        d_i[9].set_z(0)
        d_i[10].set_z(0)
        d_i[11].set_z(0)
        d_i[12].set_z(0)
        d_i[13].set_z(0)
        d_i[14].set_z(0)

#E FIELD
        d_fE[0].add_updater(lambda z: z.set_y(t.get_value()))
        d_fE[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
        d_fE[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
        d_fE[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))
        d_fE[4].add_updater(lambda z: z.set_y(t.get_value()+4/N*alpha))
        d_fE[5].add_updater(lambda z: z.set_y(t.get_value()+5/N*alpha))
        d_fE[6].add_updater(lambda z: z.set_y(t.get_value()+6/N*alpha))
        d_fE[7].add_updater(lambda z: z.set_y(t.get_value()+7/N*alpha))
        d_fE[8].add_updater(lambda z: z.set_y(t.get_value()+8/N*alpha))
        d_fE[9].add_updater(lambda z: z.set_y(t.get_value()+9/N*alpha))
        d_fE[10].add_updater(lambda z: z.set_y(t.get_value()+10/N*alpha))
        d_fE[11].add_updater(lambda z: z.set_y(t.get_value()+11/N*alpha))
        d_fE[12].add_updater(lambda z: z.set_y(t.get_value()+12/N*alpha))
        d_fE[13].add_updater(lambda z: z.set_y(t.get_value()+13/N*alpha))
        d_fE[14].add_updater(lambda z: z.set_y(t.get_value()+14/N*alpha))

        d_fE[0].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+0/N*alpha)))
        d_fE[1].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+1/N*alpha)))
        d_fE[2].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+2/N*alpha)))
        d_fE[3].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+3/N*alpha)))
        d_fE[4].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+4/N*alpha)))
        d_fE[5].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+5/N*alpha)))
        d_fE[6].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+6/N*alpha)))
        d_fE[7].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+7/N*alpha)))
        d_fE[8].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+8/N*alpha)))
        d_fE[9].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+9/N*alpha)))
        d_fE[10].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+10/N*alpha)))
        d_fE[11].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+11/N*alpha)))
        d_fE[12].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+12/N*alpha)))
        d_fE[13].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+13/N*alpha)))
        d_fE[14].add_updater(lambda z: z.set_z(amp*np.sin(3*t.get_value()+14/N*alpha)))

        linesE[0].add_updater(lambda z: z.become(Arrow(d_i[0].get_center(),d_fE[0].get_center(),buff=0,color=BLUE)))
        linesE[1].add_updater(lambda z: z.become(Arrow(d_i[1].get_center(),d_fE[1].get_center(),buff=0,color=BLUE)))
        linesE[2].add_updater(lambda z: z.become(Arrow(d_i[2].get_center(),d_fE[2].get_center(),buff=0,color=BLUE)))
        linesE[3].add_updater(lambda z: z.become(Arrow(d_i[3].get_center(),d_fE[3].get_center(),buff=0,color=BLUE)))
        linesE[4].add_updater(lambda z: z.become(Arrow(d_i[4].get_center(),d_fE[4].get_center(),buff=0,color=BLUE)))
        linesE[5].add_updater(lambda z: z.become(Arrow(d_i[5].get_center(),d_fE[5].get_center(),buff=0,color=BLUE)))
        linesE[6].add_updater(lambda z: z.become(Arrow(d_i[6].get_center(),d_fE[6].get_center(),buff=0,color=BLUE)))
        linesE[7].add_updater(lambda z: z.become(Arrow(d_i[7].get_center(),d_fE[7].get_center(),buff=0,color=BLUE)))
        linesE[8].add_updater(lambda z: z.become(Arrow(d_i[8].get_center(),d_fE[8].get_center(),buff=0,color=BLUE)))
        linesE[9].add_updater(lambda z: z.become(Arrow(d_i[9].get_center(),d_fE[9].get_center(),buff=0,color=BLUE)))
        linesE[10].add_updater(lambda z: z.become(Arrow(d_i[10].get_center(),d_fE[10].get_center(),buff=0,color=BLUE)))
        linesE[11].add_updater(lambda z: z.become(Arrow(d_i[11].get_center(),d_fE[11].get_center(),buff=0,color=BLUE)))
        linesE[12].add_updater(lambda z: z.become(Arrow(d_i[12].get_center(),d_fE[12].get_center(),buff=0,color=BLUE)))
        linesE[13].add_updater(lambda z: z.become(Arrow(d_i[13].get_center(),d_fE[13].get_center(),buff=0,color=BLUE)))
        linesE[14].add_updater(lambda z: z.become(Arrow(d_i[14].get_center(),d_fE[14].get_center(),buff=0,color=BLUE)))


#B FIELD
        d_fB[0].add_updater(lambda z: z.set_y(t.get_value()))
        d_fB[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
        d_fB[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
        d_fB[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))
        d_fB[4].add_updater(lambda z: z.set_y(t.get_value()+4/N*alpha))
        d_fB[5].add_updater(lambda z: z.set_y(t.get_value()+5/N*alpha))
        d_fB[6].add_updater(lambda z: z.set_y(t.get_value()+6/N*alpha))
        d_fB[7].add_updater(lambda z: z.set_y(t.get_value()+7/N*alpha))
        d_fB[8].add_updater(lambda z: z.set_y(t.get_value()+8/N*alpha))
        d_fB[9].add_updater(lambda z: z.set_y(t.get_value()+9/N*alpha))
        d_fB[10].add_updater(lambda z: z.set_y(t.get_value()+10/N*alpha))
        d_fB[11].add_updater(lambda z: z.set_y(t.get_value()+11/N*alpha))
        d_fB[12].add_updater(lambda z: z.set_y(t.get_value()+12/N*alpha))
        d_fB[13].add_updater(lambda z: z.set_y(t.get_value()+13/N*alpha))
        d_fB[14].add_updater(lambda z: z.set_y(t.get_value()+14/N*alpha))

        d_fB[0].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+0/N*alpha)))
        d_fB[1].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+1/N*alpha)))
        d_fB[2].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+2/N*alpha)))
        d_fB[3].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+3/N*alpha)))
        d_fB[4].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+4/N*alpha)))
        d_fB[5].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+5/N*alpha)))
        d_fB[6].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+6/N*alpha)))
        d_fB[7].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+7/N*alpha)))
        d_fB[8].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+8/N*alpha)))
        d_fB[9].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+9/N*alpha)))
        d_fB[10].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+10/N*alpha)))
        d_fB[11].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+11/N*alpha)))
        d_fB[12].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+12/N*alpha)))
        d_fB[13].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+13/N*alpha)))
        d_fB[14].add_updater(lambda z: z.set_x(amp*np.sin(3*t.get_value()+14/N*alpha)))

        linesB[0].add_updater(lambda z: z.become(Arrow(d_i[0].get_center(),d_fB[0].get_center(),buff=0,color=YELLOW)))
        linesB[1].add_updater(lambda z: z.become(Arrow(d_i[1].get_center(),d_fB[1].get_center(),buff=0,color=YELLOW)))
        linesB[2].add_updater(lambda z: z.become(Arrow(d_i[2].get_center(),d_fB[2].get_center(),buff=0,color=YELLOW)))
        linesB[3].add_updater(lambda z: z.become(Arrow(d_i[3].get_center(),d_fB[3].get_center(),buff=0,color=YELLOW)))
        linesB[4].add_updater(lambda z: z.become(Arrow(d_i[4].get_center(),d_fB[4].get_center(),buff=0,color=YELLOW)))
        linesB[5].add_updater(lambda z: z.become(Arrow(d_i[5].get_center(),d_fB[5].get_center(),buff=0,color=YELLOW)))
        linesB[6].add_updater(lambda z: z.become(Arrow(d_i[6].get_center(),d_fB[6].get_center(),buff=0,color=YELLOW)))
        linesB[7].add_updater(lambda z: z.become(Arrow(d_i[7].get_center(),d_fB[7].get_center(),buff=0,color=YELLOW)))
        linesB[8].add_updater(lambda z: z.become(Arrow(d_i[8].get_center(),d_fB[8].get_center(),buff=0,color=YELLOW)))
        linesB[9].add_updater(lambda z: z.become(Arrow(d_i[9].get_center(),d_fB[9].get_center(),buff=0,color=YELLOW)))
        linesB[10].add_updater(lambda z: z.become(Arrow(d_i[10].get_center(),d_fB[10].get_center(),buff=0,color=YELLOW)))
        linesB[11].add_updater(lambda z: z.become(Arrow(d_i[11].get_center(),d_fB[11].get_center(),buff=0,color=YELLOW)))
        linesB[12].add_updater(lambda z: z.become(Arrow(d_i[12].get_center(),d_fB[12].get_center(),buff=0,color=YELLOW)))
        linesB[13].add_updater(lambda z: z.become(Arrow(d_i[13].get_center(),d_fB[13].get_center(),buff=0,color=YELLOW)))
        linesB[14].add_updater(lambda z: z.become(Arrow(d_i[14].get_center(),d_fB[14].get_center(),buff=0,color=YELLOW)))



        self.add(d_i,d_fE,d_fB,linesE,linesB)
        self.play(t.animate.increment_value(5),run_time=5,rate_func=linear)
#        self.play(y.animate.set_value(4))
        self.wait()


class PolarizingFilter(Circle):
    CONFIG = {
        "stroke_color" : GREY_D,
        "fill_color" : GREY_B,
        "fill_opacity" : 0.5,
        "label_tex" : None,
        "filter_angle" : 0,
        "include_arrow_label" : True,
        "arrow_length" : 0.7,
    }
    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)

        if self.label_tex:
            self.label = Tex(self.label_tex)
            self.label.next_to(self.get_top(), DOWN, MED_SMALL_BUFF)
            self.add(self.label)

        arrow = Arrow(
            ORIGIN, self.arrow_length*UP, 
            color = WHITE,
            buff = 0,
        )
        arrow.shift(self.get_top())
        arrow.rotate(-self.filter_angle)
        self.add(arrow)
        self.arrow = arrow
        shade_in_3d(self)

        if self.include_arrow_label:
            arrow_label = Tex(
                "%.1f^\\circ"%(self.filter_angle*180/np.pi)
            )
            arrow_label.add_background_rectangle()
            arrow_label.next_to(arrow.get_tip(), UP)
            self.add(arrow_label)
            self.arrow_label = arrow_label

class Oscillating_Arrows_3D_ok(ThreeDScene):
    def construct(self):
        N=4
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text('Hello world', gradient=(BLUE, GREEN))
        text3d.rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-2.5,2])
#        self.add_fixed_in_frame_mobjects(text3d)
#        text3d.to_corner(UL)

        pol = Polarizer()

        self.add(axes,text3d,pol.disk,pol.vector)

        self.wait(1)

        if False :
            pol.color_polarizer(np.pi/3)
            self.add(pol.di,pol.df)
            self.play(pol.t.animate.set_value(np.pi/3),run_time=3)#,rate_func=linear)

#        grid = NumberPlane()
#        grid_title = Tex("2D grid", font_size=72)
#        self.add(grid, grid_title)  # Make sure title is on top of grid

        d_i = VGroup()
        for i in range(N):
            d_i.add(Dot([0,i/N*alpha,0],fill_opacity=0.))
        d_f = VGroup()
        for i in range(N):
            d_f.add(Dot([0,i/N*alpha,0],fill_opacity=0.))
        lines = VGroup()
        for i in range(N):
            lines.add(Arrow(d_i[i].get_center(),d_f[i].get_center()).set_color(BLUE))

        t=ValueTracker(0)
        t.set_value(-min_x-14/N*alpha)

        if False :
            d_i[0].add_updater(lambda z: z.set_x(t.get_value()))
            d_i[0].set_y(0)
            for i in range(1,N):
                d_i[i].add_updater(lambda z: z.set_x(d_i[0].get_center()))
            for i in range(N):
                d_i[i].set_y(0)
                d_f[i].add_updater(lambda z: z.set_x(t.get_value()+i/N))
                d_f[i].add_updater(lambda z: z.set_y(2*np.sin(3*t.get_value()+i/N)))
#            for i in range(N):
#                lines[i].add_updater(lambda z: z.become(Line(d_i[i].get_center(),d_f[i].get_center())))
        else :
            d_i[0].add_updater(lambda z: z.set_y(t.get_value()))
            d_i[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
            d_i[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
            d_i[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))
            d_i[0].set_z(0)
            d_i[1].set_z(0)
            d_i[2].set_z(0)
            d_i[3].set_z(0)

            d_f[0].add_updater(lambda z: z.set_y(t.get_value()))
            d_f[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
            d_f[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
            d_f[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))

            d_f[0].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+0/N*alpha),1)*2*np.sin(3*t.get_value()+0/N*alpha)))
            d_f[1].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+1/N*alpha),1)*2*np.sin(3*t.get_value()+1/N*alpha)))
            d_f[2].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+2/N*alpha),1)*2*np.sin(3*t.get_value()+2/N*alpha)))
            d_f[3].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+3/N*alpha),1)*2*np.sin(3*t.get_value()+3/N*alpha)))

            lines[0].add_updater(lambda z: z.become(Arrow(d_i[0].get_center(),d_f[0].get_center(),buff=0,color=BLUE)))
            lines[1].add_updater(lambda z: z.become(Arrow(d_i[1].get_center(),d_f[1].get_center(),buff=0,color=BLUE)))
            lines[2].add_updater(lambda z: z.become(Arrow(d_i[2].get_center(),d_f[2].get_center(),buff=0,color=BLUE)))
            lines[3].add_updater(lambda z: z.become(Arrow(d_i[3].get_center(),d_f[3].get_center(),buff=0,color=BLUE)))

        self.add(d_i,d_f,lines)
        self.play(t.animate.increment_value(10),run_time=5,rate_func=linear)
        self.wait(1)
#        self.move_camera(theta = np.pi/2)
#        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(5)


class OrientedOscillating_Arrows_3D_ok(ThreeDScene):
    def construct(self):
        N=4
        angle_in = np.pi/4
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text('Hello world', gradient=(BLUE, GREEN))
        text3d.rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-2.5,2])
#        self.add_fixed_in_frame_mobjects(text3d)
#        text3d.to_corner(UL)

        pol = Polarizer()

        self.add(axes,text3d,pol.disk,pol.vector)

        self.wait(1)

        if False :
            pol.color_polarizer(np.pi/3)
            self.add(pol.di,pol.df)
            self.play(pol.t.animate.set_value(np.pi/3),run_time=3)#,rate_func=linear)

#        grid = NumberPlane()
#        grid_title = Tex("2D grid", font_size=72)
#        self.add(grid, grid_title)  # Make sure title is on top of grid

        d_i = VGroup()
        for i in range(N):
            d_i.add(Dot([0,i/N*alpha,0],fill_opacity=0.))
        d_f = VGroup()
        for i in range(N):
            d_f.add(Dot([0,i/N*alpha,0],fill_opacity=0.))
        lines = VGroup()
        for i in range(N):
            lines.add(Arrow(d_i[i].get_center(),d_f[i].get_center()).set_color(BLUE))

        t=ValueTracker(0)
        t.set_value(-min_x-14/N*alpha)

        if False :
            d_i[0].add_updater(lambda z: z.set_x(t.get_value()))
            d_i[0].set_y(0)
            for i in range(1,N):
                d_i[i].add_updater(lambda z: z.set_x(d_i[0].get_center()))
            for i in range(N):
                d_i[i].set_y(0)
                d_f[i].add_updater(lambda z: z.set_x(t.get_value()+i/N))
                d_f[i].add_updater(lambda z: z.set_y(2*np.sin(3*t.get_value()+i/N)))
#            for i in range(N):
#                lines[i].add_updater(lambda z: z.become(Line(d_i[i].get_center(),d_f[i].get_center())))
        else :
            d_i[0].add_updater(lambda z: z.set_y(t.get_value()))
            d_i[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
            d_i[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
            d_i[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))
            d_i[0].set_z(0)
            d_i[1].set_z(0)
            d_i[2].set_z(0)
            d_i[3].set_z(0)

            d_f[0].add_updater(lambda z: z.set_y(t.get_value()))
            d_f[1].add_updater(lambda z: z.set_y(t.get_value()+1/N*alpha))
            d_f[2].add_updater(lambda z: z.set_y(t.get_value()+2/N*alpha))
            d_f[3].add_updater(lambda z: z.set_y(t.get_value()+3/N*alpha))

            d_f[0].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+0/N*alpha),1)*2*np.sin(3*t.get_value()+0/N*alpha)*np.sin(angle_in)))
            d_f[1].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+1/N*alpha),1)*2*np.sin(3*t.get_value()+1/N*alpha)*np.sin(angle_in)))
            d_f[2].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+2/N*alpha),1)*2*np.sin(3*t.get_value()+2/N*alpha)*np.sin(angle_in)))
            d_f[3].add_updater(lambda z: z.set_z(np.heaviside(-(t.get_value()+3/N*alpha),1)*2*np.sin(3*t.get_value()+3/N*alpha)*np.sin(angle_in)))
            d_f[0].add_updater(lambda z: z.set_x(np.heaviside(-(t.get_value()+0/N*alpha),1)*2*np.sin(3*t.get_value()+0/N*alpha)*np.cos(angle_in)))
            d_f[1].add_updater(lambda z: z.set_x(np.heaviside(-(t.get_value()+1/N*alpha),1)*2*np.sin(3*t.get_value()+1/N*alpha)*np.cos(angle_in)))
            d_f[2].add_updater(lambda z: z.set_x(np.heaviside(-(t.get_value()+2/N*alpha),1)*2*np.sin(3*t.get_value()+2/N*alpha)*np.cos(angle_in)))
            d_f[3].add_updater(lambda z: z.set_x(np.heaviside(-(t.get_value()+3/N*alpha),1)*2*np.sin(3*t.get_value()+3/N*alpha)*np.cos(angle_in)))

            lines[0].add_updater(lambda z: z.become(Arrow(d_i[0].get_center(),d_f[0].get_center(),buff=0,color=BLUE)))
            lines[1].add_updater(lambda z: z.become(Arrow(d_i[1].get_center(),d_f[1].get_center(),buff=0,color=BLUE)))
            lines[2].add_updater(lambda z: z.become(Arrow(d_i[2].get_center(),d_f[2].get_center(),buff=0,color=BLUE)))
            lines[3].add_updater(lambda z: z.become(Arrow(d_i[3].get_center(),d_f[3].get_center(),buff=0,color=BLUE)))

        self.add(d_i,d_f,lines)
        self.play(t.animate.increment_value(10),run_time=5,rate_func=linear)
        self.wait(1)
#        self.move_camera(theta = np.pi/2)
#        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(5)

class Oriented_Oscillating_Arrows_3D(ThreeDScene):
    def __init__(
        self,
        alpha = 3,
        angle_pol=np.pi/2,
        N = 4,
        min_x=-5,
        min_y=-5,
        min_z=-5,
        max_x=5,
        max_y=5,
        max_z=5,
        angle_in = np.pi/4,
        default_opacity = 0.6,
        **kwargs
    ):
        self.angle_in=angle_in
        self.alpha = alpha
        self.angle_pol=angle_pol
        self.N=N
        self.min_x=min_x
        self.min_y=min_y
        self.min_z=min_z
        self.max_x=max_x
        self.max_y=max_y
        self.max_z=max_z
#    def __call__(self, self.t):
#        self.disk.become(Circle(radius=self.radius, color=GREY, fill_opacity=0.75+0.25*np.sin(angle)).rotate(np.pi/2, [1,0,0]))
#        self.add_fixed_in_frame_mobjects(text3d)
#        text3d.to_corner(UL)

#        grid = NumberPlane()
#        grid_title = Tex("2D grid", font_size=72)
#        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.d_i = VGroup()
        for i in range(N):
            self.d_i.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        self.d_f = VGroup()
        for i in range(N):
            self.d_f.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        self.d_f_green = VGroup()
        for i in range(N):
            self.d_f_green.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        self.lines = VGroup()
        for i in range(N):
            self.lines.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(BLUE))
        self.lines_green = VGroup()
        for i in range(N):
            self.lines_green.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(BLUE))

        self.t=ValueTracker(0)
        self.t.set_value(-self.min_x-14/self.N*self.alpha)

        if False :
            self.d_i[0].add_updater(lambda z: z.set_x(self.t.get_value()))
            self.d_i[0].set_y(0)
            for i in range(1,N):
                self.d_i[i].add_updater(lambda z: z.set_x(self.d_i[0].get_center()))
            for i in range(N):
                self.d_i[i].set_y(0)
                self.d_f[i].add_updater(lambda z: z.set_x(self.t.get_value()+i/N))
                self.d_f[i].add_updater(lambda z: z.set_y(2*np.sin(3*self.t.get_value()+i/N)))
#            for i in range(N):
#                lines[i].add_updater(lambda z: z.become(Line(self.d_i[i].get_center(),self.d_f[i].get_center())))
        else :
            self.d_i[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_i[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_i[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_i[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))
            self.d_i[0].set_z(0)
            self.d_i[1].set_z(0)
            self.d_i[2].set_z(0)
            self.d_i[3].set_z(0)

            self.d_f[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))
            self.d_f_green[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f_green[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f_green[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f_green[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))

            self.d_f[0].add_updater(lambda z: z.set_z(np.heaviside(-(self.t.get_value()+0/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_z(np.heaviside(-(self.t.get_value()+1/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_z(np.heaviside(-(self.t.get_value()+2/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_z(np.heaviside(-(self.t.get_value()+3/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[0].add_updater(lambda z: z.set_x(np.heaviside(-(self.t.get_value()+0/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_x(np.heaviside(-(self.t.get_value()+1/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_x(np.heaviside(-(self.t.get_value()+2/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_x(np.heaviside(-(self.t.get_value()+3/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_in)))

            self.d_f_green[0].add_updater(lambda z: z.set_z(np.heaviside((self.t.get_value()+0/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_pol)))
            self.d_f_green[1].add_updater(lambda z: z.set_z(np.heaviside((self.t.get_value()+1/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_pol)))
            self.d_f_green[2].add_updater(lambda z: z.set_z(np.heaviside((self.t.get_value()+2/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_pol)))
            self.d_f_green[3].add_updater(lambda z: z.set_z(np.heaviside((self.t.get_value()+3/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_pol)))
            self.d_f_green[0].add_updater(lambda z: z.set_x(np.heaviside((self.t.get_value()+0/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_pol)))
            self.d_f_green[1].add_updater(lambda z: z.set_x(np.heaviside((self.t.get_value()+1/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_pol)))
            self.d_f_green[2].add_updater(lambda z: z.set_x(np.heaviside((self.t.get_value()+2/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_pol)))
            self.d_f_green[3].add_updater(lambda z: z.set_x(np.heaviside((self.t.get_value()+3/self.N*self.alpha),1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_pol)))

            self.lines[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f[0].get_center(),buff=0,color=BLUE)))
            self.lines[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f[1].get_center(),buff=0,color=BLUE)))
            self.lines[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f[2].get_center(),buff=0,color=BLUE)))
            self.lines[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f[3].get_center(),buff=0,color=BLUE)))
            self.lines_green[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f_green[0].get_center(),buff=0,color=GREEN)))
            self.lines_green[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f_green[1].get_center(),buff=0,color=GREEN)))
            self.lines_green[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f_green[2].get_center(),buff=0,color=GREEN)))
            self.lines_green[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f_green[3].get_center(),buff=0,color=GREEN)))

class anim_text_(Scene):
    def construct(self):
        equation = MathTex(
            r"La formule est : e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

class anim_text(Scene):
    def construct(self):#r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$', r'$\ket{\rightparrow}$',
        tex = Tex('hello : ',r'$\ket{\psi} = \ket{\nearrow}$', font_size=144).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-2.5,3])
#        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX',r'$\braket{\psi} \langle$', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        tex.set_color_by_tex('angle', BLUE)
        self.add(tex)

class show_text(ThreeDScene):
    def __init__(
        self,
        word1="",
        word2="",
        word3="",
        colors = [GREEN,BLUE,RED],
        **kwargs
    ):
        self.tex_string = Tex(r'$\ket{\nearrow}$','=',r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$','+',r'$\frac{1}{\sqrt{2}}\ket{\rightarrow}$', font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,2])
#        self.tex_string = Tex(r'$\ket{\psi} = \ket{\nearrow}$', r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$', r'$\ket{\rightparrow}$', font_size=144)
        self.tex_string.set_color_by_tex(r'$\ket{\nearrow}$', BLUE)
        self.tex_string.set_color_by_tex(r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$', GREEN)
        self.tex_string.set_color_by_tex(r'$\frac{1}{\sqrt{2}}\ket{\rightarrow}$', RED)

        self.tex_string_right = Tex(r'Réduction du paquet d\textprimstress ondes \\ de ',r'$\ket{\nearrow}$',' à ',r'$\ket{\uparrow}$', font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,3.5,2])
#        self.tex_string = Tex(r'$\ket{\psi} = \ket{\nearrow}$', r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$', r'$\ket{\rightparrow}$', font_size=144)
        self.tex_string_right.set_color_by_tex(r'$\ket{\nearrow}$', BLUE)
        self.tex_string_right.set_color_by_tex(r'$\ket{\uparrow}$', GREEN)
#        self.tex_string.set_color_by_tex('sqrt', BLUE)


class WholeAnimation(ThreeDScene):
    def construct(self):
        N=4
        angle_in = np.pi/4
        angle_pol=np.pi/2
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d1 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,4])
        text3d2 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,3])

        pol = Polarizer()
        math_text=show_text()
        self.add(axes,text3d1,text3d2,pol.disk,pol.vector, math_text.tex_string,math_text.tex_string_right)

        self.wait(1)

        if True :
            pol.color_polarizer(angle_pol)
            self.add(pol.di,pol.df,pol.label)
            self.play(pol.t.animate.set_value(angle_pol),run_time=2)#,rate_func=linear)
        wave=Oriented_Oscillating_Arrows_3D(angle_pol=angle_pol)

        self.add(wave.d_i,wave.d_f,wave.d_f_green,wave.lines,wave.lines_green)
        self.play(wave.t.animate.increment_value(10),run_time=5,rate_func=linear)
        wave.t.set_value(-min_x-14/N*alpha)
        self.wait(1)
        self.move_camera(theta = np.pi/2,phi=np.pi/2)
        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(1)
        self.play(wave.t.animate.increment_value(10),run_time=5,rate_func=linear)
        self.wait()


class Polarizer(ThreeDScene):
    def __init__(
        self,
        radius = 1.5,
		A_vect = np.array([0,0,1]),
        orthogonal_vector=[0,1,0],
        current_angle = 0,
        default_opacity = 0.6,
        **kwargs
    ):
        self.default_opacity=default_opacity
        self.current_position = [0,0,radius]
        self.current_angle=current_angle
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        top = np.array([0,0,radius])
        self.vector = Arrow(top,top+A_vect,buff=0)
        self.disk = Circle(radius=radius, color=GREY, fill_opacity=default_opacity)
        self.disk.rotate(np.pi/2, [0.1,0,0])
#    def __call__(self, self.t):
#        self.disk.become(Circle(radius=self.radius, color=GREY, fill_opacity=0.75+0.25*np.sin(angle)).rotate(np.pi/2, [1,0,0]))

    def color_polarizer(self,angle_in):
        self.t=ValueTracker(0)
        self.t.set_value(self.current_angle)
        self.di,self.df = Dot([self.radius*np.sin(self.current_angle),0,self.radius*np.cos(self.current_angle)],fill_opacity=0.),Dot([(self.radius+1)*np.sin(self.current_angle),0,(self.radius+1)*np.cos(self.current_angle)],fill_opacity=0.)

        self.label = MathTex(r"\alpha").rotate(np.pi/2, [1,0,0]).add_updater(lambda m: m.next_to(self.df, UP))
        self.di.add_updater(lambda z: z.set_z(self.radius*np.cos(self.t.get_value())))
        self.di.add_updater(lambda z: z.set_x(self.radius*np.sin(self.t.get_value())))
        self.df.add_updater(lambda z: z.set_z((self.radius+1)*np.cos(self.t.get_value())))
        self.df.add_updater(lambda z: z.set_x((self.radius+1)*np.sin(self.t.get_value())))

        self.vector.add_updater(lambda z: z.become(Arrow(self.di.get_center(),self.df.get_center(),buff=0)))
        self.disk.add_updater(lambda z: z.become(Circle(radius=self.radius, color=GREY, fill_opacity=self.default_opacity+1/2*(1-self.default_opacity)*np.sin(self.t.get_value())).rotate(np.pi/2, [1,0,0])))

        #self.play(Transform(self.vector, self.vector.rotate_about_origindefault_opacity(angle,self.orthogonal_vector) ))
#        self.vector = self.vector.rotate_about_origin(angle,self.orthogonal_vector) 
#        self.disk.become(Circle(radius=self.radius, color=GREY, fill_opacity=0.75+0.25*np.sin(angle)).rotate(np.pi/2, [1,0,0]))
"""
    def update_mobject(self, dt):
        f = self.frequency
        t = self.internal_time
        angle = 2*np.pi*f*t
        vect = np.array([
            A*np.exp(complex(0, angle + phi))
            for A, phi in zip(self.A_vect, self.phi_vect)
        ]).real
        self.update_tail()
        self.vector.put_start_and_end_on(self.tail, self.tail+vect)

    def update_tail(self):
        if self.vector_to_be_added_to is not None:
            self.tail = self.vector_to_be_added_to.get_end()
"""


class FixedInFrameMObjectTestDynamic(ThreeDScene):
    def construct(self):
        self.n = 25
        self.freq = 2
        self.pos = -TAU
        self.r = 0.3
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)
        curve1 = ParametricFunction(
            lambda u: np.array([
                0,
                u,
                np.sin(self.freq*u)
            ]), color=RED, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
        curve2 = ParametricFunction(
            lambda u: np.array([
                np.sin(self.freq*u),
                u,
                0
            ]), color=BLUE, t_range = np.array([-3*TAU, 5*TAU, 0.01])
        ).set_shade_in_3d(True)
#        self.play(FadeIn(curve1))
        intervalle = np.linspace(0,1,10)
			
        self.arrows1 = VGroup()
        self.arrows2 = VGroup()
        
        self.array_arrows1 = [Arrow([0,self.pos + self.r*i,0], [0,self.pos+self.r*i , np.sin(self.freq*(self.pos + self.r*i))], buff = 0,color = RED) for i in range(self.n+1) ]
        self.array_arrows2 = [Arrow([0,self.pos + self.r*i,0], [np.sin(self.freq*(self.pos + self.r*i)),self.pos + self.r*i , 0], buff = 0,color = BLUE) for i in range(self.n+1) ]

        x=ValueTracker(0)
        y=ValueTracker(0)
        #array_arrows2 = [Arrow([0,self.pos+offset + self.r*i,0], [np.sin(self.freq*(self.pos + self.r*i)),self.pos +offset+ self.r*i , 0], buff = 0,color = BLUE) for i in range(self.n+1) ]
        #arrows = [Arrow([0,self.pos+offset + self.r*i,0], [0,self.pos+offset+self.r*i , np.sin(self.freq*(self.pos + self.r*i))], buff = 0,color = RED) for i in range(self.n+1) ]
        self.arrows1.add(*self.array_arrows1 ) 
        self.arrows2.add(*self.array_arrows2 ) 
        self.add(axes,self.arrows1)
        self.add(axes,self.arrows2)
        for i in range(self.n+1) :
            self.array_arrows1[i].add_updater(lambda z: z.set_x(x.get_value()))
            self.array_arrows2[i].add_updater(lambda z: z.set_y(y.get_value()))
        #self.play(FadeIn(self.arrows1))
        #self.play(FadeIn(self.arrows2))
        #self.play(self.arrows1.animate.shift(dest.get_center() - group[2].get_center()))
        for i in range(self.n+1) :
            self.play(x.animate.set_value(5))
            self.play(y.animate.set_value(4))
        self.wait()

class CameraPosition(ThreeDScene):
	def construct(self):
		self.rate = 0
		self.rate2 = 2*np.pi/150 
		self.set_camera_orientation(phi=80 * DEGREES) #camera starting position
		axis=ThreeDAxes()
		self.add(axis)
		def para(t):
			return np.array((t, 2*np.sin(t),0))
		def para2(t):
			return np.array((t, 0,2*np.sin(t)))

		E_wave = ParametricFunction(para, color = RED, t_range = np.array([-TAU,TAU,0.01]))
		B_wave = ParametricFunction(para2,t_range = np.array([-TAU,TAU,0.01]), color = BLUE)

		n = 20     #number of ticks
		n_frames = 50 #Used 500 for the animation I posted 
		pos = -2*np.pi   #first tick
		r = 0.2    #rate of ticks

		#Tried with arrows, but it bugs, used lines instead
		arrows = VGroup()
		arrows.add(*[Line([pos + r*i,0,0], [pos + r*i , 2*np.sin(pos + r*i) , 0], color = RED)    for i in range(n+ 1 ) ] ) 
		arrows2 = VGroup()
		arrows2.add(*[Line([pos + r*i,0,0], [pos + r*i ,   0 ,  2*np.sin(pos + r*i)], color = BLUE)    for i in range(n+ 1 ) ] ) 

		self.begin_ambient_camera_rotation(rate=0.1)

		for v in range(n_frames):
			self.rate += self.rate2
			self.set_camera_orientation(phi=80 * DEGREES, theta = -np.pi/2 + self.rate/35)
			def para3(t):
				return np.array((t, 2*np.sin(t - self.rate),0))
			def para4(t):
				return np.array((t, 0, 2*np.sin(t - self.rate)))

			E_wave_new = ParametricFunction(para3,t_range = np.array([-TAU,TAU,0.01]), color = RED)
			B_wave_new = ParametricFunction(para4,t_range = np.array([-TAU,TAU,0.01]), color = BLUE)
			new_arrow = VGroup(  *[Line([pos + r*i , 0,0 ], [pos + r*i   ,   2*np.sin(pos + r*i - self.rate  ),0] , color = RED) for i in range(n+ 1) ] ) 
			new_arrow2 = VGroup(  *[Line([pos + r*i , 0,0 ], [pos + r*i   ,  0, 2*np.sin(pos + r*i - self.rate  )] , color = BLUE) for i in range(n+ 1) ] ) 
			self.play( Transform(arrows, new_arrow) , Transform(B_wave_new, B_wave_new) ,Transform(arrows2, new_arrow2) , Transform(E_wave, E_wave_new) ,run_time = 0.05 )



