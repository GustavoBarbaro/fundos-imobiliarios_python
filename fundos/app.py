import streamlit as st
import pandas as pd
import numpy as np

import functions




st.title('Hello world !')


df = functions.read_csv()

df = functions.fix_df(df)

dfresp1 = functions.filtra_ordena(df)


dfresp1

st.write(' outro jeito')

st.table(dfresp1)





