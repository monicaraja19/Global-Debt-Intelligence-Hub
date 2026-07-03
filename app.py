import streamlit as st
from streamlit_option_menu import option_menu
from Utility.css_styling import nav_style
from datetime import datetime
from Dashboard_Visualization.About import show_query

#Dashboard Page
def showDashboard():
    st.set_page_config(page_title="Global Debt Intelligence Hub",page_icon="Assets/gdih_logo.png",layout="wide",initial_sidebar_state="collapsed")
    # Load CSS #Cards navigators styling page
    #with open("Utility/style.css") as f:
        #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    #Padding for the page
    st.markdown("""
    <style>
    .block-container{
        padding-top: 1.5rem;
        padding-bottom: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)
    #Header and Navigation bar container
    with st.container():
        col_logo, col_title= st.columns([4,35],vertical_alignment='center')
        with col_logo:
            #image and logo Styling
            st.markdown("""
            <div style="
                display:flex;
                align-items:center;
                justify-content:center;
                height:100%;
                margin-top:-12px;
                margin-bottom:-250px;
            ">
            """, unsafe_allow_html=True)
            st.image("Assets/gdih_logo.png", width="stretch")
        with col_title:
            ShowTitle()
    #Navigation bar
    selected = option_menu(menu_title=None,options=["Executive Dashboard","Country Analysis","Reports","About"],icons=["house","flag","file-earmark-text","info-circle"],orientation="horizontal",styles =nav_style())
    if selected == "Dashboard":
        pass
    elif selected == "Country":
        pass
    elif selected == "Reports":
        pass
    elif selected == "About":
        show_query()

#Title and subtitle of the dashboard
def ShowTitle():
    return st.markdown("""
            <div style="
        display:flex;
        flex-direction:column;
        justify-content:center;
        height:100%;
        padding-left:10px;">
            <h1 style="
            margin:0;
            color:#0A2A5E;
            font-size:40px;
            font-weight:800;
            line-height:0.95;
            letter-spacing:1px;">
                GLOBAL DEBT INTELLIGENCE HUB
            </h1>
                        <!-- Accent Line -->
        <div style="
            width:297px;
            height:4px;
            background:#1683C6;
            border-radius:10px;
            margin-bottom:6px;
        ">
        </div>
                        <div style="
            color:#5F6B7C;
            font-size:18px;
            font-style:italic;
            font-weight:500;
            letter-spacing:0.5px;
        ">
            Insights. Analytics. Smarter Decisions.
        </div>
            </div>           
            """, unsafe_allow_html=True)

#Start the dashboard
if __name__ == "__main__":
    showDashboard()