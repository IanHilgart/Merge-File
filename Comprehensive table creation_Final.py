import numpy as np
import pandas as pd
df = pd.read_csv(r'file1.csv')
df2 = pd.read_csv(r'file2.csv')
print(df)
print(df2)
#df.to_csv("df.csv")
#df2.to_csv("df.csv")

df_cols_list = list(df.columns.values)
df2_cols_list = list(df2.columns.values)

#print(df_list)
#print(df2_list)
df_all_cols=df
df2_all_cols=df2
col_list1= []
for i in df2_cols_list:
    if i not in df_cols_list:
        col_list1.append(i)
print(col_list1)

for i in range(len(col_list1)):
        df_all_cols[col_list1[i]]=np.nan

col_list2=[]
for i in df_cols_list:
        if i not in df2_cols_list:
            col_list2.append(i)
for i in range(len(col_list2)):
        df2_all_cols[col_list2[i]]=np.nan


#df_all_cols.to_csv("df1cols.csv")
#df2_all_cols.to_csv("df2cols.csv")
#print(df2_all_cols)
comp_df=df_all_cols.append(df2_all_cols, ignore_index=False, sort=False)
#comp_df.to_csv("comp_df.csv")
id_list_df = pd.DataFrame(comp_df, columns=['PatientID','Timepoint'])
#START HERE
patient_tp_list= list(id_list_df[['PatientID', 'Timepoint']].itertuples(index=False, name=None))

print(patient_tp_list)
seen = set()
uniq = []
dups = []
for i in patient_tp_list:
    if i not in seen:
        uniq.append(i)
        seen.add(i)
    else: 
        dups.append(i)
print(uniq)
print(dups)


non_dups = [x for x in uniq if x not in dups]

print(non_dups)
if not dups:
        dups = uniq

comp_df_str= comp_df.select_dtypes(include=[object])
#comp_df_str.to_csv('test.csv')
comp_df_str.pop('PatientID')
string_df=pd.concat([id_list_df, comp_df_str], axis=1)

dup_str_df=string_df[string_df[['PatientID','Timepoint']].apply(tuple, 1).isin(dups)]
dup_str_df.to_csv("df.csv")
dup_str_df=dup_str_df.set_index(['PatientID', 'Timepoint'])
non_dups_str_df=string_df[string_df[['PatientID', 'Timepoint']].apply(tuple, 1).isin(non_dups)]
non_dups_str_df.set_index(["PatientID", "Timepoint"])
#non_dups_str_df.to_csv("uniq_Strs.csv")

for i in dup_str_df:
    dup_str_df[i]=dup_str_df.groupby(['PatientID', 'Timepoint'])[i].ffill()
dup_str_df.to_csv('dupstr.csv')
dup_str_df2 = dup_str_df.groupby(['PatientID', 'Timepoint'], as_index=True, level=1).apply(lambda x: x.iloc[-1])

dup_str_df2 = dup_str_df2.reset_index()
#dup_str_df2 = pd.DataFrame(dup_str_df2).set_index(["PatientID", "Timepoint"])

dup_str_df2.set_index(['PatientID', 'Timepoint'])




comp_str_df= dup_str_df2.append(non_dups_str_df, ignore_index=False, sort=False)
for i in comp_str_df:
    comp_str_df[i]=comp_str_df.groupby(['PatientID', 'Timepoint'])[i].ffill()
comp_str_df=comp_str_df.reset_index()
comp_str_df.set_index(['PatientID', 'Timepoint'])
#comp_str_df.pop('index')
comp_str_df.to_csv('testV2_2.csv')
#comp_str_df= pd.concat([non_dups_str_df,_dup_str_df2] ignore_index=False, sort=False)
#comp_str_df.to_csv("ComprehensiveStrs.csv")



  
dup_str_df.to_csv("dup_strs.csv")




comp_num_df=comp_df.groupby(['PatientID', 'Timepoint']).mean()
comp_num_df.to_csv('test2V2_2.csv')
comp_num_df=comp_num_df.reset_index()
comp_num_df.set_index(['PatientID', 'Timepoint'])
comp_num_df.to_csv('test3V2_2.csv')
df_complete=pd.merge(comp_str_df, comp_num_df, how='outer', on= (['PatientID', 'Timepoint']))
#df_complete.drop_duplicates(keep=False, inplace=True)
df_complete.to_csv('test4V2_3.csv')
df_complete.reset_index()
df_complete.pop('index')
df_complete.set_index(['PatientID', 'Timepoint'])
#df_complete=comp_num_df.append(comp_df_str, ignore_index=False, sort=False)
df_complete.to_csv('Superfile_test.csv', index=False)
comp_num_df.to_csv("comp_num.csv")
comp_df_str.to_csv("comp_str.csv")
##############


