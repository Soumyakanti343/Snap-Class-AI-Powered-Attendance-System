import streamlit as st 

# <img src='{logo_url}' style='max-height:25px' />

def footer_home():
    # logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <p style="font-weight:bold; color:yellow;"> Soumya Kanti Upadhyay </p> 
        <p style="font-weight:bold; color:orange;"> [JGEC CSE'28] </p> 
        </div>

    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <p style="font-weight:bold; color:blue;"> Soumya Kanti Upadhyay </p>
        <p style="font-weight:bold; color:green;"> [JGEC CSE'28] </p> 
        </div>
                
    """, unsafe_allow_html=True)