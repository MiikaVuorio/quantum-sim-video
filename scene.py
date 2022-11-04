from manim import *

class q_states(ThreeDScene):
    def construct(self):

        energy_color = YELLOW_A
        p1_colour = BLUE_B
        p2_colour = BLUE_C
        ground_colour = GOLD_E
        excited_colour = YELLOW_E
        q0_colour = LIGHT_PINK
        q1_colour = PINK
        q01_colour = PURPLE_A
        q012_colour = PURPLE_B

        elec_0 = Surface(
            lambda u, v: np.array([
                0.25 * np.cos(u) * np.cos(v),
                0.25* np.cos(u) * np.sin(v),
                0.25 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[PURPLE_D, PURPLE_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)


        elec_0.rotate(angle= DEGREES*122, axis=[1,0,0])
        
        elec_00 = Dot()
        elec_0.shift(RIGHT*5.5)
        elec_1 = elec_0.copy().shift(3.5*LEFT)

        always_rotate(elec_0, about_point=elec_0.get_center(), axis=[0,1,0], rate=50*DEGREES)
        always_rotate(elec_1, about_point=elec_1.get_center(), axis=[0,1,0], rate=50*DEGREES)

        self.wait()
        self.play(FadeIn(elec_0))
        self.wait() #was 19 before purge on 3.11.2022
        
        
        ket_e = MathTex(r"|", r"e", r"\rangle")
        ket_g = MathTex(r"|",r"g", r"\rangle")


        ket_e.shift(RIGHT*4+UP*2.5)
        ket_g.shift(RIGHT*4+DOWN*2.5)

        e_line = Line(ket_e.get_center(), (ket_e.get_center()+RIGHT*2))
        e_line.shift(RIGHT*0.4)
        excited_state = VGroup(ket_e, e_line)


        g_line = Line(ket_g.get_center(), (ket_g.get_center()+RIGHT*2))
        g_line.shift(RIGHT*0.4)
        ground_state = VGroup(ket_g, g_line)

        energy = Arrow(start=(ket_g.get_center()-[0,1,0]), end=(ket_e.get_center()+[0,1,0])).shift(RIGHT*2.6).set_color(energy_color)
        energy_label = MathTex(r"E").move_to((ket_g.get_center()-[0,1,0])).shift(RIGHT*2.25+UP*0.25).set_color(energy_color)
        
        #Time is approx 22
        self.wait()
        self.play(FadeIn(energy), FadeIn(energy_label))
        self.wait()
        self.play(elec_0.animate.shift(UP*1.5))
        self.wait(3)
        self.play(elec_0.animate.shift(DOWN*1.5))
        self.wait()
        #time approx 33

        self.wait() #was 12 before purge on 3.11.2022

        ### FLYEY PARTICLE HERE

        #particle_hit = Dot()
        particle_hit = Surface(
            lambda u, v: np.array([
                0.25 * np.cos(u) * np.cos(v),
                0.25* np.cos(u) * np.sin(v),
                0.25 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[YELLOW_D, YELLOW_E], resolution=(15, 32)
        ) 
        #particle_hit.rotate(angle= DEGREES*122, axis=[1,0,0])
        #always_rotate(particle_hit, about_point=particle_hit.get_center(), axis=[0,1,0], rate=50*DEGREES)
        
        
        particle_hit.shift(UP*4+LEFT*2.5)

        self.play(particle_hit.animate.shift(RIGHT*8+DOWN*4), run_time=2, rate_func=linear)
        self.play(particle_hit.animate.shift(RIGHT*4+UP), run_time=1, rate_func=linear)
        self.remove(particle_hit)
        
        self.wait() #was 8 before purge on 3.11.2022
        #We want to be at about 62 sec
        self.play(FadeOut(elec_0))
        self.wait(2)
        elec_0.shift(UP*2.5)
        self.add(elec_0)
        self.wait() #was 7 before purge on 3.11.2022

        #DEVISED ARROW SHIT COMES HERE
        observation_arrow = Arrow()


        self.bring_to_back(VGroup(excited_state, ground_state))
        self.play(FadeIn(excited_state), FadeIn(ground_state))
        self.wait()
        # self.play(g_line.animate.set_color(GOLD_E), ket_g[0].animate.set_color(GOLD_E), ket_g[-1].animate.set_color(GOLD_E))
        # self.play(e_line.animate.set_color(YELLOW_E), ket_e[0].animate.set_color(YELLOW_E), ket_e[-1].animate.set_color(YELLOW_E))
        self.play(g_line.animate.set_color(ground_colour), ket_g.animate.set_color(ground_colour))
        self.play(e_line.animate.set_color(excited_colour), ket_e.animate.set_color(excited_colour))
        elec_0.shift(UP*2.5)
        self.wait()
        elec_0.shift(DOWN*5)
        self.wait()
        self.play(elec_0.animate.shift(UP*2.5))
        self.wait()

        p_1_val = ValueTracker(0.5)
        prob_1 = always_redraw(lambda: MathTex(r"p", r"_1", r"=", round(p_1_val.get_value(), 2)).move_to(ket_g.get_center()).shift(DOWN*0.8+RIGHT*0.8).set_color(p1_colour))

        p_2_val = ValueTracker(0.5)
        prob_2 = always_redraw(lambda: MathTex(r"p", r"_2", r"=", round(p_2_val.get_value(), 2)).move_to(ket_e.get_center()).shift(UP*0.8+RIGHT*0.8).set_color(p2_colour))

        self.play(FadeIn(prob_1), FadeIn(prob_2))
        self.wait()
        elec_0.shift(UP*2.5)
        p_1_val.set_value(0)
        p_2_val.set_value(1)
        self.wait()
        self.play(p_1_val.animate.set_value(0.5), p_2_val.animate.set_value(0.5), elec_0.animate.shift(DOWN*2.5))
        self.wait()

        q_state_def = MathTex(r"|q_0\rangle",r"=", r"p", r"_1", r"|", r"g", r"\rangle", r"+", r"p", r"_2", r"|", r"e", r"\rangle")
        q_state_def[0].set_color(q0_colour)
        q_state_def[4:7].set_color(ground_colour)
        q_state_def[10:13].set_color(excited_colour)
        q_state_def[2:4].set_color(p1_colour)
        q_state_def[8:10].set_color(p2_colour)
        self.play(FadeIn(q_state_def[0:2]))
        self.wait()


        ket_g_copy = ket_g.copy()
        self.play(
            ReplacementTransform(ket_g_copy[0], q_state_def[4], path_arc=-90 * DEGREES),
            ReplacementTransform(ket_g_copy[1:len(ket_g_copy)], q_state_def[5:7], path_arc=-90 * DEGREES)
        )
        self.wait()
        ket_e_copy = ket_e.copy()
        self.play(
            ReplacementTransform(ket_e_copy[0], q_state_def[-3], path_arc=90 * DEGREES),
            ReplacementTransform(ket_e_copy[1:len(ket_g)], q_state_def[-2:len(q_state_def)], path_arc=90 * DEGREES)
        )
        self.play(FadeIn(q_state_def[7]))
        self.wait()
        prob_1_copy = prob_1.copy()
        self.play(
            ReplacementTransform(prob_1_copy[0], q_state_def[2], path_arc=-90 * DEGREES), 
            ReplacementTransform(prob_1_copy[1], q_state_def[3], path_arc=-90 * DEGREES)
        )
        prob_2_copy = prob_2.copy()
        self.play(
            ReplacementTransform(prob_2_copy[0], q_state_def[8], path_arc=90 * DEGREES), 
            ReplacementTransform(prob_2_copy[1], q_state_def[9], path_arc=90 * DEGREES)
        )
        self.wait()
        #self.play(Write(q_state_def[2]), Write(q_state_def[8])) YOU MAY WANT TO REVEAL THE SQRT AT THIS POINT
        self.wait()

        q_state_def_01 = MathTex(r"|q_0\rangle",r"=", r"p", r"_1", r"|", r"0", r"\rangle", r"+", r"p", r"_2", r"|", r"1", r"\rangle")
        q_state_def_01[0].set_color(q0_colour)
        q_state_def_01[4:7].set_color(ground_colour)
        q_state_def_01[10:13].set_color(excited_colour)
        q_state_def_01[2:4].set_color(p1_colour)
        q_state_def_01[8:10].set_color(p2_colour)

        ket_0 = MathTex(r"|", r"0", r"\rangle").move_to(ket_g.get_center()).set_color(ground_colour)
        ket_1 = MathTex(r"|", r"1", r"\rangle").move_to(ket_e.get_center()).set_color(excited_colour)


        self.play(
            Transform(q_state_def[5], q_state_def_01[5]),
            Transform(q_state_def[-2], q_state_def_01[-2]),
            Transform(ket_g[1], ket_0[1]),
            Transform(ket_e[1], ket_1[1])
        )
        self.wait()
        q_0_eq_copy = q_state_def.copy()
        q_state_def.generate_target()
        q_vec = Matrix([[r"p_1"],[r"p_2"]])
        q_def_vec = VGroup(q_0_eq_copy, MathTex("="), q_vec).arrange(RIGHT, buff=.25).shift(LEFT*0.5)
        q_state_def.target.move_to(q_0_eq_copy)
        self.play(MoveToTarget(q_state_def))
        q_vec.get_brackets().set_color(GREY_A)
        q_vec[0][0].set_color(p1_colour)
        q_vec[0][1].set_color(p2_colour)

        self.play(
            Write(q_def_vec[1]),
            Write(q_vec.get_brackets())
        )
        self.wait()

        self.play(
            TransformMatchingShapes(q_state_def[2:4].copy(), q_vec[0][0]),
            TransformMatchingShapes(q_state_def[8:10].copy(), q_vec[0][1])
        )
        


        q_vec.generate_target()
        q_vec.target.move_to(ORIGIN)
        equals_sign = q_def_vec[1]
        equals_sign.generate_target()
        equals_sign.target.align_to(q_vec.target, LEFT)
        equals_sign.target.shift(LEFT*equals_sign.width+LEFT*0.25)
        q_state_def.target.align_to(equals_sign.target, LEFT)
        q_state_def.target.shift(LEFT*q_state_def.width+LEFT*0.25)

        self.play(MoveToTarget(q_vec), MoveToTarget(q_state_def), MoveToTarget(equals_sign))

        vec_ket_0 = MathTex(r"|", r"0", r"\rangle").set_color(ground_colour)
        vec_ket_1 = MathTex(r"|", r"1", r"\rangle").set_color(excited_colour)
        vec_ket_0.move_to(q_vec[0][0].get_center()).shift(RIGHT*1.25)
        vec_ket_1.move_to(q_vec[0][1].get_center()).shift(RIGHT*1.25)

        self.play(FadeIn(vec_ket_0))
        self.play(FadeIn(vec_ket_1))
        self.wait()

        #HERE WE REVEAL SQRT
        #q_state_def = MathTex(r"|q_0\rangle=", r"p", r"_1", r"|", r"g", r"\rangle", r"+", r"p", r"_2", r"|", r"e", r"\rangle")
        #q_0_eq = VGroup(q_state_def[0:4], q_state_def[5:-1], q_state_def_01[4], q_state_def_01[10], ket_e_copy, ket_g_copy, prob_1_copy[0:2], prob_2_copy[0:2])
        #q_state_def_01 = MathTex(r"|q_0\rangle=", r"p", r"_1", r"|", r"0", r"\rangle", r"+", r"p", r"_2", r"|", r"1", r"\rangle")

        axes = ThreeDAxes(
            x_range=[-1,1,1],
            x_length=2,
            y_range=[-1,1,1],
            y_length=2,
            z_range=[-1,1,1],
            z_length=1.5,
            tips=False
        )
        vector = Vector([np.sqrt(0.5), np.sqrt(0.5), 0]).set_color(q0_colour)
        ket_q0 = MathTex(r"|q_0\rangle").next_to(vector.get_end(), RIGHT).scale(0.75).shift(LEFT*0.25).set_color(q0_colour)
        b1 = Brace(vector).shift(UP*0.25).set_color(p1_colour)
        b1text = b1.get_tex(r"\sqrt{p_1}").scale(0.75).shift(UP*0.25).set_color(p1_colour)
        b2 = Brace(vector, direction=LEFT).shift(RIGHT*0.25).set_color(p2_colour)
        b2text = b2.get_tex(r"\sqrt{p_2}").scale(0.75).shift(RIGHT*0.25).set_color(p2_colour)
        one_label = MathTex(r"1").shift(UP*0.5+RIGHT*0.3).scale(0.65)
        vec_visual_sys = VGroup(axes, vector, ket_q0, b1, b1text, b2, b2text, one_label).scale(1.25)

        vec_visual_sys.to_corner(UL).shift(RIGHT*0.5+DOWN*0.25)

        q_state_def_sqrt = MathTex(r"|q_0\rangle",r"=", r"\sqrt{",r"p_1",r"}", r"|", r"0", r"\rangle", r"+", r"\sqrt{",r"p_2",r"}", r"|", r"1", r"\rangle").align_to(q_state_def, RIGHT)
        q_state_def_sqrt[0].set_color(q0_colour)
        q_state_def_sqrt[5:8].set_color(ground_colour)
        q_state_def_sqrt[12:15].set_color(excited_colour)
        q_state_def_sqrt[3].set_color(p1_colour)
        q_state_def_sqrt[10].set_color(p2_colour)


        self.play(
            Transform(q_state_def[0:2], q_state_def_sqrt[0:2]), 
            Transform(q_state_def[2:4], q_state_def_sqrt[3]), 
            Transform(q_state_def[4:8], q_state_def_sqrt[5:9]), 
            Transform(q_state_def[8:10], q_state_def_sqrt[10]),
            Transform(q_state_def[-3:len(q_state_def)], q_state_def_sqrt[-3:len(q_state_def_sqrt)])
        )
        self.play(
            Write(q_state_def_sqrt[2]),
            Write(q_state_def_sqrt[9])
        )
        p_1_sqrt = MathTex(r"\sqrt{",r"p_1",r"}").move_to(q_vec[0][0].get_center()).shift(LEFT*0.1)
        p_2_sqrt = MathTex(r"\sqrt{",r"p_2",r"}").move_to(q_vec[0][1].get_center()).shift(LEFT*0.1)
        self.play(
            Write(p_1_sqrt[0]),
            Write(p_2_sqrt[0])
        )

        self.play(FadeIn(vec_visual_sys[0:-1]))
        self.play(FadeIn(one_label))

        pythagoras = MathTex(r"a^2",r"+",r"b^2",r"=",r"c^2").move_to(vec_visual_sys.get_center()).align_to(vec_visual_sys, RIGHT)
        pythagoras.shift(RIGHT*(pythagoras.width+1))
        pythagoras_entries = MathTex(r"\sqrt{",r"p_1",r"}^2",r"+",r"\sqrt{",r"p_2",r"}^2",r"=",r"1",r"^2").move_to(pythagoras.get_center())
        pythagoras_entries[1].set_color(p1_colour)
        pythagoras_entries[5].set_color(p2_colour)


        prob_eq = MathTex(r"p_1",r"+",r"p_2",r"=",r"1").move_to(pythagoras.get_center()).shift(DOWN*4)
        prob_eq[0].set_color(p1_colour)
        prob_eq[2].set_color(p2_colour)
        self.play(FadeIn(prob_eq[0:2]))
        self.play(FadeIn(prob_eq[2:4]))
        self.play(FadeIn(prob_eq[4]))

        
        self.play(FadeIn(pythagoras[0:2]))
        self.play(FadeIn(pythagoras[2:4]))
        self.play(FadeIn(pythagoras[4]))

        self.play(
            ReplacementTransform(pythagoras[1], pythagoras_entries[3]), 
            ReplacementTransform(pythagoras[3], pythagoras_entries[-3]), 
            pythagoras[-1].animate.move_to(pythagoras_entries[-2:len(pythagoras_entries)].get_center())
        )

        self.play(FadeOut(pythagoras[0], shift=DOWN), FadeOut(pythagoras[2], shift=DOWN))
        self.play(FadeIn(pythagoras_entries[0:3], shift=DOWN), FadeIn(pythagoras_entries[4:7], shift=DOWN))
        self.play(FadeOut(pythagoras[-1], shift=DOWN))
        self.play(FadeIn(pythagoras_entries[-2:len(pythagoras_entries)], shift=DOWN))   

        probs_eq_copy = prob_eq.copy().move_to(pythagoras_entries.get_center()).align_to(pythagoras_entries, RIGHT)

        self.play(Unwrite(pythagoras_entries[0]), Unwrite(pythagoras_entries[2]), Unwrite(pythagoras_entries[4]), Unwrite(pythagoras_entries[6]), Unwrite(pythagoras_entries[-1]))

        self.play(
            ReplacementTransform(pythagoras_entries[3], probs_eq_copy[1]), 
            ReplacementTransform(pythagoras_entries[-3], probs_eq_copy[3]),
            ReplacementTransform(pythagoras_entries[1], probs_eq_copy[0]),
            ReplacementTransform(pythagoras_entries[5], probs_eq_copy[2]),
            pythagoras_entries[-2].animate.move_to(probs_eq_copy[-1].get_center())
        )

        self.play(vec_visual_sys.animate.rotate(axis=[1,0,0], angle=-65*DEGREES, about_point=axes.coords_to_point(0,0,0)))
        self.wait()
        self.play(vec_visual_sys.animate.rotate(axis=[1,0,0], angle=65*DEGREES, about_point=axes.coords_to_point(0,0,0)))
    



        # self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES)
        # self.wait()
        # self.move_camera(0, theta=-90 * DEGREES)

        self.play(FadeOut(vec_visual_sys), FadeOut(prob_eq), FadeOut(pythagoras_entries), FadeOut(probs_eq_copy))

        vec_sys = VGroup(vec_ket_0, vec_ket_1, q_vec, equals_sign, q_state_def)
        self.play(FadeOut(vec_sys), FadeOut(p_1_sqrt[0]), FadeOut(p_2_sqrt[0]), 
            FadeOut(q_state_def_sqrt[2]), 
            FadeOut(q_state_def_sqrt[9])
        )

        sys_0 = VGroup(ket_0, ket_1, e_line, g_line)
        sys_1 = sys_0.copy().shift(LEFT*3.5)
        self.bring_to_back(sys_1)
        #always_rotate(elec_1, about_point=elec_1.get_center(), axis=[0,1,0], rate=50*DEGREES)
        sys_0_label = MathTex(r"|", r"q_0", r"\rangle").move_to(ket_1.get_center()).shift(UP+RIGHT).set_color(q0_colour)
        sys_1_label = MathTex(r"|", r"q_1", r"\rangle").move_to(sys_1[1].get_center()).shift(UP+RIGHT).set_color(q1_colour)
        self.play(FadeIn(elec_1), FadeIn(sys_1), FadeOut(prob_1), FadeOut(prob_2))
        self.wait()
        self.play(FadeIn(sys_0_label))
        self.play(FadeIn(sys_1_label))
        
        # two_q_states = MathTex(r"|", r"q_1", r"q_0", r"\rangle", r"=", r"p_1", r"|00\rangle", r"+", r"p_2", r"|01\rangle", r"+", r"p_3", r"|10\rangle", r"+",r"p_2", r"|11\rangle")
        # two_q_states.scale(0.75).to_edge(LEFT).shift(UP)
        # self.play(FadeIn(two_q_states[0:5]))
        # self.wait()


        two_q_name = MathTex(r"|", r"q_1", r"q_0", r"\rangle").set_color(q01_colour)
        four_state_vector = Matrix([[r"p_1"],[r"p_2"], [r"p_3"], [r"p_4"]]).to_edge(LEFT).shift(RIGHT)
        four_state_vector.set_color(q01_colour)
        # four_state_vector[0][0].set_color(TEAL_A)
        # four_state_vector[0][1].set_color(TEAL_B)
        # four_state_vector[0][2].set_color(TEAL_C)
        # four_state_vector[0][3].set_color(TEAL_D)

        ket_00 = MathTex(r"|00\rangle").move_to(four_state_vector[0][0].get_center()).shift(RIGHT*1.25)#.set_color(TEAL_A)
        ket_01 = MathTex(r"|01\rangle").move_to(four_state_vector[0][1].get_center()).shift(RIGHT*1.25)#.set_color(TEAL_B)
        ket_10 = MathTex(r"|10\rangle").move_to(four_state_vector[0][2].get_center()).shift(RIGHT*1.25)#.set_color(TEAL_C)
        ket_11 = MathTex(r"|11\rangle").move_to(four_state_vector[0][3].get_center()).shift(RIGHT*1.25)#.set_color(TEAL_D)
        four_state_kets = VGroup(ket_00, ket_01, ket_10, ket_11)
        four_state_kets.set_color(q01_colour)


        q01_shift = RIGHT*0.5
        two_q_name.move_to(four_state_vector.get_center()).align_to(four_state_vector, UP).shift(UP*(two_q_name.height + 0.35)+q01_shift)

        self.play(FadeIn(two_q_name))

        elec_0.shift(DOWN*2.5)
        elec_1.shift(DOWN*2.5)
        self.play(FadeIn(ket_00))
        self.wait()
        elec_0.shift(UP*5)
        self.play(FadeIn(ket_01))
        elec_0.shift(DOWN*5)
        elec_1.shift(UP*5)
        self.play(FadeIn(ket_10))
        elec_0.shift(UP*5)
        self.play(FadeIn(ket_11))
        self.play(Write(four_state_vector.get_brackets()))
        self.play(Write(four_state_vector[0]))

        three_q_name = MathTex(r"|", r"q_2", r"q_1", r"q_0", r"\rangle").scale(0.8).set_color(q012_colour)
        eight_state_vector = Matrix([[r"p_1"],[r"p_2"], [r"p_3"], [r"p_4"], [r"p_5"],[r"p_6"], [r"p_7"], [r"p_8"]]).scale(0.8).shift(LEFT*0.65)
        eight_state_vector.set_color(q012_colour)
        # teals_set = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E]
        # teal_selector = 0
        # for p in eight_state_vector[0]:
        #     p.set_color(teals_set[teal_selector])
        #     teal_selector = teal_selector + 1
        #     if teal_selector == 5:
        #         break

        # eight_state_vector[0][5].set_color(teals_set[-2])
        # eight_state_vector[0][6].set_color(teals_set[-3])
        # eight_state_vector[0][7].set_color(teals_set[-4])


        ket_000 = MathTex(r"|000\rangle").move_to(eight_state_vector[0][0].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_A)
        ket_001 = MathTex(r"|001\rangle").move_to(eight_state_vector[0][1].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_B)
        ket_010 = MathTex(r"|010\rangle").move_to(eight_state_vector[0][2].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_C)
        ket_011 = MathTex(r"|011\rangle").move_to(eight_state_vector[0][3].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_D)
        ket_100 = MathTex(r"|100\rangle").move_to(eight_state_vector[0][4].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_E)
        ket_101 = MathTex(r"|101\rangle").move_to(eight_state_vector[0][5].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_D)
        ket_110 = MathTex(r"|110\rangle").move_to(eight_state_vector[0][6].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_C)
        ket_111 = MathTex(r"|111\rangle").move_to(eight_state_vector[0][7].get_center()).shift(RIGHT*1.25).scale(0.8)#.set_color(TEAL_B)
        eight_state_kets = VGroup(ket_000, ket_001, ket_010, ket_011, ket_100, ket_101, ket_110, ket_111)
        eight_state_kets.set_color(q012_colour)

        q012_shift = 0.4*RIGHT
        three_q_name.move_to(eight_state_vector.get_center()).align_to(eight_state_vector, UP).shift(UP*(three_q_name.height + 0.3)+q012_shift)

        self.play(
            FadeOut(elec_0), 
            FadeOut(elec_1)
        )
        self.play( 
            FadeOut(sys_0), 
            FadeOut(sys_1), 
            FadeOut(ket_e), 
            FadeOut(ket_g), 
            FadeOut(energy), 
            FadeOut(energy_label),
            FadeOut(sys_0_label),
            FadeOut(sys_1_label)            
        )



        self.play(FadeIn(three_q_name))
        self.play(Write(eight_state_vector), Write(eight_state_kets))
        self.wait()
        self.play(Unwrite(four_state_kets), Unwrite(eight_state_kets))
        self.play(eight_state_vector.animate.shift(q012_shift), four_state_vector.animate.shift(q01_shift))
        self.wait()

        two_to_n = MathTex(r"2",r"^n")
        two_to_n[0].set_color(BLUE_C)
        two_to_n[-1].set_color(BLUE_D)
        d_relation = VGroup(MathTex(r"d="), two_to_n).arrange(RIGHT, buff=0.25)
        d_relation[0].set_color(BLUE_B)
        d_relation.shift(RIGHT*3.5+UP*0.25)

        self.play(FadeIn(d_relation[0]))
        self.play(Write(two_to_n))

        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )






class ket_bra(ThreeDScene):
    def construct(self):
        title = Tex("The ","mathematics ","behind ","simulating ","quantum ","systems ","with ","quantum ","computers").scale(0.8).to_edge(UP).shift(DOWN)
        for word in title:
            word.set_color(random_bright_color())
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        self.wait()

        chap_1 = Text("Chapter 1: Quantum states as vectors")
        self.play(Write(chap_1))
        self.play(FadeOut(chap_1))

        q0_vec = Matrix(
            [[1],
             [0]]
        )
        ket_q0 = MathTex(r"|q_0\rangle")
        q0_def = VGroup(ket_q0, MathTex(r"="), q0_vec).arrange(RIGHT, buff=.25)

        self.play(FadeIn(q0_def[2], shift=DOWN, run_time=0.2))
        self.wait()
        self.play(FadeIn(q0_def[0], q0_def[1], shift=DOWN, run_time=0.2))

        
        # ket_0 = MathTex(r"|0\rangle")
        # ket_1 = MathTex(r"|1\rangle")

        # ket_0_v2 = MathTex(r"|0\rangle")
        # ket_1_v2 = MathTex(r"|1\rangle")

        # ket_0_v3 = MathTex(r"""|0\rangle=\begin{pmatrix}
        #                     1\\
        #                     0
        #                     \end{pmatrix}""")
        # ket_1_v3 = MathTex(r"""|1\rangle=\begin{pmatrix}
        #                     0\\
        #                     1
        
        # self.play(Write(ket_q0), Write(ket_0), Write(ket_1))
        # self.wait(0.5)
        # self.play(FadeOut(ket_q0))
        # self.play(Transform(ket_0, ket_0_v2), Transform(ket_1, ket_1_v2))
        # self.wait(1)
        # self.play(Transform(ket_0, ket_0_v3), Transform(ket_1, ket_1_v3))
        # self.wait()
        # self.play(FadeOut(ket_0), FadeOut(ket_1))

        axes = ThreeDAxes(
            tips=False,
            x_range=[-3,3],
            y_range=[-3,3],
            z_range=[-2,2],
            x_length=6,
            y_length=6,
            z_length=4
        )
        vector = Vector([1, 0, 0])

        q0_def.generate_target()
        q0_def.target.scale(0.5)
        q0_def.target.move_to(RIGHT).shift(UP*q0_def.height*0.25+UP*0.25)

        self.play(MoveToTarget(q0_def))
        self.play(Create(vector))
        self.play(Create(axes, run_time=3, lag_ratio=0.1))
        self.play(axes.animate.rotate(phi=75 * DEGREES, theta=-45 * DEGREES))
        #self.play(Rotating(vector, radians=PI/2, axis=[0, 1, 0], rate_func=smooth, about_point=ORIGIN))
        #self.play(Rotating(vector, radians=-PI/2, axis=[0, 1, 0], rate_func=smooth, about_point=ORIGIN))
        self.wait()
        self.move_camera(0, theta=-90 * DEGREES)

        self.play(FadeOut(axes, vector))

        q0_def.generate_target()
        q0_def.target.scale(2)
        q0_def.target.move_to(ORIGIN)
        self.play(MoveToTarget(q0_def))
        # self.play(Rotating(vector, radians=-PI*4/5, rate_func=smooth, about_point=ORIGIN))
        # self.wait()
        # self.play(FadeOut(axes), FadeOut(vector))
        two_to_n = MathTex(r"2^n")
        d_relation = VGroup(MathTex(r"d="), two_to_n).arrange(RIGHT, buff=0.25)
        d_relation.shift(RIGHT*4+UP*0.25)

        self.play(Write(d_relation))
        self.wait()
        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )

class new_schrodinger_part(Scene):
    def construct(self):
        chap_2 = Text("Chapter 2: The schrödinger equatiton")
        self.play(Write(chap_2))
        self.play(FadeOut(chap_2))

        one_q = MathTex(r"|", r"q_0", r"\rangle")
        two_q = MathTex(r"|", r"q_1", r"q_0", r"\rangle")
        three_q = MathTex(r"|", r"q_2", r"q_1", r"q_0", r"\rangle")
        
        
        vec_num_1 = ValueTracker(1) 
        vec_num_2 = ValueTracker(0)

        q_notation = VGroup(one_q, two_q, three_q).arrange(DOWN, buff=.75).to_edge(LEFT).shift(RIGHT)
        q_brace = Brace(q_notation, RIGHT)
        self.play(FadeIn(q_notation, shift=RIGHT), Write(q_brace))
        self.wait()

        psi_ket = MathTex(r"|", r"\Psi", r"\rangle")
        v_psi_tar = Matrix([[1.0],[0.0]])

        psi_eq = VGroup(psi_ket, MathTex("="), v_psi_tar).arrange(RIGHT, buff=.4)
        psi_ket.shift(RIGHT*0.1)
        v_psi = always_redraw(lambda: Matrix([[round(vec_num_1.get_value(), 2)],[round(vec_num_2.get_value(), 2)]]).move_to(v_psi_tar))
        
        psi_ket_t = MathTex(r"|", r"\Psi", r"(", r"t", r")", r"\rangle")
        psi_ket_t.align_to(psi_ket, RIGHT)
        psi_ket_t_dup = psi_ket_t.copy()
        self.play(Write(psi_ket))
        self.wait()
        self.play(FadeOut(q_notation), FadeOut(q_brace))
        self.wait()
        self.play(ReplacementTransform(psi_ket[0:2], psi_ket_t[0:2]))
        self.play(Write(psi_ket_t[2:5]))     
        self.wait()

        time = ValueTracker(0)
        psi_tracked = always_redraw(lambda: MathTex(r"|",r"\Psi",r"(", round(time.get_value(), 2), r")",r"\rangle}").align_to(psi_ket, RIGHT))

        self.play(ReplacementTransform(psi_ket_t[0:3], psi_tracked[0:3]))
        self.play(FadeOut(psi_ket_t[3], shift=DOWN))
        self.play(Write(psi_tracked[3]))
        self.add(psi_tracked)

        self.play(Write(psi_eq[1]), Write(v_psi))
        self.wait()

        self.play(time.animate.set_value(1), vec_num_1.animate.set_value(0), vec_num_2.animate.set_value(1), run_time=3)

        self.play(FadeOut(psi_eq[1]), FadeOut(v_psi), FadeOut(psi_tracked[3]))
        self.play(ReplacementTransform(psi_tracked[0:3], psi_ket_t_dup[0:3]))
        self.play(Write(psi_ket_t_dup[3]))
        psi_framebox = SurroundingRectangle(psi_ket_t_dup, buff = .1)
        self.play(Create(psi_framebox))
        self.play(Uncreate(psi_framebox))
        schr_eq_1 = MathTex(r"i\hbar",r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"H",r"|\Psi(t)\rangle")
        schr_eq_1[2].align_to(psi_ket, RIGHT)
        schr_eq_1[0:2].align_to(schr_eq_1[2], LEFT).shift(LEFT*(schr_eq_1[0:2].width+0.15))
        schr_eq_1[3:len(schr_eq_1)].align_to(schr_eq_1[2], RIGHT).shift(RIGHT*(schr_eq_1[3:len(schr_eq_1)].width+0.2))
        self.play(Write(schr_eq_1[1]))
        self.wait()
        self.play(Write(schr_eq_1[-1]), Write(schr_eq_1[3]))
        self.play(Write(schr_eq_1[4]))
        schr_eq_2 = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle").align_to(schr_eq_1, RIGHT)

        shift_distance = (schr_eq_2[1].get_edge_center(LEFT) - schr_eq_1[2].get_edge_center(LEFT))
        psi_ket_group = VGroup(psi_ket_t_dup[0:4], psi_ket[-1], psi_ket_t[3:5], psi_tracked[4:6])

        self.play(
            ReplacementTransform(schr_eq_1[1], schr_eq_2[0]),
            ReplacementTransform(schr_eq_1[3], schr_eq_2[2]),
            ReplacementTransform(schr_eq_1[0], schr_eq_2[3], path_arc=90 * DEGREES),
            ReplacementTransform(schr_eq_1[4:], schr_eq_2[4:]),
            psi_ket_group.animate.shift(shift_distance)
        )
        self.wait()

        schr_eq_solv = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle",r"\Rightarrow",r"|\Psi(t)\rangle=e^{-iHt}|\Psi(0)\rangle")

        shift_distance_2_the_electric_boogaloo = (schr_eq_solv[1].get_edge_center(LEFT) - schr_eq_2[1].get_edge_center(LEFT))

        self.play(
            ReplacementTransform(schr_eq_2[0], schr_eq_solv[0]),
            ReplacementTransform(schr_eq_2[2:6], schr_eq_solv[2:6]),
            psi_ket_group.animate.shift(shift_distance_2_the_electric_boogaloo)
        )
        schr_eq_solv_copy = schr_eq_solv.copy().to_edge(UP)
        self.play(Write(schr_eq_solv[6:8]))

        #ReplacementTransform(psi_ket_group, schr_eq_solv_copy[1])
        self.remove(psi_ket_group)
        self.play(schr_eq_solv.animate.to_edge(UP))








        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )












class schrodinger_part(Scene):
    def construct(self):
        chap_2 = Text("Chapter 2: The schrödinger equatiton")
        self.play(Write(chap_2))
        self.play(FadeOut(chap_2))

        one_q = MathTex(r"|", r"q_0", r"\rangle")
        two_q = MathTex(r"|", r"q_1", r"q_0", r"\rangle")
        three_q = MathTex(r"|", r"q_2", r"q_1", r"q_0", r"\rangle")

        q_notation = VGroup(one_q, two_q, three_q).arrange(DOWN, buff=.75).to_edge(LEFT).shift(RIGHT)
        self.play(FadeIn(q_notation, shift=RIGHT))
        self.wait()

        psi_ket = MathTex(r"|", r"\Psi", r"\rangle")
        psi_ket_t = MathTex(r"|", r"\Psi", r"(", r"t", r")", r"\rangle")
        psi_ket_t.align_to(psi_ket, RIGHT)
        self.play(Write(psi_ket))
        self.wait()
        self.play(Transform(psi_ket[0:2], psi_ket_t[0:2]))
        self.play(Write(psi_ket_t[2:5]))       

        time = ValueTracker(0)
        psi_tracked = always_redraw(lambda: MathTex(r"|",r"\Psi",r"(", round(time.get_value(), 2), r")\rangle}"))
        
        
        schr_eq_1 = MathTex(r"i\hbar",r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"H",r"|\Psi(t)\rangle")
        schr_eq_2 = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle")
        schr_eq_solv = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle",r"\Rightarrow",r"|\Psi(t)\rangle=e^{-iHt}|\Psi(0)\rangle")
        solved_schr_eq = MathTex(r"|\Psi(t)\rangle=e^{-iHt}|\Psi(0)\rangle")
        framebox1 = SurroundingRectangle(schr_eq_1[2], buff = .1)
        framebox2 = SurroundingRectangle(schr_eq_1[5], buff = .1)
        framebox3 = SurroundingRectangle(schr_eq_1[4])
        eq_r_side = VGroup(schr_eq_1[4],schr_eq_1[5])
        framebox4 = SurroundingRectangle(schr_eq_2[0], buff = .1)

    


        vec_num_1 = ValueTracker(1) 
        vec_num_2 = ValueTracker(0)
        v_psi = always_redraw(lambda: Matrix([[round(vec_num_1.get_value(), 2)],[round(vec_num_2.get_value(), 2)]]).shift(RIGHT*1.35))
        vector_tar = Matrix([[1.0],[0.0]])
        dl_schrodinger = schr_eq_1.copy()
        dl_schrodinger.to_corner(DL)


        self.play(Write(schr_eq_1))
        self.wait()
        self.play(Create(framebox1), Create(framebox2))
        self.wait()
        self.play(Uncreate(framebox1), Uncreate(framebox2))
        self.play(Transform(schr_eq_1, dl_schrodinger))
        dup_psi = schr_eq_1[5].copy()
        dup_psi_tar = schr_eq_1[5].copy()
        psi_eq = VGroup(dup_psi_tar, Tex("="), vector_tar).arrange(RIGHT, buff = 0.75)
        dup_psi.generate_target()
        dup_psi.target.move_to(dup_psi_tar)

        self.play(MoveToTarget(dup_psi))


        self.play(Create(psi_eq[1]), Create(v_psi))
        self.wait()
        always_redraw(lambda: psi_tracked.move_to(dup_psi))
        
        self.play(ReplacementTransform(dup_psi, psi_tracked))
        self.wait()
        self.play(time.animate.set_value(1), vec_num_1.animate.set_value(0), vec_num_2.animate.set_value(1), run_time=3)
        self.wait()
        self.play(FadeOut(psi_tracked, shift=DOWN), FadeOut(psi_eq[1], shift=DOWN), FadeOut(v_psi, shift=DOWN))

        self.play(schr_eq_1.animate.move_to(ORIGIN))
        self.play(Create(framebox3))
        self.wait()
        self.play(Uncreate(framebox3))
        
        h_matrix_vars = Matrix([["a","b"],["c","d"]])
        x_matrix = Matrix([[0,1],[1,0]])

        self.play(Transform(schr_eq_1, dl_schrodinger))
        dup_h = schr_eq_1[4].copy()
        dup_h_tar = schr_eq_1[4].copy()
        h_eq = VGroup(dup_h_tar, Tex("="), h_matrix_vars).arrange(RIGHT, buff = 0.5)
        self.play(dup_h.animate.move_to(dup_h_tar))
        self.play(Create(h_eq[1]), Create(h_matrix_vars))
        self.wait()
        self.play(FadeOut(dup_h, shift=DOWN), FadeOut(h_eq[1], shift=DOWN), FadeOut(h_matrix_vars, shift=DOWN))
        self.play(schr_eq_1.animate.move_to(ORIGIN))
        
        self.play(schr_eq_1[5].animate.set_color(BLUE_D))
        self.play(schr_eq_1[4].animate.set_color(BLUE_D))
        self.wait()
        self.play(eq_r_side.animate.set_color(WHITE))
        self.wait()

        self.play(
            ReplacementTransform(schr_eq_1[1:4], schr_eq_2[0:3]),
            #Write(schr_eq_2[3]),
            ReplacementTransform(schr_eq_1[0], schr_eq_2[3], path_arc=90 * DEGREES),
            ReplacementTransform(schr_eq_1[4:], schr_eq_2[4:])
        )
        self.wait()

        self.play(Create(framebox4))
        self.wait()
        self.play(Uncreate(framebox4))

        self.play(ReplacementTransform(schr_eq_2, schr_eq_solv[0:6]))
        self.play(Write(schr_eq_solv[6:8]))

        self.play(schr_eq_solv.animate.to_edge(UP))
        holder_text = Tex("solved eq and link to 3b1b here")
        self.play(Write(holder_text))
        self.play(Unwrite(holder_text))

        schr_eq_solv[7].generate_target()
        schr_eq_solv[7].target.move_to(ORIGIN)
        self.play(FadeOut(schr_eq_solv[0:7]), MoveToTarget(schr_eq_solv[7]))
        self.play(FadeOut(schr_eq_solv[7]))

class h_part(ThreeDScene):
    def construct(self):
        chap_3 = Text("Chapter 3: What's a hamiltonian")
        self.play(Write(chap_3))
        self.play(FadeOut(chap_3))


        sig_colour = BLUE_D
    
        h_def = MathTex("H =",r"?")
        h_def[1].shift(RIGHT * 0.1)
        model_name = Tex("XXX-Heisenberg")
        heis_h_def = MathTex(r"H=",r"\sum_{\langle ij\rangle}^{N}J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}", r"+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}", r"+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z}",r")")
        heis_h_2= heis_h_def.copy()

        sig_x = MathTex(r"\sigma", r"^{(i)}", r"_{x}")
        sig_x_mat = Matrix([[0,1],[1,0]])
        sig_x_def = VGroup(sig_x, Tex("="), sig_x_mat).arrange(RIGHT, buff= 0.25)
        sig_x.shift(RIGHT*0.35)

        sig_y = MathTex(r"\sigma", r"^{(i)}", r"_{y}")
        sig_y_mat = Matrix([[0,"-i"],["i",0]])
        sig_y_def = VGroup(sig_y, Tex("="), sig_y_mat).arrange(RIGHT, buff= 0.25)
        sig_y.shift(RIGHT*0.35)

        sig_z = MathTex(r"\sigma", r"^{(i)}", r"_{z}")
        sig_z_mat = Matrix([[1,0],[0,-1]])
        sig_z_def = VGroup(sig_z, Tex("="), sig_z_mat).arrange(RIGHT, buff= 0.25)
        sig_z.shift(RIGHT*0.35)

        sigs_defs = VGroup(sig_x_def, sig_y_def, sig_z_def).arrange(RIGHT, buff= 1)


        self.play(Write(h_def))
        model_name.to_edge(UP)
        self.play(Write(model_name))
        self.wait()
        self.play(ReplacementTransform(h_def[0],heis_h_def[0]), FadeOut(h_def[1]))
        self.play(Write(heis_h_def[1:len(heis_h_def)]))
        self.wait()

        self.play(
            heis_h_def[2].animate.set_color(sig_colour),
            heis_h_def[4:6].animate.set_color(sig_colour),
            heis_h_def[7].animate.set_color(sig_colour),
            heis_h_def[9].animate.set_color(sig_colour),
            heis_h_def[11].animate.set_color(sig_colour),
            heis_h_def[12].animate.set_color(sig_colour),
            heis_h_def[14].animate.set_color(sig_colour),
            heis_h_def[16].animate.set_color(sig_colour),
            heis_h_def[18].animate.set_color(sig_colour),
            heis_h_def[19].animate.set_color(sig_colour),
            heis_h_def[21].animate.set_color(sig_colour)
        )
        self.wait()


        self.play(
            FadeOut(heis_h_def[0:2], shift=DOWN),
            FadeOut(heis_h_def[3], shift=DOWN),  
            FadeOut(heis_h_def[5:9], shift=DOWN),
            FadeOut(heis_h_def[10], shift=DOWN),
            FadeOut(heis_h_def[12:16], shift=DOWN),
            FadeOut(heis_h_def[17], shift=DOWN),
            FadeOut(heis_h_def[19:len(heis_h_def)], shift=DOWN),
            FadeOut(model_name)
        )
        self.play(
            ReplacementTransform(heis_h_def[2], sig_x[0]),
            ReplacementTransform(heis_h_def[4], sig_x[2]),
            ReplacementTransform(heis_h_def[9], sig_y[0]),
            ReplacementTransform(heis_h_def[11], sig_y[2]),
            ReplacementTransform(heis_h_def[16], sig_z[0]),
            ReplacementTransform(heis_h_def[18], sig_z[2])
        )
        self.play(
            Write(sig_x_def[1:3]),
            Write(sig_y_def[1:3]),
            Write(sig_z_def[1:3])
        )
        ### HERE EXPLAIN MORE ABOUT SIG_X

        self.play(
            FadeOut(sig_y[0]),
            FadeOut(sig_y[2]),
            FadeOut(sig_z[0]),
            FadeOut(sig_z[2]),
            FadeOut(sig_y_def[1:len(sig_y_def)]),
            FadeOut(sig_z_def[1:len(sig_z_def)])
        )

        sig_x_0 = MathTex(r"\sigma", r"_{x}", r"|0\rangle",r"=",r"|1\rangle")
        self.play(FadeIn(sig_x_0[2]))
        self.play(FadeIn(sig_x_0[0:2]))
        
        self.play(FadeIn(sig_x_0[3:5]))

        vec_0 = Matrix(
            [[1],
             [0]]
        )
        vec_1 = Matrix(
            [[0],
             [1]]
        )
        eq_mat = Matrix(
            [["1\cdot0+0\cdot1"],
             ["1\cdot1+0\cdot0"]]
        )
        vec_matmul = VGroup(
            sig_x_def[-1].copy(), 
            vec_0
        ).arrange(RIGHT, buff=.25).shift(UP*2)
        
        vec_matmul_step = VGroup(
            MathTex(r"1"), 
            vec_1.copy(), 
            MathTex(r"+"), 
            MathTex(r"0"), 
            vec_0.copy(), 
            MathTex(r"="), 
            eq_mat, 
            MathTex(r"="), 
            vec_1
        ).arrange(RIGHT, buff=.25)

        self.play(FadeOut(sig_x_def[1:2]), FadeOut(sig_x[0]), FadeOut(sig_x[2]))
        self.play(ReplacementTransform(sig_x_def[-1], vec_matmul[0]))
        self.play(FadeIn(vec_matmul[-1]))

        self.play(FadeOut(sig_x_0))
        self.play(
            ReplacementTransform(vec_0[0][0].copy(), vec_matmul_step[0]),
            ReplacementTransform(vec_0[0][1].copy(), vec_matmul_step[3]),
            ReplacementTransform(vec_matmul[0][0][0][0].copy(), vec_matmul_step[1][0][0]),
            ReplacementTransform(vec_matmul[0][0][1][0].copy(), vec_matmul_step[1][0][1]),
            ReplacementTransform(vec_matmul[0].get_rows()[1][0].copy(), vec_matmul_step[4][0][0]),
            ReplacementTransform(vec_matmul[0].get_rows()[1][1].copy(), vec_matmul_step[4][0][1]),
            Write(vec_matmul_step[1].get_brackets()),
            Write(vec_matmul_step[4].get_brackets()),
            FadeIn(vec_matmul_step[2]),
        )
        self.play(Write(vec_matmul_step[5:7]))
        self.play(Write(vec_matmul_step[7:9]))

        self.play(
            FadeOut(vec_matmul_step, shift=LEFT),
            FadeOut(vec_matmul, shift=LEFT)
        )

        ket_0 = MathTex(r"|", r"0", r"\rangle")
        ket_1 = MathTex(r"|",r"1", r"\rangle")

        ket_0.shift(RIGHT*4+UP*2.5)
        ket_1.shift(RIGHT*4+DOWN*2.5)

        e_line = Line(ket_0.get_center(), (ket_0.get_center()+RIGHT*2))
        e_line.shift(RIGHT*0.4)
        excited_state = VGroup(ket_0, e_line)

        g_line = Line(ket_1.get_center(), (ket_1.get_center()+RIGHT*2))
        g_line.shift(RIGHT*0.4)
        ground_state = VGroup(ket_1, g_line)

        energy = Arrow(start=(ket_1.get_center()-[0,1,0]), end=(ket_0.get_center()+[0,1,0])).shift(RIGHT*2.6)
        energy_label = MathTex(r"E").move_to((ket_1.get_center()-[0,1,0])).shift(RIGHT*2.25+UP*0.25)

        sys_0 = VGroup(ket_0, ket_1, e_line, g_line)
        sys_1 = sys_0.copy().shift(LEFT*3.5)
    
        elec_0 = Surface(
            lambda u, v: np.array([
                0.25 * np.cos(u) * np.cos(v),
                0.25* np.cos(u) * np.sin(v),
                0.25 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[PURPLE_D, PURPLE_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN)
        elec_0.rotate(angle= DEGREES*122, axis=[1,0,0])
        elec_0.shift(RIGHT*5.5)
        elec_11 = elec_0.copy().shift(LEFT*3.5)
        always_rotate(elec_0, about_point=elec_0.get_center(), axis=[0,1,0], rate=50*DEGREES)
        always_rotate(elec_11, about_point=elec_0.get_center(), axis=[0,1,0], rysoate=50*DEGREES)
        self.bring_to_back(VGroup(excited_state, ground_state))
        self.play(FadeIn(elec_0, shift=LEFT), FadeIn(sys_0, shift=LEFT))
        self.wait()
        elec_0.shift(UP*2.5)
        self.wait()
        elec_0.shift(DOWN*5)
        schr_eq_1 = MathTex(r"i\hbar",r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"H",r"|\Psi(t)\rangle")
        self.play(FadeIn(schr_eq_1))
        h_brace = Brace(schr_eq_1[-2], UP).shift(DOWN*0.1)
        sig_x_constituent = MathTex(r"\sigma", r"_{x}").move_to(h_brace.get_center())
        sig_x_constituent.shift(UP*(sig_x_constituent.height/2+0.25))
        self.play(Write(h_brace), Write(sig_x_constituent))

        self.play(elec_0.animate.shift(UP*2), run_time=8)

        self.play(FadeOut(schr_eq_1), FadeOut(h_brace), FadeOut(sig_x_constituent))

        self.bring_to_back(sys_1)
        self.play(FadeIn(sys_1))
        

        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )
        

        self.play(FadeIn(heis_h_2))
        self.play(
            heis_h_2[3].animate.set_color(YELLOW),
            heis_h_2[6].animate.set_color(YELLOW),
            heis_h_2[10].animate.set_color(YELLOW),
            heis_h_2[13].animate.set_color(YELLOW),
            heis_h_2[17].animate.set_color(YELLOW),
            heis_h_2[20].animate.set_color(YELLOW)
        )

        self.play(heis_h_2.animate.set_color(WHITE))
        self.play(
            FadeOut(heis_h_2[:2]),
            FadeOut(heis_h_2[5:len(heis_h_2)])
        )
        self.wait()
        sig_x_0 = MathTex(r"\sigma", r"^{(0)}", r"_{y}")        
        sig_x_0.move_to(heis_h_2[2:5])
        
        self.play(
            ReplacementTransform(heis_h_2[3], sig_x_0[1])
        )

        iden_mat = Matrix([[1,0],[0,1]])
        iden_def = VGroup(MathTex("I="), iden_mat).arrange(RIGHT, buff=.1)
        iden_def.shift(RIGHT*2.5)

        sig_x_op = MathTex(r"O=")
        sig_x_op.align_to(sig_x_0, LEFT)
        sig_x_op.shift(LEFT*sig_x_op.width)
        sig_x_op.shift(LEFT*0.15)
        sig_x_op.shift(UP*0.1)
        rest_of_op = MathTex(r"\otimes",r"I^{(1)}",r"\otimes",r"I^{(2)}")
        rest_of_op.align_to(sig_x_0, LEFT)
        rest_of_op.align_to(sig_x_0, UP)
        rest_of_op.shift(RIGHT*sig_x_0.width)
        rest_of_op.shift(RIGHT*0.15)
        self.wait()
        self.play(Write(iden_def))
        self.wait()
        self.play(FadeOut(iden_def))

        self.play(
            Write(rest_of_op[1]),
            Write(rest_of_op[3])
        )
        self.wait()
        self.play(
            Write(rest_of_op[0]),
            Write(rest_of_op[2])
        )
        self.play(
            FadeOut(rest_of_op[1:len(rest_of_op)], shift=DOWN),
            FadeOut(sig_x_0[1],shift=DOWN),
            FadeOut(heis_h_2[2],shift=DOWN),
            FadeOut(heis_h_2[4],shift=DOWN)
        )
        
        vars_mat_a = Matrix([[r"a_{1,1}", r"a_{1,2}"],[r"a_{2,1}",r"a_{2,2}"]])
        vars_mat_b = Matrix([[r"b_{1,1}", r"b_{1,2}"],[r"b_{2,1}",r"b_{2,2}"]])
        vars_mat_a.align_to(rest_of_op[0], LEFT)
        vars_mat_a.shift(LEFT*vars_mat_a.width)
        vars_mat_a.shift(LEFT*0.25)

        vars_mat_b.align_to(rest_of_op[0], RIGHT)
        vars_mat_b.shift(RIGHT*vars_mat_b.width)
        vars_mat_b.shift(RIGHT*0.25)

        tensor_eq_lhs = VGroup(vars_mat_a, rest_of_op[0], vars_mat_b)

        # tex_mat_11 = MathTex(
        #     r"""a_{1,1}""",r"""\begin{bmatrix}b_{1,1} & b_{1,2}\\
        #     b_{2,1} & b_{2,2}
        #     \end{bmatrix}""")
        
        # tensor_rhs_mat_end = MathTex(
        #     r"""\begin{bmatrix}a_{1,1}b_{1,1} & a_{1,1}b_{1,2} & a_{1,2}b_{1,1} & a_{1,2}b_{1,2}\\
        #     a_{1,1}b_{2,1} & a_{1,1}b_{2,2} & a_{1,2}b_{2,1} & a_{1,2}b_{2,2}\\
        #     a_{2,1}b_{1,1} & a_{2,1}b_{1,2} & a_{2,2}b_{1,1} & a_{2,2}b_{1,2}\\
        #     a_{2,1}b_{2,1} & a_{2,1}b_{2,2} & a_{2,2}b_{2,1} & a_{2,2}b_{2,2}
        #     \end{bmatrix}"""
        # )

        rhs_ex_end_mat = Matrix(
            [[r"{{ a_{1,1} }} b_{1,1}", r"{{ a_{1,2} }} b_{1,2}", r"{{ a_{1,2} }} b_{1,1}", r"{{ a_{1,2} }} b_{1,2}"],
            [r"{{ a_{1,1} }} b_{2,1}", r"{{ a_{1,1} }} b_{2,2}", r"{{ a_{1,2} }} b_{1,2}", r"{{ a_{1,2} }} b_{2,2}"],
            [r"{{ a_{2,1} }} b_{1,1}", r"{{ a_{2,1} }} b_{1,2}", r"{{ a_{2,2} }} b_{1,1}", r"{{ a_{2,2} }} b_{1,2}"],
            [r"{{ a_{2,1} }} b_{2,1}", r"{{ a_{2,1} }} b_{2,2}", r"{{ a_{2,2} }} b_{2,1}", r"{{ a_{2,2} }} b_{2,2}"]],
            h_buff=2
        )

        tensor_rhs_mat = Matrix(
            [[r"""{{ a_{1,1} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}""",
            r"""{{ a_{1,2} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}"""],
            [r"""{{ a_{2,1} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}""",
            r"""{{ a_{2,2} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}"""]],
            h_buff=3.8,
            v_buff=1.8)


        tensor_eq = VGroup(tensor_eq_lhs, Tex("="), tensor_rhs_mat)

        self.play(
            FadeIn(vars_mat_a,shift=DOWN),
            FadeIn(vars_mat_b,shift=DOWN)
        )

        tensor_eq[0].generate_target()
        tensor_eq[0].target.scale(0.8)
        tensor_eq[0].target.to_edge(LEFT)

        self.play(
            MoveToTarget(tensor_eq[0])
        )

        tensor_eq[1:len(tensor_eq)].scale(0.8)
        rhs_ex_end_mat.scale(0.8)

        tensor_eq[1].align_to(tensor_eq_lhs, RIGHT)
        tensor_eq[1].shift(tensor_eq[1].width*RIGHT + 0.25*RIGHT)

        tensor_rhs_mat.align_to(tensor_eq[1], RIGHT)
        tensor_rhs_mat.shift(tensor_rhs_mat.width*RIGHT + 0.25*RIGHT)

        rhs_ex_end = VGroup(Tex("="), rhs_ex_end_mat).arrange(RIGHT, buff=0.25)
        rhs_ex_end.to_edge(DOWN)
        rhs_ex_end.shift(UP*1)

        self.play(Write(tensor_eq[1]))

        #self.play(Create(tensor_rhs_mat.get_brackets()))

        self.play(Write(tensor_rhs_mat))

        mat_a_0 = vars_mat_a[0][0].copy()
        mat_a_1 = vars_mat_a[0][1].copy()
        mat_a_2 = vars_mat_a[0][2].copy()
        mat_a_3 = vars_mat_a[0][3].copy()

        self.play(
            mat_a_0.animate.set_color(RED_E),
            tensor_rhs_mat[0][0][0].animate.set_color(RED_E)
        )

        self.wait()

        self.play(
            vars_mat_b.animate.set_color(BLUE_D),
            tensor_rhs_mat[0][0][1].animate.set_color(BLUE_D)
        )

        self.wait()

        self.play(
            mat_a_0.animate.set_color(WHITE),
            tensor_rhs_mat[0][0][0].animate.set_color(WHITE),
            vars_mat_b.animate.set_color(WHITE),
            tensor_rhs_mat[0][0][1].animate.set_color(WHITE)
        )

        self.play(
            TransformMatchingShapes(mat_a_0, tensor_rhs_mat[0][0][0], run_time=2),
            TransformMatchingShapes(mat_a_1, tensor_rhs_mat[0][1][0], run_time=2),
            TransformMatchingShapes(mat_a_2, tensor_rhs_mat[0][2][0], run_time=2),
            TransformMatchingShapes(mat_a_3, tensor_rhs_mat[0][3][0], run_time=2)
        )

        self.play(
            FadeOut(mat_a_0),
            FadeOut(mat_a_1),
            FadeOut(mat_a_2),
            FadeOut(mat_a_3)
        )

        b_mat_0 = vars_mat_b.copy()
        b_mat_1 = vars_mat_b.copy()
        b_mat_2 = vars_mat_b.copy()
        b_mat_3 = vars_mat_b.copy()

        by_parts_0 = tensor_rhs_mat[0][0].get_part_by_tex(r"\begin{bmatrix}")
        by_parts_1 = tensor_rhs_mat[0][1].get_part_by_tex(r"\begin{bmatrix}")
        by_parts_2 = tensor_rhs_mat[0][2].get_part_by_tex(r"\begin{bmatrix}")
        by_parts_3 = tensor_rhs_mat[0][3].get_part_by_tex(r"\begin{bmatrix}")

        self.play(
            TransformMatchingShapes(b_mat_0.get_entries(), by_parts_0[1:-1], run_time=1.5),
            Transform(b_mat_0.get_brackets()[0], by_parts_0[0], run_time=1.5),
            Transform(b_mat_0.get_brackets()[1], by_parts_0[-1], run_time=1.5)
        )

        self.play(
            TransformMatchingShapes(b_mat_2.get_entries(), by_parts_2[1:-1], run_time=1.5),
            Transform(b_mat_2.get_brackets()[0], by_parts_2[0], run_time=1.5),
            Transform(b_mat_2.get_brackets()[1], by_parts_2[-1], run_time=1.5)
        )

        self.play(
            TransformMatchingShapes(b_mat_1.get_entries(), by_parts_1[1:-1], run_time=1.5),
            Transform(b_mat_1.get_brackets()[0], by_parts_1[0], run_time=1.5),
            Transform(b_mat_1.get_brackets()[1], by_parts_1[-1], run_time=1.5)
        )

        self.play(
            TransformMatchingShapes(b_mat_3.get_entries(), by_parts_3[1:-1], run_time=1.5),
            Transform(b_mat_3.get_brackets()[0], by_parts_3[0], run_time=1.5),
            Transform(b_mat_3.get_brackets()[1], by_parts_3[-1], run_time=1.5)
        )

        self.play(
            FadeOut(b_mat_0.get_brackets()),
            FadeOut(b_mat_1.get_brackets()),
            FadeOut(b_mat_2.get_brackets()),
            FadeOut(b_mat_3.get_brackets())
        )

        self.play(tensor_eq.animate.to_edge(UP))
        self.play(Write(rhs_ex_end))

        self.wait()

        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )

        new_heis_def = MathTex(r"H=",r"\sum",r"^{N}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z})")
        kronecker_heis = MathTex(r"H=",r"\sum",r"^{N}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\otimes", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\otimes", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\otimes", r"\sigma", r"^{(j)}", r"_{z})")

        self.play(FadeIn(new_heis_def, shift=DOWN))

        self.wait()

        self.play(
            ReplacementTransform(new_heis_def[0:8], kronecker_heis[0:8]),
            ReplacementTransform(new_heis_def[8:14], kronecker_heis[9:15]),
            ReplacementTransform(new_heis_def[14:20], kronecker_heis[16:22]),
            ReplacementTransform(new_heis_def[20:len(new_heis_def)], kronecker_heis[23:len(kronecker_heis)])
        )
        self.wait()
        self.play(
            Write(kronecker_heis[8]),
            Write(kronecker_heis[15]),
            Write(kronecker_heis[22])
        )
        self.play(
            Unwrite(kronecker_heis[8]),
            Unwrite(kronecker_heis[15]),
            Unwrite(kronecker_heis[22])
        )
        self.wait()
        
        old_heis_def = MathTex(r"H=",r"\sum",r"^{N}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z})")
        self.play(
            ReplacementTransform(kronecker_heis[0:8], old_heis_def[0:8]),
            ReplacementTransform(kronecker_heis[9:15], old_heis_def[8:14]),
            ReplacementTransform(kronecker_heis[16:22], old_heis_def[14:20]),
            ReplacementTransform(kronecker_heis[23:len(kronecker_heis)], old_heis_def[20:len(old_heis_def)])
        )

        nummed_heis_def = MathTex(r"H=",r"\sum",r"^{2}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z})")
        heis_def_4 = MathTex(r"H=",r"\sum",r"^{3}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z})")
        heis_def_5 = MathTex(r"H=",r"\sum",r"^{4}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z})")
        # norm_sum = MathTex(r"\sum",r"^{3}",r"_{n=1}",r"2\cdot n",r"=2\cdot 1+", r"2\cdot 2+", r"2\cdot 3")
        # norm_sum.to_edge(UP)
        # framebox_e = SurroundingRectangle(norm_sum[3])

        # self.play(Write(norm_sum[0:4]))
        # self.wait()
        # self.play(Create(framebox_e))
        # self.play(Uncreate(framebox_e))
        # self.wait()
        # self.play(Write(norm_sum[4]))
        # self.wait()
        # self.play(Write(norm_sum[5]))
        # self.wait()
        # self.play(Write(norm_sum[6]))
        # self.wait()


        # self.play(Unwrite(norm_sum))

        self.wait()

        self.play(old_heis_def[1].animate.set_color(BLUE_D))
        self.play(Transform(old_heis_def[1], nummed_heis_def[1]))
        self.wait()

        i_j_0 = MathTex("i=0,j=1")
        i_j_1 = MathTex("i=1,j=2")
        i_j_2 = MathTex("i=2,j=3")
        i_j_3 = MathTex("i=3,j=4")

        i_j_vals = VGroup(i_j_0, i_j_1, i_j_2, i_j_3).arrange(DOWN, buff=.25)
        frameboxij = SurroundingRectangle(i_j_0, buff=.1)

        i_j_vals.to_edge(UP)

        self.play(Write(i_j_0))
        self.play(Write(i_j_1))
        self.wait()
        self.play(Create(frameboxij))
        self.play(Uncreate(frameboxij))

        framebox_sig_ij = SurroundingRectangle(old_heis_def[5:11])
        # self.play(
        #     Write(i_j_2),
        #     Transform(old_heis_def[1], heis_def_4[1])
        # )
        # self.play(
        #     Write(i_j_3),
        #     Transform(old_heis_def[1], heis_def_5[1])
        # )

        
        self.play(
            Unwrite(i_j_vals[0:2])
        )

        kroned_mat = Matrix(
            [[0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0]]
        )

        #before this part drop j

        whole_heis = MathTex(r"H=",r"\sigma_{x}^{(0)}",r"\otimes",r"\sigma_{x}^{(1)}",r"\otimes",r"I^{(2)}",r"+",r"I^{(0)}\otimes\sigma_{x}^{(1)}\otimes\sigma_{x}^{(2)}+",r"\sigma_{y}^{(0)}\otimes\sigma_{y}^{(1)}\otimes I^{(2)}+",r"I^{(0)}\otimes\sigma_{y}^{(1)}\otimes\sigma_{y}^{(2)}+",r"\sigma_{z}^{(0)}\otimes\sigma_{z}^{(1)}\otimes I^{(2)}+",r"I^{(0)}\otimes\sigma_{z}^{(1)}\otimes\sigma_{z}^{(2)}")
        whole_heis.scale(0.5)
        b1 = Brace(whole_heis[1:6],direction=UP)
        self.play(ReplacementTransform(old_heis_def, whole_heis))
        self.play(Create(b1))
        self.wait()

        first_part = VGroup(sig_x_mat, MathTex("\otimes"), sig_x_mat.copy(), MathTex("\otimes"), iden_mat, MathTex("="), kroned_mat)
        first_part.scale(0.5)
        first_part.arrange(RIGHT, buff=.25)
        first_part.align_to(whole_heis[1], LEFT)
        first_part.shift(UP*kroned_mat.height/2 + 0.4*UP)

        self.play(Write(first_part[0:-2]))
        self.wait()
        self.play(
            first_part[0].animate.set_color(BLUE_D),
            whole_heis[1].animate.set_color(BLUE_D)
        )
        self.play(
            first_part[2].animate.set_color(BLUE_D),
            whole_heis[3].animate.set_color(BLUE_D)
        )
        self.play(
            first_part[4].animate.set_color(BLUE_D),
            whole_heis[5].animate.set_color(BLUE_D)
        )
        self.wait()
        self.play(Write(first_part[-2:len(first_part)]))
        self.wait()
        self.play(
            FadeOut(first_part),
            FadeOut(b1)
        )
        self.play(whole_heis[1:7].animate.set_color(BLUE_D))
        self.play(whole_heis[7].animate.set_color(BLUE_D))
        self.play(whole_heis[8].animate.set_color(BLUE_D))
        self.play(whole_heis[9].animate.set_color(BLUE_D))
        self.play(whole_heis[10].animate.set_color(BLUE_D))
        self.play(whole_heis[11].animate.set_color(BLUE_D))

        schr_eq_1 = MathTex(r"i\hbar",r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"H",r"|\Psi(t)\rangle")
        schr_eq_2 = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle")
        schr_eq_solv = MathTex(r"\frac{d}{dt}",r"|\Psi(t)\rangle",r"=",r"\frac{1}{i\hbar}",r"H",r"|\Psi(t)\rangle",r"\Rightarrow",r"|\Psi(t)\rangle=",r"e^{-iHt}",r"|\Psi(0)\rangle")


        self.play(ReplacementTransform(whole_heis, schr_eq_1[4]))
        self.play(Write(schr_eq_1[0:4]))
        self.play(Write(schr_eq_1[5:len(schr_eq_1)]))

        self.wait()

        
        self.play(
            ReplacementTransform(schr_eq_1[1:4], schr_eq_2[0:3]),
            #Write(schr_eq_2[3]),
            ReplacementTransform(schr_eq_1[0], schr_eq_2[3], path_arc=90 * DEGREES),
            ReplacementTransform(schr_eq_1[4:], schr_eq_2[4:])
        )
        self.wait()

        self.play(ReplacementTransform(schr_eq_2, schr_eq_solv[0:6]))
        self.play(Write(schr_eq_solv[6:len(schr_eq_solv)]))

        self.play(schr_eq_solv.animate.to_edge(UP))

        self.wait()
        # holder_text = Tex("solved eq and link to 3b1b here")
        # self.play(Write(holder_text))
        # self.play(Unwrite(holder_text))

        solve_schr_eq = schr_eq_solv[7:len(schr_eq_solv)]

        solve_schr_eq.generate_target()
        solve_schr_eq.target.move_to(ORIGIN)
        self.play(FadeOut(schr_eq_solv[0:7]), MoveToTarget(solve_schr_eq))
        

        framebox_e_power = SurroundingRectangle(schr_eq_solv[8])

        self.play(Create(framebox_e_power))
        self.play(Uncreate(framebox_e_power))

        self.play(FadeOut(schr_eq_solv[7], shift=DOWN), FadeOut(schr_eq_solv[9], shift=DOWN))

        u_t_eq = MathTex(r"U(t)",r"=").align_to(schr_eq_solv[8], RIGHT)
        u_t_eq.shift((schr_eq_solv[8].width+0.25)*LEFT)

        self.play(FadeIn(u_t_eq, shift=DOWN))

        u_t_schr_eq = MathTex(r"|\Psi(t)\rangle=",r"U(t)",r"|\Psi(0)\rangle")

        self.play(FadeOut(schr_eq_solv[8]), FadeOut(u_t_eq[1]))
        self.play(ReplacementTransform(u_t_eq[0], u_t_schr_eq[1]))
        self.play(Write(u_t_schr_eq[0]))
        self.play(Write(u_t_schr_eq[2]))



        # schreq_solved = MathTex(r"|\Psi(t)\rangle=e^{-i",r"H",r"t}|\Psi(0)\rangle")

        # self.play(ReplacementTransform(mid_h, schreq_solved[1]))
        # self.play(Write(schreq_solved[0]))
        # self.play(Write(schreq_solved[2]))

        # self.play(FadeOut(schreq_solved))

        #tried to get the animation for the tensor matrixes to work, but sometimes you just know that it's time to give up
        # self.play(
        #     ReplacementTransform(tensor_rhs_mat[0][0][0], rhs_ex_end_mat[0][0][0]),
        #     ReplacementTransform(tensor_rhs_mat[0][0][0].copy(), rhs_ex_end_mat[0][4][0]),
        #     ReplacementTransform(tensor_rhs_mat[0][0][0].copy(), rhs_ex_end_mat[0][1][0]),
        #     ReplacementTransform(tensor_rhs_mat[0][0][0].copy(), rhs_ex_end_mat[0][5][0]),
        #     ReplacementTransform(tensor_rhs_mat[0][0][0].copy(), rhs_ex_end_mat[0][4][0]),        
        # )
        
        #sig_x_0 = MathTex(r"\sigma",r"^{(0)}", r"_{x}")
        # self.play(
        #     ReplacementTransform(heis_h_2[2], sig_x_0[0]),
        #     ReplacementTransform(heis_h_2[3], sig_x_0[1]),
        #     ReplacementTransform(heis_h_2[4], sig_x_0[2])
        # )
        

class qcVecs(Scene):
    def construct(self):
        chap_4 = Text("Chapter 4: How do quantum computers fit into all this").scale(0.6)
        self.play(Write(chap_4))
        self.play(FadeOut(chap_4))

        part_0_ax = Axes(
            x_range=[-1,1,1],
            x_length=2,
            y_range=[-1,1,1],
            y_length=2,
            tips=False
        )
        part_0_ax.get_axes()[0].add_labels({-1: MathTex(r"|\Psi(0)\rangle"), 1: MathTex(r"|\Psi(1)\rangle")})
        
        part_1_ax = Axes(
            x_range=[-1,1,1],
            x_length=2,
            y_range=[-1,1,1],
            y_length=2,
            tips=False
        )
        part_1_ax.get_axes()[0].add_labels({-1: MathTex(r"|\Psi(0)\rangle"), 1: MathTex(r"|\Psi(1)\rangle")})

        part_2_ax = Axes(
            x_range=[-1,1,1],
            x_length=2,
            y_range=[-1,1,1],
            y_length=2,
            tips=False
        )
        part_2_ax.get_axes()[0].add_labels({-1: MathTex(r"|\Psi(0)\rangle"), 1: MathTex(r"|\Psi(1)\rangle")})

        part_0_state = Vector([-1,0])
        part_1_state = Vector([-1,0])
        part_2_state = Vector([-1,0])

        part_0 = VGroup(part_0_ax, part_0_state)
        part_1 = VGroup(part_1_ax, part_1_state)
        part_2 = VGroup(part_2_ax, part_2_state)

        particles = VGroup(part_0, part_1, part_2).arrange(RIGHT, buff=.5).scale(0.5)

        particles.to_corner(UL)

        self.play(Create(particles))
        
        rx_mat = Matrix([[r"\cos(\frac{\theta}{2})", r"-i\sin(\frac{\theta}{2})"],[r"-i\sin(\frac{\theta}{2})", r"\cos(\frac{\theta}{2})"]], v_buff=1.5, h_buff=2.6)
        ry_mat = Matrix([[r"\cos(\frac{\theta}{2})", r"-\sin(\frac{\theta}{2})"],[r"\sin(\frac{\theta}{2})", r"\cos(\frac{\theta}{2})"]], v_buff=1.5, h_buff=2.5)
        rz_mat = Matrix([[r"e^{-i\frac{\theta}{2}}", r"0"], [r"0", r"e^{i\frac{\theta}{2}}"]])
        cnot_mat = Matrix(
            [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]]
        )

        rx_eq = VGroup(MathTex(r"{R}_{x}(\theta)"), MathTex(r"="), rx_mat).scale(0.5).arrange(RIGHT, buff=.25)
        ry_eq = VGroup(MathTex(r"{R}_{y}(\theta)"), MathTex(r"="), ry_mat).scale(0.5).arrange(RIGHT, buff=.25)
        rz_eq = VGroup(MathTex(r"{R}_{z}(\theta)"), MathTex(r"="), rz_mat).scale(0.5).arrange(RIGHT, buff=.25)
        cnot_eq = VGroup(MathTex(r"\text{CNOT}"), MathTex(r"="), cnot_mat).scale(0.5).arrange(RIGHT, buff=.25)
        rotation_ops = VGroup(rx_eq, ry_eq, rz_eq).arrange(DOWN, buff=.25)
        qc_ops = VGroup(rotation_ops, cnot_eq).arrange(RIGHT, buff=.5)

        self.play(Write(qc_ops))
        self.wait()
        self.play(FadeOut(qc_ops, shift=DOWN))

        initial_state_psi = MathTex(r"|",r"\Psi",r"(t)\rangle")
        initial_state_q = MathTex(r"|",r"Q",r"(t)\rangle")
        
        self.play(FadeIn(initial_state_psi))
        self.play(FadeOut(initial_state_psi[1], shift=DOWN))
        self.play(FadeIn(initial_state_q[1], shift=DOWN))

        start_state = Matrix(
            [[1],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0],
            [0]]
        ).scale(0.75)
        init_eq_mat = VGroup(MathTex(r"="), start_state)
        init_eq_mat.align_to(initial_state_psi, RIGHT).shift(init_eq_mat.width * RIGHT + 0.25*RIGHT) 

        #start_mat_rep = start_state.coordinate_label()
        self.play(Create(start_state))

        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects]
        )

        schr_eq = MathTex(r"|\Psi(t)\rangle", r"=",r"e^{-iHt}",r"|\Psi(0)\rangle")
        u_func = MathTex(r"U(t)=")
        u_func.align_to(schr_eq[2], LEFT).shift(u_func.width*LEFT + LEFT*.25)

        self.play(FadeIn(schr_eq[0]))
        self.play(FadeIn(schr_eq[3]))
        self.play(FadeIn(schr_eq[2]))
        self.play(Write(schr_eq[1]))

        self.play(FadeOut(schr_eq[0], schr_eq[1], schr_eq[3], shift=DOWN))
        self.play(FadeIn(u_func, shift=DOWN))
        u_def = VGroup(u_func, schr_eq[2])
        self.play(u_def.animate.to_corner(DL))

        schr_eq_u = MathTex(r"|\Psi(t)\rangle", r"=",r"U(t)",r"|\Psi(0)\rangle")
        something_eq = MathTex(r"=?")
        something_eq.align_to(schr_eq[2], RIGHT).shift(RIGHT*something_eq.width + RIGHT*.25)

        #self.play(FadeIn())
        

        trotterisation = MathTex(r"e^{-i\sum_{l}H_{l}t}=\lim_{n\rightarrow\infty}\left({\displaystyle \prod}e^{-iH_{l}t/n}\right)^{n}")


        # psi = MathTex("")
        # self.play(Write(psi))

class chTitle1(Scene):
    def construct(self):
        pass

class chTitle2(Scene):
    def construct(self):
        pass

class chTitle3(Scene):
    def construct(self):
        pass

class chTitle4(Scene):
    def construct(self):
        pass


class wholeVid(ThreeDScene):
    def construct(self):
        #chTitle1.construct(self)
        q_states.construct(self)
        
        #chTitle2.construct(self)
        new_schrodinger_part.construct(self)
        
        #chTitle3.construct(self)
        h_part.construct(self)
        
        #chTitle4.construct(self)
        qcVecs.construct(self)





class test(Scene):
    def construct(self):
        big_mat = MathTex(r"""\begin{bmatrix}a_{1,1}\begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix} & a_{1,2}\begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}\\
            a_{2,1}\begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix} & a_{2,2}\begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}
            \end{bmatrix}"""
        )

        big_mat.to_edge(UP)
        big_mat_parts = big_mat.get_part_by_tex(r"""a_{1,1}""")
        tex_mat_11 = MathTex(
            r"""{{ a_{1,1} }} \begin{bmatrix} b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}""")
        mat_test = Matrix([[r"""{{ a_{1,1} }} \begin{bmatrix} b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}""",
            r"""{{ a_{1,2} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}"""],
            [r"""{{ a_{2,1} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}""",
            r"""{{ a_{2,2} }} \begin{bmatrix}b_{1,1} & b_{1,2}\\
            b_{2,1} & b_{2,2}
            \end{bmatrix}"""]],
            h_buff=3.8,
            v_buff=1.8)
        mat_test.to_edge(DOWN)

        rhs_ex_end_mat = Matrix([[r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}"],
            [r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}"],
            [r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}"],
            [r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}", r"a_{1,1}b_{1,1}"]],
            h_buff=2
        )
        
        mat_part_1 = mat_test[0][0]
        mat_p1_parts = mat_part_1.get_part_by_tex(r"b_{1,1]")

        get_by_parts = tex_mat_11.get_part_by_tex(r"\begin{bmatrix}")

        new_heis_def = MathTex(r"H=",r"\sum",r"^{N}",r"_{\langle ij\rangle}",r"J(",r"\sigma",r"^{(i)}", r"_{x}", r"\sigma", r"^{(j)}", r"_{x}+", r"\sigma", r"^{(i)}", r"_{y}", r"\sigma", r"^{(j)}", r"_{y}+", r"\sigma", r"^{(i)}", r"_{z}", r"\sigma", r"^{(j)}", r"_{z}")



        #FRESHEST TESNTEST
        kroned_mat = Matrix(
            [[0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0]]
        )

        whole_heis = MathTex(r"H=",r"\sigma_{x}^{(0)}\otimes\sigma_{x}^{(1)}\otimes I^{(2)}",r"+I^{(0)}\otimes\sigma_{x}^{(1)}\otimes\sigma_{x}^{(2)}+\sigma_{y}^{(0)}\otimes\sigma_{y}^{(1)}\otimes I^{(2)}+I^{(0)}\otimes\sigma_{y}^{(1)}\otimes\sigma_{y}^{(2)}+\sigma_{z}^{(0)}\otimes\sigma_{z}^{(1)}\otimes I^{(2)}+I^{(0)}\otimes\sigma_{z}^{(1)}\otimes\sigma_{z}^{(2)}")
        whole_heis.scale(0.5)
        b1 = Brace(whole_heis[1],direction=UP)
        self.play(Create(b1))
        
        whole_heis = MathTex(r"H=",r"\sigma_{x}^{(0)}\otimes\sigma_{x}^{(1)}\otimes I^{(2)}",r"+I^{(0)}\otimes\sigma_{x}^{(1)}\otimes\sigma_{x}^{(2)}+\sigma_{y}^{(0)}\otimes\sigma_{y}^{(1)}\otimes I^{(2)}+I^{(0)}\otimes\sigma_{y}^{(1)}\otimes\sigma_{y}^{(2)}+\sigma_{z}^{(0)}\otimes\sigma_{z}^{(1)}\otimes I^{(2)}+I^{(0)}\otimes\sigma_{z}^{(1)}\otimes\sigma_{z}^{(2)}")
        whole_heis.scale(0.5)
        b1 = Brace(whole_heis[1],direction=UP)


        #self.play(Create(whole_heis))
        self.play(Create(b1))
        self.wait()

        sig_x_mat = Matrix([[0,1],[1,0]])
        iden_mat = Matrix([[1,0],[0,1]])

        first_part = VGroup(sig_x_mat, MathTex("\otimes"), sig_x_mat.copy(), MathTex("\otimes"), iden_mat, MathTex("="), kroned_mat)
        first_part.scale(0.5)
        first_part.arrange(RIGHT, buff=.25)
        first_part.align_to(whole_heis[1], LEFT)
        #first_part.shift(UP*kroned_mat.height/2 + 1*UP)

        self.play(Write(first_part[2]))

        self.play(Unwrite(first_part[0]))
        






























































class q_states_test(ThreeDScene):
    def construct(self):
        # elec_0 = Surface(
        #     lambda u, v: np.array([
        #         0.25 * np.cos(u) * np.cos(v),
        #         0.25* np.cos(u) * np.sin(v),
        #         0.25 * np.sin(u)
        #     ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
        #     checkerboard_colors=[PURPLE_D, PURPLE_E], resolution=(15, 32)
        # )
        # self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        # #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # elec_0.rotate(angle= DEGREES*122, axis=[1,0,0])
        elec_0=Dot()
        elec_0.shift(RIGHT*5.5)
        elec_1 = elec_0.copy().shift(3.5*LEFT)

        #always_rotate(elec_0, about_point=elec_0.get_center(), axis=[0,1,0], rate=50*DEGREES)
        self.play(FadeIn(elec_0))
        

        



        ket_e = MathTex(r"|", r"e", r"\rangle")
        ket_g = MathTex(r"|",r"g", r"\rangle")

        ket_e.shift(RIGHT*4+UP*2.5)
        ket_g.shift(RIGHT*4+DOWN*2.5)

        e_line = Line(ket_e.get_center(), (ket_e.get_center()+RIGHT*2))
        e_line.shift(RIGHT*0.4)
        excited_state = VGroup(ket_e, e_line)

        g_line = Line(ket_g.get_center(), (ket_g.get_center()+RIGHT*2))
        g_line.shift(RIGHT*0.4)
        ground_state = VGroup(ket_g, g_line)

        energy = Arrow(start=(ket_g.get_center()-[0,1,0]), end=(ket_e.get_center()+[0,1,0])).shift(RIGHT*2.6)
        energy_label = MathTex(r"E").move_to((ket_g.get_center()-[0,1,0])).shift(RIGHT*2.25+UP*0.25)

        

        self.wait()
        self.play(FadeIn(energy), FadeIn(energy_label))
        self.play(elec_0.animate.shift(UP*1.5))
        self.wait()
        self.play(elec_0.animate.shift(DOWN*1.5))
        self.wait()


        self.play(FadeIn(excited_state), FadeIn(ground_state))
        self.remove(elec_0)
        self.add(elec_0)
        self.wait()
        elec_0.shift(UP*2.5)
        self.wait()
        elec_0.shift(DOWN*5)
        self.wait()
        self.play(elec_0.animate.shift(UP*2.5))
        self.wait()

        p_1_val = ValueTracker(0.5)
        prob_1 = always_redraw(lambda: MathTex(r"p", r"_1", r"=", round(p_1_val.get_value(), 2)).move_to(ket_g.get_center()).shift(DOWN*0.8+RIGHT*0.8))

        p_2_val = ValueTracker(0.5)
        prob_2 = always_redraw(lambda: MathTex(r"p", r"_2", r"=", round(p_2_val.get_value(), 2)).move_to(ket_e.get_center()).shift(UP*0.8+RIGHT*0.8))

        self.play(FadeIn(prob_1), FadeIn(prob_2))
        self.wait()
        elec_0.shift(UP*2.5)
        p_1_val.set_value(0)
        p_2_val.set_value(1)
        self.wait()
        self.play(p_1_val.animate.set_value(0.5), p_2_val.animate.set_value(0.5), elec_0.animate.shift(DOWN*2.5))
        self.wait()

        q_state_def = MathTex(r"|q_0\rangle=", r"p", r"_1", r"|", r"g\rangle", r"+", r"p", r"_2", r"|", r"e\rangle")
        self.play(FadeIn(q_state_def[0]))
        self.wait()


        ket_g_copy = ket_g.copy()
        self.play(
            Transform(ket_g_copy[0], q_state_def[3], path_arc=-90 * DEGREES),
            Transform(ket_g_copy[1:len(ket_g_copy)], q_state_def[4], path_arc=-90 * DEGREES)
        )
        self.wait()
        ket_e_copy = ket_e.copy()
        self.play(
            Transform(ket_e_copy[0], q_state_def[-2], path_arc=90 * DEGREES),
            Transform(ket_e_copy[1:len(ket_g)], q_state_def[-1], path_arc=90 * DEGREES)
        )
        self.play(FadeIn(q_state_def[5]))
        self.wait()
        prob_1_copy = prob_1.copy()
        self.play(
            ReplacementTransform(prob_1_copy[0], q_state_def[1], path_arc=-90 * DEGREES), 
            ReplacementTransform(prob_1_copy[1], q_state_def[2], path_arc=-90 * DEGREES)
        )
        prob_2_copy = prob_2.copy()
        self.play(
            ReplacementTransform(prob_2_copy[0], q_state_def[6], path_arc=90 * DEGREES), 
            ReplacementTransform(prob_2_copy[1], q_state_def[7], path_arc=90 * DEGREES)
        )
        self.wait()
        #self.play(Write(q_state_def[2]), Write(q_state_def[8])) YOU MAY WANT TO REVEAL THE SQRT AT THIS POINT
        self.wait()

        q_state_def_01 = MathTex(r"|q_0\rangle=", r"p", r"_1", r"|", r"0", r"\rangle", r"+", r"p", r"_2", r"|", r"1", r"\rangle")
        ket_0 = MathTex(r"|", r"0", r"\rangle").move_to(ket_g.get_center())
        ket_1 = MathTex(r"|", r"1", r"\rangle").move_to(ket_e.get_center())

        self.play(
            Transform(ket_g_copy[1], q_state_def_01[4]),
            Transform(ket_e_copy[1], q_state_def_01[-2]),
            Transform(ket_g[1], ket_0[1]),
            Transform(ket_e[1], ket_1[1])
        )
        self.wait()
        q_0_eq = VGroup(q_state_def[0:4], q_state_def[5:-1], q_state_def_01[4], q_state_def_01[10], ket_e_copy, ket_g_copy, prob_1_copy[0:2], prob_2_copy[0:2])
        q_0_eq_copy = q_0_eq.copy()
        q_0_eq.generate_target()
        q_vec = Matrix([[r"p_1"],[r"p_2"]])
        q_def_vec = VGroup(q_0_eq_copy, MathTex("="), q_vec).arrange(RIGHT, buff=.25).shift(LEFT*0.5)
        q_0_eq.target.move_to(q_0_eq_copy)
        self.play(MoveToTarget(q_0_eq))

        self.play(
            Write(q_def_vec[1]),
            Write(q_vec.get_brackets())
        )
        self.wait()

        self.play(
            TransformMatchingShapes(q_state_def[1:3].copy(), q_vec[0][0]),
            TransformMatchingShapes(q_state_def[6:8].copy(), q_vec[0][1])
        )
        # AT THIS POINT ADD THE REVEAL FOR THE SQRT
        # self.play(
        #     FadeOut(q_0_eq),
        #     FadeOut(q_def_vec[1])
        # )
        
        q_vec.generate_target()
        q_vec.target.move_to(ORIGIN)
        equals_sign = q_def_vec[1]
        equals_sign.generate_target()
        equals_sign.target.align_to(q_vec.target, LEFT)
        equals_sign.target.shift(LEFT*equals_sign.width+LEFT*0.25)
        q_0_eq.target.align_to(equals_sign.target, LEFT)
        q_0_eq.target.shift(LEFT*q_0_eq.width+LEFT*0.25)

        self.play(MoveToTarget(q_vec), MoveToTarget(q_0_eq), MoveToTarget(equals_sign))

        vec_ket_0 = MathTex(r"|", r"0", r"\rangle")
        vec_ket_1 = MathTex(r"|", r"1", r"\rangle")
        vec_ket_0.move_to(q_vec[0][0].get_center()).shift(RIGHT*1.25)
        vec_ket_1.move_to(q_vec[0][1].get_center()).shift(RIGHT*1.25)

        self.play(FadeIn(vec_ket_0))
        self.play(FadeIn(vec_ket_1))

        vec_sys = VGroup(vec_ket_0, vec_ket_1, q_vec, equals_sign, q_0_eq)
        self.play(FadeOut(vec_sys))

        sys_0 = VGroup(ket_0, ket_1, e_line, g_line)
        sys_1 = sys_0.copy().shift(LEFT*3.5)
        #always_rotate(elec_1, about_point=elec_1.get_center(), axis=[0,1,0], rate=50*DEGREES)
        self.remove(elec_1)
        self.add(elec_1)
        sys_0_label = MathTex(r"|", r"q_0", r"\rangle").move_to(ket_1.get_center()).shift(UP+RIGHT)
        sys_1_label = MathTex(r"|", r"q_1", r"\rangle").move_to(sys_1[1].get_center()).shift(UP+RIGHT)
        self.play(FadeIn(elec_1), FadeIn(sys_1), FadeOut(prob_1), FadeOut(prob_2))
        self.wait()
        self.play(FadeIn(sys_0_label))
        self.play(FadeIn(sys_1_label))
        
        # two_q_states = MathTex(r"|", r"q_1", r"q_0", r"\rangle", r"=", r"p_1", r"|00\rangle", r"+", r"p_2", r"|01\rangle", r"+", r"p_3", r"|10\rangle", r"+",r"p_2", r"|11\rangle")
        # two_q_states.scale(0.75).to_edge(LEFT).shift(UP)
        # self.play(FadeIn(two_q_states[0:5]))
        # self.wait()


        two_q_name = MathTex(r"|", r"q_1", r"q_0", r"\rangle")
        four_state_vector = Matrix([[r"p_1"],[r"p_2"], [r"p_3"], [r"p_4"]]).to_edge(LEFT).shift(RIGHT)
        four_state_vector.set_color(GREY_A)
        ket_00 = MathTex(r"|00\rangle").move_to(four_state_vector[0][0].get_center()).shift(RIGHT*1.25)
        ket_01 = MathTex(r"|01\rangle").move_to(four_state_vector[0][1].get_center()).shift(RIGHT*1.25)
        ket_10 = MathTex(r"|10\rangle").move_to(four_state_vector[0][2].get_center()).shift(RIGHT*1.25)
        ket_11 = MathTex(r"|11\rangle").move_to(four_state_vector[0][3].get_center()).shift(RIGHT*1.25)
        two_q_name.move_to(four_state_vector.get_center()).align_to(four_state_vector, UP).shift(UP*(two_q_name.height + 0.35)+RIGHT*0.5)

        self.play(FadeIn(two_q_name))

        elec_0.shift(DOWN*2.5)
        elec_1.shift(DOWN*2.5)
        self.play(FadeIn(ket_00))
        self.wait()
        elec_0.shift(UP*5)
        self.play(FadeIn(ket_01))
        elec_0.shift(DOWN*5)
        elec_1.shift(UP*5)
        self.play(FadeIn(ket_10))
        elec_0.shift(UP*5)
        self.play(FadeIn(ket_11))
        self.play(Write(four_state_vector.get_brackets()))
        self.play(Write(four_state_vector[0]))

        three_q_name = MathTex(r"|", r"q_2", r"q_1", r"q_0", r"\rangle").scale(0.8)
        eight_state_vector = Matrix([[r"p_1"],[r"p_2"], [r"p_3"], [r"p_4"], [r"p_5"],[r"p_6"], [r"p_7"], [r"p_8"]]).scale(0.8).shift(LEFT*0.65)
        ket_000 = MathTex(r"|000\rangle").move_to(eight_state_vector[0][0].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_001 = MathTex(r"|001\rangle").move_to(eight_state_vector[0][1].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_010 = MathTex(r"|010\rangle").move_to(eight_state_vector[0][2].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_011 = MathTex(r"|011\rangle").move_to(eight_state_vector[0][3].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_100 = MathTex(r"|100\rangle").move_to(eight_state_vector[0][4].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_101 = MathTex(r"|101\rangle").move_to(eight_state_vector[0][5].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_110 = MathTex(r"|110\rangle").move_to(eight_state_vector[0][6].get_center()).shift(RIGHT*1.25).scale(0.8)
        ket_111 = MathTex(r"|111\rangle").move_to(eight_state_vector[0][7].get_center()).shift(RIGHT*1.25).scale(0.8)
        eight_state_kets = VGroup(ket_000, ket_001, ket_010, ket_011, ket_100, ket_101, ket_110, ket_111)

        three_q_name.move_to(eight_state_vector.get_center()).align_to(eight_state_vector, UP).shift(UP*(three_q_name.height + 0.3)+RIGHT*0.3)

        self.play(
            FadeOut(elec_0), 
            FadeOut(elec_1), 
            FadeOut(sys_0), 
            FadeOut(sys_1), 
            FadeOut(ket_e), 
            FadeOut(ket_g), 
            FadeOut(energy), 
            FadeOut(energy_label),
            FadeOut(sys_0_label),
            FadeOut(sys_1_label)
        )


        self.play(FadeIn(three_q_name))
        self.play(Write(eight_state_vector), Write(eight_state_kets))

        two_to_n = MathTex(r"2^n")
        d_relation = VGroup(MathTex(r"d="), two_to_n).arrange(RIGHT, buff=0.25)
        d_relation[0].set_color(BLUE_B)
        d_relation.shift(RIGHT*3.5+UP*0.25)
        

        self.play(Write(d_relation))
        

















class sphere_test(ThreeDScene):
    def construct(self):
        entry_00 = MathTex("0")
        matrix = Matrix([["0"], ["1"]])
        self.add(matrix)
        # arrow = Arrow(ORIGIN, RIGHT*6)
        # self.add(arrow)
        # sphere = Surface(
        #     lambda u, v: np.array([
        #         0.25 * np.cos(u) * np.cos(v),
        #         0.25* np.cos(u) * np.sin(v),
        #         0.25 * np.sin(u)
        #     ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
        #     checkerboard_colors=[YELLOW_D, YELLOW_E], resolution=(15, 32)
        # )
        # #self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        # #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # sphere.rotate(angle= DEGREES*122, axis=[1,0,0])
        # sphere.shift(RIGHT*5+IN)
        # self.add(sphere)
        # self.bring_to_front(arrow)

        # #always_rotate(sphere, about_point=sphere.get_center(), axis=[0,1,0], rate=90*DEGREES)
        # #self.wait()
        
        # axes = ThreeDAxes(
        #     x_range=[-1,1,1],
        #     x_length=2,
        #     y_range=[-1,1,1],
        #     y_length=2,
        #     z_range=[-1,1,1],
        #     z_length=1.5,
        #     tips=False
        # )
        # vector = Vector([np.sqrt(0.5), np.sqrt(0.5), 0])
        # ket_q0 = MathTex(r"|q_0\rangle").next_to(vector.get_end(), RIGHT).scale(0.75).shift(LEFT*0.25)
        # b1 = Brace(vector).shift(UP*0.25)
        # b1text = b1.get_tex(r"p_1").scale(0.75).shift(UP*0.25)
        # b2 = Brace(vector, direction=LEFT).shift(RIGHT*0.25)
        # b2text = b2.get_tex(r"p_2").scale(0.75).shift(RIGHT*0.25)
        # one_label = MathTex(r"1").shift(UP*0.5+RIGHT*0.3).scale(0.65)
        # vec_visual_sys = VGroup(axes, vector, ket_q0, b1, b1text, b2, b2text, one_label).scale(1.25)

        # vec_visual_sys.to_corner(UL).shift(RIGHT*0.55+DOWN*0.25)

        # self.add(vec_visual_sys)

        # self.play(vec_visual_sys.animate.rotate(axis=[1,0,0], angle=-65*DEGREES, about_point=axes.coords_to_point(0,0,0)))
        # self.wait()
        # self.play(vec_visual_sys.animate.rotate(axis=[1,0,0], angle=65*DEGREES, about_point=axes.coords_to_point(0,0,0)))


        # self.move_camera(phi=65 * DEGREES, theta=-105 * DEGREES)
        # self.wait()
        # self.move_camera(0, theta=-90 * DEGREES)





class sphere_test_fast(ThreeDScene):
    def construct(self):
        elec_0 = Surface(
            lambda u, v: np.array([
                0.25 * np.cos(u) * np.cos(v),
                0.25* np.cos(u) * np.sin(v),
                0.25 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[PURPLE_D, PURPLE_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        elec_0.rotate(angle= DEGREES*122, axis=[1,0,0])
        elec_0.shift(RIGHT*5.25)
        

        



        ket_e = MathTex(r"|", r"e", r"\rangle")
        ket_g = MathTex(r"|",r"g", r"\rangle")

        ket_e.shift(RIGHT*4+UP*2.5)
        ket_g.shift(RIGHT*4+DOWN*2.5)

        e_line = Line(ket_e.get_center(), (ket_e.get_center()+RIGHT*2))
        e_line.shift(RIGHT*0.4)
        excited_state = VGroup(ket_e, e_line)

        g_line = Line(ket_g.get_center(), (ket_g.get_center()+RIGHT*2))
        g_line.shift(RIGHT*0.4)
        ground_state = VGroup(ket_g, g_line)


        energy = Arrow(start=(ket_g.get_center()-[0,1,0]), end=(ket_e.get_center()+[0,1,0])).shift(RIGHT*2.6)
        energy_label = MathTex(r"E").move_to((ket_g.get_center()-[0,1,0])).shift(RIGHT*2.25+UP*0.25)



        always_rotate(elec_0, about_point=elec_0.get_center(), axis=[0,1,0], rate=50*DEGREES)
        self.add(elec_0)
        self.wait()
        self.play(FadeIn(energy), FadeIn(energy_label))
        self.play(elec_0.animate.shift(UP*1.5))
        self.wait()
        self.play(elec_0.animate.shift(DOWN*1.5))

        self.wait()
        self.play(FadeIn(ground_state), FadeIn(excited_state))
        self.remove(elec_0)
        self.add(elec_0)
        self.wait()
        #self.play(FadeOut(energy), FadeOut(energy_label))
        elec_0.shift(UP*2.5)
        self.wait()
