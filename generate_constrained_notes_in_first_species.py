#!/usr/bin/env python
# coding: utf-8


from constraints_from_rules_in_first_species import *
import pyqubo
from pyqubo import Array, Binary,  Constraint, solve_qubo, Mul

def generate_constrained_notes(section_cf,treble_clef_notes,num_notes,q,w,POSSIBLE_FREQUENCIES):
            
    penalties={"vertical_intervals"          :    17,    #P_1,P_2,P_3,P_4,P_5,P_18
               "only_one_outcome"            :    20,    #P_22
               "consecutive_notes_3_6_10"    : 0.001,    #P_6,P_7,P_8
               "big_leap"                    :    12,    #p_9,P_10,P_11,P_12,P_13
               "repeat"                      :   0.1,    #P_14
               "compensate"                  :  0.1,     #P_15
               "arpeggiating"                 : 0.2,     #P_17
               "compensate2"                 : 0.000001, #P_16
               "imperfect"                   : -0.01,    #P_20
               "step_motion"                 :-0.001,    #P_21
               "motion"                      : -0.1,    #P_19

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
        
        
        #Constraint no. 1 Only P1 or P5 intervals in between beginning note
        #Constraint no. 2 Only P1 intervals in between last vertical notes
        #Constraint no. 3 Only consonant intervals in between the vertical notes


        constraint_expression+=constraint_notes_vertical(note_position,penalties["vertical_intervals"],q,
                                                         treble_clef_notes,section_cf)
    
        #Constraint no. 4 No cross over in between voices
        constraint_expression+=constraint_no_crossing(note_position,penalties["vertical_intervals"],q,treble_clef_notes,section_cf,max_cf)
            
        #Constraint no. 5 No cross tritone =='d5' in between voices
        if(note_position>0 and note_position<num_notes-1):
            constraint_expression+=constraint_cross_tritone(note_position,penalties["vertical_intervals"],q,treble_clef_notes,section_cf,num_notes)

        #Constraint no. 9 Entering fifth/
        #Constraint no. 10 Entering octave
        if(note_position>1 and note_position<num_notes-1):
            constraint_expression+=constraint_entering_fifth_or_octave(note_position,penalties["big_leap"],q,treble_clef_notes,section_cf)
        
        #Constraint no. 12 No big leap in consecutive notes of counterpoint\
        #Constraint no. 13 No tritone move in consecutive notes of counterpoint
        if(note_position<num_notes-1):
            constraint_expression+=constraint_big_leap_no_tritone(note_position,penalties["big_leap"],q,treble_clef_notes)
        
        #Constraint no. 19 Motion constraint
        #Constraint no. 20 Imperfect motion
        #Constraint no. 21 Step motion
        if(note_position>0 and note_position<num_notes-1):
            constraint_expression+=constraint_motion(note_position,penalties["motion"],penalties["imperfect"],penalties["step_motion"],
                                                     q,treble_clef_notes,section_cf)


        #Constraint 0- Only one q[:] is 1
        constraint_expression+=constraint_all_notes(penalties["only_one_outcome"],q[note_position])

    print("calculating horizontal rules") 

    #Horizontal Rules
    
    print("calculating consecutive thirds, sixths and tenths...")    
    #Constraint no. 6 No more than three consecutive thirds in between voices
    #Constraint no. 7 No more than three consecutive sixths in between voices
    #Constraint no. 8 No more than three consecutive tenths in between voices

    constraint_expression+=constraint_consecutive_369(penalties["consecutive_notes_3_6_10"],penalties["compensate2"],q,w,treble_clef_notes,section_cf)
    
    
    print("calculating suitable range...")    
    #Constraint no. 11 Suitable Range#
    constraint_expression+=constraint_suitable_range(penalties["big_leap"],q,treble_clef_notes)

    #print("Calculating repeat move...")    
    #Constraint no. 14 No repeat move in consecutive notes of counterpoint
    constraint_expression+=constraint_repeat_moves(penalties["repeat"],q,w,treble_clef_notes)

    print("calculating Compensate Leaps and arpeggiating traids...")    
    #Constraint no. 15 Compensate Leaps
    #Constraint no. 17 Arpeggiating triads
    constraint_expression+=constraint_compensate_leaps_and_arpeggiating_triads(penalties["compensate"],penalties["arpeggiating"],
                                                                               q,w,treble_clef_notes)

    #Constraint no. 16 Compensate Octave Leaps #aleady included in the constraint 369
    #constraint_expression+=constraint_octave_leaps(penalties["compensate2"],q,w,treble_clef_notes)

    #Constraint no. 18 Cadence
    print("calculating cadence") 
    constraint_expression+=constraint_cadence(-2,penalties["vertical_intervals"],q,treble_clef_notes)

    print("calculating qubo")
    Q=Constraint(constraint_expression, label='constraint total')
    
    return num_notes,Q


#        
#      
#         
#         
#         
#             
#         
#         
#         
#         
#         
