import streamlit as st
import pandas as pd
st.title("Wasel Is here for you")
df=pd.read_csv("/Users/kassemhajjoul/Desktop/NLP/Book1.csv")
st.table(df)
st.sidebar.header("Options")
import datetime
options_form=st.form("options_form")
CustomerName=options_form.text_input("Customer Name")
Merchandise=options_form.text_input("Merchandise")
DeliveryAddress=options_form.text_input("Delivery Address")
Phone_Number=options_form.text_input("Phone Number")
TradeArea=options_form.selectbox('Trade Area', ('Beirut','Aley','Akkar','North','Jbeil','Tripoli','Jounieh','Mount Lebanon','Baabda','Chouf','Saida','Nabatieh','Tyr','Zgharta','South Lebanon','Bekaa','Baalbek'))
Notes=options_form.text_input("Notes")
today = datetime.date.today()
Date = options_form.date_input('Date', today)
distbeirut=10
distsaida=38
distnabatieh=67
disttyr=75
distsouth=80
distjbeil=39
distakkar=91
distmount=27
distbaabda=13
distchouf=30
distaley=16
distjounieh=17
distbekaa=43
distbaalbeck=72
disttripoli=77
distnorth=50
distzgharta=77
update_data=options_form.form_submit_button()
if update_data:
    New_data={"Name":CustomerName,"Merchandise":Merchandise,"Delivery Address":DeliveryAddress,"Date":Date,"TradeArea":TradeArea,"Phone Number":Phone_Number,"Notes":Notes}
    df=df.append(New_data,ignore_index=True)
    df["Date"]=pd.to_datetime(df["Date"],utc=False)
    df["Phone Number"]=df["Phone Number"].astype(str)
    st.write(df)
    if TradeArea=="Beirut":
        st.header("Delivery fee:")
        st.header(distbeirut*0.11)
    if TradeArea=="Saida":
        st.header("Delivery fee:")
        st.header(distsaida*0.11)
    if TradeArea=="Jbeil":
        st.header("Delivery fee:")
        st.header(distjbeil*0.11)
    if TradeArea=="Nabatieh":
        st.header("Delivery fee:")
        st.header(distnabatieh*0.11)
    if TradeArea=="Tyr":
        st.header("Delivery fee:")
        st.header(disttyr*0.11)
    if TradeArea=="South Lebanon":
        st.header("Delivery fee:")
        st.header(distsouth*0.11)
    if TradeArea=="Akkar":
        st.header("Delivery fee:")
        st.header(distakkar*0.11)
    if TradeArea=="Mount Lebanon":
        st.header("Delivery fee:")
        st.header(distmount*0.11)
    if TradeArea=="Baabda":
        st.header("Delivery fee:")
        st.header(distbaabda*0.11)
    if TradeArea=="Chouf":
        st.header("Delivery fee:")
        st.header(distchouf*0.11)
    if TradeArea=="Aley":
        st.header("Delivery fee:")
        st.header(distaley*0.11)
    if TradeArea=="Jounieh":
        st.header("Delivery fee:")
        st.header(distjounieh*0.11)
    if TradeArea=="Baalbek":
        st.header("Delivery fee:")
        st.header(distbaalbeck*0.11)
    if TradeArea=="Tripoli":
        st.header("Delivery fee:")
        st.header(disttripoli*0.11)
    if TradeArea=="North Lebanon":
        st.header("Delivery fee:")
        st.header(distnorth*0.11)
    if TradeArea=="Zgharta":
        st.header("Delivery fee:")
        st.header(distzgharta*0.11)
submit_form=st.form("submit_form")
submit_data=submit_form.form_submit_button()
if submit_data:
    New_data={"Name":CustomerName,"Merchandise":Merchandise,"Delivery Address":DeliveryAddress,"Date":Date,"TradeArea":TradeArea,"Phone Number":Phone_Number,"Notes":Notes}
    df=df.append(New_data,ignore_index=True)
    df["Date"]=pd.to_datetime(df["Date"],utc=False)
    df["Phone Number"]=df["Phone Number"].astype(str)    
    df.to_csv("/Users/kassemhajjoul/Desktop/NLP/Book1.csv",index=False)

