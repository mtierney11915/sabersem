import pandas as pd
import streamlit as st
import altair as alt

#Set Page Configuration
st.set_page_config(
    page_title="Saberseminar Project Model Application",
    layout="wide",
    page_icon=":baseball:")
#st.title("Saberseminar Project Model Application")
st.markdown(
    """
    <h1 style='text-align: center;'>Saberseminar Project Model Application</h1>
    """,
    unsafe_allow_html=True
)
#Select A Model
st.subheader("Select a Type of Model to Project")
position=st.selectbox("Hitter or Pitcher?",("Hitter","Pitcher"))
conf=st.selectbox("Level of Baseball?",("Power 5 Conference","Non Power 5 Conference","High School/JUCO"))

#Pitcher P5
if position == "Pitcher" and conf == "Power 5 Conference":
    st.subheader("Input Pitcher Statistics")
    era=st.number_input("ERA:",value=0.0)
    IP=st.number_input("Innings Pitched:",value=0.0)
    WHIP=st.number_input("WHIP:",value=0.0)
    HR9=st.number_input("HR/9:",value=0.0)
    BB9=st.number_input("BB/9:",value=0.0)
    SO9=st.number_input("SO9:",value=0.0)
    SOw=st.number_input("Strikeout to Walk Ratio:",value=0.0)
    predictedp5=(-13.35499+(-.69823*era)+(.06487*IP)+(5.89958*WHIP)+(-1.46797*HR9)+(-1.11435*BB9)+(.80572*SO9)+(.34855*SOw))
    st.metric("Predicted War:",f"{predictedp5:.2f}")
    mlbready = (6.71532 + (.12468 * era) + (-.01610 * IP) + (-1.93953 * WHIP) + (1.17481 * HR9) + (.90382 * BB9) + (-.47395 * SO9) + (.38684 * SOw))
    st.metric("Predicted Time to Reach MLB:", f"{mlbready:.2f} years")
    mlblong = (-5.70364 + (-.54303 * era) + (.04037 * IP) + (4.34623 * WHIP) + (.57316 * HR9) + (-.71274 * BB9) + (.43111 * SO9) + (.10935 * SOw))
    st.metric("Predicted MLB Career Length:", f"{mlblong:.2f} years")
#Pitcher N5
if position == "Pitcher" and conf == "Non Power 5 Conference":
    st.subheader("Input Pitcher Statistics")
    xera=st.number_input("ERA:",value=0.0)
    xIP=st.number_input("Innings Pitcher:",value=0.0)
    xWHIP=st.number_input("WHIP:",value=0.0)
    xHR9=st.number_input("HR/9:",value=0.0)
    xBB9=st.number_input("BB/9:",value=0.0)
    xSO9=st.number_input("SO9:",value=0.0)
    xSOw=st.number_input("Strikeout to Walk Ratio:",value=0.0)
    xpredictedp5=(3.3099 +(-.52151*xera)+(-.01845*xIP)+(1.12144*xWHIP)+(-1.31908*xHR9)+(-.48485*xBB9)+(-.08020*xSO9)+(.18308*xSOw))
    st.metric("Predicted War:",f"{xpredictedp5:.2f}")
    xmlbready = (1.191447 + (.311831 * xera) + (.005943 * xIP) + (.511360 * xWHIP) + (-.544042 * xHR9) + (-.087242 * xBB9) + (.014701 * xSO9) + (.067421 * xSOw))
    st.metric("Predicted Time to Reach MLB:", f"{xmlbready:.2f} years")
    xmlblong = (6.145376 + (-.661705 * xera) + (-.009827 * xIP) + (-.687242 * xWHIP) + (1.493082 * xHR9) + (-.291182 * xBB9) + (-.037914 * xSO9) + (-.012064 * xSOw))
    st.metric("Predicted MLB Career Length:", f"{xmlblong:.2f} years")

#Juco/HS Pitcher
if position == "Pitcher" and conf == "High School/JUCO":
    st.subheader("Input Pitcher Statistics")
    yera=st.number_input("ERA:",value=0.0)
    yIP=st.number_input("Innings Pitcher:",value=0.0)
    yWHIP=st.number_input("WHIP:",value=0.0)
    yHR9=st.number_input("HR/9:",value=0.0)
    yBB9=st.number_input("BB/9:",value=0.0)
    ySO9=st.number_input("SO9:",value=0.0)
    ySOw=st.number_input("Strikeout to Walk Ratio:",value=0.0)
    ytoA=st.number_input("Years to Single A:",value=0.0)
    ypredictedp5=(-3.53637 +(-.56064*yera)+(0.02223*yIP)+(1.42353*yWHIP)+(-.36428*yHR9)+(-.10288*yBB9)+(-.38674*ySO9)+(.25250*ySOw)+(-.31812*ytoA))
    st.metric("Predicted War:",f"{ypredictedp5:.2f}")
    ymlbready=(5.518778 +(-.007632*yera)+(-.008507*yIP)+(.838669*yWHIP)+(-.091802*yHR9)+(-.105406*yBB9)+(-.139258*ySO9)+(-.090533*ySOw)+(.693129*ytoA))
    st.metric("Predicted Time to Reach MLB:", f"{ymlbready:.2f} years")
    ymlblong = (-.964261 + (-.287487 * yera) + (.020536 * yIP) + (.202303 * yWHIP) + (.057179 * yHR9) + (-.120293 * yBB9) + (.387417 * ySO9) + (.087680 * ySOw) + (-.149181 * ytoA))
    st.metric("Predicted MLB Career Length:", f"{ymlblong:.2f} years")
#Hitter P5
if position == "Hitter" and conf == "Power 5 Conference":
    st.subheader("Input Hitter Statistics")
    runs=st.number_input("Runs:",value=0)
    sb=st.number_input("SB:",value=0)
    XBH=st.number_input("Total Extra Base Hits:",value=0)
    HRrate=st.number_input("Home Run Rate:",value=0.0)
    SORate=st.number_input("Strikeout Rate:",value=0.0)
    WalkRate=st.number_input("Walk Rate:",value=0.0)
    OPS=st.number_input("OPS:",value=0.0)
    predhitter5=(7.074771 +(-.007111*runs)+(.268339*sb)+(.448599*XBH)+(56.124926*HRrate)+(-28.110378*SORate)+(45.000647*WalkRate)+(-23.916247*OPS))
    st.metric("Predicted War:", f"{predhitter5:.2f}")
    predmlb = (10.274933 + (.011031 * runs) + (-.053789 * sb) + (.003092 * XBH) + (15.463913 * HRrate) + (-5.512848 * SORate) + (-9.531319 * WalkRate) + (-5.311478 * OPS))
    st.metric("Predicted Time to Reach MLB:", f"{predmlb:.2f} years")
    predmlblong = (-.15521 + (.03725 * runs) + (.04785 * sb) + (.07292 * XBH) + (19.83294 * HRrate) + (-12.08794 * SORate) + (9.61725 * WalkRate) + (-.77007 * OPS))
    st.metric("Predicted MLB Career Length:", f"{predmlblong:.2f} years")

#Hitter Non p5
if position == "Hitter" and conf == "Non Power 5 Conference":
    st.subheader("Input Hitter Statistics")
    xruns=st.number_input("Runs:",value=0)
    xsb=st.number_input("SB:",value=0)
    xXBH=st.number_input("Total Extra Base Hits:",value=0)
    xHRrate=st.number_input("Home Run Rate:",value=0.0)
    xSORate=st.number_input("Strikeout Rate:",value=0.0)
    xWalkRate=st.number_input("Walk Rate:",value=0.0)
    xOPS=st.number_input("OPS:",value=0.0)
    xpredhitter5=(-18.66240 +(-.11467*xruns)+(.05062*xsb)+(.09609*xXBH)+(-65.01413*xHRrate)+(-.10683*xSORate)+(112.94747*xWalkRate)+(12.34521*xOPS))
    st.metric("Predicted War:", f"{xpredhitter5:.2f}")
    xpredmlb = (10.274933 + (.011031*xruns)+(-.053789 * xsb) + (.003092 * xXBH) + (15.463913 * xHRrate) + (-5.512848 * xSORate) + (-9.531319 * xWalkRate) + (-5.311478 * xOPS))
    st.metric("Predicted Time to Reach MLB:", f"{xpredmlb:.2f} years")
    xpredmlblong = (-3.51255 + (-.09734 * xruns) + (.10598 * xsb) + (.14339 * xXBH) + (-45.42311 * xHRrate) + (-10.14891 * xSORate) + (31.92478 * xWalkRate) + (5.82717 * xOPS))
    st.metric("Predicted MLB Career Length:", f"{xpredmlblong:.2f} years")

#HS Hitter
if position == "Hitter" and conf == "High School/JUCO":
    st.subheader("Input Hitter Statistics")
    yruns=st.number_input("Runs:",value=0)
    ysb=st.number_input("SB:",value=0)
    yXBH=st.number_input("Total Extra Base Hits:",value=0)
    yHRrate=st.number_input("Home Run Rate:",value=0.0)
    ySORate=st.number_input("Strikeout Rate:",value=0.0)
    yWalkRate=st.number_input("Walk Rate:",value=0.0)
    yOPS=st.number_input("OPS:",value=0.0)
    yxtoa=st.number_input("Years to Single A:",value=0.0)
    ypredhitter5=(-9.965928 +(.019165*yruns)+(.042159*ysb)+(.009875*yXBH)+(-81.652452*yHRrate)+(-13.091434*ySORate)+(38.530004*yWalkRate)+(14.002029*yOPS)+(-1.012992*yxtoa))
    st.metric("Predicted War:",  f"{ypredhitter5:.2f}")
    ypredmlb= (6.914882 +(.003736*ysb)+(.001657*yXBH)+(-6.226212*yHRrate)+(3.430989*ySORate)+(.604821*yWalkRate)+(-4.813329*yOPS)+(.661929*yxtoa))
    st.metric("Predicted Time to Reach MLB:",f"{ypredmlb:.2f} years")
    ypredmlb = (-1.8478099 + (.0094542 * ysb) + (.0006778 * yXBH) + (17.7061467 * yHRrate) + (-4.4357358 * ySORate) + (3.2331205 * yWalkRate) + (8.7617960 * yOPS) + (-.7267853 * yxtoa))
    st.metric("Predicted MLB Career Length:", f"{ypredmlb:.2f} years")
