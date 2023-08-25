#!/usr/bin/env python
# coding: utf-8


from calculate_interval_music21 import *
import music21
from music21 import *

#Constraint No. 1 for first note of counterpoint
#Constraint No. 2 for last note of counterpoint
#Constraint No. 3 for middle note of counterpoint


def constraint_notes_vertical(note_position,pen,q,treble_clef_notes,section_cf):
    penalty_expression=0
    
    valid_interval={
        'start' :          [0,7,12,24],
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
            if(interval.isConsonant() and not('Octave' in interval.niceName) ):
                pass
            else:
                penalty_expression+=pen*q[note_position][i]   
                
    return penalty_expression
    


#Constraint Nno. 4 contraint on no crossing over of voices

def  constraint_no_crossing(note_position,pen,q,treble_clef_notes,section_cf,max_cf):  
    penalty_expression=0
    for i in range(len(q[note_position])):
        
        possible_note=treble_clef_notes[i]
        
        
        interval=calculate_interval(max_cf,possible_note)
        if(interval.semitones>0):
            pass
        else:
            penalty_expression+=pen*q[note_position][i] 
          
    return penalty_expression
    


#Constraint No. 5 No cross tritone

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
           
        
        
    #print(penalty_expression,"ex")
    return penalty_expression


#Constraint No. 6 No more than three consecutive thirds
#Constraint No. 7 No more than three consecutive sixths
#Constraint No. 8 No more than three consecutive tenths


def constraint_consecutive_369(pen,octave, q,w,treble_clef_notes,section_cf):
    
    
    penalty_expression=0
    for i in range(len(q)-3):
        print("constraint_consecutive_369 ",i)

        for j1 in range(len(q[i])):
            for j2 in range(len(q[i])):
                if(abs(j1-j2)>16):
                    continue
                for j3 in range(len(q[i])):
                    if(abs(j1-j2)>16 or abs(j1-j3)>16 or abs(j2-j3)>16):
                        continue
                
                    for j4 in range(len(q[i])):
                        if(abs(j1-j2)>16 or abs(j1-j3)>16 or abs(j1-j4)>16 or abs(j2-j3)>16 or abs(j2-j4)>16 or abs(j3-j4)>16):
                            continue
        
                        possible_note1=treble_clef_notes[j1]
                        possible_note2=treble_clef_notes[j2]
                        possible_note3=treble_clef_notes[j3]
                        possible_note4=treble_clef_notes[j4]

            
                        interval0=calculate_interval(section_cf[i],possible_note1)
                        interval1=calculate_interval(section_cf[i+1],possible_note2)
                        interval2=calculate_interval(section_cf[i+2],possible_note3)
                        interval3=calculate_interval(section_cf[i+3],possible_note4)



                        if((abs(interval0.semitones)==3 or abs(interval0.semitones)==4) and
                           (abs(interval1.semitones)==3 or abs(interval1.semitones)==4) and 
                           (abs(interval2.semitones)==3 or abs(interval2.semitones)==4) and 
                           (abs(interval3.semitones)==3 or abs(interval3.semitones)==4)):
                            
                            penalty_expression+=pen*(q[i][j1]*q[i+1][j2] + q[i][j1]*q[i+2][j3] + q[i][j1]*q[i+3][j4] +
                                                     q[i+1][j2]*q[i+2][j3] + q[i+1][j2]*q[i+3][j4] + q[i+2][j3]*q[i+3][j4] +
                                                     w[0]*(-2*q[i][j1] -2*q[i+1][j2] -2*q[i+2][j3] -2*q[i+3][j4] + 3))
                            
                        #penalty_expression+=pen*(q[i][j1]*q[i+1][j2]*q[i+2][j3])

                        else:
                            pass
                        
                        if((abs(interval0.semitones)==8 or abs(interval0.semitones)==9) and
                           (abs(interval1.semitones)==8 or abs(interval1.semitones)==9) and 
                           (abs(interval2.semitones)==8 or abs(interval2.semitones)==9) and 
                           (abs(interval3.semitones)==8 or abs(interval3.semitones)==9)):
                            
                            penalty_expression+=pen*(q[i][j1]*q[i+1][j2] + q[i][j1]*q[i+2][j3] + q[i][j1]*q[i+3][j4] +
                                                     q[i+1][j2]*q[i+2][j3] + q[i+1][j2]*q[i+3][j4] + q[i+2][j3]*q[i+3][j4] +
                                                     w[1]*(-2*q[i][j1] -2*q[i+1][j2] -2*q[i+2][j3] -2*q[i+3][j4] + 3))
                            
                        else:
                            pass
                        
                        if((abs(interval0.semitones)==15 or abs(interval0.semitones)==16) and
                           (abs(interval1.semitones)==15 or abs(interval1.semitones)==16) and 
                           (abs(interval2.semitones)==15 or abs(interval2.semitones)==16) and 
                           (abs(interval3.semitones)==15 or abs(interval3.semitones)==16)):
                            
                            penalty_expression+=pen*(q[i][j1]*q[i+1][j2] + q[i][j1]*q[i+2][j3] + q[i][j1]*q[i+3][j4] +
                                                     q[i+1][j2]*q[i+2][j3] + q[i+1][j2]*q[i+3][j4] + q[i+2][j3]*q[i+3][j4] +
                                                     w[2]*(-2*q[i][j1] -2*q[i+1][j2] -2*q[i+2][j3] -2*q[i+3][j4] + 3))
                            
                        else:
                            pass
                        
                        
                #Constraint No. 15 Compensate Octave leaps
                # Apply ~a or b == P*(~a.b) in QUBO

                        interval1_2=calculate_interval(possible_note2,possible_note1)
                        interval2_3=calculate_interval(possible_note3,possible_note2)
                        interval1_3=calculate_interval(possible_note3,possible_note1)
                        interval2_4=calculate_interval(possible_note2,possible_note4)
                        interval3_4=calculate_interval(possible_note3,possible_note4)                            
                            
                        A= abs(interval2_3.semitones)==12
                        B= (abs(interval1_2.semitones)<12 and abs(interval1_3.semitones)<12 and 
                            abs(interval2_4.semitones)<12 and abs(interval3_4.semitones)<12)
                        
                        if((not A) or B): 
                            pass
                        else:     
                            penalty_expression+=octave*(q[i][j1]*q[i+1][j2] + q[i][j1]*q[i+2][j3] + q[i][j1]*q[i+3][j4] +
                                                     q[i+1][j2]*q[i+2][j3] + q[i+1][j2]*q[i+3][j4] + q[i+2][j3]*q[i+3][j4] +
                                                     w[6]*(-2*q[i][j1] -2*q[i+1][j2] -2*q[i+2][j3] -2*q[i+3][j4] + 3))
                            
                            ##                         x1x2 +x1x3+ x1x4 + x2x3 + x2x4 + x3x4 + w(-2 (x1+x2+x3+x4) +3)


                    
                                        
    #print("thirds ", penalty_expression)
    return penalty_expression


#Constraint No. 9 Entering fifth
#Constraint No. 10 Entering octave
        
def constraint_entering_fifth_or_octave(note_position,pen,q,treble_clef_notes,section_cf):

    penalty_expression=0

    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position-1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            
            interval_cf_cp=calculate_interval(section_cf[note_position],possible_note1)
            interval_cp1_cp=calculate_interval(possible_note1,possible_note2)
            interval_cf1_cf=calculate_interval(section_cf[note_position],section_cf[note_position-1])
            interval_cf1_cp1=calculate_interval(section_cf[note_position-1],possible_note2)

            A= abs(interval_cf_cp.semitones)==12
            B1= interval_cp1_cp.semitones*interval_cf1_cf.semitones<0
            B2= abs(interval_cp1_cp.semitones) <=2 
            B3= abs(interval_cf1_cf.semitones) <=2 
            B4= interval_cp1_cp.semitones*interval_cf1_cf.semitones==0
            B5= interval_cf1_cp1.semitones!=12


            if(~A or ((B1 and B2 and B3) or (B4 and B5))): 
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position-1][j2]
                
            A= abs(interval_cf_cp.semitones)==7
            B5= interval_cf1_cp1.semitones!=7

            if(~A or ((B1 and B2 and B3) or (B4 and B5))): 
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position-1][j2]
            
    
    return penalty_expression



#Constraint No. 11 Suitable Range in the notes of counterpoint max-min<=16

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
    


#Constraint No. 12 No big leap in consecutive notes of the couterpoint
#Constraint No. 13 No tritone move in consecutive notes of the couterpoint 

def constraint_big_leap_no_tritone(note_position,pen,q,treble_clef_notes):
    penalty_expression=0

    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position+1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            interval=calculate_interval(possible_note2,possible_note1)
                
            if(abs(interval.semitones)<=7 or abs(interval.semitones)==12 or interval.semitones==-8): 
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position+1][j2]
                
            if(abs(interval.semitones)!=6):
                pass
            else:
                penalty_expression+=pen*q[note_position][j1]*q[note_position+1][j2]
                        
    
    
    return penalty_expression



#Constraint No. 14 No repeat move in consecutive notes of the couterpoint

def constraint_repeat_moves(pen,q,w,treble_clef_notes):
    penalty_expression=0
    for i in range(1,len(q)-2):
        for j1 in range(len(q[i])):
            #penalty_expression+=pen*(q[i][j1]*q[i+1][j1]*q[i+2][j1])
            penalty_expression+=pen* (q[i][j1] * q[i+1][j1] + q[i][j1] *q[i+2][j1] + q[i+1][j1]* q[i+2][j1] 
                                          +w[3]*(- q[i][j1]- q[i+1][j1] - q[i+2][j1] +1 ))
            
        
    #print("no repeat notes ", penalty_expression)
    return penalty_expression


#Constraint No. 15 Compensate leaps
#Constraint No. 17 Arpeggiating triads
# Apply ~a or b == P*(~a.b) in QUBO

import itertools

def constraint_compensate_leaps_and_arpeggiating_triads(pen,arpeggiating,q,w,treble_clef_notes):
    
    penalty_expression=0
    for i in range(0,len(q)-2):
        print("compensate leaps ", i)       
        for j1,j2,j3 in itertools.product(range(len(q[i])),range(len(q[i])),range(len(q[i]))):
            if(abs(j1-j2)>16):
                continue
            if(abs(j1-j2)>16 or abs(j2-j3)>16 or abs(j1-j3)>16):
                continue                
            if(i==6):
                pass
                #print("J1 ",j1,"j2 ",j2,"j3 ",j3)

            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            possible_note3=treble_clef_notes[j3]

     
            interval1=calculate_interval(possible_note2,possible_note1)
            interval2=calculate_interval(possible_note2,possible_note3)
            
            A=interval1.semitones>=7
            B=interval2.semitones>0

            if(~ A or B):
                pass
            elif(A or (~B and abs(interval2.semitones)<=2)):
                pass
            else:
                penalty_expression+=pen* (q[i][j1] * q[i+1][j2] + q[i][j1] *q[i+2][j3] + q[i+1][j2]* q[i+2][j3] 
                                          +w[4]*(- q[i][j1]- q[i+1][j2] - q[i+2][j3] +1 ))
                
                             
            #Constraint No. 17 arpeggiating triads # Apply ~a or b == P*(~a.b) in QUBO
            interval1_2=calculate_interval(possible_note2,possible_note1)
            interval2_3=calculate_interval(possible_note3,possible_note2)
                        
            A= (abs(interval1_2.semitones)>2) and (abs(interval2_3.semitones)>2) and (interval1_2.semitones*interval2_3.semitones>0)                    
            B= abs(interval1_2.semitones) <=4 and abs(interval2_3.semitones)<=4
                            
            if((not A) or B):
                pass
            else:
                penalty_expression+=arpeggiating* (q[i][j1] * q[i+1][j2] + q[i][j1] *q[i+2][j3] + q[i+1][j2]* q[i+2][j3] 
                                                   +w[5]*(- q[i][j1]- q[i+1][j2] - q[i+2][j3] +1 ))
                
    return penalty_expression




#Constraint No. 16 Compensate Octave leaps
# Apply ~a or b == P*(~a.b) in QUBO

def constraint_octave_leaps(pen,q,w,treble_clef_notes):
    
    penalty_expression=0
    for i in range(0,len(q)-3):
        print("compensate octave leaps ", i)
        for j1 in range(len(q[i])):
            for j2 in range(len(q[i])):
                if(abs(j1-j2)>16):
                    continue
                for j3 in range(len(q[i])):
                    if(abs(j1-j2)>16 or abs(j1-j3)>16 or abs(j2-j3)>16):
                        continue
                
                    for j4 in range(len(q[i])):
                        if(abs(j1-j2)>16 or abs(j1-j3)>16 or abs(j1-j4)>16 or abs(j2-j3)>16 or abs(j2-j4)>16 or abs(j3-j4)>16):
                            continue
                
#                         if(i==5 and j1==26):
#                             print("J1 ",j1,"j2 ",j2,"j3 ",j3,'j4',j4)

                        possible_note1=treble_clef_notes[j1]   #i-1
                        possible_note2=treble_clef_notes[j2]   #i
                        possible_note3=treble_clef_notes[j3]   #i+1
                        possible_note4=treble_clef_notes[j4]   #i+2

                            
                        interval1_2=calculate_interval(possible_note2,possible_note1)
                        interval2_3=calculate_interval(possible_note3,possible_note2)
                        interval1_3=calculate_interval(possible_note3,possible_note1)
                        interval2_4=calculate_interval(possible_note2,possible_note4)
                        interval3_4=calculate_interval(possible_note3,possible_note4)                            
                            
                        A= abs(interval2_3.semitones)==12
                        B= (abs(interval1_2.semitones)<12 and abs(interval1_3.semitones)<12 and 
                            abs(interval2_4.semitones)<12 and abs(interval3_4.semitones)<12)
                        
                        if((not A) or B): 
                            pass
                        else:     
                            penalty_expression+=pen*(q[i][j1]*q[i+1][j2] + q[i][j1]*q[i+2][j3] + q[i][j1]*q[i+3][j4] +
                                                     q[i+1][j2]*q[i+2][j3] + q[i+1][j2]*q[i+3][j4] + q[i+2][j3]*q[i+3][j4] +
                                                     w[6]*(-2*q[i][j1] -2*q[i+1][j2] -2*q[i+2][j3] -2*q[i+3][j4] + 3))
                            
                            ##                         x1x2 +x1x3+ x1x4 + x2x3 + x2x4 + x3x4 + w(-2 (x1+x2+x3+x4) +3)


                            
                            #penalty_expression+=pen*(q[i][j1]+q[i+1][j2]+q[i+2][j3]+q[i+3][j4]-3)
        
    #print("contraint octave leaps ", penalty_expression)
    return penalty_expression



#Constraint No. 18 Cadence for last note of counterpoint

def constraint_cadence(note_position,pen,q,treble_clef_notes):
    penalty_expression=0
    
    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            interval=calculate_interval(possible_note2,possible_note1)
                
            if(abs(interval.semitones) == 1 or abs(interval.semitones) == 2 or abs(interval.semitones) == 7 ):
                pass
            else:
                penalty_expression+=pen*q[note_position][j2]*q[note_position+1][j1]
          
    return penalty_expression
    


#Constraint No. 19,20,21 Motion Rules maximize the  Imperfects+Steps 3*Contraray + Similar- 2*Parallel - Oblique 
#Prefer Imperfect Consonances
#Prefer step wise motion in counterpoint

    
def constraint_motion(note_position,motion,imperfect,step_motion,q,treble_clef_notes,section_cf):
    penalty_expression=0

    for j1 in range(len(q[note_position])):
        for j2 in range(len(q[note_position+1])):
            possible_note1=treble_clef_notes[j1]
            possible_note2=treble_clef_notes[j2]
            
#             interval1=calculate_interval(possible_note1,possible_note2)
#             interval2=calculate_interval(section_cf[note_position],section_cf[note_position+1])
            
            interval_cf_cp=calculate_interval(section_cf[note_position],possible_note1)
    
            interval_cp_cp1=calculate_interval(possible_note2,possible_note1)
                
            vl = voiceLeading.VoiceLeadingQuartet(possible_note1, possible_note2, section_cf[note_position], section_cf[note_position+1])
            motion_type=vl.motionType()
            
            if(('Major' in interval_cf_cp.niceName or 'Minor' in interval_cf_cp.niceName) and interval_cf_cp.isConsonant() and
              abs(interval_cf_cp.semitones)<=24):
                penalty_expression+=imperfect*q[note_position][j1]  
            else:
                pass
                
            if(interval_cp_cp1.isStep):
                penalty_expression+=step_motion*q[note_position][j1]*q[note_position+1][j2]            

            if(motion_type=='Contrary'):
                penalty_expression+=3*motion*q[note_position][j1]*q[note_position+1][j2]                
            
            elif(motion_type=='Parallel'):
                penalty_expression-=2*motion*q[note_position][j1]*q[note_position+1][j2]   
                
            elif(motion_type=='Oblique'):
                penalty_expression-=motion*q[note_position][j1]*q[note_position+1][j2]  
                
            elif(motion_type=='Similar'):
                penalty_expression+=motion*q[note_position][j1]*q[note_position+1][j2] 
            else:
                pass
            
            
    return penalty_expression


#Constraint No. 0

def constraint_all_notes(pen_all,q_note_position):
    penalty_expression=pen_all*(sum(q_note_position)-1)**2
    #print(penalty_expression)
    return penalty_expression

