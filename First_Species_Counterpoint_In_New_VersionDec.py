#!/usr/bin/env python
# coding: utf-8

# **First Species Counterpoint Generation Using Quantum Annealing**
# 
# Reference: https://raw.githubusercontent.com/martisekpetr/First-Species-Counterpoint-Constructor/master/counterpoint.pdf
# 

#Import required libraries

# !dwave solvers
# !pip install -U music21
# !pip install -U pandas
# !pip install -U matplotlib
# !pip install -U dwave-ocean-sdk

from dwave.system import EmbeddingComposite, DWaveSampler, LeapHybridSampler
import pyqubo
from pyqubo import Array, Binary,  Constraint, solve_qubo, Mul
import neal
from pprint import pprint
import pandas as pd
import numpy as np

import music21
from music21 import *


from calculate_interval_music21 import *
from constraints_from_rules_in_first_species import *
from generate_constrained_notes_in_first_species import *
from compose_new_midi_with_generated_counterpoint_first_species import *
from compile_sections_first import *
from verify_first_species import *

environment.set("musescoreDirectPNGPath",  r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe')


# *Define Treble Clef*
# 
# This is required as we have assumed that the counterpoint line is going to be written on Treble Clef.
# We are taking a maximal set of notes from Treble Clef: from A3 to B5.

treble_clef_notes=[]
treble_clef_start=note.Note('A3')
treble_clef_notes.append(treble_clef_start)
treble_clef_notes[0].pitch.frequency
aInterval=interval.Interval(1)
for i in range (1,27):
    aInterval.noteStart=treble_clef_notes[i-1]
    #print(aInterval.noteEnd.pitch,aInterval.noteEnd.pitch.frequency)
    treble_clef_notes.append(aInterval.noteEnd)
POSSIBLE_FREQUENCIES=len(treble_clef_notes)
print("POSSIBLE_FREQUENCIES ",POSSIBLE_FREQUENCIES)


# *Reading the midi*

mf = midi.MidiFile()

#fp='Counterpoint_First_Species_new_example_musescore12.mid'
fp='First_Species_new.mid' #correct version
#fp='Counterpoint_First_Species_only_three.mid'
mf.open(fp)
mf.read()
mf.close()
base_midi=midi.translate.midiFileToStream(mf)

file = base_midi#converter.parse(fp)

stream_cp = []
stream_cf = []

stream_cp_frequency = []
stream_cf_frequency = []

#file.parts[0].flat.notes[0].pitch = pitch.Pitch('a#4')

for i1 in range(len(file.parts)):
    #print(i1+1)
    for i2 in range(len(file.parts[1].flat.notes)):
       # print(file.parts[i1].flat.notes[i2].pitch)
        if(i1==0):
            stream_cp.append(file.parts[i1].flat.notes[i2].pitch)
            stream_cp_frequency.append(file.parts[i1].flat.notes[i2].pitch.frequency)
        if(i1==1):
            stream_cf.append(file.parts[i1].flat.notes[i2].pitch)
            stream_cf_frequency.append(file.parts[i1].flat.notes[i2].pitch.frequency)

print(stream_cp)
print(stream_cf)

print('pitch: \n')
print(stream_cp_frequency)
print(stream_cf_frequency)

max_cf=max(stream_cf_frequency)
min_cf=min(stream_cf_frequency)
print(min_cf," ",max_cf)

max_cp=max(stream_cp_frequency)
min_cp=min(stream_cp_frequency)
print(min_cp," ",max_cp)


# *Display the given music sheet from the midi file and play it*


base_midi.show('mid')
#base_midi.show()


# This step is required to divide the music into multiple sections. As the rules of counterpoint are applied section wise we will divide the given c.f. into sections. The section breaks have to be fed manually.


#section_breaks=[8,17,26,36,46] #[[0, 8],[9,17],[18,26],[27,36],[37,46]]

section_breaks=[9] #Place holder for the section break point
#section_breaks=[12] #  [8,16,24,36,48,60,76,92,108,124] #[[0, 8],[9,17],[18,26],[27,36],[37,46]]
#section_breaks= [8,16,24] #,36,48,60,76,92,108,124]
sectionized_cp=[] #2D array to hold the sectio wise divided c.p.
sectionized_cf=[] #2D array to hold the sectio wise divided c.f.

sectionized_cp_frequency=[] #2D array to hold the sectio wise divided c.p. frequency
sectionized_cf_frequency=[] #2D array to hold the sectio wise divided c.f. frequency

for i in range(len(section_breaks)):

    if(i==0):
        start=0
        end=section_breaks[i]
    
    if(i==len(section_breaks)-1):
        end=len(stream_cp)
    
    
    sectionized_cp.append(stream_cp[start:end])
    sectionized_cf.append(stream_cf[start:end])
    sectionized_cp_frequency.append(stream_cp_frequency[start:end])
    sectionized_cf_frequency.append(stream_cf_frequency[start:end])
    
    start=end
    if(i<len(section_breaks)-1):
        end=section_breaks[i+1]
        
for i in range(len(sectionized_cp)):
    print(i)
    print(len(sectionized_cp[i]), sectionized_cp[i],"\n",sectionized_cf[i],"\n")


# *Define the function to generate the counterpoint*


def generate_cp_sections(section_cf,section_cf_frequency,treble_clef,num_notes,POSSIBLE_FREQUENCIES):
    
    q = Array.create('q', shape=(num_notes,POSSIBLE_FREQUENCIES), vartype='BINARY')
    w = Array.create('w', shape=(7), vartype='BINARY')
    
    num_notes,Q=generate_constrained_notes(section_cf,treble_clef_notes,num_notes,q,w,POSSIBLE_FREQUENCIES)
    
    model = Q.compile()
    qubo, offset = model.to_qubo()
    #Simulated quantum annealer
    #sampler = neal.SimulatedAnnealingSampler()

    #Real quantum annealer
    #sampler_auto = EmbeddingComposite(DWaveSampler()) #Uncomment if using the Real quantum anneaner
    #sampleset = sampler_auto.sample_qubo(qubo, num_reads = 1000,label='QUBO Counterpoint') #Uncomment if using the Real quantum anneaner

    
    #dwave hybrid solver
    sampler = LeapHybridSampler()
    sampleset = sampler.sample_qubo(qubo)
    
#     Real quantum annealer
#     sampler = EmbeddingComposite(DWaveSampler())
#     sampleset = sampler.sample_qubo(qubo, num_reads = 1000,label='QUBO Counterpoint')

    #sampleset = sampler.sample_qubo(qubo, num_reads = 3000,label='QUBO Counterpoint')
    
    sample = sampleset.first.sample
    selected_notes = {i:[] for i in range(num_notes)}
    for i in range(num_notes):
        for j in range(POSSIBLE_FREQUENCIES):
            if (sample[f'q[{i}][{j}]']==1):
                selected_notes[i].append(j)
                
    print(selected_notes)

    return [selected_notes,sampleset]
    
    


# Call the function to perform QUBO and stitch together the counterpoint generated in each section of c.f.


generated_counterpoint=[]

for i in range(len(sectionized_cf)):

    section_cp=sectionized_cp[i]
    section_cf=sectionized_cf[i]
    section_cp_frequency=sectionized_cp_frequency[i]
    section_cf_frequency=sectionized_cf_frequency[i]
    print("section ", i)
    #print(section_cf)
    
    num_notes=len(section_cf)
    print("num_notes= ",num_notes)
    
#     sampleset_pd,sampleset_pd_all,offset=generate_cp_sections(section_cf,section_cf_frequency,
#                                                               treble_clef_notes,num_notes, POSSIBLE_FREQUENCIES)
    
    [selected_notes,sampleset]=generate_cp_sections(section_cf,section_cf_frequency,treble_clef_notes,
                                                    num_notes, POSSIBLE_FREQUENCIES)
    print(selected_notes)
    generated_section=[]
    for key, values in selected_notes.items():
        generated_section.append(treble_clef_notes[selected_notes[key][0]])
        
    

#     generated_section= compile_solutions(sampleset_pd,num_notes,POSSIBLE_FREQUENCIES,treble_clef_notes)

    print("section ",i," generated counterpoint section ",generated_section)
    result_verify=verify_generated_counterpoint(generated_section,section_cf)
    
    for el in result_verify:
        print("Verified: ", el)
    generated_counterpoint.extend(generated_section)
    
print(generated_counterpoint)
    

#Edit base_midi with the generated counterpoint notes
base_midi=compose_new_midi(base_midi,generated_counterpoint,fp)    

