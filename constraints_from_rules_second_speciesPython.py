#!/usr/bin/env python
# coding: utf-8

#Constraint 1: Perfect beginning- Only P1,P8 or P5 vertical interval between beginning notes
#Constraint 2: Perfect ending- Only P1,P8 vertical intervals between last notes
#Constraint 23: Downbeats consonant- Only consonant intervals between the vertical notes 


from calculate_interval_music21 import *
import music21
from music21 import *
    
def constraint_notes_vertical(note_position,pen,q,treble_clef_notes,section_cf):
    penalty_expression=0
    
    valid_interval={
        'start' :            [0,7,12,24],
        'end'   :            [0,12,24],
    }
    
    #imperfect_interval=[3,4,8,9,10,15,16,20,21,22]
    
    for i in range(len(q[note_position])):
        
        possible_note=treble_clef_notes[i]
        
        interval=calculate_interval(section_cf[note_position],possible_note)
        
        if (note_position==0):
            if(interval.semitones in valid_interval['start']) : #'P1' or 'P5'):
                pass
            else:
                penalty_expression+=pen*q[0][i] 
        
        elif (note_position==len(section_cf)-1):
            if(interval.semitones in valid_interval['end']) : #'P1' or interval.simpleName=='P5'):
                pass
            else:
                penalty_expression+=pen*q[-1][i] 
        
        else:
            
            if(note_position%2==0): #downbeat
                if(interval.isConsonant()):
                    pass
                else:
                    penalty_expression+=pen*q[note_position][i]                                 
                            
    return penalty_expression


#Constraint 4: No crossing- No cross over in between voices

def  constraint_no_crossing(note_position,pen,q,treble_clef_notes,section_cf,max_cf):  
    penalty_expression=0
    for i in range(len(q[note_position])):
        
        possible_note=treble_clef_notes[i]
        
        
        interval=calculate_interval(max_cf,possible_note)
        if(interval.semitones>=0):
            pass
        else:
            penalty_expression+=pen*q[note_position][i] 
          
    return penalty_expression
    
#Constraint 5: No cross tritone- No cross tritone =='d5' between voices

def constraint_cross_tritone(note_position,pen,q,treble_clef_notes,section_cf,num_notes):

    penalty_expression=0
    for i in range(len(q[note_position])):
        possible_note=treble_clef_notes[i]
        
        #forward cross note
        interval1=calculate_interval(section_cf[note_position+1],possible_note)
        if(abs(interval1.semitones)==6):
            penalty_expression+=pen*q[note_position][i]
        
    for i in range(len(q[note_position])):
        possible_note=treble_clef_notes[i]
        
        #backward cross note
        if(note_position>0):
            interval2=calculate_interval(section_cf[note_position-1],possible_note)
            if(abs(interval2.semitones)==6):
                  penalty_expression+=pen*q[note_position][i]
           
    return penalty_expression

#Constraint 11: Range- Suitable Range Suitable Range in the notes of counterpoint max-min<=16

def constraint_suitable_range(pen,q,treble_clef_notes):
    penalty_expression=0
    
    for l in range(1,len(q)-1):
        for m in range(1,len(q)-1):
            for j1 in range(len(q[0])):
                for j2 in range(len(q[0])):
                    possible_note1=treble_clef_notes[j1]
                    possible_note2=treble_clef_notes[j2]
                    interval=calculate_interval(possible_note2,possible_note1)
                
                    if(abs(interval.semitones<=16)):
                        pass
                    else:
                        penalty_expression+=pen*q[l][j1]*q[m][j2]
                
    return penalty_expression


#Constraint 14: No repetition of note- No repeat move in consecutive notes of counterpoint 

def constraint_repeat_moves(pen,q,w,treble_clef_notes):
    penalty_expression=0
    for i in range(0,len(q)-1):
        for j1 in range(len(q[i])):
            penalty_expression+=pen* (q[i][j1] * q[i+1][j1])            
        
    #print("no repeat notes ", penalty_expression)
    return penalty_expression


#Constraint 18: Cadence rule- Cadence, Cadence for last note of counterpoint

def constraint_cadence(note_position,pen,q,treble_clef_notes,section_cf):
    
    penalty_expression=0
    
   
    
    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position])):
        
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
        
            interval_melodic=calculate_interval(possible_note1,possible_note2)

            #if(abs(interval_melodic.semitones)==1 or abs(interval_melodic.semitones)==2 or abs(interval_melodic.semitones)==7):
            if(interval_melodic.isStep):
                pass
            else:
                penalty_expression+=pen*q[-2][j1]*q[-2+1][j2]
          
    return penalty_expression 


#Constraint 19: Motion constraint
#Constraint 20: Imperfect intervals
#Constraint 21: Steps preferred over leaps
    
def constraint_motion(note_position,motion,imperfect,step_motion,q,treble_clef_notes,section_cf):
    penalty_expression=0
    
    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position+1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
                        
            interval_cf_cp=calculate_interval(section_cf[note_position],possible_note1)
    
            interval_cp_cp1=calculate_interval(possible_note2,possible_note1)
            
            if(note_position%2==0):
                vl = voiceLeading.VoiceLeadingQuartet(possible_note1, possible_note2, section_cf[note_position], section_cf[note_position+2])
            else:
                vl = voiceLeading.VoiceLeadingQuartet(possible_note1, possible_note2, section_cf[note_position], section_cf[note_position+1])

            
            motion_type=vl.motionType()
            
            if(('Major' in interval_cf_cp.niceName or 'Minor' in interval_cf_cp.niceName) and interval_cf_cp.isConsonant() and
              abs(interval_cf_cp.semitones)<=24):
                pass
            else:
                penalty_expression+=imperfect*q[note_position][j1]*q[note_position+1][j2]                             
            
            #Step motion preferred
            if(abs(interval_cp_cp1.semitones)<=2):
                penalty_expression+=step_motion*q[note_position][j1]*q[note_position+1][j2]        

            #Contrary motion preferred
            if(motion_type=='Contrary'):
                penalty_expression+=3*motion*q[note_position][j1]*q[note_position+1][j2]                
            
            elif(motion_type=='Parallel'):
                penalty_expression-=motion*q[note_position][j1]*q[note_position+1][j2]   
                
            elif(motion_type=='Oblique'):
                penalty_expression-=2*motion*q[note_position][j1]*q[note_position+1][j2]  
                
            elif(motion_type=='Similar'):
                penalty_expression+=motion*q[note_position][j1]*q[note_position+1][j2] 
            else:
                pass
            
            
    return penalty_expression

#Constraint 22: Dissonant leaps- No dissonat leaps and only small leaps 

def constraint_dissonant_leap(note_position,pen,q,treble_clef_notes):
    penalty_expression=0

    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position+1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            interval=calculate_interval(possible_note2,possible_note1)

            #small_semitones=abs(interval.semitones)<=5            
            if((abs(interval.semitones)<=5) and (interval.semitones!=0)):
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position+1][j2]
                            
    return penalty_expression

#Constraint 24: Passing tones- Passing Tones upbeat Passing tones at the up beat notes
        
def constraint_passing_tones(note_position,pen,q,w,treble_clef_notes,section_cf):

    penalty_expression=0
    for i in range(len(q)-3):
        print("constraint_passing tones ",i)
        if(i%2==0):
            continue

        for j1 in range(len(q[i])):
            for j2 in range(len(q[i])):
                if(abs(j1-j2)>16):
                    continue
                for j3 in range(len(q[i])):
                    if(abs(j1-j2)>16 or abs(j1-j3)>16 or abs(j2-j3)>16):
                        continue
                
                    possible_note_previous=treble_clef_notes[j1]
                    possible_note_current=treble_clef_notes[j2]
                    possible_note_next=treble_clef_notes[j3]
    
                    interval_previous_current=calculate_interval(possible_note_previous,possible_note_current)
                    interval_current_next=calculate_interval(possible_note_current,possible_note_next)
                    vertical_interval_current= calculate_interval(section_cf[i],possible_note_current)

                    #Passing tones
                    if(interval_previous_current.isStep):
                        A=True
                    else:
                        A=False
                    if(interval_current_next.isStep):
                        B=True
                    else:
                        B=False
                    if(abs(vertical_interval_current.semitones) in [1,2,6,10,11,13,14,18,22]):
                        C=True
                    else:
                        C=False
                    if(interval_previous_current.semitones*interval_current_next.semitones>0):
                        D=True
                    else:
                        D=False
                    if((not C) or (A and B and D)):
                        E=True
                    else:
                        E=False                 
                    
                    if(E): 
#                 print(interval_previous_current.semitones, " ", C, " A ", interval_previous_current.semitones,
#                       " B ", interval_current_next.semitones, " ", D ," ",E)

                        pass
                    else:
                        penalty_expression+=pen* (q[i-1][j1] * q[i][j2] + q[i-1][j1] *q[i+1][j3] + q[i][j2]* q[i+1][j3] 
                                                  +w[7]*(- q[i-1][j1]- q[i][j2] - q[i+1][j3] +1 ))
                
    return penalty_expression

#Constraint 25: Approaching perfect intervals at downbea- A perfect consonance on the downbeat must not be approached in similar motion. 
    
def constraint_downbeat_similar(note_position,motion,q,treble_clef_notes,section_cf):
    penalty_expression=0

    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position-1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            
            interval_previous_cp=calculate_interval(possible_note2,possible_note1)
            interval_previous_cf=calculate_interval(section_cf[note_position-1],section_cf[note_position])
            
            interval_vertical=calculate_interval(section_cf[note_position],possible_note1)
    
            vl = voiceLeading.VoiceLeadingQuartet(possible_note2, possible_note1, section_cf[note_position-1], section_cf[note_position])
            
            motion_type=vl.motionType()
            
            A= 'Perfect' in interval_vertical.niceName
            #print(interval_vertical.niceName)
            
            if(not A or (motion_type!='Similar')):
                pass
            else:
                penalty_expression+=2*motion*q[note_position][j1]*q[note_position-1][j2]   
    return penalty_expression


#Constraint 26: Avoid same perfect consonance at the downbeat- Consecutive bars must not have perfect consonances of the same numerical name on the downbeat:

def constraint_downbeat_consecutive(note_position,pen,q,treble_clef_notes,section_cf):
    penalty_expression=0
    
    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position-2])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            
            interval_vertical=calculate_interval(section_cf[note_position],possible_note1)
            interval_vertical2=calculate_interval(section_cf[note_position-2],possible_note2)
            
            A= 'Perfect Fifth' in interval_vertical2.name or 'Perfect Octave' in interval_vertical2.name
            B= 'Perfect Fourth' in interval_vertical.name
            
            #C= interval_vertical.directedNiceName!=interval_vertical2.directedNiceName

            if(not (A) or B):
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position-2][j2]                
            
            
    return penalty_expression    


#Constraint 27: Avoid augmented /diminished notes unless there is augmented/diminished note in the c.f 

def constraint_aug_dim(note_position,pen,q,treble_clef_notes,section_cf):
    penalty_expression=0

    for j in range(len(q[note_position])):
        possible_note1=treble_clef_notes[j]
            
        if(('-' in str(possible_note1.pitch) or '#' in str(possible_note1.pitch)) and
          ('-' not in str(section_cf[note_position]) and '#' not in str(section_cf[note_position]))):
            penalty_expression+=pen*q[note_position][j]
            #print("aug dim",str(possible_note1.pitch)," ",section_cf[note_position])
        else:
            pass
                  
    return penalty_expression
    
#Constraint 0: Only one note at a position-Only one q[:] is 1

def constraint_all_notes(pen_all,q_note_position):
    penalty_expression=0
    sum_of_qi=0
    for i in q_note_position:
        sum_of_qi+=i

    penalty_expression=pen_all*(sum_of_qi-1)**2
    #print(penalty_expression)
    return penalty_expression

