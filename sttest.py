import streamlit as st
import pandas as pd
st.header("this is a test")
# Using the "with" syntax
st.write("hey")
form1 = st.form(key='my-form1')
CustomerName = form1.text_input('Customer Name')
form2 = st.form(key='my-form2')
TradeArea = form2.text_input('Trade Area')
form3 = st.form(key='my-form3')
Merchandise = form3.text_input('Merchandise')
submit = form1.form_submit_button('Submit')
submit = form2.form_submit_button('Submit')
submit = form3.form_submit_button('Submit')
DeliveryArea = st.text_input('DeliveryArea')
data = {
    'Name': ['Hardik', 'Pollard', 'Bravo'],
    'Run': [50, 63, 15],
    'Wicket': [0, 2, 3],
    'Catch': [4, 2, 1]
}
data1={
    'CustomerName':CustomerName,
    'TradeArea': TradeArea,
    'Merchandise':Merchandise,
    'DeliveryArea':DeliveryArea
}
#df=pd.DataFrame(data1)
if submit:
    st.write(f'hello {CustomerName}')

    #https://drive.google.com/file/d/11l0hsl9FGYlzo6qFa_F0wEggI-vYgiSM/view?usp=sharing
            # User Data Entry
def user_report():
                Diabetes = st.slider('Diabetes',min_value =0,max_value=1,step=1)
                Stroke= st.slider('Previous Stroke',min_value =0,max_value=1,step=1)
                user_report_data = {
                'Diabetes': Diabetes,
                'Stroke' : Stroke,
                }
                report_data =pd.DataFrame(user_report_data, index = [0])
                return report_data
user_data = user_report()
user_data.to_csv('/Users/kassemhajjoul/Desktop/NLP/Book1.csv', mode='a', index=False, header=False)  
st.header('Guest Data')
st.table(user_data)