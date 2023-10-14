import pandas as pd
import numpy as np
import streamlit as st

st.header("Utilizando DataFrame")
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.header("Utilizando Table")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

st.header("Utilizando Metric")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.header("Utilizando JSON")

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })