#!/usr/bin/env python
# coding: utf-8
import music21
from music21 import *


def calculate_interval(start_note,end_note):
    aInterval = interval.Interval(noteStart=start_note, noteEnd=end_note)
    return aInterval 
    


def calculate_interval_undirected(start_note,end_note):
    aInterval = interval.Interval(noteStart=start_note, noteEnd=end_note)
    return aInterval.name 

