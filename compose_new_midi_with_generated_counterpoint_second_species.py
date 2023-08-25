#!/usr/bin/env python
# coding: utf-8

from datetime import datetime,date

def compose_new_midi_in_second_species(base_midi,generated_counterpoint,fp):
    file=base_midi
    for i1 in range(len(file.parts)):
        for i2 in range(len(file.parts[i1].flat.notes)):
            if(i1==0):
                file.parts[i1].flat.notes[i2].pitch=generated_counterpoint[i2].pitch
            
    [fp,_]=fp.split('.')
    print(fp)
    #f'generated\ {fp}_counter_point'
    fp_write = file.write('midi',f'generated\ {fp}_counterpoint' + f'{date.today()}.midi' )
    base_midi.show()
    base_midi.show('mid')
    

