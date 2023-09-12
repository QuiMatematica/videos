from manim import *

from qui_matematica.qmath import EqSystem

DATO_1_LABEL = 'BC=AC+7'
DATO_2_LABEL = 'AB=AC+BC-14'
DATO_3_LABEL = 'Pitagora'


def get_up_arrow(start, end, start_shift=ORIGIN, end_shift=ORIGIN):
    return Arrow(start=start.get_top() + .1 * UP + start_shift,
                 end=end.get_bottom() + .1 * DOWN + end_shift,
                 buff=0,
                 max_stroke_width_to_length_ratio=1,
                 max_tip_length_to_length_ratio=1)


def get_down_arrow(start, end, start_shift=ORIGIN, end_shift=ORIGIN):
    return Arrow(start=start.get_bottom() + .1 * DOWN + start_shift,
                 end=end.get_top() + .1 * UP + end_shift,
                 buff=0,
                 max_stroke_width_to_length_ratio=1,
                 max_tip_length_to_length_ratio=1)


def mid_math_tex(text):
    return MathTex(text).scale(.5)


class Definizioni(VGroup):

    def __init__(self):
        self.definizione_x = mid_math_tex(r"\overline{AC} = x")
        self.definizione_y = mid_math_tex(r"\overline{BC} = y")
        self.definizione_z = mid_math_tex(r"\overline{AB} = z")
        self.condizione_x = mid_math_tex(r"x > 0")
        self.condizione_y = mid_math_tex(r"y > 0")
        self.condizione_z = mid_math_tex(r"z > 0")
        super().__init__(self.definizione_x, self.condizione_x,
                         self.definizione_y, self.condizione_y,
                         self.definizione_z, self.condizione_z)
        self.arrange_in_grid(3, 2)


class Risoluzione(VGroup):

    def __init__(self):
        super().__init__()
        self.definizioni = Definizioni()
        self.add(self.definizioni)

        self.sistema_1 = EqSystem(
            MathTex(r"y=x+7"),
            MathTex(r"z=x+y-14"),
            MathTex(r"z^2=x^2+y^2")
        ).scale(.5)
        self.add(self.sistema_1)

        self.sistema_2 = EqSystem(
            MathTex(r"y=x+7"),
            MathTex(r"z=x+(x+7)-14"),
            MathTex(r"z^2=x^2+(x+7)^2")
        ).scale(.5)
        self.add(self.sistema_2)

        self.sistema_3 = EqSystem(
            MathTex(r"y=x+7"),
            MathTex(r"z=2x-7"),
            MathTex(r"z^2=x^2+(x+7)^2")
        ).scale(.5)
        self.add(self.sistema_3)

        self.sistema_4 = EqSystem(
            MathTex(r"y=x+7"),
            MathTex(r"z=2x-7"),
            MathTex(r"(2x-7)^2=x^2+(x+7)^2")
        ).scale(.5)
        self.add(self.sistema_4)

        self.equazione_1 = mid_math_tex(r"4x^2-28x+49=x^2+x^2+14x+49")
        self.add(self.equazione_1)

        self.equazione_2 = mid_math_tex(r"4x^2-28x=2x^2+14x")
        self.add(self.equazione_2)

        self.equazione_3 = mid_math_tex(r"4x^2-2x^2-28x-14x=0")
        self.add(self.equazione_3)

        self.equazione_4 = mid_math_tex(r"2x^2-42x=0")
        self.add(self.equazione_4)

        self.equazione_5 = mid_math_tex(r"x^2-21x=0")
        self.add(self.equazione_5)

        self.equazione_6 = mid_math_tex(r"x(x-21)=0")
        self.add(self.equazione_6)

        self.equazione_7 = mid_math_tex(r"x = 0 \quad\lor\quad x=21")
        self.add(self.equazione_7)

        self.sistema_5 = EqSystem(
            MathTex(r"x=21"),
            MathTex(r"y=x+7"),
            MathTex(r"z=2x-7")
        ).scale(.5)
        self.add(self.sistema_5)

        self.sistema_6 = EqSystem(
            MathTex(r"x=21"),
            MathTex(r"y=28"),
            MathTex(r"z=35")
        ).scale(.5)
        self.add(self.sistema_6)

        self.formula_1 = mid_math_tex(r"\overline{AC} = x = 21")
        self.formula_2 = mid_math_tex(r"\overline{BC} = y = 28")
        self.formula_3 = mid_math_tex(r"\overline{AB} = z = 35")
        self.add(self.formula_1)
        self.add(self.formula_2)
        self.add(self.formula_3)

        self.formula_4 = mid_math_tex(r"2P &= \overline{AC} + \overline{BC} + \overline{AB} = \\ &= 21 + 28 + 35 = 84")
        self.add(self.formula_4)

        self.risposta = Tex(r"Il perimetro del triangolo \\ è 84 cm.").scale(.5)
        self.add(self.risposta)

        vert_buff = .3
        colonna1 = VGroup(self.definizioni, self.sistema_1, self.sistema_2)
        colonna1.arrange(DOWN, buff=vert_buff, aligned_edge=LEFT)

        colonna2 = VGroup(self.sistema_3, self.sistema_4, self.equazione_1, self.equazione_2, self.equazione_3)
        colonna2.arrange(DOWN, buff=vert_buff, aligned_edge=LEFT)

        colonna3 = VGroup(self.equazione_4, self.equazione_5, self.equazione_6,self.equazione_7, self.sistema_5, self.sistema_6)
        colonna3.arrange(DOWN, buff=vert_buff, aligned_edge=LEFT)

        colonna4 = VGroup(self.formula_1, self.formula_2, self.formula_3, self.formula_4, self.risposta)
        colonna4.arrange(DOWN, buff=vert_buff, aligned_edge=LEFT)

        VGroup(colonna1, colonna2, colonna3, colonna4).arrange(RIGHT, buff=.8, aligned_edge=UP)

        self.shift(1.5 * DOWN)


def align_left(new_one, old_one):
    new_one.move_to(old_one)
    new_one.shift(old_one.get_left() - old_one.get_center() + new_one.get_center() - new_one.get_left())


def crea_riquadro(obj):
    return SurroundingRectangle(obj, color=YELLOW, fill_opacity=1, fill_color=BLACK, buff=.25, z_index=1)



class Scene(MovingCameraScene):

    def construct(self):
        self.delay = 30

        self.wait(.5)

        # for _i in range(-8, 8):
        #     for _j in range(-5, 5):
        #         self.add(Dot(_i * RIGHT + _j * UP, color=DARK_GRAY))

        # In un triangolo rettangolo, un cateto misura 7 cm in più dell'altro cateto e l'ipotenusa 14 cm in meno della
        # somma dei due cateti. Determina il perimetro del triangolo.

        self.disegno_e_dati_con_cm()

        # Innanzitutto, visto che tutte le misure sono in cm, posso trascurare l'unità e lavorare solo con i numeri.
        # Nel fare questo passaggio devo aggiungere la lineetta sopra i nomi dei lati per indicare la misura.

        self.disegno_e_dati()

        self.scala_disegno_e_dati()

        # Costruisco il grafico del problema.

        self.costruzione_primo_grafico()

        # Come dati ho le due relazioni che legano tra loro i lati del triangolo. La richiesta riguarda il perimetro.

        self.grafico_dati_e_richiesta()

        # Parto dal fondo: quali informazioni mi servono per calcolare il perimetro? Beh, qui non ho molta scelta: mi
        # servono le lunghezze dei lati.

        self.grafico_lati_verso_richiesta()

        # Le misure dei lati sono esattamente gli elementi utilizzati nelle due relazioni.

        self.grafico_lati_verso_dati()

        # Il grafico è chiuso e lo analizzo.
        # Le due relazioni in alto hanno solo frecce entranti e sono frecce rivolte dal basso verso l'alto. Significa
        # che queste due relazioni rappresentano due equazioni che mi permetteranno di risolvere il problema.

        self.grafico_evidenzia_equazioni()

        # Allora devo determinare quali sono le incognite di tali equazioni. Le incognite sono rappresentate dai nodi
        # del grafico che hanno solo frecce uscenti: quindi sono i tre lati.

        self.grafico_evidenzia_incognite()

        # Ma ho un problema. Ho tre incognite, i tre lati, ma solo due equazioni. Per poter risolvere un problema ho
        # bisogno di tante equazioni tante quante sono le incognite. Se ho tre incognite, devo avere tre equazioni.
        # C'è qualcosa che non ho sfruttato?
        # Non ho sfruttato il fatto che il triangolo è rettangolo, e se è un triangolo rettangolo conosco una ben
        # precisa relazione che lega tra loro i lati: il teorema di Pitagora.

        self.grafico_aggiungo_pitagora()

        # Adesso sì che il diagramma è completo: ho tre incognite (i lati) e ho tre equazioni: le due del testo e il
        # teorema di Pitagora.

        self.grafico_evidenzia_incognite_2()

        self.grafico_evidenzia_equazioni_2()

        # Allora parto con la risoluzione. Do un nome alle tre incognite: la lunghezza di AC la chiamo x, la lunghezza
        # di BC la chiamo y e la lunghezza di AB la chiamo z.

        self.scala_grafico()

        self.costruisci_risoluzione()

        self.definizione_variabili()

        # Devo scrivere anche le condizioni di esistenza delle incognite: visto che rappresentano le lunghezze dei
        # lati di un triangolo devono essere positive. Posso evitare di scrivere le altre condizioni sui lati perché
        # sono garantite dal teorema di Pitagora.

        self.condizioni_variabili()

        # La prima relazione del testo diventa y = x + 7, la seconda relazione diventa z = x + y - 14 e il teorema di
        # Pitagora lo scrivo come z^2 = x^2 + y^2.
        # Metto a sistema queste tre equazioni.

        self.trasformazione_equazioni()

        # Noto che le prime due equazioni sono di primo grado, mentre la terza equazione (il teorema di Pitagora) è di
        # secondo grado. Il grado del sistema è dato dal prodotto dei gradi delle equazioni, quindi il sistema è di
        # secondo grado. Mi aspetto quindi due soluzioni: non è detto che siano tutte e due valide.

        # Il modo migliore per risolvere questo sistema è lavorare per sostituzioni successive. La prima equazione mi
        # dice già che y è uguale a x + 7, quindi posso sostituire le y della seconda e della terza equazione con
        # x + 7. Occhio alle parentesi.

        self.sistema_2()

        # Semplifico il secondo membro della seconda equazione. Ottengo che z è uguale a 2x - 7.

        self.sistema_3()

        # Quindi nella terza equazione sostituisco la z con 2x - 7.

        self.sistema_4()

        # Bene, adesso la terza equazione contiene solo l'incognita x. Quindi la porto fuori dal sistema e la risolvo.
        # Svolgo i quadrati di binomio.

        self.equazione_1()

        # Ho il termine 49 sia al primo membro, sia al secondo membro: li posso
        # cancellare. Inoltre al secondo membro posso sommare i due x^2.

        self.play(Write(self.risoluzione.equazione_2))
        self.cut_and_wait()

        # Porto tutto al primo membro ...

        self.play(Write(self.risoluzione.equazione_3))
        self.cut_and_wait()

        # e sommo i
        # monomi simili.

        self.play(Write(self.risoluzione.equazione_4))
        self.cut_and_wait()

        # Interessante. L'equazione di secondo grado ha perso il termine noto: è un'equazione spuria. Tutti i
        # coefficienti sono pari, quindi li posso dividere per 2.

        self.play(Write(self.risoluzione.equazione_5))
        self.cut_and_wait()

        # Raccolgo una x a fattor comune

        self.play(Write(self.risoluzione.equazione_6))
        self.cut_and_wait()

        # e applico la legge
        # dell'annullamento del prodotto. Ottengo x = 0 o x = 21.

        self.play(Write(self.risoluzione.equazione_7))
        self.cut_and_wait()

        # La prima soluzione non è accettabile perché x, che è
        # la lunghezza del lato AC, deve essere maggiore di 0.

        self.play(Indicate(self.risoluzione.definizioni.condizione_x))

        # Quindi ho un'unica soluzione accettabile: x = 21.

        # Ritorno nel sistema e trovo i valori delle altre due incognite.

        self.play(Write(self.risoluzione.sistema_5))
        self.cut_and_wait()

        # La soluzione accettabile per il problema è
        # x = 21, y = 28 e z = 35.

        self.play(Write(self.risoluzione.sistema_6))
        self.cut_and_wait()

        # A questo punto conosco le lunghezze dei lati. E' una terna pitagorica che conosco già: è la terza 3,4,5
        # moltiplicata per 7.

        self.play(Write(self.risoluzione.formula_1))
        self.play(Write(self.risoluzione.formula_2))
        self.play(Write(self.risoluzione.formula_3))
        self.cut_and_wait()

        # Per calcolare il perimetro mi basta sommare le lunghezze dei lati.

        self.play(Write(self.risoluzione.formula_4))
        self.cut_and_wait()

        # E, nella risposta, devo ricordarmi di aggiungere l'unità di misura.
        # Il perimetro del triangolo è 84 cm.

        self.play(Write(self.risoluzione.risposta))
        self.cut_and_wait()

        self.wait(30)

    def cut_and_wait(self):
        if self.delay > 0:
            self.wait(self.delay)
            self.next_section()

    def disegno_e_dati_con_cm(self):
        ac = 21
        bc = 28
        ab = 35

        abc_scale = 3 / ab

        cos_a = ac / ab
        sin_a = bc / ab
        ah = ac * cos_a
        ch = ac * sin_a

        abc = Polygon([0, 0, 0], [ab, 0, 0], [ah, ch, 0]).scale(abc_scale)
        abc_vertices = abc.get_vertices()
        ac_side = Line(abc_vertices[2], abc_vertices[0])
        bc_side = Line(abc_vertices[2], abc_vertices[1])
        c_right_angle = RightAngle(ac_side, bc_side, length=.3, color=BLUE)
        a_label = MathTex("A").next_to(abc_vertices[0], (DOWN + LEFT) * .7)
        b_label = MathTex("B").next_to(abc_vertices[1], (DOWN + RIGHT) * .7)
        c_label = MathTex("C").next_to(abc_vertices[2], UP)

        self.gruppo_triangolo = VGroup(abc, c_right_angle, a_label, b_label, c_label)

        self.dato_1_con_cm = MathTex(r"BC = AC + 7 \text{ cm}")
        self.dato_2_con_cm = MathTex(r"AB = AC + BC - 14 \text{ cm}")
        self.richiesta = MathTex(r"2P = \,\,?")
        gruppo_dati_con_cm = VGroup(self.dato_1_con_cm, self.dato_2_con_cm, self.richiesta). \
            arrange(DOWN, aligned_edge=LEFT)

        gruppo_triangolo_e_dati = VGroup(self.gruppo_triangolo, gruppo_dati_con_cm).arrange(RIGHT, buff=1)

        self.play(Create(abc))
        self.play(Create(c_right_angle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.cut_and_wait()

        self.play(Write(self.dato_1_con_cm))
        self.cut_and_wait()
        self.play(Write(self.dato_2_con_cm))
        self.cut_and_wait()
        self.play(Write(self.richiesta))
        self.cut_and_wait()

    def disegno_e_dati(self):
        self.dato_1 = MathTex(r"\overline{BC} = \overline{AC} + 7")
        self.dato_2 = MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14")
        copia_richiesta = self.richiesta.copy()
        gruppo_dati = VGroup(self.dato_1, self.dato_2, copia_richiesta).arrange(DOWN, aligned_edge=LEFT)

        copia_gruppo_triangolo = self.gruppo_triangolo.copy()

        VGroup(copia_gruppo_triangolo, gruppo_dati).arrange(RIGHT, buff=1)

        self.play(
            ReplacementTransform(self.dato_1_con_cm, self.dato_1),
            ReplacementTransform(self.dato_2_con_cm, self.dato_2),
            self.richiesta.animate.move_to(copia_richiesta),
            self.gruppo_triangolo.animate.move_to(copia_gruppo_triangolo))
        self.cut_and_wait()

        self.gruppo_triangolo_e_dati = VGroup(
            self.gruppo_triangolo,
            VGroup(self.dato_1, self.dato_2, self.richiesta))

    def scala_disegno_e_dati(self):
        self.play(self.gruppo_triangolo_e_dati.animate.scale(.5).move_to(3.5 * LEFT + 2.5 * UP))
        self.cut_and_wait()

    def costruzione_primo_grafico(self):
        self.nodi_grafico = {
            DATO_1_LABEL: MathTex(r"\overline{BC} = \overline{AC} + 7"),
            DATO_2_LABEL: MathTex(r"\overline{AB} = \overline{AC} + \overline{BC} - 14"),
            DATO_3_LABEL: MathTex(r"\overline{AB}^2 = \overline{AC}^2 + \overline{BC}^2"),
            '2P': MathTex(r"2P"),
            'AC': MathTex(r"\overline{AC}"),
            'BC': MathTex(r"\overline{BC}"),
            'AB': MathTex(r"\overline{AB}")
        }

        buff_schema = 1.5
        self.dati_grafico = self.build_row('BC=AC+7', 'AB=AC+BC-14', buff=buff_schema)
        lati_grafico = self.build_row('AC', 'BC', 'AB', buff=buff_schema)
        self.richiesta_grafico = self.build_row('2P')
        self.grafico = VGroup(self.dati_grafico, lati_grafico, self.richiesta_grafico). \
            arrange(DOWN, buff=buff_schema).shift(1.3 * DOWN)

    def build_row(self, *node_names, buff=1.):
        nodes = []
        for name in node_names:
            nodes.append(self.nodi_grafico[name])
        return VGroup(*nodes).arrange(RIGHT, buff=buff)

    def copy_and_move_to_node(self, vmobject, node_name):
        node = self.nodi_grafico[node_name]
        the_copy = vmobject.copy()
        the_copy.target = node.copy()
        self.play(MoveToTarget(the_copy))
        self.remove(the_copy)
        self.add(node)

    def grafico_dati_e_richiesta(self):
        self.riquadro_dati = SurroundingRectangle(self.dati_grafico, color=YELLOW, fill_opacity=.2, buff=.25)
        self.play(Create(self.riquadro_dati))

        self.copy_and_move_to_node(self.dato_1, DATO_1_LABEL)
        self.copy_and_move_to_node(self.dato_2, DATO_2_LABEL)
        self.cut_and_wait()

        riquadro_richiesta = SurroundingRectangle(self.richiesta_grafico, color=RED, fill_opacity=.2, buff=.25)
        self.play(Create(riquadro_richiesta))

        self.copy_and_move_to_node(self.richiesta, '2P')
        self.cut_and_wait()

        self.grafico.add(self.riquadro_dati)
        self.grafico.add(riquadro_richiesta)

    def grafico_lati_verso_richiesta(self):
        ac = self.nodi_grafico['AC']
        bc = self.nodi_grafico['BC']
        ab = self.nodi_grafico['AB']
        richiesta = self.nodi_grafico['2P']

        self.play(Write(ac))
        self.play(Write(bc))
        self.play(Write(ab))
        self.cut_and_wait()

        arrow_to_schema_ac = get_down_arrow(ac, richiesta, end_shift=.4 * LEFT)
        arrow_to_schema_bc = get_down_arrow(bc, richiesta)
        arrow_to_schema_ab = get_down_arrow(ab, richiesta, end_shift=.4 * RIGHT)

        self.grafico.add(arrow_to_schema_ac)
        self.grafico.add(arrow_to_schema_bc)
        self.grafico.add(arrow_to_schema_ab)

        self.play(Create(arrow_to_schema_ac), Create(arrow_to_schema_bc), Create(arrow_to_schema_ab))
        self.cut_and_wait()

    def grafico_lati_verso_dati(self):
        schema_ac = self.nodi_grafico['AC']
        schema_bc = self.nodi_grafico['BC']
        schema_ab = self.nodi_grafico['AB']
        schema_dato_1 = self.nodi_grafico[DATO_1_LABEL]
        schema_dato_2 = self.nodi_grafico[DATO_2_LABEL]

        arrow_ac_to_dato_1 = get_up_arrow(schema_ac, schema_dato_1, start_shift=.2 * LEFT)
        arrow_bc_to_dato_1 = get_up_arrow(schema_bc, schema_dato_1, start_shift=.2 * LEFT, end_shift=RIGHT)
        arrow_ac_to_dato_2 = get_up_arrow(schema_ac, schema_dato_2, start_shift=.2 * RIGHT, end_shift=2 * LEFT)
        arrow_bc_to_dato_2 = get_up_arrow(schema_bc, schema_dato_2, start_shift=.2 * RIGHT, end_shift=LEFT)
        arrow_ab_to_dato_2 = get_up_arrow(schema_ab, schema_dato_2)

        self.nodi_grafico['arrow_ac_to_dato_1'] = arrow_ac_to_dato_1
        self.nodi_grafico['arrow_bc_to_dato_1'] = arrow_bc_to_dato_1
        self.nodi_grafico['arrow_ac_to_dato_2'] = arrow_ac_to_dato_2
        self.nodi_grafico['arrow_bc_to_dato_2'] = arrow_bc_to_dato_2
        self.nodi_grafico['arrow_ab_to_dato_2'] = arrow_ab_to_dato_2

        self.grafico.add(arrow_ac_to_dato_1)
        self.grafico.add(arrow_bc_to_dato_1)
        self.grafico.add(arrow_ac_to_dato_2)
        self.grafico.add(arrow_bc_to_dato_2)
        self.grafico.add(arrow_ab_to_dato_2)

        self.play(Create(arrow_ac_to_dato_1), Create(arrow_bc_to_dato_1))
        self.cut_and_wait()

        self.play(Create(arrow_ac_to_dato_2), Create(arrow_bc_to_dato_2), Create(arrow_ab_to_dato_2))
        self.cut_and_wait()

    def grafico_evidenzia_equazioni(self):
        schema_dato_1 = self.nodi_grafico[DATO_1_LABEL]
        schema_dato_2 = self.nodi_grafico[DATO_2_LABEL]
        arrow_ac_to_dato_1 = self.nodi_grafico['arrow_ac_to_dato_1']
        arrow_bc_to_dato_1 = self.nodi_grafico['arrow_bc_to_dato_1']
        arrow_ac_to_dato_2 = self.nodi_grafico['arrow_ac_to_dato_2']
        arrow_bc_to_dato_2 = self.nodi_grafico['arrow_bc_to_dato_2']
        arrow_ab_to_dato_2 = self.nodi_grafico['arrow_ab_to_dato_2']

        self.play(Circumscribe(schema_dato_1), Circumscribe(schema_dato_2))
        self.play(Indicate(arrow_ac_to_dato_1), Indicate(arrow_bc_to_dato_1),
                  Indicate(arrow_ac_to_dato_2), Indicate(arrow_bc_to_dato_2),
                  Indicate(arrow_ab_to_dato_2))
        self.cut_and_wait()

    def grafico_evidenzia_equazioni_2(self):
        schema_dato_1 = self.nodi_grafico[DATO_1_LABEL]
        schema_dato_2 = self.nodi_grafico[DATO_2_LABEL]
        schema_dato_3 = self.nodi_grafico[DATO_3_LABEL]

        self.play(Circumscribe(schema_dato_1), Circumscribe(schema_dato_2), Circumscribe(schema_dato_3))
        self.cut_and_wait()

    def grafico_evidenzia_incognite(self):
        schema_ac = self.nodi_grafico['AC']
        schema_bc = self.nodi_grafico['BC']
        schema_ab = self.nodi_grafico['AB']
        self.riquadro_ac = SurroundingRectangle(schema_ac, color=BLUE, fill_opacity=.2, buff=.25, corner_radius=.4)
        self.riquadro_bc = SurroundingRectangle(schema_bc, color=BLUE, fill_opacity=.2, buff=.25, corner_radius=.4)
        self.riquadro_ab = SurroundingRectangle(schema_ab, color=BLUE, fill_opacity=.2, buff=.25, corner_radius=.4)
        self.play(Create(self.riquadro_ac), Create(self.riquadro_bc), Create(self.riquadro_ab))
        self.cut_and_wait()
        self.grafico.add(self.riquadro_ab)
        self.grafico.add(self.riquadro_ac)
        self.grafico.add(self.riquadro_bc)

    def grafico_evidenzia_incognite_2(self):
        self.play(Indicate(self.riquadro_ac), Indicate(self.riquadro_bc), Indicate(self.riquadro_ab))

    def grafico_aggiungo_pitagora(self):
        schema_dato_1_bis = self.nodi_grafico[DATO_1_LABEL].copy()
        schema_dato_2_bis = self.nodi_grafico[DATO_2_LABEL].copy()
        schema_dato_3 = self.nodi_grafico[DATO_3_LABEL]
        VGroup(schema_dato_1_bis, schema_dato_3, schema_dato_2_bis).arrange(RIGHT, buff=.7).move_to(self.dati_grafico)

        schema_dato_1 = self.nodi_grafico[DATO_1_LABEL]
        schema_dato_2 = self.nodi_grafico[DATO_2_LABEL]

        schema_ac = self.nodi_grafico['AC']
        schema_bc = self.nodi_grafico['BC']
        schema_ab = self.nodi_grafico['AB']

        arrow_ac_to_dato_1 = self.nodi_grafico['arrow_ac_to_dato_1']
        arrow_bc_to_dato_1 = self.nodi_grafico['arrow_bc_to_dato_1']
        arrow_ac_to_dato_2 = self.nodi_grafico['arrow_ac_to_dato_2']
        arrow_bc_to_dato_2 = self.nodi_grafico['arrow_bc_to_dato_2']
        arrow_ab_to_dato_2 = self.nodi_grafico['arrow_ab_to_dato_2']

        arrow_ac_to_dato_1.add_updater(
            lambda a: a.become(get_up_arrow(schema_ac, schema_dato_1, start_shift=.2 * LEFT))
        )
        arrow_bc_to_dato_1.add_updater(
            lambda a: a.become(get_up_arrow(schema_bc, schema_dato_1, start_shift=.2 * LEFT, end_shift=RIGHT))
        )
        arrow_ac_to_dato_2.add_updater(
            lambda a: a.become(get_up_arrow(schema_ac, schema_dato_2, start_shift=.2 * RIGHT, end_shift=2 * LEFT))
        )
        arrow_bc_to_dato_2.add_updater(
            lambda a: a.become(get_up_arrow(schema_bc, schema_dato_2, start_shift=.2 * RIGHT, end_shift=LEFT))
        )
        arrow_ab_to_dato_2.add_updater(
            lambda a: a.become(get_up_arrow(schema_ab, schema_dato_2))
        )
        self.riquadro_dati.add_updater(
            lambda a: a.become(SurroundingRectangle(self.dati_grafico, color=YELLOW, fill_opacity=.2, buff=.25))
        )

        self.play(schema_dato_1.animate.move_to(schema_dato_1_bis), schema_dato_2.animate.move_to(schema_dato_2_bis))
        self.cut_and_wait()

        arrow_ac_to_dato_1.clear_updaters()
        arrow_bc_to_dato_1.clear_updaters()
        arrow_ac_to_dato_2.clear_updaters()
        arrow_bc_to_dato_2.clear_updaters()
        arrow_ab_to_dato_2.clear_updaters()
        self.riquadro_dati.clear_updaters()

        self.play(Write(schema_dato_3))
        self.cut_and_wait()

        arrow_ac_to_dato_3 = get_up_arrow(schema_ac, schema_dato_3, end_shift=1 * LEFT)
        arrow_bc_to_dato_3 = get_up_arrow(schema_bc, schema_dato_3)
        arrow_ab_to_dato_3 = get_up_arrow(schema_ab, schema_dato_3, start_shift=.2 * LEFT, end_shift=1 * RIGHT)

        self.play(Create(arrow_ac_to_dato_3), Create(arrow_bc_to_dato_3), Create(arrow_ab_to_dato_3))
        self.cut_and_wait()

        self.grafico.add(schema_dato_3, arrow_ac_to_dato_3, arrow_bc_to_dato_3, arrow_ab_to_dato_3)

    def scala_grafico(self):
        pass
        self.play(self.grafico.animate.scale(.5).move_to(3.5 * RIGHT + 2.2 * UP))

    def costruisci_risoluzione(self):
        self.risoluzione = Risoluzione()
        # self.add(self.risoluzione)

    def definizione_variabili(self):
        self.play(Write(self.risoluzione.definizioni.definizione_x))
        self.play(Write(self.risoluzione.definizioni.definizione_y))
        self.play(Write(self.risoluzione.definizioni.definizione_z))
        self.cut_and_wait()

    def condizioni_variabili(self):
        self.play(Write(self.risoluzione.definizioni.condizione_x))
        self.play(Write(self.risoluzione.definizioni.condizione_y))
        self.play(Write(self.risoluzione.definizioni.condizione_z))
        self.cut_and_wait()

    def trasformazione_equazioni(self):
        self.play(Write(self.risoluzione.sistema_1))
        self.cut_and_wait()

    def sistema_2(self):
        self.play(Write(self.risoluzione.sistema_2))
        self.cut_and_wait()

    def sistema_3(self):
        self.play(Write(self.risoluzione.sistema_3))
        self.cut_and_wait()

    def sistema_4(self):
        self.play(Write(self.risoluzione.sistema_4))
        self.cut_and_wait()

    def equazione_1(self):
        self.play(Write(self.risoluzione.equazione_1))
        self.cut_and_wait()

