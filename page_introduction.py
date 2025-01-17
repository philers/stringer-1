import streamlit as st

def page_introduction():

    st.text('page_introduction')

    st.image('./images/stringer_logo.png')
    st.title('Surfacing Viral Misinformation')

    st.write('___')

    # Spacing
    st.write("")

    st.image('./images/three_keys.png')

    st.write('___')

    st.image('./images/how_we_do_it.png')

    st.write('___')

    st.image('./images/our_metrics.png')

    return
