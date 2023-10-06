from manim import *

from qui_matematica.util import TableHelper

SMALL_FONT_SIZE = 20
BASE_FONT_SIZE = 40
DELAY = 30
SCALE_RATIO = 1.5

SMALL_PERC_SCALE = .7


class Tabella(MobjectTable):

    def __init__(self, **kwargs):
        table = [
            [Tex("", font_size=BASE_FONT_SIZE), Tex("non pranza", font_size=30), Tex("pranza", font_size=30), Tex("", font_size=BASE_FONT_SIZE)],
            [Tex(r"non mangia\\ yogurt", font_size=30), Tex("?", font_size=BASE_FONT_SIZE), Tex("?", font_size=BASE_FONT_SIZE), Tex(r"33\%", font_size=BASE_FONT_SIZE)],
            [Tex(r"mangia\\ yogurt", font_size=30), Tex("?", font_size=BASE_FONT_SIZE), Tex("?", font_size=BASE_FONT_SIZE), Tex(r"67\%", font_size=BASE_FONT_SIZE)],
            [Tex("", font_size=BASE_FONT_SIZE), Tex(r"23\%", font_size=BASE_FONT_SIZE), Tex(r"77\%", font_size=BASE_FONT_SIZE), Tex("", font_size=BASE_FONT_SIZE)]
        ]
        super().__init__(
            table,
            v_buff=.3, h_buff=.4, **kwargs)
        self.helper = TableHelper(self)
        self.view = VGroup()

    def create_table(self, scene: Scene, show_percentages=False):
        linee = [
            self.helper.get_horizontal_line(1, start=1, end=3),
            self.helper.get_horizontal_line(2, start=1, end=3),
            self.helper.get_horizontal_line(3, start=1, end=3),
            self.helper.get_vertical_line(1, start=1, end=3),
            self.helper.get_vertical_line(2, start=1, end=3),
            self.helper.get_vertical_line(3, start=1, end=3)
        ]
        headers = [
            self.get_entries_without_labels((1, 2)),
            self.get_entries_without_labels((1, 3)),
            self.get_entries_without_labels((2, 1)),
            self.get_entries_without_labels((3, 1))
        ]
        if show_percentages:
            headers.append(self.get_entries_without_labels((4, 2)))
            headers.append(self.get_entries_without_labels((4, 3)))
            headers.append(self.get_entries_without_labels((2, 4)))
            headers.append(self.get_entries_without_labels((3, 4)))
        scene.play(
            *[Create(_l) for _l in linee],
            *[Write(_h) for _h in headers]
        )
        for _l in linee:
            self.view.add(_l)
        for _h in headers:
            self.view.add(_h)

    def copy_label(self, scene: Scene, source, entry):
        label = source.copy()
        label.target = self.get_entries_without_labels(entry)
        scene.play(MoveToTarget(label))
        scene.add(self.get_entries_without_labels(entry))
        scene.remove(label)
        self.view.add(self.get_entries_without_labels(entry))

    def show_value(self, scene: Scene, pos, value):
        entry = self.get_entries_without_labels(pos)
        tex = Tex(str(value) + r"\%", font_size=BASE_FONT_SIZE).move_to(entry)
        entry.become(tex)
        scene.play(Write(entry))
        self.view.add(entry)

    def get_view(self):
        return self.view


class Scene(MovingCameraScene):

    def construct(self):
        self.wait(.5)

        initial_font_size = SMALL_FONT_SIZE

        testo = VGroup(
            VGroup(
                Tex("Da un’intervista ad un gruppo di persone è emerso che:", font_size=initial_font_size),
                Tex(r"- il 23\% salta il pranzo;", font_size=initial_font_size),
                Tex(r"- il 40\% mangia lo yogurt a pranzo;", font_size=initial_font_size),
                Tex(r"- il 33\% non mangia lo yogurt.", font_size=initial_font_size),
                Tex("Possiamo dedurre con certezza che:", font_size=initial_font_size)
            ).arrange(DOWN, aligned_edge=LEFT, buff=.1),
            VGroup(
                Tex("A: esistono persone che saltano il pranzo e non mangiano lo yogurt;", font_size=initial_font_size),
                Tex("B: tutte le persone che mangiano lo yogurt pranzano;", font_size=initial_font_size),
                Tex("C: tutte le persone che pranzano mangiano lo yogurt;", font_size=initial_font_size),
                Tex("D: esistono persone che mangiano lo yogurt, ma non a pranzo;", font_size=initial_font_size),
                Tex(r"E: la percentuale di persone che non salta il pranzo è inferiore al 70\%.", font_size=initial_font_size)
            ).arrange(DOWN, aligned_edge=LEFT, buff=.1)
        ).arrange(RIGHT, buff=1).to_edge(UP, buff=.2)

        self.add(testo)

        self.add(Line(start=3*LEFT, end=3*RIGHT).next_to(testo, DOWN))

        self.add(Line(start=testo[1][0].get_left(), end=testo[1][0].get_right(), color=RED))
        self.add(Line(start=testo[1][1].get_left(), end=testo[1][1].get_right(), color=RED))
        self.add(Line(start=testo[1][2].get_left(), end=testo[1][2].get_right(), color=RED))
        self.add(Line(start=testo[1][4].get_left(), end=testo[1][4].get_right(), color=RED))
        self.cut_and_wait()

        # La risposta D dice: esistono persone che mangiano lo yogurt, ma non a pranzo.

        risposta_d = testo[1][3].copy()
        risposta_d.target = testo[1][3].copy().scale(SCALE_RATIO).move_to(UP)
        self.play(MoveToTarget(risposta_d))
        self.cut_and_wait()

        # Attenzione che questa frase non corrisponde alla casella in basso a sinistra.

        tabella = Tabella().move_to(DOWN)
        tabella.create_table(self, show_percentages=True)
        punto_di_domanda = Tex("?", color=YELLOW).move_to(tabella.get_entries_without_labels((3, 2)))
        self.play(Write(punto_di_domanda))
        self.cut_and_wait()

        # Infatti non ci dice che le persone saltano il pranzo.
        # Ci dice che non mangiano lo yogurt a pranzo, ma potrebbero pranzare mangiando qualcos'altro.

        x = Tex("X", color=RED, z_index=10).move_to(tabella.get_entries_without_labels((3, 2)))
        self.play(FadeOut(punto_di_domanda), Write(x))
        self.cut_and_wait()

        # Ma allora come possiamo essere certi che sia la risposta corretta?
        # Beh, innanzitutto nota che c'è una frase del testo che non abbiamo ancora sfruttato.

        frase_2 = testo[0][2].copy()
        frase_2.target = testo[0][2].copy().scale(SCALE_RATIO).next_to(tabella, DOWN)
        self.play(MoveToTarget(frase_2))
        self.cut_and_wait()

        # Sappiamo che il 40% della popolazione mangia lo yogurt a pranzo. Questa affermazione ci dice tre cose:
        # - questo 40% della popolazione mangia lo yogurt, quindi siamo nelle caselle in basso;

        backs = [
            BackgroundRectangle(tabella.get_cell((3, 2)), color=GREEN),
            BackgroundRectangle(tabella.get_cell((3, 3)), color=GREEN)
        ]
        self.play(*[Create(b) for b in backs])
        self.cut_and_wait()

        # - questo 40% della popolazione pranza, quindi siamo nelle caselle a destra;

        self.play(FadeOut(backs[0]))
        back = backs[1]
        self.cut_and_wait()

        # - inoltre questo 40% della popolazione mangia lo yogurt a pranzo.
        # Si tratta quindi di un sottoinsieme della popolazione rappresentata dalla casella in basso a destra.

        insieme = Ellipse(width=1.5, color=YELLOW, z_index=1).scale(.55).\
            move_to(tabella.get_entries_without_labels((3, 3)).get_center() + .1 * UR + .1 * RIGHT)
        percentuale_insieme = Tex(r"40\%", color=YELLOW).scale(SMALL_PERC_SCALE).move_to(insieme)
        self.play(Create(insieme))
        self.cut_and_wait()
        self.play(Write(percentuale_insieme))
        self.cut_and_wait()

        # Sappiamo che questo sottoinsieme contiene sempre il 40% della popolazione.
        # La parte esterna di tale sottoinsieme è composto dalle persone che mangiano a pranzo, mangiano yogurt, ma non
        # mangiano yogurt a pranzo. Ed è proprio quello che stiamo cercando.

        back_piccolo = Difference(back, insieme, color=GREEN, fill_opacity=1)
        self.play(FadeOut(back), FadeIn(back_piccolo))

        # Ora, torniamo alle nostre due situazioni estreme.

        self.play(FadeOut(tabella.get_view()), FadeOut(x), FadeOut(back_piccolo), FadeOut(insieme),
                  FadeOut(percentuale_insieme))
        self.cut_and_wait()

        estremo_sn = Tabella().shift(DOWN).shift(4 * LEFT)
        estremo_dx = Tabella().shift(DOWN).shift(4 * RIGHT)
        estremo_sn.create_table(self, show_percentages=True)
        estremo_dx.create_table(self, show_percentages=True)
        self.cut_and_wait()

        estremo_sn.show_value(self, (2, 2), 23)
        estremo_sn.show_value(self, (3, 2), 0)
        estremo_dx.show_value(self, (3, 2), 23)
        estremo_dx.show_value(self, (2, 2), 0)
        estremo_sn.show_value(self, (2, 3), 10)
        estremo_sn.show_value(self, (3, 3), 67)
        estremo_dx.show_value(self, (2, 3), 33)
        estremo_dx.show_value(self, (3, 3), 44)
        self.cut_and_wait()

        # Nella prima situazione estrema la percentuale di chi pranza e mangia yogurt è del 67%.

        back_sn = back.copy().set_z_index(-1).shift(4*LEFT)
        self.play(Create(back_sn))
        self.cut_and_wait()

        # Questo 67% si distribuisce nel 40% che mangia yogurt a pranzo

        insieme_sn = insieme.copy().shift(4*LEFT)
        percentuale_insieme_sn = percentuale_insieme.copy().shift(4*LEFT)
        back_piccolo_sn = back_piccolo.copy().shift(4*LEFT)

        self.add(back_piccolo_sn)
        self.play(
            FadeOut(back_sn), FadeOut(estremo_sn.get_entries_without_labels((3, 3))),
            Create(insieme_sn), Write(percentuale_insieme_sn)
        )
        self.cut_and_wait()

        # e in un residuo 27% di chi non mangia yogurt a pranzo.

        self.play(
            FadeOut(back_piccolo_sn),
            Write(Tex(r"27\%", color=YELLOW).scale(SMALL_PERC_SCALE).
                  move_to(estremo_sn.get_entries_without_labels((3, 3)).get_center() + .3 * DL))
        )
        self.cut_and_wait()

        # Nella seconda situazione estrema la percentuale di chi pranza e mangia yogurt è del 44%.

        back_dx = back.copy().set_z_index(-1).shift(4*RIGHT)
        self.play(Create(back_dx))
        self.cut_and_wait()

        # 40% mangia lo yogurt a pranzo

        insieme_dx = insieme.copy().shift(4*RIGHT)
        percentuale_insieme_dx = percentuale_insieme.copy().shift(4*RIGHT)
        back_piccolo_dx = back_piccolo.copy().shift(4*RIGHT)

        self.add(back_piccolo_dx)
        self.play(
            FadeOut(back_dx), FadeOut(estremo_dx.get_entries_without_labels((3, 3))),
            Create(insieme_dx), Write(percentuale_insieme_dx)
        )
        self.cut_and_wait()

        # e un residuo 4% non mangia yogurt a pranzo.

        self.play(
            FadeOut(back_piccolo_dx),
            Write(Tex(r"4\%", color=YELLOW).scale(SMALL_PERC_SCALE).
                  move_to(estremo_dx.get_entries_without_labels((3, 3)).get_center() + .3 * DL))
        )
        self.cut_and_wait()

        # In entrambi le situazione intermedie esiste sempre una percentuale residua di chi non mangia yogurt a pranzo.
        # Quindi la risposta D è quella corretta.

        contorno = SurroundingRectangle(risposta_d)
        self.play(Create(contorno))

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()
