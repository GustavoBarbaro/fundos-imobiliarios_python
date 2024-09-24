import pandas as pd
import numpy as np



def read_csv():

    df = pd.read_csv('statusinvest-busca-avancada.csv', sep=';')
    return df



def fix_df(df):

    cols_float = ['PRECO', 'ULTIMO DIVIDENDO', 'DY', 'VALOR PATRIMONIAL COTA', 'P/VP', 'LIQUIDEZ MEDIA DIARIA', 'PERCENTUAL EM CAIXA', 'PATRIMONIO', 'N COTISTAS']
    limpar_vazios = ['PRECO', 'DY', 'ULTIMO DIVIDENDO', 'VALOR PATRIMONIAL COTA', 'P/VP', 'LIQUIDEZ MEDIA DIARIA', 'PERCENTUAL EM CAIXA', 'PATRIMONIO', 'N COTISTAS', 'GESTAO']

    #limpando linhas vazias
    df = df.dropna(subset=limpar_vazios)

    for cols in cols_float:
        #tirar os pontos e trocar a virgula por ponto EX: 60.509,60 -> 60509.60
        df[cols] = df[cols].str.replace('.', '').str.replace(',', '.')


    #convertendo os valores
    df[cols_float] = df[cols_float].astype(float)

    return df



def ordena(df_filtrado):

    #PARAMETROS

    # liq_med_diaria = 200000
    # patrimonio = 1000000000
    # pvp = 0.8

    mostrar = ['TICKER', 'PRECO', 'ULTIMO DIVIDENDO', 'DY', 'VALOR PATRIMONIAL COTA', 'P/VP']

    df_res1 = df_filtrado.sort_values(by=['DY', 'P/VP'], ascending=[True, False]).head(10)
    df_res2 = df_filtrado.sort_values(by=['P/VP', 'DY'], ascending=[True, False]).head(10)

    #tenho dois df para mostrar, duas possibilidades, por enquanto vou voltar apenas o 1

    return df_res1



def filtra(df, liq_med_diaria, patrimonio, pvp):
    
    return df[ (df['LIQUIDEZ MEDIA DIARIA'] >= liq_med_diaria) & (df['PATRIMONIO'] >= patrimonio) & (df['P/VP'] >= pvp) ].sort_values(by='P/VP')