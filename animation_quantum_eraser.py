from math import e
from os import POSIX_FADV_NORMAL
#from typing_extensions import runtime
from manim import *
from manim_physics import *
from matplotlib import colors
import numpy as np
from manim.scene.three_d_scene import * 
from oscillating_arrow import *

import requests
from PIL import Image

import sys
sys.setrecursionlimit(10000)

from manim import *






#Laser_setup
class Scene_setup(ThreeDScene):
    def construct(self):
        color_change=True
        colors=[BLUE,RED]
        colors_before_last_filter=[BLUE,RED]
        colors_end=[PURPLE,PURPLE]#[BLUE,RED]
        borne_min = -7
        borne_max = 7
        radius=1
        run_time=2
        screen_distance=5
        N=8
        resolution_cyl=10#00
        angle_pol=[0,np.pi/4,np.pi/3]#,np.pi/3]
        min_x,max_x,min_y,max_y,min_z,max_z = borne_min,borne_max,borne_min,borne_max,borne_min,borne_max
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        pos_mirrors=[[-2,-3,0],[2,3,0]]
        pos_spliters=[[2,-3,0],[-2,3,0]]
        pos_filters=[[2,0,0],[-2,0,0],[-2,3+screen_distance/2,0]]#        pos_filters=[[2,0,0],[-2,0,0],[-2,3+screen_distance/2,0]]
        screen_2 = Screen(color=GREY,angle_1=np.pi/2,angle_2=np.pi/2,pos_screen=np.array(pos_spliters[1])+np.array([0,screen_distance,0]))
        screen_1 = Screen(color=GREY,angle_1=np.pi/2,angle_2=0,pos_screen=np.array(pos_spliters[1])+np.array([-screen_distance,0,0]))
        pol_1 = Polarizer(radius=radius,pos_polarizer=pos_filters[0])
        pol_2 = Polarizer(radius=radius,pos_polarizer=pos_filters[1])
        pol_3 = Polarizer(radius=radius,pos_polarizer=pos_filters[2])
        spliter1=Spliter(pos_spliter=pos_spliters[0],orthogonal_vector=pos_mirrors[0],radius = radius,resolution=resolution_cyl,width=0.2)
        spliter2=Spliter(pos_spliter=pos_spliters[1],orthogonal_vector=pos_mirrors[0],radius = radius,resolution=resolution_cyl,width=0.2)
        mirror1=Mirror(pos_mirror=pos_mirrors[0],orthogonal_vector=pos_mirrors[0],radius = radius,resolution=resolution_cyl,width=0.2)
        mirror2=Mirror(pos_mirror=pos_mirrors[1],orthogonal_vector=pos_mirrors[0],radius = radius, resolution=resolution_cyl, width=0.2)
        laser = Laser(pos_spliters=pos_spliters, pos_mirrors=pos_mirrors, arrow_mode=True,positive_infinity_pos=np.array([0,screen_distance,0]),run_time=run_time)
        self.add(axes,spliter1.disk,spliter2.disk,mirror1.disk,mirror2.disk,spliter1.disk_2,spliter2.disk_2,screen_2.square,screen_1.square,pol_1.vector,pol_1.disk,pol_2.vector,pol_2.disk)

        text3d1 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,4])
        text_group = VGroup()
        text_group.add(Text('Beam spliter', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_spliters[0])))
        text_group.add(Text('Beam spliter', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_spliters[1])))
        text_group.add(Text('Mirror', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_mirrors[0])))
        text_group.add(Text('Mirror', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_mirrors[1])))
        text_group.add(Text('Polariseur', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_filters[0])))
        text_group.add(Text('Polariseur', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_filters[1])))
        text_group.add(Text('Polariseur', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(pos_filters[2])))
        text_group.add(Text('Écran', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(screen_2.pos_screen)))
        text_group.add(Text('Écran', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to(np.array([0,0,1.4])+np.array(screen_1.pos_screen)))
###        text3d2 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,3])

        self.add(pol_3.vector,pol_3.disk)
        pol_3.vector.move_to(pos_filters[2]+radius*np.array([0,0,1.5*radius])).shift(4*LEFT)
        pol_3.disk.move_to(pos_filters[2]).shift(4*LEFT)#+[0,screen_distance/2,0]))
        self.play(FadeIn(pol_3.vector),FadeIn(pol_3.disk))#+[0,screen_distance/2,0]))
        self.play(pol_3.vector.animate.move_to(pos_filters[2]+radius*np.array([0,0,1.5*radius])),pol_3.disk.animate.move_to(pos_filters[2]))#+[0,screen_distance/2,0]))


        self.add(text_group)

        self.play(Create(laser.beam_1),Create(laser.beam_2),run_time=run_time,rate_func=linear)
        self.wait()
        self.play(FadeOut(laser.beam_1),FadeOut(laser.beam_2),run_time=run_time,rate_func=linear)

        photons=Photons(pos_spliters=pos_spliters, pos_mirrors=pos_mirrors, positive_infinity_pos=np.array([0,screen_distance,0]),pos_filters=pos_filters)
        if color_change :
            self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[0]),MoveAlongPath(photons.dots_2[0],photons.beam_2[0]),run_time=run_time,rate_func=linear)
            self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[1]),MoveAlongPath(photons.dots_2[0],photons.beam_2[1]),run_time=run_time,rate_func=linear)
            photons.change_color(colors,n=2)
            self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[2]),MoveAlongPath(photons.dots_2[0],photons.beam_2[2]),run_time=run_time,rate_func=linear)
            photons.change_color(colors,n=1)
            for i in range(3,len(photons.beam_1)-2):
                self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[i]),MoveAlongPath(photons.dots_2[0],photons.beam_2[i]),run_time=run_time,rate_func=linear)
            photons.change_color(colors_before_last_filter,n=1)
            self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[len(photons.beam_1)-2]),MoveAlongPath(photons.dots_2[0],photons.beam_2[len(photons.beam_1)-2]),run_time=run_time,rate_func=linear)
            photons.change_color(colors_end,n=1)
            self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[len(photons.beam_1)-1]),MoveAlongPath(photons.dots_2[0],photons.beam_2[len(photons.beam_1)-1]),run_time=run_time,rate_func=linear)
        else :
            for i in range(len(photons.beam_1)):
                self.play(MoveAlongPath(photons.dots_1[0],photons.beam_1[i]),MoveAlongPath(photons.dots_2[0],photons.beam_2[i]),run_time=run_time,rate_func=linear)
        self.wait()

#Wave going through 3 polarizers
class Scene_threePol(ThreeDScene):
    def construct(self):
        pos_filters=[-2,0,2]
        colors=[BLUE,GREEN,YELLOW,RED]
        N=4
        angle_in = np.pi/4
        angle_pol=[0,np.pi/4,np.pi/3]#,np.pi/3]
        min_x,max_x,min_y,max_y,min_z,max_z = -7,7,-7,7,-7,7
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d1 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,4])
        text3d2 = Text('Hello world', gradient=(BLUE, GREEN), font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,3])

        pol = Polarizer(pos_polarizer=[0,pos_filters[0],0])
        pol2 = Polarizer(pos_polarizer=[0,pos_filters[1],0])
        pol3 = Polarizer(pos_polarizer=[0,pos_filters[2],0])

        math_text=show_text()
        self.add(axes,text3d1,text3d2,pol.disk,pol.vector,pol2.disk,pol2.vector,pol3.disk,pol3.vector, math_text.tex_string,math_text.tex_string_right)
#        self.wait(1)

        if False :
            pol.orientation_polarizer(angle_pol[0])
            self.add(pol.di,pol.df,pol.label)
            self.play(pol.t.animate.set_value(angle_pol),run_time=2)#,rate_func=linear)
        wave=Tricolored_Oriented_Oscillating_Arrows_3D(x_range=x_range,y_range=y_range,z_range=z_range,colors=colors,angle_in=angle_in,pos_filters=pos_filters,angle_pol=angle_pol)
        pol.color_polarizer(wave.d_f)
        pol2.color_polarizer(wave.d_f)
        pol3.color_polarizer(wave.d_f)

        self.add(wave.d_i,wave.d_f,wave.d_f_green,wave.d_f_yellow,wave.d_f_red,wave.lines,wave.lines_green,wave.lines_yellow,wave.lines_red)
#        self.add(wave.d_i,wave.d_f,wave.d_f_green,wave.lines,wave.lines_green)

        self.play(wave.t.animate.increment_value(10),run_time=5,rate_func=linear)
        wave.t.set_value(-min_x-14/N*alpha)
        self.wait(1)

"""
        self.move_camera(theta = np.pi/2,phi=np.pi/2)
        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(1)
        self.play(wave.t.animate.increment_value(10),run_time=5,rate_func=linear)
        self.wait()

        self.add(Rays.Dot_group_1,Rays.Dot_group_2,Rays.Dot_group_3)
        self.add(Rays.lines_1,Rays.lines_2,Rays.lines_3,Rays.lines_4)
        self.wait()
"""
# Light ray mode
#        self.add(axes,text3d1,text3d2,pol.disk,pol.vector,pol2.disk,pol2.vector,pol3.disk,pol3.vector, math_text.tex_string,math_text.tex_string_right)
#        Rays=LightRays(pos_filters=pos_filters)
#        self.add(Rays.Dot_group_1,Rays.Dot_group_2,Rays.Dot_group_3)
#        self.add(Rays.lines_1,Rays.lines_2,Rays.lines_3,Rays.lines_4)

#        for e in range(len(Rays.Dot_group_1)):
#            print(Rays.set_of_dots_1[e,:])
            #print(Rays.Dot_group_1[e].get_center())
#        exit(0)
#        self.wait()
#        self.play(FadeIn(Rays.lines_1))
#        self.remove()

### E-M wave in a plane
class Scene_wave_in_plane(ThreeDScene):
    def construct(self):
        display_rays=False
        pos_filters=[0,1000,1000]#-2,-2]
        colors=[BLUE,BLUE,RED,YELLOW]
        N=8
        radius=1
        angle_in = np.pi/4
        angle_ortho=np.pi/4
        angle_pol=[angle_ortho,np.pi/4,np.pi/3]#,np.pi/3]
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        start_trainwave=min_x-2/N*alpha
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-35 * DEGREES)
#        text3d1 = Text('Description classique de la lumière ', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,3])
#        text3d2 = Text('comme une onde électromagnétique', gradient=(BLUE, GREEN), font_size=20).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,2.5])
        line1=Line(start=np.array([0,0,-0.01]), end=1.5*np.array([0,0,1])).rotate(angle_in,axis=np.array([0,1,0]),about_point=ORIGIN)#.rotate(angle_in,axis=np.array([1,0,0]),about_point=np.array([0,1,0]))#np.array([(np.sqrt(pol.radius)+0.5)*np.cos(angle_in),0,(np.sqrt(pol.radius)+0.5)*np.sin(angle_in)])
        line2=Line(start=np.array([0,0,-0.01]), end=1.5*np.array([0,0,1])).rotate(angle_pol[0],axis=np.array([0,1,0]),about_point=ORIGIN)#np.array([(np.sqrt(pol.radius)+0.5)*np.cos(angle_in),0,(np.sqrt(pol.radius)+0.5)*np.sin(angle_in)])
        #end2=np.array([(np.sqrt(pol.radius)+0.5)*np.cos(angle_pol[0]),0,(np.sqrt(pol.radius)+0.5)*np.sin(angle_pol[0])])
        angle=Arc(radius=1.0, start_angle=min(angle_in,angle_pol[0]), angle=-np.abs(angle_in-angle_pol[0]), arc_center=ORIGIN).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN)
        #Angle(line1,line2,radius=0.5,quadrant=(1,-1)).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN)
        
        tex = MathTex(r"\theta").move_to(angle).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN).shift([1,0,1])
        math_text=show_text_2()
        self.add(axes,math_text.tex_string,math_text.tex_string_right)#,tex)#,text3d1,text3d2)
        self.wait(1)
        wave=Simple_Oriented_Oscillating_Arrows_3D(alpha=alpha,block=1,centered_triangle=True,x_range=x_range,y_range=y_range,z_range=z_range,colors=colors,angle_in=angle_in,pos_filters=pos_filters,angle_pol=angle_pol,width_rectangle=4*radius,height_rectangle=-2.5*start_trainwave)
        wave.t.set_value(start_trainwave)
        self.add(wave.d_i,wave.d_f,wave.d_f_green,wave.lines,wave.lines_green,wave.rectangle)
###        pol.color_polarizer(wave.d_f)
        self.play(wave.t.animate.increment_value(11),FadeOut(wave.lines_green),run_time=4,rate_func=linear)
#        self.play(FadeOut(wave.lines_green),run_time=0.5)
        self.wait()



### Waves through polarizer, 2 planes. 3D version not working
class Scene_waves_through_pol(ThreeDScene):
    def construct(self):
        display_rays=False
        pos_filters=[0,1000,1000]#-2,-2]
        colors=[PURPLE,BLUE,RED,BLUE,YELLOW]
        N=8
        radius=1
        angle_in = np.pi/4
        angle_ortho=np.pi/2
        angle_pol=[0,np.pi/4,np.pi/3]#,np.pi/3]#[angle_ortho,np.pi/4,np.pi/3]#,np.pi/3]
        min_x,max_x,min_y,max_y,min_z,max_z = -5,5,-5,5,-5,5
        x_range=(min_x,max_x,1)
        y_range=(min_y,max_y,1)
        z_range=(min_z,max_z,1)
        alpha=3
        start_trainwave=min_x-2/N*alpha
        axes = ThreeDAxes(x_range,y_range,z_range)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-35 * DEGREES)
        pol = Polarizer(radius = radius,pos_polarizer=[0,pos_filters[0],0])

        line1=Line(start=np.array([0,0,-0.01]), end=1.5*np.array([0,0,1])).rotate(angle_in,axis=np.array([0,1,0]),about_point=ORIGIN)#.rotate(angle_in,axis=np.array([1,0,0]),about_point=np.array([0,1,0]))#np.array([(np.sqrt(pol.radius)+0.5)*np.cos(angle_in),0,(np.sqrt(pol.radius)+0.5)*np.sin(angle_in)])
        line2=Line(start=np.array([0,0,-0.01]), end=1.5*np.array([0,0,1])).rotate(angle_pol[0],axis=np.array([0,1,0]),about_point=ORIGIN)#np.array([(np.sqrt(pol.radius)+0.5)*np.cos(angle_in),0,(np.sqrt(pol.radius)+0.5)*np.sin(angle_in)])
        angle=Arc(radius=1.0, start_angle=min(angle_in,angle_pol[0]), angle=np.abs(angle_in-angle_pol[0]), arc_center=ORIGIN).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN)
#        angle=Arc(radius=1.0, start_angle=min(angle_in,angle_pol[0]), angle=-np.abs(angle_in-angle_pol[0]), arc_center=ORIGIN).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN)
        tex = MathTex(r"\theta").move_to(angle).rotate(PI/2,axis=np.array([1,0,0]),about_point=ORIGIN).shift([1,0,1])
        math_text=show_text_2(colors=colors)
        self.add(axes,pol.disk,pol.vector, math_text.tex_string,math_text.tex_string_right)
        if True :
            pol.orientation_polarizer(angle_pol[0])
            self.add(pol.di,pol.df,pol.label)
            self.play(pol.t.animate.set_value(angle_pol[0]),run_time=2)#,rate_func=linear)
        wave=Simple_Oriented_Oscillating_Arrows_3D(alpha=alpha,block=1,centered_triangle=False,x_range=x_range,y_range=y_range,z_range=z_range,colors=colors,angle_in=angle_in,pos_filters=pos_filters,angle_pol=angle_pol,width_rectangle=4*radius,height_rectangle=-1.5*start_trainwave)
        wave.t.set_value(start_trainwave)
        self.add(wave.d_i,wave.d_f,wave.d_f_green,wave.lines,wave.lines_green)
        self.play(FadeIn(wave.rectangle),FadeIn(wave.red_rectangle),FadeIn(angle),FadeIn(tex))
###        pol.color_polarizer(wave.d_f)
        self.play(wave.t.animate.increment_value(11),FadeOut(wave.lines_green),run_time=4,rate_func=linear)
#        self.play(FadeOut(wave.lines_green),run_time=0.5)
        self.wait()
"""
        self.move_camera(theta = np.pi/2,phi=np.pi/2)
        self.begin_ambient_camera_rotation(rate=0.01)
        wave.t.set_value(start_trainwave)
        self.play(wave.t.animate.increment_value(11),FadeOut(wave.lines_green),run_time=4,rate_func=linear)
        self.wait()
"""


####################################

class Spliter(ThreeDScene):
    def __init__(
        self,
        pos_spliter=[0,0,0],
        radius = 1.5,
		A_vect = np.array([0,0,1]),
        orthogonal_vector=[0,1,0],
        current_angle = 0,
        default_opacity = 0.6,
        color_blocking=[GREY,RED],
        resolution=20,
        width=0.2,
        **kwargs
    ):
        self.pos_spliter=pos_spliter
        self.color_blocking=color_blocking
        self.default_opacity=default_opacity
        self.current_position = [0,0,radius]
        self.current_angle=current_angle
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        self.disk = Cylinder(radius=radius, height=width,direction=np.array(pos_spliter),fill_color=GREY,resolution=(10,resolution),fill_opacity=0.5).shift(pos_spliter)#Circle(radius=radius, color=self.color_blocking[0], fill_opacity=0.8,arc_center=pos_mirror)
        self.disk_2 = Cylinder(radius=radius, height=width,direction=np.array(pos_spliter),fill_color=WHITE,resolution=(10,resolution),fill_opacity=1.).shift((width/(pos_spliter[1]**2+pos_spliter[2]**2)+1)*np.array(pos_spliter))#Circle(radius=radius, color=self.color_blocking[0], fill_opacity=0.8,arc_center=pos_mirror)
        self.disk.set_color(WHITE)
        self.disk_2.set_color(GREY_D)
#        self.disk = Circle(radius=radius, color=self.color_blocking[0], fill_opacity=0.8,arc_center=pos_spliter)
#        self.disk.rotate(np.pi/2, orthogonal_vector)

class Mirror(ThreeDScene):
    def __init__(
        self,
        pos_mirror=[0,1,0],
        radius = 1.5,
		A_vect = np.array([0,0,1]),
        orthogonal_vector=[0,1,0],
        current_angle = 0,
        default_opacity = 0.6,
        color_blocking=[GREY,RED],
        resolution=20,
        width=0.2,
        **kwargs
    ):
        self.pos_mirror=pos_mirror
        self.color_blocking=color_blocking
        self.default_opacity=default_opacity
        self.current_angle=current_angle
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        self.disk = Cylinder(radius=radius, height=width,direction=np.array(pos_mirror),fill_color=GREY_C,resolution=(10,resolution)).shift(pos_mirror)#Circle(radius=radius, color=self.color_blocking[0], fill_opacity=0.8,arc_center=pos_mirror)
        self.disk.set_color(GREY_C)
#        self.disk = Circle(radius=radius, color=self.color_blocking[0], fill_opacity=0.8,arc_center=pos_mirror).rotate(np.pi/2, orthogonal_vector)

class Laser(ThreeDScene):
    def __init__(
        self,
        arrow_mode=True,
        pos_spliters=[[0,0,0]],
        pos_mirrors=[[0,0,0]],
        positive_infinity_pos=[0,3,0],
        radius = 1.5,
        orthogonal_vector=[0,1,0],
        default_opacity = 0.6,
        colors=[YELLOW,GREY,RED],
        **kwargs
    ):
        self.pos_spliters=pos_spliters
        self.default_opacity=default_opacity
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        self.start_points_1=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_mirrors[0],pos_spliters[1]])
        self.end_points_1=np.array([pos_spliters[0],pos_mirrors[0],pos_spliters[1],np.array(pos_spliters[1])+np.array([-positive_infinity_pos[1],0,0])])
        self.start_points_2=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_mirrors[1],pos_spliters[1]])
        self.end_points_2=np.array([pos_spliters[0],pos_mirrors[1],pos_spliters[1],np.array(pos_spliters[1])+np.array(positive_infinity_pos)])
        self.beam_1=VGroup()
        self.beam_2=VGroup()
        for e in range(len(self.start_points_1)):
            if arrow_mode :
                self.beam_1.add(Arrow(start=self.start_points_1[e],end=self.end_points_1[e],buff=0,color=colors[0]))
                self.beam_2.add(Arrow(start=self.start_points_2[e],end=self.end_points_2[e],buff=0,color=colors[0]))
            else :
                self.beam_1.add(Line(start=self.start_points_1[e],end=self.end_points_1[e],buff=0,color=colors[0]))
                self.beam_2.add(Line(start=self.start_points_2[e],end=self.end_points_2[e],buff=0,color=colors[0]))

#weird stuff
class Screen(ThreeDScene):
    def __init__(
        self,
        color=GREY,
        angle_1=np.pi/2,
        angle_2=np.pi/2,
        pos_screen=np.array([0,0,0]),
        positive_infinity_pos=[0,3,0],
        radius = 1.5,
        orthogonal_vector=[0,1,0],
        default_opacity = 0.6,
        **kwargs
    ):
        self.pos_screen=pos_screen
        self.default_opacity=default_opacity
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        self.square = Square(color=color, fill_opacity=1).rotate(angle_1, UP).rotate(angle_2, [0,0,1]).shift(np.array(pos_screen))
        #.rotate(np.pi/2, RIGHT)
class Photons(ThreeDScene):
    def __init__(
        self,
        N_photons=10,
        pos_spliters=[[0,0,0]],
        pos_mirrors=[[0,0,0]],
        pos_filters=[[0,0,0]],
        positive_infinity_pos=[0,3,0],
        radius = 1.5,
        orthogonal_vector=[0,1,0],
        default_opacity_1 = 1.,
        default_opacity_2 = 1.,
        colors=[YELLOW,GREY,RED],
        **kwargs
    ):
        self.default_opacity_1 = default_opacity_1
        self.default_opacity_2 = default_opacity_2
        self.N_photons = N_photons
        self.pos_spliters=pos_spliters
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        if pos_filters==[[0,0,0]]:
            self.start_points_1=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_mirrors[0],pos_spliters[1]])
            self.end_points_1=np.array([pos_spliters[0],pos_mirrors[0],pos_spliters[1],np.array(pos_spliters[1])+np.array(positive_infinity_pos)])
            self.start_points_2=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_spliters[0],pos_mirrors[1],pos_spliters[1]])
            self.end_points_2=np.array([pos_spliters[0],pos_mirrors[1],pos_spliters[1],np.array(pos_spliters[1])+np.array([-positive_infinity_pos[1],0,0])])
        else :
            self.start_points_1=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_mirrors[0],pos_filters[1],pos_spliters[1]])
            self.end_points_1=np.array([pos_spliters[0],pos_mirrors[0],pos_filters[1],pos_spliters[1],np.array(pos_spliters[1])+np.array(positive_infinity_pos)])
            self.start_points_2=np.array([np.array(pos_spliters[0])-np.array(positive_infinity_pos),pos_spliters[0],pos_filters[0],pos_mirrors[1],pos_spliters[1]])
            self.end_points_2=np.array([pos_spliters[0],pos_filters[0],pos_mirrors[1],pos_spliters[1],np.array(pos_spliters[1])+np.array([-positive_infinity_pos[1],0,0])])
        self.beam_1=VGroup()
        self.beam_2=VGroup()
        for e in range(len(self.start_points_1)):
            self.beam_1.add(Line(start=self.start_points_1[e],end=self.end_points_1[e],buff=0,color=colors[0]))
            self.beam_2.add(Line(start=self.start_points_2[e],end=self.end_points_2[e],buff=0,color=colors[0]))
        self.dots_1 = VGroup()
        self.dots_2 = VGroup()
        for i in range(self.N_photons):
            self.dots_1.add(Dot(color=YELLOW,fill_opacity=self.default_opacity_1))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
            self.dots_2.add(Dot(color=YELLOW,fill_opacity=self.default_opacity_2))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
    def change_color(self,colors,n=0):
        if n==1 :
            for i in range(self.N_photons):
                self.dots_1.become(Dot(color=colors[0],fill_opacity=self.default_opacity_1))#))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        if n==2 :
            for i in range(self.N_photons):
                self.dots_2.become(Dot(color=colors[1],fill_opacity=self.default_opacity_2))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
        else :            
            for i in range(self.N_photons):
                self.dots_1.become(Dot(color=colors[0],fill_opacity=self.default_opacity_1))#self.default_opacity))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))
                self.dots_2.become(Dot(color=colors[1],fill_opacity=self.default_opacity_2))#[0,i/self.N*self.alpha+2*origin_shift,0],fill_opacity=0.))


class Polarizer(ThreeDScene):
    def __init__(
        self,
        pos_polarizer=[0,-2,0],
        radius = 1.5,
		A_vect = np.array([0,0,1]),
        orthogonal_vector=[0,1,0],
        current_angle = 0,
        default_opacity = 0.6,
        color_blocking=[GREY,RED],
        **kwargs
    ):
        self.pos_polarizer=pos_polarizer
        self.color_blocking=color_blocking
        self.default_opacity=default_opacity
        self.current_position = [0,0,radius]
        self.current_angle=current_angle
        self.orthogonal_vector= orthogonal_vector
        self.radius=radius
        top = np.array([0,0,radius])
        self.vector = Arrow(start = np.array(self.pos_polarizer)+top, end= top+A_vect+np.array(self.pos_polarizer),buff=0)
        self.disk = Circle(radius=radius, color=self.color_blocking[0], fill_opacity=default_opacity,arc_center=self.pos_polarizer)
        self.disk.rotate(np.pi/2, [0.1,0,0])
    def orientation_polarizer(self,angle_in):
        self.t=ValueTracker(0)
        self.t.set_value(self.current_angle)
        self.di,self.df = Dot([self.radius*np.sin(self.current_angle),self.pos_polarizer[1],self.radius*np.cos(self.current_angle)],fill_opacity=0.),Dot([(self.radius+1)*np.sin(self.current_angle),self.pos_polarizer[1],(self.radius+1)*np.cos(self.current_angle)],fill_opacity=0.)
        self.label = MathTex(r"\alpha").rotate(np.pi/2, [1,0,0]).add_updater(lambda m: m.next_to(self.df, UP))
        self.di.add_updater(lambda z: z.set_z(self.radius*np.cos(self.t.get_value())))
        self.di.add_updater(lambda z: z.set_x(self.pos_polarizer[0]+self.radius*np.sin(self.t.get_value())))
        self.di.add_updater(lambda z: z.set_y(self.pos_polarizer[1]))
        self.df.add_updater(lambda z: z.set_z((self.radius+1)*np.cos(self.t.get_value())))
        self.df.add_updater(lambda z: z.set_x(self.pos_polarizer[0]+(self.radius+1)*np.sin(self.t.get_value())))
        self.df.add_updater(lambda z: z.set_y(self.pos_polarizer[1]))
        self.vector.add_updater(lambda z: z.become(Arrow(self.di.get_center(),self.df.get_center(),buff=0)))
        self.disk.add_updater(lambda z: z.become(Circle(radius=self.radius, color=self.color_blocking[0], fill_opacity=self.default_opacity+1/2*(1-self.default_opacity)*np.sin(self.t.get_value()),arc_center=self.pos_polarizer).rotate(np.pi/2, [1,0,0])))
        self.current_angle=angle_in
    def color_polarizer(self,d_f):
        self.disk.add_updater(lambda z: z.become(Circle(radius=self.radius, color=self.color_blocking[int(np.heaviside(d_f[0].get_center()[1]-self.pos_polarizer[1],1))+int(np.heaviside(-d_f[-1].get_center()[1]+self.pos_polarizer[1],1))-1], fill_opacity=self.default_opacity+1/2*(1-self.default_opacity)*np.sin(self.current_angle),arc_center=self.pos_polarizer).rotate(np.pi/2, [1,0,0])))

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
        self.tex_string.set_color_by_tex(r'$\ket{\nearrow}$', BLUE)
        self.tex_string.set_color_by_tex(r'$\frac{1}{\sqrt{2}} \ket{\uparrow}$', GREEN)
        self.tex_string.set_color_by_tex(r'$\frac{1}{\sqrt{2}}\ket{\rightarrow}$', RED)
        self.tex_string_right = Tex(r'Réduction du paquet d\textprimstress ondes \\ de ',r'$\ket{\nearrow}$',' à ',r'$\ket{\uparrow}$', font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,3.5,2])
        self.tex_string_right.set_color_by_tex(r'$\ket{\nearrow}$', BLUE)
        self.tex_string_right.set_color_by_tex(r'$\ket{\uparrow}$', GREEN)

class show_text_2(ThreeDScene):
    def __init__(
        self,
        word1="",
        word2="",
        word3="",
        colors=[BLUE,GREEN,YELLOW],
        **kwargs
    ):
        self.tex_string = Tex(r' Photon dans l\textprimstress état \\  de superposition ', r'$\ket{\nearrow}$', r'$=$', r'$\ket{\uparrow}$', r'$+$', r'$\ket{\rightarrow}$', font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,-3.5,1.6])
        self.tex_string.set_color_by_tex(r'$\ket{\nearrow}$', colors[0])
        self.tex_string.set_color_by_tex(r'$\ket{\uparrow}$', colors[1])
        self.tex_string.set_color_by_tex(r'$\ket{\rightarrow}$', colors[2])
        self.tex_string_right = Tex(r' Photon dans l\textprimstress état \\  de superposition ', r'$\ket{\uparrow}$', ' ou ', r'$\ket{\rightarrow}$', font_size=40).rotate(np.pi/2, UP).rotate(np.pi/2, RIGHT).move_to([0,+3.5,1.6])
        self.tex_string_right.set_color_by_tex(r'$\ket{\uparrow}$', colors[1])
        self.tex_string_right.set_color_by_tex(r'$\ket{\rightarrow}$', colors[2])
