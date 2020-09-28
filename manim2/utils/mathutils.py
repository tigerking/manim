from manim2.imports import *


def set_k_color(*args):
    for f in args:
        for letter, color in [("1001", RED), ("728", BLUE)]:
            f.set_color_by_tex(letter, color)


def calc_vertical(scene, a, b, op='+', x=3 * UP, y=4.5 * RIGHT, va=None, vb=None):
    m_op = {
        '+': (lambda x, y: x + y, '+'),
        '-': (lambda x, y: x - y, '-'),
        '*': (lambda x, y: x * y, '\\times'),
        '/': (lambda x, y: int(x / y), '/'),
    }
    vstep = 0.5

    if va is None:
        va = TexMobject(str(a))
        va.move_to(x + y)
        scene.play(Write(va), run_time=2)
        scene.wait()

    if vb is None:
        vb = TexMobject(str(b))
        vb.move_to(x - (vstep * UP) + y)
        vb.align_to(va, RIGHT)

        scene.play(Write(vb), run_time=2)

    vop = TexMobject(m_op[op][1])
    vop.move_to(x - (vstep * UP) + y)
    vop.next_to(vb, LEFT)

    # self.play(Write(vop, run_time=2))
    scene.add(vop)

    vline = Line(va.get_left() - 0.5 * X_AXIS, va.get_right(), stroke_opatity=0.5)
    vline.move_to(x - (2 * vstep * UP) + y)
    vline.align_to(va, RIGHT)
    scene.play(Write(vline))

    r = m_op[op][0](a, b)
    result_digits = list(str(r))
    vresult = TexMobject(*result_digits)
    vresult.move_to(x - (3 * vstep * UP) + y)
    vresult.align_to(va, RIGHT)

    for i in range(len(result_digits) - 1, -1, -1):
        # print(i)
        scene.play(Write(vresult[i]))

    return (VGroup(va, vb, vop, vline, vresult), vresult, r)
