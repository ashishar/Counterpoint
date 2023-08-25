#!/usr/bin/env python
# coding: utf-8
from constraints_from_rules_second_speciesPython import *


import pyqubo
from pyqubo import Array, Binary,  Constraint, solve_qubo, Mul


def generate_constrained_notes_second_species(section_cf,treble_clef_notes,num_notes,q,w,POSSIBLE_FREQUENCIES):
       
    penalties={"vertical_intervals"          :    30,     #P_1,P_2,P_23,P_4,P_5,P_18
               "only_one_outcome"            :    30,     #P_0
               "range"                       :     2,     #P_11
               "repeat"                      :    15,     #P_14
               "motion"                      :    -3,     #P_19,P_25,     
               "imperfect"                   :   0.1,     #P_20
               "step_motion"                 :    -6,     #P_21
               "dissonant_leap"              :    30,     #P_22
               "passing_tones"               :     1,     #P_24
               "down_consec"                 :  0.00001,  #P_26
               "aug_dim"                     :     15,     #P_27
              }
    
        
    #Maximum frequency of the cantus firmus
    max_cf=max(section_cf, key=lambda x: x.frequency)
    max_cf_index=section_cf.index(max_cf)
    print("max cf ",max_cf, 'index ',max_cf_index)


    #Create constraints
    constraint_expression=0
    
    #Vertical Rules
    for note_position in range(num_notes):
        print("calculating note ",note_position)
        
        
        #Constraint 1: Perfect beginning- Only P1,P8 or P5 vertical interval between beginning notes
        #Constraint 2: Perfect ending- Only P1,P8 vertical intervals between last notes
        #Constraint 23: Downbeats consonant- Only consonant intervals between the vertical notes 
        
        constraint_expression+=constraint_notes_vertical(note_position,penalties["vertical_intervals"],q,
                                                         treble_clef_notes,section_cf)
        
        #Constraint 4: No crossing- No cross over in between voices
        constraint_expression+=constraint_no_crossing(note_position,penalties["vertical_intervals"],q,
                                                      treble_clef_notes,section_cf,max_cf)
            
        #Constraint 5: No cross tritone- No cross tritone =='d5' between voices
        if(note_position>0 and note_position<num_notes-1):
            constraint_expression+=constraint_cross_tritone(note_position,penalties["vertical_intervals"],
                                                            q,treble_clef_notes,section_cf,num_notes)
                
        #Constraint 19: Motion constraint
        #Constraint 20: Imperfect intervals
        #Constraint 21: Steps preferred over leaps
        if(note_position>=0 and note_position<num_notes-1):
            constraint_expression+=constraint_motion(note_position,penalties["motion"],penalties["imperfect"],
                                                     penalties["step_motion"], q,treble_clef_notes,section_cf)

        #Constraint 22: Dissonant leaps- No dissonat leaps and only small leaps
        if(note_position<num_notes-1):
            constraint_expression+=constraint_dissonant_leap(note_position,penalties["dissonant_leap"],q,treble_clef_notes)

        #Constraint 25: Approaching perfect intervals at downbea- A perfect consonance on the downbeat must not be approached in similar motion. 
        if(note_position>=3 and note_position<num_notes-2 and note_position%2==1):
            constraint_expression+=constraint_downbeat_similar(note_position,penalties["motion"],q,treble_clef_notes,section_cf)
            
        #Constraint 26: Avoid same perfect consonance at the downbeat- Consecutive bars must not have perfect consonances of the same numerical name on the downbeat:
        if(note_position>=1 and note_position<num_notes-2 and note_position%2==1):
            constraint_expression+=constraint_downbeat_consecutive(note_position,penalties["down_consec"],q,treble_clef_notes,section_cf)
            
            
        #Constraint 27: Avoid augmented /diminished notes unless there is augmented/diminished note in the c.f 
        if(note_position<=num_notes):
            constraint_expression+=constraint_aug_dim(note_position,penalties["aug_dim"],q,treble_clef_notes,section_cf)
    
        #Constraint 0: Only one note at a position-Only one q[:] is 1
        constraint_expression+=constraint_all_notes(penalties["only_one_outcome"],q[note_position])

    print("calculating horizontal constraints") 

    #Horizontal Rules
    
    print("calculating suitable range...")    
    #Constraint 11: Range- Suitable Range
    constraint_expression+=constraint_suitable_range(penalties["range"],q,treble_clef_notes)
    
    print("Calculating repeat move...")    
    #Constraint 14: No repetition of note- No repeat move in consecutive notes of counterpoint
    constraint_expression+=constraint_repeat_moves(penalties["repeat"],q,w,treble_clef_notes)
    
    #print("calculating Compensate Leaps and arpeggiating traids...")    
    
    #Constraint 18: Cadence rule- Cadence
    print("calculating cadence") 
    constraint_expression+=constraint_cadence(-2,penalties["vertical_intervals"],q,treble_clef_notes,section_cf)
        
    #Constraint 24: Passing tones- Passing Tones upbeat
    print("calculating passing tones...")    
    constraint_expression+=constraint_passing_tones(note_position,penalties["passing_tones"],q,w,treble_clef_notes,section_cf)


    print("calculating qubo")
    Q=Constraint(constraint_expression, label='constraint total')
    
    return num_notes,constraint_expression

#========================        
