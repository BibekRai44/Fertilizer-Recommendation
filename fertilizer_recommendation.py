import streamlit as st

crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

def get_placeholder(crop):
    if crop == 'rice':
        return ("Enter nitrogen value (0-80)","Enter phosphorous value (0-40)",'Enter potassium value (0-40)','Enter soil moisture value (0-30)','Enter pH value (0.0-5.5)')
    elif crop == 'maize':
        return ("Enter nitrogen value (0-80)","Enter phosphorous value (0-40)",'Enter potassium value (0-40)','Enter soil moisture value (0-30)','Enter pH value (0.0-5.5)')
    elif crop == 'chickpea':
        return ("Enter nitrogen value (0-40)","Enter phosphorous value (0-60)",'Enter potassium value (0-80)','Enter soil moisture value (0-60)','Enter pH value (0.0-5.5)')
    elif crop == 'kidneybeans':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-60)",'Enter potassium value (0-20)','Enter soil moisture value (0-45)','Enter pH value (0.0-5.5)')
    elif crop == 'pigeonpeas':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-60)",'Enter potassium value (0-20)','Enter soil moisture value (0-45)','Enter pH value (0.0-5.5)')
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
        elif crop == 'chickpea':
            if 0 <= int(nitrogen) <= 40 and 0 <= int(phosphorus) <= 60 and 0 <= int(potassium) <= 80 and 0 <= int(soil_moisture) <= 60 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in chickpea is NPK 5:10:10 which is low in nitrogen (N) and higher in potassium (P) and phosphorus (K). \n\n Locally available organic fertilizer like animal dung would be perfect to yield chickpeas production. \n\n चनामा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 5:10:10 हो जसमा नाइट्रोजन (N) कम र पोटासियम (P) र फस्फोरस (K) बढी हुन्छ। \n\n स्थानीय रूपमा उपलब्ध जैविक मल जस्तै जनावरको गोबर चना उत्पादन गर्न उपयुक्त हुनेछ।")
                st.image('https://i.etsystatic.com/23088193/r/il/885022/3716760807/il_fullxfull.3716760807_hfje.jpg',caption='NPK 5:10:10')
                st.image('https://www.wur.nl/upload/5160f541-9f91-44b7-bfbc-08e0f4727505_shutterstock_1284414196.jpg',caption='Animal manure (पशु मल)',use_column_width=True)
            else:
                st.success("You have entered wrong input values for chickpea. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'kidneybeans':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 60 and 0 <= int(potassium) <= 20 and 0 <= int(soil_moisture) <= 45 and 0.0 <= float(ph) <= 5.5:
                st.success("Kidney beans do not need much specific fertiliser. As they are legumes their roots have nodules that contain bacteria that will fix nitrogen, so they can grow even in nitrogen poor soils. They grow best in rich soil containing compost or other organic matter \n\n किड्नी बीन्सलाई खास मलको आवश्यकता पर्दैन। तिनीहरू फलफूल भएकाले तिनीहरूको जरामा नोडलहरू हुन्छन् जसमा ब्याक्टेरिया हुन्छन् जसले नाइट्रोजनलाई ठीक गर्छ, त्यसैले तिनीहरू नाइट्रोजन कम माटोमा पनि बढ्न सक्छन्। तिनीहरू कम्पोस्ट वा अन्य जैविक पदार्थ भएको समृद्ध माटोमा राम्रोसँग बढ्छन् | \n\n स्थानीय रूपमा उपलब्ध जैविक मल जस्तै जनावरको गोबर चना उत्पादन गर्न उपयुक्त हुनेछ।")
                st.image('https://www.wur.nl/upload/5160f541-9f91-44b7-bfbc-08e0f4727505_shutterstock_1284414196.jpg',caption='Animal manure (पशु मल)',use_column_width=True)
            else:
                st.success("You have entered wrong input values for kidneybeans. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'pigeonpeas':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 60 and 0 <= int(potassium) <= 20 and 0 <= int(soil_moisture) <= 45 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in pigeonpeas is DAP (Diammonium Phosphate). DAP is a commonly used fertilizer that provides a balanced supply of nitrogen and phosphorus, which are essential nutrients for pigeonpea plants. It promotes healthy plant growth, improves yield, and enhances the overall quality of the harvested crop.\n\nपरेवा दाना प्रयोग गर्ने सबैभन्दा राम्रो मल डीएपी (डायमोनियम फास्फेट) हो। डीएपी सामान्यतया प्रयोग हुने मल हो जसले नाइट्रोजन र फस्फोरसको सन्तुलित आपूर्ति प्रदान गर्दछ, जुन परेवा दाना बोटका लागि आवश्यक पोषक तत्व हुन्। यसले स्वस्थ बिरुवाको वृद्धिलाई बढावा दिन्छ, उत्पादनमा सुधार गर्छ, र फसल बालीको समग्र गुणस्तर बढाउँछ | \n\n स्थानीय रूपमा उपलब्ध जैविक मल जस्तै जनावरको गोबर परेवा दाना उत्पादन गर्न उपयुक्त हुनेछ।")
                st.image('https://static-01.daraz.pk/p/ab4cb3c33dcce9ac0534708393c578c7.jpg',caption='DAP',use_column_width=True)
                st.image('https://www.wur.nl/upload/5160f541-9f91-44b7-bfbc-08e0f4727505_shutterstock_1284414196.jpg',caption='Animal manure (पशु मल)',use_column_width=True)
            else:
                st.success("You have entered wrong input values for pigeon peas. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        else:
            st.success("Recommended Fertilizer for {} crop: Urea".format(crop))

if __name__ == '__main__':
    main()
