#!/usr/bin/env python
# coding: utf-8

# In[1]:


#código filtro dados

#extrair todos os arquivos na mesma pasta que python estiver rodando.
#trocar o ano no nome do arquivo csv
#o procedimento pode ser feito para cada mês também.

#importando módulos
import pandas as pd
import glob
#criar lista com os arquivos do ano
dados = glob.glob('starnet*.dat')
#loop para ler todos arquivos e filtrar pela Coluna 11 que são os dados de qualidade
for i in range(0,365):
    df = pd.read_csv(dados[i], sep="\s+",header=None, prefix="Coluna_" )
    filtro1 = df[(df.Coluna_11==0) & (df.Coluna_7<=-19.49) & (df.Coluna_7>=-20.39) & 
                 (df.Coluna_8<=-43.56) & (df.Coluna_8>=-44.67) ][["Coluna_0","Coluna_1",
                                                                  "Coluna_2","Coluna_3",
                                                                  "Coluna_4","Coluna_5",
                                                                  "Coluna_7","Coluna_8",
                                                                  "Coluna_11"]]
    filtro1.to_csv('%i_2014.csv' %i)
# juntando todos os arquivos criados no filtro e criar um arquivo csv com todos os dados do ano
dados2014 = pd.concat(map(pd.read_csv, glob.glob('*_2014.csv')),ignore_index=True, axis=0)
dados2014.to_csv('dados2014.csv',index=False)


# In[ ]:




