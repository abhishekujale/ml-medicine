import streamlit as st
import pickle
import pandas as pd


# st.markdown("[HOME](http://127.0.0.1:5000/home)", unsafe_allow_html=True)
                                        ## To Add External CSS ##
with open('css/style.css') as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


                                        ## Application Backend ##

                    # To load medicine-dataframe from pickle in the form of dictionary
medicines_dict = pickle.load(open('medicine_dict.pkl','rb'))
medicines = pd.DataFrame(medicines_dict)

                    # To load similarity-vector-data from pickle in the form of dictionary
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(medicine):
     medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
     distances = similarity[medicine_index]
     medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_medicines = []
     for i in medicines_list:
         recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
     return recommended_medicines

                                   # Title of the Application
st.title('Alternative Medicine Recommender System')
# st.header("Home")

                                        # Searchbox
selected_medicine_name = st.selectbox(
'Medicine Name',
     medicines['Drug_Name'].values)


                                   # Recommendation Program
if st.button('Alternative Medicine'):
     recommendations = recommend(selected_medicine_name)
     j=1
     for i in recommendations:
          st.write(j,i)                      # Recommended-drug-name
         
          j+=1



                                         ## Image load ##
# from PIL import Image
# image = Image.open('images/images.jpeg')
# st.image(image, caption='Recommended Medicines')


