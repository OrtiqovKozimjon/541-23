import pandas as pd
data ={
       'ism':['Kozimjon', 'Furqtabek','Zuxriddin','Saidakbar','Esonali','Diyorbek',
              'Asadbek','Madinaxon','Mahsudjon','Shohjahon','Azamjon','Saidabbos'],
       'yoshi':[21,23,22,19,19,19,19,25,19,22,19,19],
       'shahar':['QUVA','KOSOMSOY','TOSHKENT','XOJAOBOD','OLTIARIQ','BUVAYDA',
                  'YAYPAN','KOSONSOY','YAYPAN','OLTIARIQ','FARGONA','YAYPAN']
       }
df=pd.DataFrame(data)
print(df)
young_people=df[df['yoshi']<22]
print("22 yoshdan kichiklar:\n",young_people)
df['yoshi']+=1
print("yangilangann DataFrame:\n",df)
df.to_csv('data.csv',index=False)
yaypan_people = df[df['shahar'] == 'YAYPAN']
print("Yaypanliklar:\n", yaypan_people)
