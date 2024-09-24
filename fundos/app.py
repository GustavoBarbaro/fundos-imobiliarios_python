import streamlit as st
import pandas as pd
import numpy as np

import functions


st.set_page_config(page_title='AFii', layout="wide", page_icon=':house:')

st.logo('imagens/logo2.png')

st.html("""
  <style>
    [alt=Logo] {
      height: 5rem;
    }
  </style>
        """)


st.title('Analisador de Fundos Imobiliários :house: :department_store: ')
st.subheader('FONTE: [Status Invest](https://statusinvest.com.br/fundos-imobiliarios/busca-avancada)', divider='green')

tab1, tab2 = st.tabs(['Base', 'Estatégia'])

with tab1:

    # Tratando o data set

    df = functions.read_csv()
    df = functions.fix_df(df)


    with st.sidebar:

        st.write('# **Filtros:**')

        liqMed_min, liqMed_max = df['LIQUIDEZ MEDIA DIARIA'].min(), df['LIQUIDEZ MEDIA DIARIA'].max()
        liq_med_diaria = st.number_input('Liquidez Média Diaria **Mínima**:', min_value=float(liqMed_min), max_value=float(liqMed_max))

        pat_min, pat_max = df['PATRIMONIO'].min(), df['PATRIMONIO'].max()
        patrimonio = st.number_input('Patrimônio **Mínimo** :', min_value=float(pat_min), max_value=float(pat_max))


        pvp_min, pvp_max = df['P/VP'].min(), df['P/VP'].max()
        pvp = st.number_input('P/VP **Mínimo**:', min_value=float(pvp_min), max_value=float(pvp_max), value=pvp_min)

    df_base = functions.filtra(df, liq_med_diaria, patrimonio, pvp)


    # =========================================


    st.markdown('## Base')
    st.dataframe(df_base)

    dfresp1 = functions.filtra(df, liq_med_diaria, patrimonio, pvp)
    dfresp1 = functions.ordena(dfresp1)

    st.table(dfresp1)


with tab2:

    dfresp1 = functions.filtra(df, liq_med_diaria, patrimonio, pvp)
    dfresp1 = functions.ordena(dfresp1)

    st.table(dfresp1)






