#!/usr/bin/env python
# coding: utf-8

# **Second Species Counterpoint Generation Using Quantum Annealing**
# 
# Reference: http://www.music.mcgill.ca/~cmckay/software/musictech/SpciesChecker/Help/rules.html#second

# In[1]:


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
import ipython
import music21
from music21 import *


# In[2]:


get_ipython().run_line_magic('run', 'calculate_interval_music21.ipynb')
get_ipython().run_line_magic('run', 'constraints_from_rules_second_speciesDecember.ipynb')
get_ipython().run_line_magic('run', 'generate_constrained_notes_second_speciesDecember.ipynb')
get_ipython().run_line_magic('run', 'compile_sections.ipynb')
get_ipython().run_line_magic('run', 'verify_second_speciesasDecember.ipynb')
get_ipython().run_line_magic('run', 'compose_new_midi_with_generated_counterpoint_second_species.ipynb')

#Setting up environment is required to invoke Musescore from inside the Python script
#Path given in the second argument is machine specific
environment.set("musescoreDirectPNGPath",  r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe')


# *Define Treble Clef*
# 
# This is required as we have assumed that the counterpoint line is going to be written on Treble Clef.
# We are taking a maximal set of notes from Treble Clef: from A3 to B5.

# In[3]:


treble_clef_notes=[]
treble_clef_start=note.Note('A3')
treble_clef_notes.append(treble_clef_start)

aInterval=interval.Interval(1)

for i in range (1,27):
    aInterval.noteStart=treble_clef_notes[i-1]
    treble_clef_notes.append(aInterval.noteEnd)

POSSIBLE_FREQUENCIES=len(treble_clef_notes)
print("POSSIBLE_FREQUENCIES ",POSSIBLE_FREQUENCIES)


# *Reading the midi*

# In[15]:


mf = midi.MidiFile()

#fp='Second_Species_Counterpoint_Exercise_9notes.mid'
#fp='Second_Species_Counterpoint_another_example_14notes.mid'

fp='Second_Species_Counterpoint_another_example_with_9_notes.mid'
#fp='Second_Species_Counterpoint_New_Example2.mid'
#New_Example2.mid' ## #First_Species_new_example_musescore12.mid'
#fp='First_Species_new.mid' #correct version
#fp='Counterpoint_First_Species_only_three.mid'
mf.open(fp)
mf.read()
mf.close()

file=midi.translate.midiFileToStream(mf)

stream_cp = [] #Place holder for the counterpoint track
stream_cf = [] #Place holder for the c.f. track

stream_cp_frequency = [] #Place holder for the counterpoint track frequencies
stream_cf_frequency = [] #Place holder for the c.f. track frequencies

#Extract the notes of counterpoint and append to array stream_cp. We are assuming the c.p. is above c.f.
for i2 in range(len(file.parts[0].flat.notes)):
    stream_cp.append(file.parts[0].flat.notes[i2].pitch)
    stream_cp_frequency.append(file.parts[0].flat.notes[i2].pitch.frequency)

for i2 in range(len(file.parts[1].flat.notes)):
    stream_cf.append(file.parts[1].flat.notes[i2].pitch)
    stream_cf_frequency.append(file.parts[1].flat.notes[i2].pitch.frequency)

print(stream_cp)
print(stream_cf)

print('pitch: \n')
print(stream_cp_frequency)
print(stream_cf_frequency)

#Get the maximum and minimum frequencies used in c.f.
max_cf=max(stream_cf_frequency)
min_cf=min(stream_cf_frequency)
print(min_cf," ",max_cf)


empty_note_position=list(range(1, 2*len(stream_cf), 2))
print(empty_note_position)
#[1,3,5,7,9,11,13,15,17,19,21,23,25,27] #This is required to make the stream_cf have same no. of notes as c.p.


# *The stream_cf has only half the notes as compared to stream_cp (second species), we will fill the empty note positions in stream_cf by repeting the previous note. This is just to have an easier formulation of constraints. This will not have any effect on the outcome of quantum annealing/QUBO*

# In[16]:


stream_cf2=[] #Placeholder for the modified stream_cf, this will have the same number of notes as c.p.
stream_cf_frequency2 = [] #Placeholder for the modified stream_cf frequencies, this will have the same number of notes as c.p.

j=0
for i in range(len(stream_cp)):
    if(i in empty_note_position):
        stream_cf2.append(stream_cf[j])
        stream_cf_frequency2.append(stream_cf_frequency[j])
        j+=1
        
    else:
        stream_cf2.append(stream_cf[j])
        stream_cf_frequency2.append(stream_cf_frequency[j])

print(stream_cf2)
print(stream_cf)
print(stream_cf_frequency2)    


# *Display the given music sheet from the midi file and play it*

# In[17]:


file.show('mid')


# *This step is required to divide the music into multiple sections. As the rules of counterpoint are applied section wise we will divide the given c.f. into sections. The section breaks have to be fed manually.*

# In[18]:


#section_breaks=[8,17,26,36,46] #[[0, 8],[9,17],[18,26],[27,36],[37,46]]

section_breaks=[21] 
#section_breaks=[12] #  [8,16,24,36,48,60,76,92,108,124] #[[0, 8],[9,17],[18,26],[27,36],[37,46]]
#section_breaks= [7,14,21] #,36,48,60,76,92,108,124]
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
    sectionized_cf.append(stream_cf2[start:end])
    
    sectionized_cp_frequency.append(stream_cp_frequency[start:end])
    sectionized_cf_frequency.append(stream_cf_frequency2[start:end])
    
    
    start=end
    if(i<len(section_breaks)-1):
        end=section_breaks[i+1]
        
for i in range(len(sectionized_cp)):
    print(i)
    print(len(sectionized_cp[i]), sectionized_cp[i],"\n",len(sectionized_cf[i]), sectionized_cf[i],"\n")


# *Define the function to generate the counterpoint*

# In[19]:


def generate_cp_sections(section_cf,section_cf_frequency,treble_clef,num_notes,POSSIBLE_FREQUENCIES):
    
    q = Array.create('q', shape=(num_notes,POSSIBLE_FREQUENCIES), vartype='BINARY')
    w = Array.create('w', shape=(9), vartype='BINARY')
    
    num_notes,Q=generate_constrained_notes_second_species(section_cf,treble_clef_notes,num_notes,q,w,POSSIBLE_FREQUENCIES)
    
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
    
    sample = sampleset.first.sample
    selected_notes = {i:[] for i in range(num_notes)}

    for i in range(num_notes):
        for j in range(POSSIBLE_FREQUENCIES):
            if (sample[f'q[{i}][{j}]']==1):
                selected_notes[i].append(j)
                
    print(selected_notes) #1,selected_notes2)
    
    dec = model.decode_sample(sample, vartype='BINARY')
    pprint(dec.constraints())
    
    
    return selected_notes,sample


# *Call the function to perform QUBO and stitch together the counterpoint generated in each section of c.f.*

# In[21]:


get_ipython().run_line_magic('run', 'calculate_interval_music21.ipynb')
get_ipython().run_line_magic('run', 'constraints_from_rules_second_speciesDecember.ipynb')
get_ipython().run_line_magic('run', 'generate_constrained_notes_second_speciesDecember.ipynb')
get_ipython().run_line_magic('run', 'compile_sections.ipynb')
get_ipython().run_line_magic('run', 'verify_second_speciesasDecember.ipynb')
get_ipython().run_line_magic('run', 'compose_new_midi_with_generated_counterpoint_second_species.ipynb')

generated_counterpoint=[] #Placeholder for the generated counterpoint

for i in range(len(sectionized_cf)):
    section_cp=sectionized_cp[i]
    section_cf=sectionized_cf[i]
    section_cp_frequency=sectionized_cp_frequency[i]
    section_cf_frequency=sectionized_cf_frequency[i]
    print("section ", i)
    #print(section_cf)
    
    num_notes=len(section_cf)
    print("num_notes= ",num_notes)
        
    [selected_notes,sampleset]=generate_cp_sections(section_cf,section_cf_frequency,treble_clef_notes,
                                                    num_notes, POSSIBLE_FREQUENCIES)
    print(selected_notes)
    generated_section=[]
    for key, values in selected_notes.items():
        generated_section.append(treble_clef_notes[selected_notes[key][0]])
        
    print("section ",i," generated counterpoint section ",generated_section)
    
    result_verify=verify_generated_counterpoint(generated_section,section_cf)
    
    for el in result_verify:
        print("Verified: ", el)
    
    generated_counterpoint.extend(generated_section)
    
    
for el in generated_counterpoint:
    print(el.pitch,end=" ")


# *Lets us print what QUBO has generated*

# In[22]:


compose_new_midi_in_second_species(file,generated_counterpoint,fp)


# 

# In[ ]:




