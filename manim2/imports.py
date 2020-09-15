"""
I won't pretend like this is best practice, by in creating animations for a video,
it can be very nice to simply have all of the Mobjects, Animations, Scenes, etc.
of manim available without having to worry about what namespace they come from.

Rather than having a large pile of "from <module> import *" at the top of every such
script, the intent of this file is to make it so that one can just include
"from manim2.imports import *".  The effects of adding more modules
or refactoring the library on current or older scene scripts should be entirely
addressible by changing this file.

Note: One should NOT import from this file for main library code, it is meant only
as a convenience for scripts creating scenes for videos.
"""


from manim2.constants import *

from manim2.animation.animation import *
from manim2.animation.composition import *
from manim2.animation.creation import *
from manim2.animation.fading import *
from manim2.animation.growing import *
from manim2.animation.indication import *
from manim2.animation.movement import *
from manim2.animation.numbers import *
from manim2.animation.rotation import *
from manim2.animation.specialized import *
from manim2.animation.transform import *
from manim2.animation.update import *

from manim2.camera.camera import *
from manim2.camera.mapping_camera import *
from manim2.camera.moving_camera import *
from manim2.camera.three_d_camera import *

from manim2.mobject.coordinate_systems import *
from manim2.mobject.changing import *
from manim2.mobject.frame import *
from manim2.mobject.functions import *
from manim2.mobject.geometry import *
from manim2.mobject.matrix import *
from manim2.mobject.mobject import *
from manim2.mobject.number_line import *
from manim2.mobject.numbers import *
from manim2.mobject.probability import *
from manim2.mobject.shape_matchers import *
from manim2.mobject.svg.brace import *
from manim2.mobject.svg.drawings import *
from manim2.mobject.svg.svg_mobject import *
from manim2.mobject.svg.tex_mobject import *
from manim2.mobject.svg.text_mobject import *
from manim2.mobject.svg.code_mobject import *
from manim2.mobject.three_d_utils import *
from manim2.mobject.three_dimensions import *
from manim2.mobject.types.image_mobject import *
from manim2.mobject.types.point_cloud_mobject import *
from manim2.mobject.types.vectorized_mobject import *
from manim2.mobject.mobject_update_utils import *
from manim2.mobject.value_tracker import *
from manim2.mobject.vector_field import *

from manim2.for_3b1b_videos.common_scenes import *
from manim2.for_3b1b_videos.pi_creature import *
from manim2.for_3b1b_videos.pi_creature_animations import *
from manim2.for_3b1b_videos.pi_creature_scene import *

from manim2.once_useful_constructs.arithmetic import *
from manim2.once_useful_constructs.combinatorics import *
from manim2.once_useful_constructs.complex_transformation_scene import *
from manim2.once_useful_constructs.counting import *
from manim2.once_useful_constructs.fractals import *
from manim2.once_useful_constructs.graph_theory import *
from manim2.once_useful_constructs.light import *

from manim2.scene.graph_scene import *
from manim2.scene.moving_camera_scene import *
from manim2.scene.reconfigurable_scene import *
from manim2.scene.scene import *
from manim2.scene.sample_space_scene import *
from manim2.scene.graph_scene import *
from manim2.scene.scene_from_video import *
from manim2.scene.three_d_scene import *
from manim2.scene.vector_space_scene import *
from manim2.scene.zoomed_scene import *

from manim2.utils.bezier import *
from manim2.utils.color import *
from manim2.utils.config_ops import *
from manim2.utils.debug import *
from manim2.utils.images import *
from manim2.utils.iterables import *
from manim2.utils.file_ops import *
from manim2.utils.paths import *
from manim2.utils.rate_functions import *
from manim2.utils.simple_functions import *
from manim2.utils.sounds import *
from manim2.utils.space_ops import *
from manim2.utils.strings import *


# TK
from manim2.scene.end_video import *
# TK END


# Non manim libraries that are also nice to have without thinking

import inspect
import itertools as it
import numpy as np
import operator as op
import os
import random
import re
import string
import sys
import math

from PIL import Image
from colour import Color
