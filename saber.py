import pandas as pd
import streamlit as st
import altair as alt

#Set Page Configuration
st.set_page_config(
    page_title="Saberseminar Project Model Application",
    layout="wide",
    page_icon=":baseball:")
st.title("Saberseminar Project Model Application")

#Select A Model
st.subheader("Select a Type of Model to Project")
position=st.selectbox("Hitter or Pitcher?",("Hitter","Pitcher"))
conf=st.selectbox("Power 5 Conference?",("Yes","No"))

#Pitcher P5
if position == "Pitcher" and conf == "Yes":
    st.subheader("Input Pitcher Statistics")
    era=st.number_input("ERA:",value=0.0)
    IP=st.number_input("Innings Pitcher:",value=0.0)
    WHIP=st.number_input("WHIP:",value=0.0)
    HR9=st.number_input("HR/9:",value=0.0)
    BB9=st.number_input("BB/9:",value=0.0)
    SO9=st.number_input("SO9:",value=0.0)
    SOw=st.number_input("Strikeout to Walk Ratio:",value=0.0)
    predictedp5=(-13.35499+(-.69823*era)+(.06487*IP)+(5.89958*WHIP)+(-1.46797*HR9)+(-1.11435*BB9)+(.80572*SO9)+(.34855*SOw))
    st.metric("Predicted War:",predictedp5)
#Pitcher N5
if position == "Pitcher" and conf == "No":
    st.subheader("Input Pitcher Statistics")
    xera=st.number_input("ERA:",value=0.0)
    xIP=st.number_input("Innings Pitcher:",value=0.0)
    xWHIP=st.number_input("WHIP:",value=0.0)
    xHR9=st.number_input("HR/9:",value=0.0)
    xBB9=st.number_input("BB/9:",value=0.0)
    xSO9=st.number_input("SO9:",value=0.0)
    xSOw=st.number_input("Strikeout to Walk Ratio:",value=0.0)
    xpredictedp5=(3.3099 +(-.52151*xera)+(-.01845*xIP)+(1.12144*xWHIP)+(-1.31908*xHR9)+(-.48485*xBB9)+(-.08020*xSO9)+(.18308*xSOw))
    st.metric("Predicted War:",xpredictedp5)
#Hitter P5
if position == "Hitter" and conf == "Yes":
    st.subheader("Input Hitter Statistics")
    runs=st.number_input("Runs:",value=0)
    sb=st.number_input("SB:",value=0)
    XBH=st.number_input("Total Extra Base Hits:",value=0)
    HRrate=st.number_input("Home Run Rate:",value=0.0)
    SORate=st.number_input("Strikeout Rate:",value=0.0)
    WalkRate=st.number_input("Walk Rate:",value=0.0)
    OPS=st.number_input("OPS:",value=0.0)
    predhitter5=(7.074771 +(-.007111*runs)+(.268339*sb)+(.448599*XBH)+(56.124926*HRrate)+(-28.110378*SORate)+(45.000647*WalkRate)+(-23.916247*OPS))
    st.metric("Predicted War:", predhitter5)

#Hitter Non p5
if position == "Hitter" and conf == "No":
    st.subheader("Input Hitter Statistics")
    xruns=st.number_input("Runs:",value=0)
    xsb=st.number_input("SB:",value=0)
    xXBH=st.number_input("Total Extra Base Hits:",value=0)
    xHRrate=st.number_input("Home Run Rate:",value=0.0)
    xSORate=st.number_input("Strikeout Rate:",value=0.0)
    xWalkRate=st.number_input("Walk Rate:",value=0.0)
    xOPS=st.number_input("OPS:",value=0.0)
    xpredhitter5=(-18.66240 +(-.11467*xruns)+(.05062*xsb)+(.09609*xXBH)+(-65.01413*xHRrate)+(-.10683*xSORate)+(112.94747*xWalkRate)+(12.34521*xOPS))
    st.metric("Predicted War:", xpredhitter5)
