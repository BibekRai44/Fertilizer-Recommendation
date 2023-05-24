import streamlit as st

crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

def get_placeholder(crop):
    if crop == 'rice':
        return ("Enter nitrogen value (0-80)","Enter phosphorous value (0-40)",'Enter potassium value (0-40)','Enter soil moisture value (0-30)','Enter pH value (0.0-5.5)')
    elif crop == 'maize':
        return ("Enter nitrogen value (0-80)","Enter phosphorous value (0-40)",'Enter potassium value (0-40)','Enter soil moisture value (0-30)','Enter pH value (0.0-5.5)')
    else:
        return "Nothing"
    
def main():
    st.title("Fertilizer Recommendation System")
    crop = st.selectbox('Select Crop', crops)
    placeholders = get_placeholder(crop)
    nitrogen = st.text_input('Nitrogen', placeholder=placeholders[0])
    phosphorus = st.text_input('Phosphorous', placeholder=placeholders[1])
    potassium = st.text_input('Potassium', placeholder=placeholders[2])
    soil_moisture = st.text_input('Soil Moisture', placeholder=placeholders[3])
    ph = st.text_input('Ph Value',placeholder=placeholders[4])

    if st.button('Recommend Fertilizer'):
        if crop == 'rice':
            if 0 <= int(nitrogen) <= 80 and 0 <= int(phosphorus) <= 40 and 0 <= int(potassium) <= 40 and 0 <= int(soil_moisture) <= 30 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in rice is Urea. \n\n you can use locally available fertilizer like animal dung to increase land fertility as well as rice production \n\n धानमा प्रयोग गर्ने सबैभन्दा राम्रो मल युरिया हो। यूरिया प्रयोग गर्नुहोस् | \n\n जमिनको उर्वराशक्ति र धान उत्पादन बढाउन स्थानीय स्तरमा उपलब्ध मल जस्तै जनावरको गोबर प्रयोग गर्न सकिन्छ ।")
                st.image('images/143797_shutterstock_723175018.jpg', caption='Urea (युरिया)', use_column_width=True)
                st.image('images/istockphoto-684977254-612x612.jpg', caption='Animal dung (जनावरको गोबर)', use_column_width=True)
            else:
                st.success("You have entered wrong input values for rice. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'maize':
            if 0 <= int(nitrogen) <= 80 and 0 <= int(phosphorus) <= 40 and 0 <= int(potassium) <= 40 and 0 <= int(soil_moisture) <= 50 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in maize is NPK 15:15:15 which contains 15% of nitrogen,phosphrous and potassium. \n\n Locally available organic fertilizer like animal dung would be perfect to yield maize production. \n\n मकैमा प्रयोग गर्ने उत्तम मल NPK 15:15:15 हो जसमा 15% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n स्थानीय रूपमा उपलब्ध जैविक मल जस्तै जनावरको गोबर मकै उत्पादन गर्न उपयुक्त हुनेछ।")
                st.image('https://saprotan-utama.com/wp-content/uploads/2020/11/15_NPK151515.jpg',caption='NPK 15:15:15')
                st.image('https://www.wur.nl/upload/5160f541-9f91-44b7-bfbc-08e0f4727505_shutterstock_1284414196.jpg',caption='Animal manure (पशु मल)',use_column_width=True)
            else:
                st.success("You have entered wrong input values for maize. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        else:
            st.success("Recommended Fertilizer for {} crop: Urea".format(crop))

if __name__ == '__main__':
    main()
