import streamlit as st
import pickle
import numpy as np
import base64
import time

model = pickle.load(open('Pickle_RL_Model.pkl','rb'))

def main():
    string = "Offical Release"
    st.set_page_config(page_title=string, page_icon="chart_with_upwards_trend")
    st.header("HEALTHMATE YOUR HEALTH BUDDY!!!!!!!!!!!!!!!!!")
    st.header("Your HeathSolution at one place!!!!!")
    st.markdown("##### Are you planning to buy Medical Insurance!?\n##### So let's try evaluating the amount.. 🤖 ")
    st.image(
            "https://cdn.pixabay.com/photo/2021/05/10/10/19/car-crash-6243099_960_720.jpg",
            width=500, # Manually Adjust the width of the image as per requirement
 )
    st.sidebar.metric(label="Made By", value="Aditya Bhatt")
    st.sidebar.header("Know Your chances of getting diabetes")
    st.sidebar.subheader("https://diabetesmodel12.herokuapp.com/")
    st.sidebar.header("Know Your chances of getting Stroke") 
    st.sidebar.subheader("https://strokeapp1.herokuapp.com/")
    st.sidebar.header("Get to know about country's Mental Health(Happiness Score):")
    st.sidebar.subheader("https://happynessindex.herokuapp.com/")
    age = st.slider('What is your Age?',0, 90, step=1, key ='age')
    sex=st.radio("Select your Gender ?", ("Male", "Female"), key ='sex')
    if sex=="Male":
        gender=0
    else:
        gender=1
    rating= st.slider('What is your BMI?',10,60 ,step=1, key ='bmi')
    children= st.slider('How many children you have?',0, 10, step=1, key ='children')
    smoke= st.radio('Do your smoke?',("Yes","No") ,key ='smoker')
    if smoke=="Yes":
        smoking=1
    else:
        smoking=0
    place=st.radio("Where do you live", ("Southeast", "Northeast","Northwest",'Southwest') ,key='region')
    if place=="Southeast":
        region=1
    elif place=="Northeast":
        region=2
    elif place=="Northwest":
        region=3
    else:
        region=4


    if st.button("Estmate your Medical Insurance", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[age,gender,rating,children,smoking,region]])
            output =np.round(prediction[0],2)
            if output<0:
                st.warning("Some error is there !!")
            else:
                st.success("Your medical insurance is estimated to be ${} 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")



if __name__ == '__main__':
    main()