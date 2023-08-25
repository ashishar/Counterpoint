#!/usr/bin/env python
# coding: utf-8
from calculate_interval_music21 import *


def verify_generated_counterpoint(generated_section,section_cf):
    constraints_violated=[]
    
    rule0_result=verify_rule0(generated_section,section_cf)
    
    if rule0_result==True:
        constraints_violated.append(f'Rule0 number of notes are same {rule0_result}')

    else:
        if rule0_result>0:
            return constraints_violated.append(f'Rule0 number of notes in generated section are more {rule0_result}')
        
        if rule0_result<0:
            return constraints_violated.append(f'Rule0 number of notes in generated section are les {rule0_result}')
    
    
    rule1_result=verify_rule1(generated_section,section_cf)
    
    if rule1_result==True:
        constraints_violated.append(f'Rule1 Beginning note {rule1_result}')
        

    else:
        constraints_violated.append(f'Rule1 Beginning note Violated {rule1_result}')
    
    
    rule2_result=verify_rule2(generated_section,section_cf)
    
    if rule2_result==True:
        constraints_violated.append(f'Rule2 Last note {rule2_result}')

    else:
        constraints_violated.append(f'Rule2 Last note Violated {rule2_result}')
    
    rule3_result=verify_rule3(generated_section,section_cf)
    
    if rule3_result==True:
        constraints_violated.append(f'Rule3 Middle notes {rule3_result}')

    else:
        constraints_violated.append(f'Rule3 Middle note Violated {rule3_result}')
    
    rule4_result=verify_rule4(generated_section,section_cf)
    
    if rule4_result==True:
        constraints_violated.append(f'Rule4 No crossing notes {rule4_result}')

    else:
        constraints_violated.append(f'Rule4 No crossing of the notes Violated , not required if both track are on same clef{rule4_result}')
    
    rule5_result=verify_rule5(generated_section,section_cf)
    
    if rule5_result==True:
        constraints_violated.append(f'Rule5 No cross tritone notes {rule5_result}')

    else:
        constraints_violated.append(f'Rule5 No cross tritone notes Violated {rule5_result}')
       
    rule6_result=verify_rule6(generated_section,section_cf)
    
    if rule6_result==True:
        constraints_violated.append(f'Rule6 No more than three consec. thirds Automatic satisfied {rule6_result}')

    else:
        constraints_violated.append(f'Rule6 No more than three consec. thirds Violated Not required {rule6_result}')
    
    rule7_result=verify_rule7(generated_section,section_cf)
    
    if rule7_result==True:
        constraints_violated.append(f'Rule7 No more than three consec. sixths, Automatic satisfied {rule7_result}')

    else:
        constraints_violated.append(f'Rule7 No more than three consec. sixths, Violated {rule7_result}')
    
    rule8_result=verify_rule8(generated_section,section_cf)
    
    if rule8_result==True:
        constraints_violated.append(f'Rule8 No more than three consec. tenths, Automatic satisfied {rule8_result}')

    else:
        constraints_violated.append(f'Rule8 No more than three consec. tenths, Violated, Not required {rule8_result}')
    
    rule9_result=verify_rule9(generated_section,section_cf)

    if rule9_result==True:
        constraints_violated.append(f'Rule9 No violation of entering fifth, Automatic satisfied {rule9_result}')

    else:
        constraints_violated.append(f'Rule9 Violation of entering fifth, Not required {rule9_result}')
    
    rule10_result=verify_rule10(generated_section,section_cf)

    if rule10_result==True:
        constraints_violated.append(f'Rule10 No violation of entering Octave, Automatic satisfied{rule10_result}')

    else:
        constraints_violated.append(f'Rule10 Violation of entering Octave, Not required {rule10_result}')
    
    rule11_result=verify_rule11(generated_section)
    
    if rule11_result==True:
        constraints_violated.append(f'Rule11 Suitable Range {rule11_result}')

    else:
        constraints_violated.append(f'Rule11 Suiatble Range Violated {rule11_result}')
        
    rule12_result=verify_rule12(generated_section)
    
    if rule12_result==True:
        constraints_violated.append(f'Rule12 No big leap, Automatic satisfied {rule12_result}')

    else:
        constraints_violated.append(f'Rule12 No big leap Violated, Not required {rule12_result}')
    
    rule13_result=verify_rule13(generated_section)
    
    if rule13_result==True:
        constraints_violated.append(f'Rule13 No tritone moves, Automatic satisfied{rule13_result}')

    else:
        constraints_violated.append(f'Rule13 No tritone moves is Violated, Not required {rule13_result}')

    rule14_result=verify_rule14(generated_section)
    
    if rule14_result==True:
        constraints_violated.append(f'Rule14 No repeat moves {rule14_result}')

    else:
        constraints_violated.append(f'Rule14 No repeat moves is Violated {rule14_result}')
        
    rule15_result=verify_rule15(generated_section)
    
    if rule15_result==True:
        constraints_violated.append(f'Rule15 Compensate leaps, Automatic satisfied {rule15_result}')

    else:
        constraints_violated.append(f'Rule15 Compensate leaps Violated, Not required {rule15_result}')
    
       
    rule16_result=verify_rule16(generated_section)
    
    if rule16_result==True:
        constraints_violated.append(f'Rule16 Compensate Octave leaps, Automatic satisfied {rule16_result}')

    else:
        constraints_violated.append(f'Rule16 Compensate Octave leaps has been Violated, not required {rule16_result}')
    
    rule17_result=verify_rule17(generated_section)
    
    if rule17_result==True:
        constraints_violated.append(f'Rule17 Arpeggiating Triads, Automatic satisfied {rule17_result}')

    else:
        constraints_violated.append(f'Rule17 Arpeggiating Triads has been Violated, not required {rule17_result}')
        
    rule18_result=verify_rule18(generated_section,section_cf)
    
    if rule18_result==True:
        constraints_violated.append(f'Rule18 Cadence last note {rule18_result}')

    else:
        constraints_violated.append(f'Rule18 Cadence last note is Violated {rule18_result}')
        
    rule192021_result=verify_rule192021(generated_section,section_cf)
    
    if rule192021_result==True:
        constraints_violated.append(f'Rule19 Rule 20 Rule 21 on Motion Rule {rule192021_result}')

    else:
        constraints_violated.append(f'Rule19 Rule 20 Rule 21 on Motion violated {rule192021_result}')

    rule22_result=verify_rule22(generated_section)
    
    if rule22_result==True:
        constraints_violated.append(f'Rule22 No dissonant leap {rule22_result}')

    else:
        constraints_violated.append(f'Rule22 No dissonant leap is Violated {rule22_result}')
    
    rule23_result=verify_rule23(generated_section,section_cf)
    
    if rule23_result==True:
        constraints_violated.append(f'Rule23 Downbeats consonants {rule23_result}')

    else:
        constraints_violated.append(f'Rule23 Downbeats only consonants is Violated {rule23_result}')
        
    rule24_result=verify_rule24(generated_section,section_cf)
    
    if rule24_result==True:
        constraints_violated.append(f'Rule24 Passing tones {rule24_result}')

    else:
        constraints_violated.append(f'Rule24 Passing tones violated {rule24_result}')

    rule25_result=verify_rule25(generated_section,section_cf)
    
    if rule25_result==True:
        constraints_violated.append(f'Rule25 Approach perfect interval at downbeat {rule25_result}')

    else:
        constraints_violated.append(f'Rule25 Approach perfect interval at downbeat violated {rule25_result}')
        
    rule26_result=verify_rule26(generated_section,section_cf)
    
    if rule26_result==True:
        constraints_violated.append(f'Rule26 Downbeat Pefect with same name avoided {rule26_result}')

    else:
        constraints_violated.append(f'Rule26 Downbeat Pefect with same name violated {rule26_result}')

    rule27_result=verify_rule27(generated_section,section_cf)
    
    if rule27_result==True:
        constraints_violated.append(f'Rule27 Avoid Augmented/Diminshed is fulfilled {rule27_result}')

    else:
        constraints_violated.append(f'Rule27 Avoid Augmented/Diminshed is violated {rule27_result}')

       
    return constraints_violated

    
def verify_rule0(generated_section,section_cf):
    
    diff_length=len(generated_section)- len(section_cf)
    if(diff_length==0):
        return True 
    else:
        return diff_length 

def verify_rule1(generated_section,section_cf):
    valid_interval={
        'start' :          [0,7,12,24],
    }
    
    interval=calculate_interval(section_cf[0],generated_section[0])
    print("Rule 1 ",interval.name)
    if(interval.semitones in valid_interval['start']):
        return True 
    else:
        return interval 


def verify_rule2(generated_section,section_cf):
    valid_interval={
        'end' :          [0,12,24],
    }
    
    
    interval=calculate_interval(section_cf[-1],generated_section[-1])
    print("Rule 2 ",interval.name)

    if(interval.semitones in valid_interval['end']):
        return True 
    else:
        return interval 


def verify_rule3(generated_section,section_cf):
    intervals=[]

    for i in range(len(generated_section)-2):
        interval=calculate_interval(section_cf[i],generated_section[i])
        
        if(i%2==0):
            if(interval.isConsonant()):
                intervals.append(True)
            else:
                intervals.append(f'{i }'+ interval.name+" ") 
        
        if(i%2==1):
            if(interval.isConsonant()):
                intervals.append(True)
            else:
                
                possible_note_previous=generated_section[i-1]
                possible_note_current=generated_section[i]
                possible_note_next=generated_section[i+1]

                interval_previous_current=calculate_interval(possible_note_previous,possible_note_current)
                interval_current_next=calculate_interval(possible_note_current,possible_note_next)
                vertical_interval_current= calculate_interval(section_cf[i],possible_note_current)


                if(interval_previous_current.isStep):
                    A=True
                else:
                    A=False
                if(interval_current_next.isStep):
                    B=True
                else:
                    B=False
                if(abs(vertical_interval_current.semitones) in [1,2,6,10,11]):
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
                    
                #Neighbour notes
                if(possible_note_previous==possible_note_next):
                    F=True
                else:
                    F=False

                if((not C) or (F)):
                    G=True
                else:
                    G=False  

                if(E ): 
                    intervals.append(True)
                else:
                    intervals.append(f'{i }'+" "+ vertical_interval_current.name+" "+interval_previous_current.niceName+
                                     " "+interval_current_next.niceName+" ")

    
    print("Rule 3 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):
    #if(all(intervals)):
        return True
    else:
        return intervals  

def verify_rule4(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)):
        interval=calculate_interval(section_cf[i],generated_section[i])
        if(interval.semitones>0):
            intervals.append(True) 
        else:
            intervals.append(f'{i }'+ interval.name+" ") 
    
    print("Rule 4 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule5(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)):
        #forward cross note
        if(i<len(generated_section)-1):
            interval1=calculate_interval(section_cf[i+1],generated_section[i])
            if(abs(interval1.semitones)!=6):
                intervals.append(True)
            else:
                intervals.append(f'{i } '+ interval1.name+" ") 
        
        #backward cross note
        if(i>0):
            interval2=calculate_interval(section_cf[i-1],generated_section[i])
            if(abs(interval2.semitones)!=6):
                intervals.append(True)
            else:
                intervals.append(f'{i } '+ interval2.name+" ") 
        
    print("Rule 5 ",intervals)
    
    if(all(str(flag) == 'True' for (flag) in intervals)):

#    if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule6(generated_section,section_cf):

    intervals=[]
    
    for i in range(len(generated_section)-3):
        interval0=calculate_interval(section_cf[i],generated_section[i])
        interval1=calculate_interval(section_cf[i+1],generated_section[i+1])
        interval2=calculate_interval(section_cf[i+2],generated_section[i+2])
        interval3=calculate_interval(section_cf[i+3],generated_section[i+3])

            
        if((abs(interval0.semitones)==3 or abs(interval0.semitones)==4) and
           (abs(interval1.semitones)==3 or abs(interval1.semitones)==4) and 
           (abs(interval2.semitones)==3 or abs(interval2.semitones)==4) and
           (abs(interval3.semitones)==3 or abs(interval3.semitones)==4)):
            intervals.append(f'{i }'+ interval0.name+" "+f'{i }'+ interval1.name+" "+f'{i+1 }'+ interval2.name+" "+f'{i+2 }') 

        else:
            intervals.append(True)
                    
            
    print("Rule 6 ",intervals)
    if(all(str(flag) == 'True' for (flag) in intervals)):

#    if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule7(generated_section,section_cf):

    intervals=[]
    
    for i in range(len(generated_section)-3):
        interval0=calculate_interval(section_cf[i],generated_section[i])
        interval1=calculate_interval(section_cf[i+1],generated_section[i+1])
        interval2=calculate_interval(section_cf[i+2],generated_section[i+2])
        interval3=calculate_interval(section_cf[i+3],generated_section[i+3])

            
        if((abs(interval0.semitones)==8 or abs(interval0.semitones)==9) and
           (abs(interval1.semitones)==8 or abs(interval1.semitones)==9) and 
           (abs(interval2.semitones)==8 or abs(interval2.semitones)==9) and
           (abs(interval3.semitones)==8 or abs(interval3.semitones)==9)):
            intervals.append(f'{i }'+ interval0.name+" "+f'{i }'+ interval1.name+" "+f'{i+1 }'+ interval2.name+" "+f'{i+2 }') 

        else:
            intervals.append(True)
                
    print("Rule 7 ",intervals)
    if(all(str(flag) == 'True' for (flag) in intervals)):
        
#    if(all(intervals)):
        return True
    else:
        return intervals



def verify_rule8(generated_section,section_cf):

    intervals=[]
    
    for i in range(len(generated_section)-3):
        interval0=calculate_interval(section_cf[i],generated_section[i])
        interval1=calculate_interval(section_cf[i+1],generated_section[i+1])
        interval2=calculate_interval(section_cf[i+2],generated_section[i+2])
        interval3=calculate_interval(section_cf[i+3],generated_section[i+3])

            
        if((abs(interval0.semitones)==15 or abs(interval0.semitones)==16) and
           (abs(interval1.semitones)==15 or abs(interval1.semitones)==16) and 
           (abs(interval2.semitones)==15 or abs(interval2.semitones)==16) and
           (abs(interval3.semitones)==15 or abs(interval3.semitones)==16)):
            intervals.append(f'{i }'+ interval0.name+" "+f'{i }'+ interval1.name+" "+f'{i+1 }'+ interval2.name+" "+f'{i+2 }') 

        else:
            intervals.append(True)
            
    print("Rule 8 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals



def verify_rule9(generated_section,section_cf):

    intervals=[]
    
    for i in range(1,len(generated_section)-1):
        interval_cf_cp=calculate_interval(section_cf[i],generated_section[i])
        interval_cp1_cp=calculate_interval(generated_section[i],generated_section[i-1])
        interval_cf1_cf=calculate_interval(section_cf[i],section_cf[i-1])
        interval_cf1_cp1=calculate_interval(section_cf[i-1],generated_section[i-1])
        
        
        A= abs(interval_cf_cp.semitones)==7
        B5= interval_cf1_cp1.semitones!=7
    
        if(~A or ((B1 and B2 and B3) or (B4 and B5))): 
            intervals.append(True)
        else:
            intervals.append(f'{generated_section[i-1]} {generated_section[i]} '+ str(interval_cf_cp.semitones)+" "+ B1+" "+ B2+" "+B3+" "+B4+" "+ B5+" ") 
            
    
    print("Rule 9 ",intervals)
         
    if(all(str(flag) == 'True' for (flag) in intervals)):
        return True
    else:
        return intervals


def verify_rule10(generated_section,section_cf):

    intervals=[]
    
    for i in range(1,len(generated_section)-1):
        interval_cf_cp=calculate_interval(section_cf[i],generated_section[i])
        interval_cp1_cp=calculate_interval(generated_section[i],generated_section[i-1])
        interval_cf1_cf=calculate_interval(section_cf[i],section_cf[i-1])
        interval_cf1_cp1=calculate_interval(section_cf[i-1],generated_section[i-1])
        
        A= abs(interval_cf_cp.semitones)==12
        B1= interval_cp1_cp.semitones*interval_cf1_cf.semitones<0
        B2= abs(interval_cp1_cp.semitones) <=2 
        B3= abs(interval_cf1_cf.semitones) <=2 
        B4= interval_cp1_cp.semitones*interval_cf1_cf.semitones==0
        B5= interval_cf1_cp1.semitones!=12

        if(~A or ((B1 and B2 and B3) or (B4 and B5))): 
            intervals.append(True)
        else:
            intervals.append(f'{generated_section[i-1]} {generated_section[i]} '+ str(interval_cf_cp.semitones)+" "+ B1+" "+ B2+" "+B3+" "+B4+" "+ B5+" ") 
            
    
    print("Rule 10 ",intervals)
         
    if(all(str(flag) == 'True' for (flag) in intervals)):
#    if(all(intervals)):
        return True
    else:
        return intervals


#Range

def verify_rule11(generated_section):

    intervals=[]
    
    max_generated_section=max(generated_section, key=lambda x: x.pitch.frequency)
    max_generated_sectionindex=generated_section.index(max_generated_section)
    
    min_generated_section=min(generated_section, key=lambda x: x.pitch.frequency)
    min_generated_sectionindex=generated_section.index(min_generated_section)
    
    print("max generated section ",max_generated_section, 'index ',max_generated_sectionindex,
          "min generated section ",min_generated_section, 'index ',min_generated_sectionindex)

    
    interval1=calculate_interval(generated_section[min_generated_sectionindex],generated_section[max_generated_sectionindex])
        
    if(abs(interval1.semitones)<=16):
        intervals.append(True)
    else:
        intervals.append(f'{max_generated_section }'+" "+ f'{max_generated_sectionindex}')
        intervals.append(f'{min_generated_section }'+" "+ f'{min_generated_sectionindex}'+" "+ f'{interval1.name}'+" ") 

    print("Rule 11 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):
  
    #if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule12(generated_section):

    intervals=[]
    for i in range(len(generated_section)):
        if(i<len(generated_section)-1):
            interval1=calculate_interval(generated_section[i+1],generated_section[i])

            if(abs(interval1.semitones)<=5):# or abs(interval1.semitones)==12 or abs(interval1.semitones)==-8):
                intervals.append(True)
            else:
                intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ str(interval1.semitones)+" ") 

    print("Rule 12 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):

   # if(all(intervals)):
        return True
    else:
        return intervals



def verify_rule13(generated_section):

    intervals=[]
    for i in range(len(generated_section)):
        if(i<len(generated_section)-1):
            interval1=calculate_interval(generated_section[i],generated_section[i+1])

            if(abs(interval1.semitones)!=6):
                intervals.append(True)
            else:
                intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ str(interval1.semitones)+" ") 

    print("Rule 13 ",intervals)
    if(all(str(flag) == 'True' for (flag) in intervals)):
         
#    if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule14(generated_section):

    intervals=[]
    for i in range(len(generated_section)-1):
        
        if(generated_section[i]==generated_section[i+1]): # and generated_section[i+1]==generated_section[i+2]):
            intervals.append(f'{generated_section[i]} {generated_section[i+1]} {generated_section[i+2]} ') 

        else:
            intervals.append(True)


    print("Rule 14 ",intervals)
    if(all(str(flag) == 'True' for (flag) in intervals)):
         
#    if(all(intervals)):
        return True
    else:
        return intervals


#Rule 15 Complensate leaps

def verify_rule15(generated_section):

    intervals=[]
    for i in range(len(generated_section)-2):
        possible_note1=generated_section[i]
        possible_note2=generated_section[i+1]
        possible_note3=generated_section[i+2]

        interval1=calculate_interval(generated_section[i+1],generated_section[i])
        interval2=calculate_interval(generated_section[i+1],generated_section[i+2])
            
        A=interval1.semitones>=7
        B=interval2.semitones>0
        
        if(~ A or B):
            intervals.append(True)
        elif(A or (~B and abs(interval2.semitones)<=2)):
            intervals.append(True)
        else:
            intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ interval1.name+" "+interval2.name) 
            
            
#         if(not interval1.semitones>=7 or interval2.semitones>0):
#             intervals.append(True)
#         else:
#             intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ interval1.name+" "+interval2.name) 


#         if(not interval1.semitones<7 or (interval2.semitones<0 and abs(interval2.semitones)<=2)):
#             intervals.append(True)

#         else:
#             intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ interval1.name+" "+interval2.name) 
   
                        

    print("Rule 15 ",intervals)
    if(all(str(flag) == 'True' for (flag) in intervals)):

#    if(all(intervals)):
        return True
    else:
        return intervals
    

#Rule 16 Compensate Octave leaps

def verify_rule16(generated_section):

    intervals=[]
    for i in range(len(generated_section)-3):
        possible_note1=generated_section[i]
        possible_note2=generated_section[i+1]
        possible_note3=generated_section[i+2]
        possible_note4=generated_section[i+3]

        interval1_2=calculate_interval(possible_note1,possible_note2)
        interval2_3=calculate_interval(possible_note2,possible_note3)
        interval1_3=calculate_interval(possible_note1,possible_note3)
        interval2_4=calculate_interval(possible_note2,possible_note4)
        interval3_4=calculate_interval(possible_note3,possible_note4)                            
                            
        A= abs(interval2_3.semitones)==12
        B= abs(interval1_2.semitones)<12 and abs(interval1_3.semitones)<12 and abs(interval2_4.semitones)<12 and abs(interval3_4.semitones)<12
                            
        if(not A or B): 
            intervals.append(True)
        else:  
            intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ str(interval1_2.semitones)+" "+
                            str(interval2_3.semitones)+" "+str(interval1_3.semitones)+" "+str(interval2_4.semitones)+" "+
                            str(interval3_4.semitones) )
                        
    print("Rule 16 ",intervals)
    
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals


#Rule 17 Arpeggiating Triads

def verify_rule17(generated_section):

    intervals=[]
    for i in range(len(generated_section)-2):
        possible_note1=generated_section[i]
        possible_note2=generated_section[i+1]
        possible_note3=generated_section[i+2]

        interval1_2=calculate_interval(possible_note2,possible_note1)
        interval2_3=calculate_interval(possible_note3,possible_note2)
                        
        A= (abs(interval1_2.semitones)>2) and (abs(interval2_3.semitones)>2) and (interval1_2.semitones*interval2_3.semitones>0)                    
        B= abs(interval1_2.semitones) <=4 and abs(interval2_3.semitones)<=4
                            
        if((not A) or B):
            intervals.append(True)
        else:
            intervals.append(f'{generated_section[i]} {generated_section[i+1]} ' + str(interval1_2.semitones)+" "+str(interval2_3.semitones)) 
                        
    print("Rule 17 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals


#Rule 18 Cadence

def verify_rule18(generated_section,section_cf):

    intervals=[]
    
    interval1=calculate_interval(generated_section[-2],generated_section[-1])

    #if(abs(interval1.semitones)==1 or abs(interval1.semitones)==2 or abs(interval1.semitones)==7):
    if(interval1.isStep):

        intervals.append(True)
    else:
        intervals.append(f'{generated_section[-1]}'+ interval1.name+" ") 

    
    print("Rule 18 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):

#    if(all(intervals)):
        return True
    else:
        return intervals


#Rule 19 Rule 20 Rule 21 on Motion

def verify_rule192021(generated_section,section_cf):
    intervals=[]

    contra_motion=0
    parallel_motion=0
    oblique_motion=0
    similar_motion=0
    imperfect=0
    step_motion=0
    non_steps=[]
    not_imperfect=[]
        
    for i in range(len(generated_section)-1):
        possible_note1=generated_section[i]
        possible_note2=generated_section[i+1]
            
        interval1=calculate_interval(possible_note1,possible_note2)
        interval2=calculate_interval(section_cf[i],section_cf[i+1])
        
        interval_cf_cp=calculate_interval(section_cf[i],possible_note1)
    
        interval_cp_cp1=calculate_interval(possible_note2,possible_note1)
                
        if(('Major' in interval_cf_cp.niceName or 'Minor' in interval_cf_cp.niceName) and interval_cf_cp.isConsonant()):
            imperfect+=1
        else:
            not_imperfect.append(f' not_inperfect {i} {section_cf[i]} {possible_note1} ' + str(interval_cf_cp.semitones)+" ") 

            
            
        if(abs(interval_cp_cp1.semitones<=2)):
            step_motion+=1
        else:
            non_steps.append(f' non step {i} {generated_section[i]} {generated_section[i+1]} ' + str(interval_cp_cp1.semitones)+" ") 
                       

        
        #music21.voiceLeading.VoiceLeadingQuartet(v1n1=None, v1n2=None, v2n1=None, v2n2=None, analyticKey=None)
        #vl = voiceLeading.VoiceLeadingQuartet(n1_a4, n2_c5, m1_d4, m2_f4)
        vl = voiceLeading.VoiceLeadingQuartet(possible_note1, possible_note2, section_cf[i], section_cf[i+1])
        motion_type=vl.motionType()

        if(motion_type=='Contrary'):
            contra_motion+=1
            
        elif(motion_type=='Parallel'):
            parallel_motion+=1
                
        elif(motion_type=='Oblique'):
            oblique_motion+=1
                
        elif(motion_type=='Similar'):
            similar_motion+=1
        else:
            pass
            
    if(3*contra_motion+ similar_motion > 2* parallel_motion+oblique_motion):
        intervals.append(True)
    else:
        intervals.append(str(3*contra_motion+ similar_motion- 2* parallel_motion-oblique_motion)) 

        
                    
            
    print("Rule 19,20,21 ", "imperfects ", imperfect, " notes not imperfect ", not_imperfect," steps ",step_motion, " notes non steps ",
          non_steps ," contra_motion " , str(contra_motion)+ " similar_motion "+ str(similar_motion)+
          " parallel_motion "+ str(parallel_motion)+ " oblique_motion "+ str(oblique_motion))

    if(all(str(flag) == 'True' for (flag) in intervals)):

#    if(all(intervals)):
        return True
    else:
        return intervals
    

def verify_rule22(generated_section):
    
    intervals=[]
    for i in range(len(generated_section)):
        if(i<len(generated_section)-1):
            interval1=calculate_interval(generated_section[i],generated_section[i+1])
            
            if(abs(interval1.semitones)<=5 and interval1.semitones!=0):# or abs(interval.semitones)==12 or interval.semitones==-8): 
                intervals.append(True)

            else:
                intervals.append(f'{generated_section[i]} {generated_section[i+1]} '+ interval1.name+" "+" isstep "+
                                 str(interval1.isStep))            
                
    print("Rule 22 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):

   # if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule23(generated_section,section_cf):
    intervals=[]

    for i in range(len(generated_section)-2):
        interval=calculate_interval(section_cf[i],generated_section[i])
        
        if(i%2==0):
            if(interval.isConsonant()):
                intervals.append(True)
            else:
                intervals.append(f'{i }'+ interval.name+" ") 
        
    print("Rule 23 ",intervals)

    if(all(str(flag) == 'True' for (flag) in intervals)):
        return True
    else:
        return intervals  
        

def verify_rule24(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)-3):
        if(i%2==0):
            continue

        possible_note_previous=generated_section[i-1]
        possible_note_current=generated_section[i]
        possible_note_next=generated_section[i+1]
    
        interval_previous_current=calculate_interval(possible_note_previous,possible_note_current)
        interval_current_next=calculate_interval(possible_note_current,possible_note_next)
        vertical_interval_current= calculate_interval(section_cf[i],possible_note_current)

       
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
                    
#         #Neighbour notes
#         if(possible_note_previous==possible_note_next):
#             F=True
#         else:
#             F=False
                    
#         if((not C) or (F)):
#             G=True
#         else:
#             G=False  
            
        if(E): 
            intervals.append(True)
        else:
            intervals.append(f'{i }'+" "+ vertical_interval_current.name+" "+interval_previous_current.niceName+
                             " "+interval_current_next.niceName+" ")
                        
    print("Rule 24 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals



def verify_rule25(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)-2):
        if(i>0 and i%2==1):
            possible_note1=generated_section[i]
            possible_note2=generated_section[i-1]
            
            interval_previous_cp=calculate_interval(possible_note2,possible_note1)
            interval_previous_cf=calculate_interval(section_cf[i-1],section_cf[i])
            
            interval_vertical=calculate_interval(section_cf[i],possible_note1)
    
            vl = voiceLeading.VoiceLeadingQuartet(possible_note2, possible_note1, section_cf[i-1], section_cf[i])
            
            motion_type=vl.motionType()
            
            A= 'Perfect' in interval_vertical.niceName
            #print(interval_vertical.niceName)
            
            if(not A or (motion_type!='Similar')):
                intervals.append(True)
            else:
                intervals.append(f'{generated_section[i-1]} {generated_section[i]} ' + motion_type+ " "+interval_vertical.niceName) 
                        
    print("Rule 25 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals


def verify_rule26(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)-2):
        if(i>1 and i%2==1):
            
            possible_note1=generated_section[i]
            possible_note2=generated_section[i-2]
            
            interval_vertical=calculate_interval(section_cf[i],possible_note1)
            interval_vertical2=calculate_interval(section_cf[i-2],possible_note2)
            
            A= 'Perfect Fifth' in interval_vertical2.name or 'Perfect Octave' in interval_vertical2.name
            B= 'Perfect Fourth' in interval_vertical.name
            
            if(not (A) or B):
                intervals.append(True)
            else:
                intervals.append(f'{generated_section[i-2]} {generated_section[i]} ' + interval_vertical2.niceName+
                                " "+interval_vertical.niceName+ " "+interval_vertical2.directedNiceName+ " "+
                                 interval_vertical.directedNiceName ) 
                        
    print("Rule 26 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals
    


def verify_rule27(generated_section,section_cf):

    intervals=[]
    for i in range(len(generated_section)):
        
        possible_note=generated_section[i]
        
        if(('-' in str(possible_note.pitch) or '#' in str(possible_note.pitch)) and
          ('-' not in str(section_cf[i]) and '#' not in str(section_cf[i]))):
            
            intervals.append(f'violated {generated_section[i]} '+str(section_cf[i]) +" "+" Augmented/diminished ")
            #print("aug dim",str(possible_note1.pitch)," ",section_cf[note_position])
        else:
            intervals.append(True)
            #print(f'{i} True {possible_note.pitch} semitones {str(section_cf)}',end='\n')

        
              
    print("Rule 27 ",intervals)
   
    if(all(str(flag) == 'True' for (flag) in intervals)):

    #if(all(intervals)):
        return True
    else:
        return intervals
    
