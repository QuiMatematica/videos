from manim import *

from qpercentage import Percentage
from util import TableHelper

SMALL_FONT_SIZE = 20
BASE_FONT_SIZE = 40
DELAY = 0
SCALE_RATIO = 1.5


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
        self.cut_and_wait()

        separatore = Line(start=3*LEFT, end=3*RIGHT).next_to(testo, DOWN)

        self.play(Create(separatore))
        self.cut_and_wait()

        affermazione_1 = testo[0][1].copy()
        affermazione_3 = testo[0][3].copy()

        popolazione_pranzo = Percentage((("non pranza", 23), ("pranza", 77)))
        popolazione_yogurt = Percentage((("non mangia yogurt", 33), ("mangia yogurt", 67)))

        impaginazione = VGroup(
            affermazione_1.copy().scale(SCALE_RATIO),
            popolazione_pranzo,
            affermazione_3.copy().scale(SCALE_RATIO),
            popolazione_yogurt
        ).arrange(DOWN, buff=.5).shift(DOWN)

        self.play(affermazione_1.animate.scale(SCALE_RATIO).move_to(impaginazione[0]))
        popolazione_pranzo.show_percentages(self)
        self.cut_and_wait()

        risposta_a = testo[1][0].copy()
        risposta_b = testo[1][1].copy()
        risposta_c = testo[1][2].copy()
        risposta_d = testo[1][3].copy()
        risposta_e = testo[1][4].copy()
        self.play(risposta_e.animate.scale(SCALE_RATIO).move_to(impaginazione[2]))
        cancella_risposta_e = Line(start=risposta_e.get_left(), end=risposta_e.get_right(), color=RED)
        self.play(Create(cancella_risposta_e))
        self.cut_and_wait()

        self.play(cancella_risposta_e.animate.scale(1/SCALE_RATIO).move_to(testo[1][4]),
                  FadeOut(risposta_e))
        self.cut_and_wait()

        self.play(affermazione_3.animate.scale(SCALE_RATIO).move_to(impaginazione[2]))
        popolazione_yogurt.show_percentages(self)
        self.cut_and_wait()

        impaginazione = VGroup(
            popolazione_pranzo.copy().scale(1/SCALE_RATIO),
            popolazione_yogurt.copy().scale(1/SCALE_RATIO)
        ).arrange(RIGHT, buff=2).next_to(separatore, DOWN)

        self.play(
            FadeOut(affermazione_1), FadeOut(affermazione_3),
            popolazione_pranzo.animate.scale(1/SCALE_RATIO).move_to(impaginazione[0]),
            popolazione_yogurt.animate.scale(1/SCALE_RATIO).move_to(impaginazione[1])
        )
        self.cut_and_wait()

        impaginazione = VGroup(
            risposta_a.copy().scale(SCALE_RATIO),
            risposta_b.copy().scale(SCALE_RATIO),
            risposta_c.copy().scale(SCALE_RATIO)
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN)

        self.play(
            risposta_a.animate.scale(SCALE_RATIO).move_to(impaginazione[0]),
            risposta_b.animate.scale(SCALE_RATIO).move_to(impaginazione[1]),
            risposta_c.animate.scale(SCALE_RATIO).move_to(impaginazione[2])
        )
        self.cut_and_wait()

        self.play(
            FadeOut(risposta_a),
            FadeOut(risposta_b),
            FadeOut(risposta_c)
        )
        self.cut_and_wait()

        prima_tabella = Tabella().shift(DOWN)
        prima_tabella.create_table(self)
        self.cut_and_wait()

        backs = [
            BackgroundRectangle(prima_tabella.get_cell((2, 2)), color=GREEN),
            BackgroundRectangle(prima_tabella.get_cell((3, 2)), color=GREEN)
        ]
        self.play(*[Create(b) for b in backs])
        prima_tabella.copy_label(self, popolazione_pranzo.percentages[0], (4, 2))
        self.cut_and_wait()

        self.play(*[FadeOut(b) for b in backs])

        backs = [
            BackgroundRectangle(prima_tabella.get_cell((2, 3)), color=GREEN),
            BackgroundRectangle(prima_tabella.get_cell((3, 3)), color=GREEN)
        ]
        self.play(*[Create(b) for b in backs])
        prima_tabella.copy_label(self, popolazione_pranzo.percentages[1], (4, 3))
        self.cut_and_wait()

        self.play(*[FadeOut(b) for b in backs])

        backs = [
            BackgroundRectangle(prima_tabella.get_cell((2, 2)), color=GREEN),
            BackgroundRectangle(prima_tabella.get_cell((2, 3)), color=GREEN)
        ]
        self.play(*[Create(b) for b in backs])
        prima_tabella.copy_label(self, popolazione_yogurt.percentages[0], (2, 4))
        self.cut_and_wait()

        self.play(*[FadeOut(b) for b in backs])

        backs = [
            BackgroundRectangle(prima_tabella.get_cell((3, 2)), color=GREEN),
            BackgroundRectangle(prima_tabella.get_cell((3, 3)), color=GREEN)
        ]
        self.play(*[Create(b) for b in backs])
        prima_tabella.copy_label(self, popolazione_yogurt.percentages[1], (3, 4))
        self.play(*[FadeOut(b) for b in backs])
        self.cut_and_wait()

        prima_tabella.show_value(self, (2, 2), 8)
        self.cut_and_wait()

        prima_tabella.show_value(self, (2, 3), 25)
        prima_tabella.show_value(self, (3, 2), 15)
        prima_tabella.show_value(self, (3, 3), 52)
        self.cut_and_wait()

        self.play(prima_tabella.get_view().animate.shift(4*LEFT))

        seconda_tabella = Tabella().shift(DOWN).shift(4*RIGHT)
        seconda_tabella.create_table(self, show_percentages=True)
        seconda_tabella.show_value(self, (2, 2), 7)
        seconda_tabella.show_value(self, (2, 3), 26)
        seconda_tabella.show_value(self, (3, 2), 16)
        seconda_tabella.show_value(self, (3, 3), 51)
        self.cut_and_wait()

        # Cosa devo fare allora per rispondere con certezza al quiz? Devo lavorare sulle situazioni estreme e da queste
        # dedurre le conclusioni certe.

        self.play(
            *[FadeOut(e) for e in prima_tabella.get_view()],
            *[FadeOut(e) for e in seconda_tabella.get_view()]
        )

        estremo_sn = Tabella().shift(DOWN)
        estremo_sn.create_table(self, show_percentages=True)
        self.cut_and_wait()

        # Come fare? Conviene partire dalla percentuale più bassa: il 23% della popolazione che salta il pranzo.

        self.play(Indicate(estremo_sn.get_entries_without_labels((4, 2))))
        self.cut_and_wait()

        # Questo 23% potrebbe stare o tutto nella casella in basso o tutto nella casella in alto. Ho quindi due
        # situazioni estreme.

        estremo_dx = estremo_sn.copy()
        self.play(
            estremo_sn.get_view().animate.shift(4 * LEFT),
            estremo_dx.get_view().animate.shift(4 * RIGHT)
        )

        cancella = Tex("CANCELLA", color=RED)
        self.add(cancella)
        self.remove(estremo_sn.get_view(), estremo_dx.get_view(), estremo_sn, estremo_dx)
        estremo_sn = Tabella().shift(DOWN).shift(4 * LEFT)
        estremo_dx = Tabella().shift(DOWN).shift(4 * RIGHT)
        estremo_sn.create_table(self, show_percentages=True)
        estremo_dx.create_table(self, show_percentages=True)
        self.remove(cancella)

        estremo_sn.show_value(self, (2, 2), 23)
        estremo_sn.show_value(self, (3, 2), 0)
        estremo_dx.show_value(self, (3, 2), 23)
        estremo_dx.show_value(self, (2, 2), 0)
        self.cut_and_wait()

        # Eseguo i calcoli nelle due situazioni.

        estremo_sn.show_value(self, (2, 3), 10)
        estremo_sn.show_value(self, (3, 3), 67)
        estremo_dx.show_value(self, (2, 3), 33)
        estremo_dx.show_value(self, (3, 3), 44)
        self.cut_and_wait()

        # Tutte le altre possibili situazioni saranno comprese tra queste due situazioni estreme.
        
        self.situazioni_intermedie(estremo_sn, estremo_dx)
        
        # Quindi concentriamoci sulle due situazioni estreme e vediamo cosa possiamo dire delle possibili risposte.
        # La risposta C dice: tutte le persone che pranzano mangiano yogurt.

        risposta_c = testo[1][2].copy()
        risposta_c.target = testo[1][2].copy().scale(SCALE_RATIO).move_to(3 * DOWN)
        self.play(MoveToTarget(risposta_c))
        self.cut_and_wait()

        # Le persone che pranzano sono quelle delle caselle a destra.

        borders = [
            SurroundingRectangle(estremo_sn.get_entries_without_labels((2, 3))),
            SurroundingRectangle(estremo_sn.get_entries_without_labels((3, 3))),
            SurroundingRectangle(estremo_dx.get_entries_without_labels((2, 3))),
            SurroundingRectangle(estremo_dx.get_entries_without_labels((3, 3))),
        ]
        self.play(*[Create(b) for b in borders])
        self.cut_and_wait()

        # Ma in entrambi le situazioni estreme esiste sempre qualcuno che pranza ma non mangia
        # yogurt.

        self.play(FadeOut(borders[0]), FadeOut(borders[2]))
        self.cut_and_wait()

        # Quindi questa risposta è sbagliata.

        cancella_risposta_c = Line(start=risposta_c.get_left(), end=risposta_c.get_right(), color=RED)
        self.play(Create(cancella_risposta_c))
        self.cut_and_wait()

        self.play(cancella_risposta_c.animate.scale(1 / SCALE_RATIO).move_to(testo[1][2]),
                  FadeOut(risposta_c), FadeOut(borders[1]), FadeOut(borders[3]))
        self.cut_and_wait()

        # La risposta B dice: tutte le persone che mangiano lo yogurt pranzano.

        risposta_b = testo[1][1].copy()
        risposta_b.target = testo[1][1].copy().scale(SCALE_RATIO).move_to(3 * DOWN)
        self.play(MoveToTarget(risposta_b))
        self.cut_and_wait()

        # Le persone che mangiano lo yogurt sono quelle che stanno nelle due caselle in basso.

        borders = [
            SurroundingRectangle(estremo_sn.get_entries_without_labels((3, 2))),
            SurroundingRectangle(estremo_sn.get_entries_without_labels((3, 3))),
            SurroundingRectangle(estremo_dx.get_entries_without_labels((3, 2))),
            SurroundingRectangle(estremo_dx.get_entries_without_labels((3, 3))),
        ]
        self.play(*[Create(b) for b in borders])
        self.cut_and_wait()

        # Nella seconda situazione estrema, tutte le persone che mangiano
        # lo yogurt pranzano, mentre nella prima situazione estrema ci sono persone che mangiano lo yogurt ma non
        # pranzano.

        self.play(FadeOut(borders[1]), FadeOut(borders[2]), FadeOut(borders[3]))
        self.cut_and_wait()

        # Quindi non possiamo dire con certezza che la risposta B è vera.
        # Quindi la escludiamo.

        cancella_risposta_b = Line(start=risposta_b.get_left(), end=risposta_b.get_right(), color=RED)
        self.play(Create(cancella_risposta_b))
        self.cut_and_wait()

        self.play(cancella_risposta_b.animate.scale(1 / SCALE_RATIO).move_to(testo[1][1]),
                  FadeOut(risposta_b), FadeOut(borders[0]))
        self.cut_and_wait()

        # Risposta A: esistono persone che saltano il pranzo e non mangiano lo yogurt.

        risposta_a = testo[1][0].copy()
        risposta_a.target = testo[1][0].copy().scale(SCALE_RATIO).move_to(3 * DOWN)
        self.play(MoveToTarget(risposta_a))
        self.cut_and_wait()

        # Questo è vero nella seconda
        # situazione estrema, ma non è vero nella prima situazione estrema in cui abbiamo uno 0% di persone che saltano
        # il pranzo e non mangiano lo yogurt.

        borders = [
            SurroundingRectangle(estremo_sn.get_entries_without_labels((2, 2))),
            SurroundingRectangle(estremo_dx.get_entries_without_labels((2, 2)))
        ]
        self.play(*[Create(b) for b in borders])
        self.cut_and_wait()

        # Quindi anche questa risposta è sbagliata perché non è certa, anche se
        # possibile.

        cancella_risposta_a = Line(start=risposta_a.get_left(), end=risposta_a.get_right(), color=RED)
        self.play(Create(cancella_risposta_a))
        self.cut_and_wait()

        self.play(cancella_risposta_a.animate.scale(1 / SCALE_RATIO).move_to(testo[1][0]),
                  FadeOut(risposta_a), FadeOut(borders[0]), FadeOut(borders[1]))
        self.cut_and_wait()

        self.wait(30)

    def cut_and_wait(self):
        if DELAY > 0:
            self.wait(DELAY)
            self.next_section()

    def situazioni_intermedie(self, estremo_sn, estremo_dx):
        copy_view = estremo_sn.get_view().copy().set_z_index(10)
        self.add(copy_view)
        self.play(
            estremo_sn.get_view().animate.set_color(GRAY_E),
            estremo_dx.get_view().animate.set_color(GRAY_E)
        )

        tracker = ValueTracker(0)

        def move_view(old_view):
            amount = (estremo_dx.get_center()[0] - estremo_sn.get_center()[0]) * tracker.get_value() / 23
            old_view.move_to(estremo_sn.get_center() + amount * RIGHT)

        copy_view.add_updater(lambda c: move_view(c))

        def update_no_pranzo_no_yogurt(old_tex):
            tex = Tex(str(23 - int(tracker.get_value())) + r"\%", font_size=BASE_FONT_SIZE).move_to(old_tex)
            old_tex.become(tex)

        def update_no_pranzo_si_yogurt(old_tex):
            tex = Tex(str(int(tracker.get_value())) + r"\%", font_size=BASE_FONT_SIZE).move_to(old_tex)
            old_tex.become(tex)

        def update_si_pranzo_no_yogurt(old_tex):
            tex = Tex(str(10 + int(tracker.get_value())) + r"\%", font_size=BASE_FONT_SIZE).move_to(old_tex)
            old_tex.become(tex)

        def update_si_pranzo_si_yogurt(old_tex):
            tex = Tex(str(67 - int(tracker.get_value())) + r"\%", font_size=BASE_FONT_SIZE).move_to(old_tex)
            old_tex.become(tex)

        no_pranzo_no_yogurt = copy_view[len(copy_view) - 4]
        no_pranzo_no_yogurt.add_updater(lambda b: update_no_pranzo_no_yogurt(b))

        no_pranzo_si_yogurt = copy_view[len(copy_view) - 3]
        no_pranzo_si_yogurt.add_updater(lambda b: update_no_pranzo_si_yogurt(b))

        si_pranzo_no_yogurt = copy_view[len(copy_view) - 2]
        si_pranzo_no_yogurt.add_updater(lambda b: update_si_pranzo_no_yogurt(b))

        si_pranzo_si_yogurt = copy_view[len(copy_view) - 1]
        si_pranzo_si_yogurt.add_updater(lambda b: update_si_pranzo_si_yogurt(b))

        self.play(tracker.animate.set_value(23), run_time=5, rate_func=linear)

        copy_view.clear_updaters()
        self.play(
            estremo_sn.get_view().animate.set_color(WHITE),
            estremo_dx.get_view().animate.set_color(WHITE)
        )
        self.remove(copy_view)
        self.cut_and_wait()
