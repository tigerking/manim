#!/usr/bin/env python
import manim2.config
import manim2.constants
import manim2.extract_scene


def main():
    args = manimlib.config.parse_cli()
    config = manimlib.config.get_configuration(args)
    manimlib.constants.initialize_directories(config)
    manimlib.extract_scene.main(config)
