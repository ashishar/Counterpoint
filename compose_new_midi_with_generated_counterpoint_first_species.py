#!/usr/bin/env python
# coding: utf-8



from datetime import datetime,date

def compose_new_midi(base_midi,generated_counterpoint,fp):
    
    i=0
    for given_note in base_midi.parts[0].notes:
    #print(given_note.pitch, " ",generated_counterpoint[i].pitch, end='\n')
        given_note.pitch= generated_counterpoint[i].pitch
        if(given_note.pitch!=generated_counterpoint[i].pitch):
            print('error')
        i+=1
    
    [fp,_]=fp.split('.')

    #f'generated\ {fp}_counter_point'
    fp_write = base_midi.write('midi',f'generated\ {fp}_counterpoint' + f'{date.today()}.midi' )
    #base_midi.show()
    base_midi.show('mid')
      
    return base_midi

