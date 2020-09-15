#!/usr/bin/env python
import manim2.config
import manim2.constants
import manim2.extract_scene


def main():
    args = manim2.config.parse_cli()
    config = manim2.config.get_configuration(args)
    manim2.constants.initialize_directories(config)
    manim2.extract_scene.main(config)
