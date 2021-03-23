#!/usr/bin/env python
# coding: utf-8

# In[1]:


##  importar pandas e dados
import pandas as pd
import glob


# In[2]:


## Teste: abrindo arquivo único e renomeando colunas com prefixo padrão

df = pd.read_csv("starnet_2014-12-31_flash.dat", sep="\s+",header=None, prefix="Coluna_" )
#df = pd.concat(map(pd.read_csv, glob.glob('starnet*.dat')),ignore_index=True, axis=1) 


# In[3]:


## Visualizando o arquivo aberto agora como dataframe - apenas 5 primeiras linhas
df.head()


# In[6]:


## Teste: filtrando pela coluna 11 de qualidade e chamando apenas as colunas relevantes...
## Ano,mês,dia, hora, minuto, segundo, Latitude, Longitude, Qualidade
## Comando cria filtro, chamando dados relacionados à Coluna_11 igual a zero.
filtro1 = df[df.Coluna_11==0][["Coluna_0","Coluna_1","Coluna_2","Coluna_3","Coluna_4","Coluna_5","Coluna_7","Coluna_8","Coluna_11"]]
filtro1


# In[10]:


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
    filtro1 = df[df.Coluna_11==0][["Coluna_0","Coluna_1","Coluna_2","Coluna_3","Coluna_4","Coluna_5","Coluna_7","Coluna_8","Coluna_11"]]
    filtro1.to_csv('%i_2014.csv' %i)
# juntando todos os arquivos criados no filtro e criar um arquivo csv com todos os dados do ano
dados2014 = pd.concat(map(pd.read_csv, glob.glob('*_2014.csv')),ignore_index=True, axis=0)
dados2014.to_csv('dados2014.csv',index=False)


# In[ ]:




