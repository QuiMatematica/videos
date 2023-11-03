from manim import *

from qui_matematica.piano_cartesiano.parabola import ParabolaDaFuocoEDirettrice
from qui_matematica.piano_cartesiano.punto import Punto, POINT_DISTANCE_RATIO
from qui_matematica.piano_cartesiano.retta import RettaParallelaAsseX, LINE_DISTANCE_RATIO

DELAY = 30


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        colore_fuoco_direttrice = GREEN
        colore_parabola = YELLOW

        xF = 4
        yF = 0
        yd = -1.5
        ya_max = 3.5

        fuoco = Punto(xF, yF, nome="F", color=colore_fuoco_direttrice)
        label_fuoco = MathTex("F", color=fuoco.get_color()).next_to(fuoco, POINT_DISTANCE_RATIO * UR)
        direttrice = RettaParallelaAsseX(yd, nome="d", color=colore_fuoco_direttrice, x_range=[1, 7])
        label_direttrice = MathTex("d", color=direttrice.get_color()).next_to(direttrice.get_start(), LINE_DISTANCE_RATIO * DR)
        parabola = ParabolaDaFuocoEDirettrice(fuoco, direttrice, color=colore_parabola, x_range=[1, 7])

        asse = DashedLine(start=[xF, ya_max, 0], end=[xF, -ya_max, 0], color=colore_parabola)
        label_asse = MathTex("a", color=colore_parabola).next_to(asse.get_start(), LINE_DISTANCE_RATIO * DL)

        vertice = Dot([xF, (yF + yd) / 2, 0], color=colore_parabola)
        label_vertice = MathTex("V", color=vertice.get_color()).next_to(vertice, POINT_DISTANCE_RATIO * DR)

        self.play(Create(fuoco), Write(label_fuoco))
        self.play(Create(direttrice), Write(label_direttrice))
        self.play(Create(parabola))
        self.cut_and_wait()

        x_min = -3
        x_max = 10 + x_min
        y_min = -2
        y_max = 12 + y_min

        scale_factor = .6

        x_length = (x_max - x_min) * scale_factor
        y_length = (y_max - y_min) * scale_factor

        riferimento = Axes(x_range=[x_min, x_max, 100],
                           y_range=[y_min, y_max, 100],
                           x_length=x_length,
                           y_length=y_length).set_color(BLUE).shift(4 * LEFT)
        x_label = riferimento.get_x_axis_label(Tex("$x$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        y_label = riferimento.get_y_axis_label(Tex("$y$", color=BLUE).scale(0.7), direction=DL, buff=.4)
        self.play(Create(riferimento))
        self.add(x_label, y_label)
        self.cut_and_wait()

        self.play(Create(asse), Write(label_asse))
        self.cut_and_wait()

        self.play(Create(vertice), Write(label_vertice))
        self.cut_and_wait()

        # Per non complicarci troppo le cose fin da subito, consideriamo una parabola con asse parallelo all'asse delle
        # ordinate.
        label_asse.add_updater(
            lambda old: old.next_to(asse.get_start(), LINE_DISTANCE_RATIO * DL)
        )

        self.play(asse.animate.shift(8*LEFT))
        label_asse.clear_updaters()
        self.cut_and_wait()

        # Decidiamo inoltre dove collocare il vertice della parabola.

        label_vertice.add_updater(
            lambda old: old.next_to(vertice, POINT_DISTANCE_RATIO * DR)
        )

        self.play(vertice.animate.shift(8*LEFT))
        label_vertice.clear_updaters()
        self.cut_and_wait()

        # Per stare generici chiameremo xV e yV le suo coordinate.

        coordinate_vertice = MathTex(r"(x_V, y_V)", color=YELLOW).next_to(label_vertice, RIGHT, buff=.1)
        self.play(Write(coordinate_vertice))
        self.cut_and_wait()

        # Ora decidiamo dove collocare il fuoco della parabola.
        # Deve essere lungo l'asse, perché l'asse passa per il fuoco.

        label_fuoco.add_updater(
            lambda old: old.next_to(fuoco, POINT_DISTANCE_RATIO * UR)
        )

        self.play(fuoco.animate.shift(8*LEFT))
        label_fuoco.clear_updaters()
        self.cut_and_wait()

        # Ma possiamo scegliere la distanza tra il fuoco e il vertice. Chiamiamo f questa distanza.

        brace_fuoco = CurvedArrow(vertice.get_center(), fuoco.get_center(), color=RED).shift(.1*RIGHT)
        self.play(Create(brace_fuoco))

        f_fuoco = MathTex(r"f", color=RED).next_to(brace_fuoco, RIGHT, buff=.1)
        self.play(Write(f_fuoco))
        self.cut_and_wait()

        # Anzi, per la precisione: f è positivo se il fuoco si trova sopra il vertice, mentre f è negativo se si trova
        # sotto il vertice. Quindi f è la quantità da aggiungere all'ordinata del vertice per trovare l'ordinata del
        # fuoco.
        # Le coordinate del fuoco, quindi, sono x_V e y_V + f.

        coordinate_fuoco = MathTex(r"(x_V, y_V + f)", color=GREEN).next_to(label_fuoco, RIGHT, buff=.1)
        self.play(Create(BackgroundRectangle(coordinate_fuoco)), Write(coordinate_fuoco))
        self.cut_and_wait()

        # Fissato il fuoco, rimane fissata anche la direttrice.

        label_direttrice.add_updater(
            lambda old: old.next_to(direttrice.get_start(), LINE_DISTANCE_RATIO * DR)
        )

        self.play(direttrice.animate.shift(8 * LEFT))
        label_direttrice.clear_updaters()
        self.cut_and_wait()

        # Infatti il vertice appartiene alla parabola, quindi si
        # trova alla stessa distanza da fuoco e dalla direttrice. Quindi se f è la distanza del fuoco dal vertice, f è
        # anche la distanza della direttrice dal vertice, ma in direzione opposta.

        brace_direttrice = CurvedArrow(vertice.get_center(), [asse.get_start()[0], direttrice.get_start()[1], 0], color=RED).shift(.1*LEFT)
        self.play(Create(brace_direttrice))

        f_direttrice = MathTex(r"-f", color=RED).next_to(brace_direttrice, LEFT, buff=.1)
        self.play(Write(f_direttrice))
        self.cut_and_wait()

        # Quindi l'equazione della direttrice è y = yV - f.

        equazione_direttrice = MathTex(r": y = y_V - f", color=GREEN).next_to(label_direttrice, RIGHT, buff=.1).shift(.05 * DOWN)
        self.play(Create(BackgroundRectangle(equazione_direttrice)), Write(equazione_direttrice))

        # Fissato fuoco e direttrice, siamo in grado di disegnare la parabola sul piano cartesiano.

        self.play(FadeOut(brace_direttrice), FadeOut(brace_fuoco), FadeOut(f_fuoco), FadeOut(f_direttrice),
                  FadeOut(vertice), FadeOut(label_vertice), FadeOut(coordinate_vertice))
        self.play(parabola.animate.shift(8 * LEFT))
        self.cut_and_wait()

        # Per trovare l'equazione prendiamo un generico punto P di generiche coordinate x e y.

        punto_p = Dot(6 * LEFT + 2 * UP)
        label_punto_p = MathTex("P(x, y)", color=punto_p.get_color()).add_background_rectangle().next_to(punto_p, POINT_DISTANCE_RATIO * UR)
        self.play(Create(punto_p))
        self.play(Write(label_punto_p))
        self.cut_and_wait()

        distanza_pf = DashedLine(start=punto_p, end=fuoco, color=WHITE)
        self.play(Create(distanza_pf))
        distanza_pd = DashedLine(start=punto_p, end=[punto_p.get_center()[0], direttrice.get_start()[1], 0], color=WHITE)
        self.play(Create(distanza_pd))
        self.cut_and_wait()

        # Imponiamo che tale punto appartenga alla parabola, ovvero che la distanza di P dal fuoco e la distanza di P
        # dalla direttrice siano uguali.

        circonferenza = DashedVMobject(Circle(radius=punto_p.get_center()[1] - direttrice.get_start()[1], color=WHITE), num_dashes=100).move_to(punto_p.get_center())
        self.play(Create(circonferenza))

        label_punto_p.add_updater(
            lambda old: old.next_to(punto_p, POINT_DISTANCE_RATIO * UR)
        )
        distanza_pf.add_updater(
            lambda old: old.become(DashedLine(start=punto_p, end=fuoco, color=WHITE))
        )
        distanza_pd.add_updater(
            lambda old: old.become(DashedLine(start=punto_p, end=[punto_p.get_center()[0], direttrice.get_start()[1], 0], color=WHITE))
        )
        circonferenza.add_updater(
            lambda old: old.become(DashedVMobject(Circle(radius=punto_p.get_center()[1] - direttrice.get_start()[1], color=WHITE), num_dashes=100).move_to(punto_p.get_center()))
        )

        destinazione = [punto_p.get_center()[0], parabola.get_ordinata_parabola(punto_p.get_center()[0] + 8), 0]
        self.play(punto_p.animate.move_to(destinazione))
        label_punto_p.clear_updaters()
        distanza_pf.clear_updaters()
        distanza_pd.clear_updaters()
        circonferenza.clear_updaters()
        self.cut_and_wait()

        # Per semplificarci i calcoli consideriamo il punto H che è piede della distanza del punto P dalla direttrice.
        # Tale punto H ha coordinate x (l'ascissa di P) e y_V - f (l'ordinata della direttrice).

        punto_h = Dot([punto_p.get_center()[0], direttrice.get_start()[1], 0], color=WHITE)
        label_punto_h = MathTex("H(x, y_V - f)", color=punto_h.get_color()).add_background_rectangle().next_to(punto_h, POINT_DISTANCE_RATIO * UR)
        self.play(FadeOut(circonferenza))
        self.play(Create(punto_h))
        self.play(Write(label_punto_h))
        self.cut_and_wait()

        # Otterremo l'equazione del luogo geometrico imponendo che la lunghezza del segmento PF sia uguale alla
        # lunghezza del segmento PH.

        scale=.7

        eqs = VGroup()

        eq = MathTex(r"\overline{PF} = \overline{PH}").scale(scale).move_to(3.1 * RIGHT + 3 * UP)
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # Il punto P e il punto F hanno sia ascissa sia ordinata diversi, quindi per calcolare la lunghezza di PF devo
        # utilizzare la formula generale, quella con la radice quadrata.
        # Invece il punto P e il punto H hanno la stessa ascissa, quindi mi basta fare la differenza delle ordinate in
        # valore assoluto.

        neq = MathTex(r"\sqrt{(x_P-x_F)^2 + (y_P-y_F)^2} = {{ \left|y_P - y_H \right| }}").scale(scale).next_to(eq, DOWN, buff=.4)
        eq = neq
        self.play(Write(eq[0]))
        eqs.add(eq)
        self.cut_and_wait()
        self.play(Write(eq[1]))
        self.cut_and_wait()

        # Sostituiamo i valori. Le coordinate del punto P sono le generiche x e y, che saranno le incognite
        # dell'equazione. Le coordinate del fuoco sono xV e yV + f. L'ordinata di H è yV - f.

        color = RED

        neq = MathTex(r"\sqrt{(x-x_V)^2 + (y-y_V - f)^2} = \left|y - y_V + f \right|").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][3].set_color(color)
        neq[0][11].set_color(color)
        neq[0][21].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # Ora, per togliere la radice quadrata e il valore assoluto ci basta elevare i due membri dell'equazione al
        # quadrato. Non abbiamo problemi di concordanza del segno o di condizioni di esistenza perché tutte le quantità
        # coinvolte sono positive.

        neq = MathTex(r"(x-x_V)^2 + (y-y_V - f)^2 = (y - y_V + f)^2").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][1].set_color(color)
        neq[0][9].set_color(color)
        neq[0][19].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # Svolgiamo i quadrati.

        neq = MathTex(r"x^2 - 2 x_Vx + x_V^2 + y^2 + y_V^2 + f^2 -2y_Vy - 2fy + \\"
                      r"+ 2fy_V = y^2 + f^2 + y_V^2 + 2fy - 2y_Vy - 2fy_V").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][0].set_color(color)
        neq[0][6].set_color(color)
        neq[0][12].set_color(color)
        neq[0][25].set_color(color)
        neq[0][29].set_color(color)
        neq[0][37].set_color(color)
        neq[0][49].set_color(color)
        neq[0][54].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # E cancelliamo i monomi uguali.

        neq = MathTex(r"x^2 - 2 x_Vx + x_V^2 - 2fy + 2fy_V = 2fy - 2fy_V").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][0].set_color(color)
        neq[0][6].set_color(color)
        neq[0][14].set_color(color)
        neq[0][23].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # Adesso portiamo al primo membro tutti i monomi con la x e i termini noti, mentre portiamo al secondo membro i
        # monomi con la y.

        self.play(eqs.animate.shift(4*UP))
        neq = MathTex(r"x^2 - 2 x_Vx + x_V^2 + 4fy_V = 4fy").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][0].set_color(color)
        neq[0][6].set_color(color)
        neq[0][19].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs = VGroup(eqs, eq)
        self.cut_and_wait()

        # Invertiamo i due membri, visto che l'uguaglianza gode della proprietà simmetrica.

        neq = MathTex(r"4fy = x^2 - 2 x_Vx + x_V^2 + 4fy_V").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][2].set_color(color)
        neq[0][4].set_color(color)
        neq[0][10].set_color(color)
        eq = neq
        self.play(Write(eq))
        eqs.add(eq)
        self.cut_and_wait()

        # E infine isoliamo la y dividendo i membri per 4f.

        neq = MathTex(r"y = \dfrac{1}{4f} x^2 - \dfrac{2 x_V}{4f}x + \dfrac{x_V^2 + 4fy_V}{4f}").scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][0].set_color(color)
        neq[0][6].set_color(color)
        neq[0][15].set_color(color)
        eq = neq
        self.play(Write(eq))
        self.cut_and_wait()

        # Analizziamo ora cosa abbiamo ottenuto. Stavamo cercando l'equazione che rappresenta una generica parabola sul
        # piano cartesiano. L'unico vincolo che abbiamo posto è che abbia asse parallelo all'asse delle ordinate.
        # Abbiamo ottenuto un'equazione in cui c'è un unico monomio in y di primo grado, un monomio in x di secondo
        # grado, un monomio in x di primo grado e un termine noto.
        # Questo significa che partendo con dei certi valori per le coordinate del vertice e una certa distanza del
        # fuoco dal vertice, siamo in grado di trovare l'equazione della parabola che sarà un'equazione di primo grado
        # in y e di secondo grado in x, quindi del tipo y = ax^2 + bx + c.

        self.play(FadeOut(eqs))
        neq = MathTex(r"y = a x^2 + bx + c", z_index=10).scale(scale).next_to(eq, DOWN, buff=.4)
        neq[0][0].set_color(color)
        neq[0][3].set_color(color)
        neq[0][7].set_color(color)
        coppia = VGroup(eq.copy(), neq).move_to([eq.get_center()[0], 0, 0])
        self.play(eq.animate.move_to(coppia[0]))
        self.play(Write(neq))
        self.cut_and_wait()

        dest = neq.copy().scale(4).move_to(ORIGIN)
        self.play(
            Create(BackgroundRectangle(dest, fill_opacity=.95, buff=.5)),
            neq.animate.scale(4).move_to(ORIGIN),
            Create(SurroundingRectangle(dest, buff=.5)))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
