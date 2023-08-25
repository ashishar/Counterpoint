#!/usr/bin/env python
# coding: utf-8



def compile_solutions(sampleset_pd,num_notes,POSSIBLE_FREQUENCIES,treble_clef_notes):
    #num_notes=5#len(section_cf_frequency)
    
    q = Array.create('q', shape=(num_notes,POSSIBLE_FREQUENCIES), vartype='BINARY')

    print("no. of solution ",sampleset_pd.shape[0])

    for sol in range(1):#sampleset_pd.shape[0]):
        sampleset_pd1=pd.DataFrame(sampleset_pd.iloc[0].to_list())
    
        COLUMN_NAMES=[]
        for i in range(num_notes):
            col_name=f'q[{i}]'
            COLUMN_NAMES.append(f'{col_name}')

        sampleset_table=pd.DataFrame(columns=COLUMN_NAMES) # Note that there are row data inserted.

        for i in range(num_notes):
            for j in range(POSSIBLE_FREQUENCIES):
            #sampleset_table.iloc[f'q[{i}]',j]=sampleset_pd.iloc[0][f'q[{i}][{j}]']
                sampleset_table.loc[j,f'q[{i}]']=sampleset_pd.loc[sol,f'q[{i}][{j}]']

        sampleset_table.loc['Total',:]= sampleset_table[COLUMN_NAMES].sum(axis=0)
        print("Solution no ",sol)
        #display(sampleset_table)
    
        section_cp_calculated=[]
        for i in range(num_notes):
            for j in range(POSSIBLE_FREQUENCIES):
                if (sampleset_table.loc[j,f'q[{i}]']==1):
                    #print(i,j,treble_clef_notes[j].pitch)
                    section_cp_calculated.append(treble_clef_notes[j])
        
                
        return section_cp_calculated


# In[17]:




