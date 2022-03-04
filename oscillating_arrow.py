#from animation_EM_wave import *
from manim import *
from manim_physics import *
import numpy as np
from manim.scene.three_d_scene import * 

class Simple_Oriented_Oscillating_Arrows_3D(ThreeDScene):
    def __init__(
        self,
        block=1,
        centered_triangle = False,
        pos_filters=[-2,0,2],
        angle_pol=[0,np.pi/4,np.pi/3],#,4*np.pi/10,np.pi/3],
        colors=[BLUE,GREEN,YELLOW,RED],
        alpha = 3,
        N = 8,
        x_range=(-7,7,1),
        y_range=(-7,7,1),
        z_range=(-7,7,1),
        angle_in = 0,
        origin_shift=-3,
        width_rectangle = 2,
        height_rectangle = 5, 
        default_opacity = 0.6,
        **kwargs
    ):
        self.block=block
        self.origin_shift=origin_shift
        self.x_range=x_range
        self.y_range=y_range
        self.z_range=z_range
        self.min_x=self.x_range[0]
        self.colors=colors
        self.pos_filters=pos_filters
        self.angle_in=angle_in
        self.alpha = alpha
        self.angle_pol=angle_pol
        self.N=N
        #DOTS
        self.d_i = VGroup()
        for i in range(N):
            self.d_i.add(Dot([0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        self.d_f = VGroup()
        for i in range(N):
            self.d_f.add(Dot([0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        self.d_f_green = VGroup()
        for i in range(N):
            self.d_f_green.add(Dot([0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        #LINES
        self.lines = VGroup()
        for i in range(N):
            self.lines.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(self.colors[0]))
        self.lines_green = VGroup()
        for i in range(N):
            self.lines_green.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center(),fill_opacity=0.).set_color(self.colors[1]))

        if centered_triangle :
            self.rectangle = Rectangle(width=width_rectangle,height=height_rectangle, color=colors[0], fill_opacity=0.4).rotate(np.pi/2+self.angle_in, [0,1,0])#.shift(height_rectangle/2*np.array([0,-1,0]))
        else :
            self.rectangle = Rectangle(width=width_rectangle,height=height_rectangle, color=colors[0], fill_opacity=0.4).rotate(np.pi/2+self.angle_in, [0,1,0]).shift(height_rectangle/2*np.array([0,-1,0]))

        self.red_rectangle = Rectangle(width=width_rectangle,height=height_rectangle, color=colors[1], fill_opacity=0.4).rotate(np.pi/2+self.angle_pol[0], [0,1,0]).shift(height_rectangle/2*np.array([0,+1,0]))

        self.t=ValueTracker(0)
        self.t.set_value(-10-14/self.N*self.alpha)

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
            self.d_i[4].add_updater(lambda z: z.set_y(self.t.get_value()+4/self.N*self.alpha))
            self.d_i[5].add_updater(lambda z: z.set_y(self.t.get_value()+5/self.N*self.alpha))
            self.d_i[6].add_updater(lambda z: z.set_y(self.t.get_value()+6/self.N*self.alpha))
            self.d_i[7].add_updater(lambda z: z.set_y(self.t.get_value()+7/self.N*self.alpha))
            self.d_i[0].set_z(0)
            self.d_i[1].set_z(0)
            self.d_i[2].set_z(0)
            self.d_i[3].set_z(0)
            self.d_i[4].set_z(0)
            self.d_i[5].set_z(0)
            self.d_i[6].set_z(0)
            self.d_i[7].set_z(0)

            self.d_f[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))
            self.d_f[4].add_updater(lambda z: z.set_y(self.t.get_value()+4/self.N*self.alpha))
            self.d_f[5].add_updater(lambda z: z.set_y(self.t.get_value()+5/self.N*self.alpha))
            self.d_f[6].add_updater(lambda z: z.set_y(self.t.get_value()+6/self.N*self.alpha))
            self.d_f[7].add_updater(lambda z: z.set_y(self.t.get_value()+7/self.N*self.alpha))
            self.d_f_green[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f_green[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f_green[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f_green[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))
            self.d_f_green[4].add_updater(lambda z: z.set_y(self.t.get_value()+4/self.N*self.alpha))
            self.d_f_green[5].add_updater(lambda z: z.set_y(self.t.get_value()+5/self.N*self.alpha))
            self.d_f_green[6].add_updater(lambda z: z.set_y(self.t.get_value()+6/self.N*self.alpha))
            self.d_f_green[7].add_updater(lambda z: z.set_y(self.t.get_value()+7/self.N*self.alpha))

            self.d_f[0].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[0].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[1].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[2].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[3].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[4].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[4].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+4/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[5].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[5].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+5/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[6].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[6].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+6/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[7].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[7].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+7/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[0].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[0].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[1].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[2].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[3].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[4].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[4].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+4/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[5].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[5].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+5/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[6].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[6].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+6/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[7].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[7].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+7/self.N*self.alpha)*np.sin(self.angle_in)))

            self.d_f_green[0].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[1].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[2].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[3].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[4].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[4].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[4].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+4/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[5].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[5].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[5].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+5/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[6].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[6].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[6].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+6/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[7].add_updater(lambda z: z.set_z(block*(np.heaviside(self.d_f[7].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[7].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+7/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[0].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[1].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[2].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[3].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[4].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[4].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[4].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+4/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[5].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[5].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[5].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+5/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[6].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[6].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[6].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+6/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[7].add_updater(lambda z: z.set_x(block*(np.heaviside(self.d_f[7].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[7].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+7/self.N*self.alpha)*np.sin(self.angle_pol[0])))

            self.lines[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f[0].get_center(),buff=0,color=self.colors[0])))
            self.lines[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f[1].get_center(),buff=0,color=self.colors[0])))
            self.lines[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f[2].get_center(),buff=0,color=self.colors[0])))
            self.lines[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f[3].get_center(),buff=0,color=self.colors[0])))
            self.lines[4].add_updater(lambda z: z.become(Arrow(self.d_i[4].get_center(),self.d_f[4].get_center(),buff=0,color=self.colors[0])))
            self.lines[5].add_updater(lambda z: z.become(Arrow(self.d_i[5].get_center(),self.d_f[5].get_center(),buff=0,color=self.colors[0])))
            self.lines[6].add_updater(lambda z: z.become(Arrow(self.d_i[6].get_center(),self.d_f[6].get_center(),buff=0,color=self.colors[0])))
            self.lines[7].add_updater(lambda z: z.become(Arrow(self.d_i[7].get_center(),self.d_f[7].get_center(),buff=0,color=self.colors[0])))
            self.lines_green[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f_green[0].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f_green[1].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f_green[2].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f_green[3].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[4].add_updater(lambda z: z.become(Arrow(self.d_i[4].get_center(),self.d_f_green[4].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[5].add_updater(lambda z: z.become(Arrow(self.d_i[5].get_center(),self.d_f_green[5].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[6].add_updater(lambda z: z.become(Arrow(self.d_i[6].get_center(),self.d_f_green[6].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[7].add_updater(lambda z: z.become(Arrow(self.d_i[7].get_center(),self.d_f_green[7].get_center(),buff=0,color=self.colors[1])))


class Tricolored_Oriented_Oscillating_Arrows_3D(ThreeDScene):
    def __init__(
        self,
        pos_filters=[-2,0,2],
        angle_pol=[0,np.pi/4,np.pi/3],#,4*np.pi/10,np.pi/3],
        colors=[BLUE,GREEN,YELLOW,RED],
        alpha = 3,
        N = 4,
        x_range=(-7,7,1),
        y_range=(-7,7,1),
        z_range=(-7,7,1),
        angle_in = 0,
        origin_shift=-3,
        default_opacity = 0.6,
        **kwargs
    ):
        self.origin_shift=origin_shift
        self.x_range=x_range
        self.y_range=y_range
        self.z_range=z_range
        self.min_x=self.x_range[0]
        self.colors=colors
        self.pos_filters=pos_filters
        self.angle_in=angle_in
        self.alpha = alpha
        self.angle_pol=angle_pol
        self.N=N
        #DOTS
        self.d_i = VGroup()
        for i in range(N):
            self.d_i.add(Dot([0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        self.d_f = VGroup()
        for i in range(N):
            self.d_f.add(Dot([0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        self.d_f_green = VGroup()
        for i in range(N):
            self.d_f_green.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        self.d_f_yellow = VGroup()
        for i in range(N):
            self.d_f_yellow.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        self.d_f_red = VGroup()
        for i in range(N):
            self.d_f_red.add(Dot([0,i/self.N*self.alpha,0],fill_opacity=0.))
        #LINES
        self.lines = VGroup()
        for i in range(N):
            self.lines.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(self.colors[0]))
        self.lines_green = VGroup()
        for i in range(N):
            self.lines_green.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(self.colors[1]))
        self.lines_yellow = VGroup()
        for i in range(N):
            self.lines_yellow.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(self.colors[2]))
        self.lines_red = VGroup()
        for i in range(N):
            self.lines_red.add(Arrow(self.d_i[i].get_center(),self.d_f[i].get_center()).set_color(self.colors[3]))

        self.t=ValueTracker(0)
        self.t.set_value(origin_shift-self.min_x-14/self.N*self.alpha)

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
            self.d_f_yellow[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f_yellow[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f_yellow[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f_yellow[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))
            self.d_f_red[0].add_updater(lambda z: z.set_y(self.t.get_value()))
            self.d_f_red[1].add_updater(lambda z: z.set_y(self.t.get_value()+1/self.N*self.alpha))
            self.d_f_red[2].add_updater(lambda z: z.set_y(self.t.get_value()+2/self.N*self.alpha))
            self.d_f_red[3].add_updater(lambda z: z.set_y(self.t.get_value()+3/self.N*self.alpha))

            self.d_f[0].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[0].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[1].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[2].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_z(np.heaviside(-self.d_f[3].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_in)))
            self.d_f[0].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[0].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[1].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[1].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[2].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[2].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_in)))
            self.d_f[3].add_updater(lambda z: z.set_x(np.heaviside(-self.d_f[3].get_center()[1]+self.pos_filters[0],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_in)))

            self.d_f_green[0].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[1].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[2].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[3].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_pol[0])))
            self.d_f_green[0].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[1].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[2].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_pol[0])))
            self.d_f_green[3].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[0],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_pol[0])))

            self.d_f_yellow[0].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_pol[1])))
            self.d_f_yellow[1].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_pol[1])))
            self.d_f_yellow[2].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_pol[1])))
            self.d_f_yellow[3].add_updater(lambda z: z.set_z((np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_pol[1])))
            self.d_f_yellow[0].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_pol[1])))
            self.d_f_yellow[1].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_pol[1])))
            self.d_f_yellow[2].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_pol[1])))
            self.d_f_yellow[3].add_updater(lambda z: z.set_x((np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[1],1)-np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[2],1))*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_pol[1])))

            self.d_f_red[0].add_updater(lambda z: z.set_z(np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.cos(self.angle_pol[2])))
            self.d_f_red[1].add_updater(lambda z: z.set_z(np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.cos(self.angle_pol[2])))
            self.d_f_red[2].add_updater(lambda z: z.set_z(np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.cos(self.angle_pol[2])))
            self.d_f_red[3].add_updater(lambda z: z.set_z(np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.cos(self.angle_pol[2])))
            self.d_f_red[0].add_updater(lambda z: z.set_x(np.heaviside(self.d_f[0].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+0/self.N*self.alpha)*np.sin(self.angle_pol[2])))
            self.d_f_red[1].add_updater(lambda z: z.set_x(np.heaviside(self.d_f[1].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+1/self.N*self.alpha)*np.sin(self.angle_pol[2])))
            self.d_f_red[2].add_updater(lambda z: z.set_x(np.heaviside(self.d_f[2].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+2/self.N*self.alpha)*np.sin(self.angle_pol[2])))
            self.d_f_red[3].add_updater(lambda z: z.set_x(np.heaviside(self.d_f[3].get_center()[1]-self.pos_filters[2],1)*2*np.sin(3*self.t.get_value()+3/self.N*self.alpha)*np.sin(self.angle_pol[2])))

            self.lines[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f[0].get_center(),buff=0,color=self.colors[0])))
            self.lines[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f[1].get_center(),buff=0,color=self.colors[0])))
            self.lines[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f[2].get_center(),buff=0,color=self.colors[0])))
            self.lines[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f[3].get_center(),buff=0,color=self.colors[0])))
            self.lines_green[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f_green[0].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f_green[1].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f_green[2].get_center(),buff=0,color=self.colors[1])))
            self.lines_green[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f_green[3].get_center(),buff=0,color=self.colors[1])))
            self.lines_yellow[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f_yellow[0].get_center(),buff=0,color=self.colors[2])))
            self.lines_yellow[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f_yellow[1].get_center(),buff=0,color=self.colors[2])))
            self.lines_yellow[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f_yellow[2].get_center(),buff=0,color=self.colors[2])))
            self.lines_yellow[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f_yellow[3].get_center(),buff=0,color=self.colors[2])))
            self.lines_red[0].add_updater(lambda z: z.become(Arrow(self.d_i[0].get_center(),self.d_f_red[0].get_center(),buff=0,color=self.colors[3])))
            self.lines_red[1].add_updater(lambda z: z.become(Arrow(self.d_i[1].get_center(),self.d_f_red[1].get_center(),buff=0,color=self.colors[3])))
            self.lines_red[2].add_updater(lambda z: z.become(Arrow(self.d_i[2].get_center(),self.d_f_red[2].get_center(),buff=0,color=self.colors[3])))
            self.lines_red[3].add_updater(lambda z: z.become(Arrow(self.d_i[3].get_center(),self.d_f_red[3].get_center(),buff=0,color=self.colors[3])))

