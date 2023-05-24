import streamlit as st

crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

def main():
    st.title("Fertilizer Recommendation System")
    nitrogen = st.text_input('Nitrogen', placeholder="Enter nitrogen value (20-120)")
    phosphorus = st.text_input('Phosphorous', placeholder='Enter phosphorous value (10-125)')
    potassium = st.text_input('Potassium', placeholder='Enter potassium value (10-200)')
    soil_moisture = st.text_input('Soil Moisture', placeholder='Enter soil moisture value (15-90)')
    ph = st.text_input('Ph Value', placeholder='Enter pH value (4.0-6.5)')
    crop = st.selectbox('Select Crop', crops)

    if st.button('Recommend Fertilizer'):
        if crop == 'rice':
            if 20 <= int(nitrogen) <= 120 and 10 <= int(phosphorus) <= 125 and 10 <= int(potassium) <= 200 and 15 <= int(soil_moisture) <= 90 and 4.0 <= float(ph) <= 6.5:
                st.success("The best fetilizer to use in rice is Urea. \n\n you can use locally available fertilizer like animal dung to increase land fertility as well as rice production \n\n धानमा प्रयोग गर्ने सबैभन्दा राम्रो मल युरिया हो। यूरिया प्रयोग गर्नुहोस् | \n\n जमिनको उर्वराशक्ति र धान उत्पादन बढाउन स्थानीय स्तरमा उपलब्ध मल जस्तै जनावरको गोबर प्रयोग गर्न सकिन्छ ।")
                st.image('images/143797_shutterstock_723175018.jpg', caption='Urea', use_column_width=True)
                st.image('images/istockphoto-684977254-612x612.jpg', caption='Animal dung', use_column_width=True)
            else:
                st.success("You have entered wrong input values for rice. Please check again.")
        elif crop == 'maize':
            if 30 <= int(nitrogen) <= 150 and 20 <= int(phosphorus) <= 135 and 15 <= int(potassium) <= 180 and 20 <= int(soil_moisture) <= 80 and 5.5 <= float(ph) <= 7.0:
                st.success("Recommended Fertilizer for maize: DAP (Diammonium Phosphate)")
            else:
                st.success("You have entered wrong input values for maize. Please check again.")
        else:
            st.success("Recommended Fertilizer for {} crop: Urea".format(crop))

if __name__ == '__main__':
    main()
