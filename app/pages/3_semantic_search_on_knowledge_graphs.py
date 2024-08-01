# streamlit_app.py
import time
import streamlit as st
import streamlit.components.v1 as components


if 'run_button' in st.session_state and st.session_state.run_button == True:
    st.session_state.running = True
else:
    st.session_state.running = False



if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage):
    st.session_state.stage = stage

if st.button('⚙️ Build a Neo4j database.', 
    disabled=st.session_state.running,
    key='run_button', 
    on_click=set_stage,
    args=(1,)):
    status = st.progress(0)
    for t in range(3):
        time.sleep(.2)
        status.progress(10*t+10)
    st.experimental_rerun()

if st.session_state.stage > 0:
    components.iframe(src="http://localhost:7474/browser/",
     width=None, 
     height=None, 
     scrolling=False)

st.markdown("""---""")


# if st.session_state.stage > 1:
#     # More code, etc
#     st.button('Third Button', on_click=set_stage, args=(3,))