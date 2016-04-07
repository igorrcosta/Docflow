#!/usr/bin/env python
# -*- coding: utf-8 -*-
# model.py

'''Define our classes.'''

class Docflow():
    def __init__(self, stages = []):
        self.stages = stages

    def add_stage(self, stage):
        self.stages.append(stage)

    def construct(self):
        for stage in stages:
            print stage

class Stages():
    def __init__(self):
        self.phrases = []

    def __str__(self):
        return '\n'.join(self.phrases)

    def add_phrase(self, phrase):
        self.phrases.append(phrase)
