import streamlit as st

crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'banana', 'mango', 'grapes', 'watermelon', 'apple', 'orange']

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
    elif crop == 'mothbeans':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-40)",'Enter potassium value (0-20)','Enter soil moisture value (0-30)','Enter pH value (0.0-5.5)')
    elif crop == 'mungbean':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-40)",'Enter potassium value (0-20)','Enter soil moisture value (0-80)','Enter pH value (0.0-5.5)')
    elif crop == 'banana':
        return ("Enter nitrogen value (0-100)","Enter phosphorous value (0-75)",'Enter potassium value (0-50)','Enter soil moisture value (0-40)','Enter pH value (0.0-6.5)')
    elif crop == 'mango':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-20)",'Enter potassium value (0-30)','Enter soil moisture value (0-15)','Enter pH value (0-5)')
    elif crop == 'grapes':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-125)",'Enter potassium value (0-200)','Enter soil moisture value (0-60)','Enter pH value (0-4)')
    elif crop == 'watermelon':
        return ("Enter nitrogen value (0-100)","Enter phosphorous value (0-10)",'Enter potassium value (0-50)','Enter soil moisture value (0-60)','Enter pH value (0-4)')
    elif crop == 'apple':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-125)",'Enter potassium value (0-200)','Enter soil moisture value (0-50)','Enter pH value (0.0-6.5)')
    elif crop == 'orange':
        return ("Enter nitrogen value (0-20)","Enter phosphorous value (0-10)",'Enter potassium value (0-10)','Enter soil moisture value (0-60)','Enter pH value (0-4)')
    else:
        return "Nothing"
    
def main():
    st.image('images/header.png')
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
                st.image('https://d2cbg94ubxgsnp.cloudfront.net/Pictures/480x270/7/9/7/143797_shutterstock_723175018.jpg', caption='Urea (युरिया)', use_column_width=True)
                st.image('https://businessfocus.co.ug/wp-content/uploads/2020/07/Manure.jpg', caption='Animal dung (जनावरको गोबर)', use_column_width=True)
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
        elif crop == 'mothbeans':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 40 and 0 <= int(potassium) <= 20 and 0 <= int(soil_moisture) <= 30 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in moth beans is NPK . \n\n Organic fertlizers like fish emulsion, seaweed extract, and bone meal would be good for moth beans than inorganic fertilizers.\n\n मोथ बीन्समा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK हो। जैविक मलहरू जस्तै माछा इमल्शन, समुद्री शैवाल निकासी, र हड्डीको खाना अकार्बनिक मलहरू भन्दा माथ बीन्सका लागि राम्रो हुन्छ। म अर्गानिक मल प्रयोग गर्न सुझाव दिन्छु ")
                st.image('https://m.media-amazon.com/images/I/71yy+QZTCHL._SX466_.jpg',caption='NPk',use_column_width=True)
            else:
                st.success("You have entered wrong input values for moth beans. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'mungbean':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 40 and 0 <= int(potassium) <= 20 and 0 <= int(soil_moisture) <= 80 and 0.0 <= float(ph) <= 5.5:
                st.success("The best fertilizer to use in mung beans is NPK 10-10-10 which contains 10% of nitrogen,phosphrous and potassium. \n\n Organic fertlizers like compost manure would be better alternative to use than inorganic fertilizers.\n\n  मुग दालमा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 10-10-10 हो जसमा 10% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n अजैविक मल भन्दा कम्पोष्ट मल जस्ता प्राङ्गारिक मल प्रयोगको लागि उत्तम विकल्प हुनेछ।")
                st.image('https://n1.sdlcdn.com/imgs/j/n/y/Greatindos-Premium-Quality-1000gram-NPK-SDL289482178-1-a9d2a.jpg',caption='NPK 10-10-10',use_column_width=True)
                st.image('https://www.agrifarming.in/wp-content/uploads/2015/03/Organic-Compost.jpg',caption='Compost Manure (कम्पोस्ट मल)',use_column_width=True)
            else:
                st.success("You have entered wrong input values for mung bean. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'banana':
            if 0 <= int(nitrogen) <= 100 and 0 <= int(phosphorus) <= 75 and 0 <= int(potassium) <= 50 and 0 <= int(soil_moisture) <= 40 and 0.0 <= float(ph) <= 6.5:
                st.success("The best fertilizer to use in banana is NPK 14-14-14 which contains 14% of nitrogen,phosphrous and potassium. \n\n Locally available well-rotted animal manure, such as cow or horse manure, can be an effective organic fertilizer for banana plants\n\n  केरामा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 14-14-14 हो जसमा 10% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n स्थानीय रूपमा उपलब्ध राम्ररी सडेको पशु मल, जस्तै गाई वा घोडाको मल, केराको बोटको लागि प्रभावकारी जैविक मल हुन सक्छ।")
                st.image('https://partners.simplot.com/-/media/simplot-mvc/simplot-partners/images/products/best-and-apex/74420_apex_14-14-14_bag_mockup2-a1200x1200-jpg.jpg?h=600&la=en&mw=600&w=600',caption='NPK 14-14-14',use_column_width=True)
            else:
                st.success("You have entered wrong input values for banana. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'mango':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 20 and 0 <= int(potassium) <= 30 and 0 <= int(soil_moisture) <= 15 and 0 <= int(ph) <= 5:
                st.success("The best fertilizer to use in banana is NPK 14-14-14 which contains 14% of nitrogen,phosphrous and potassium. \n\n Locally available well-rotted animal manure, such as cow or horse manure, can be an effective organic fertilizer for banana plants\n\n  केरामा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 14-14-14 हो जसमा 10% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n स्थानीय रूपमा उपलब्ध राम्ररी सडेको पशु मल, जस्तै गाई वा घोडाको मल, केराको बोटको लागि प्रभावकारी जैविक मल हुन सक्छ।")
                st.image('https://partners.simplot.com/-/media/simplot-mvc/simplot-partners/images/products/best-and-apex/74420_apex_14-14-14_bag_mockup2-a1200x1200-jpg.jpg?h=600&la=en&mw=600&w=600',caption='NPK 14-14-14',use_column_width=True)
            else:
                st.success("You have entered wrong input values for mango. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'grapes':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 125 and 0 <= int(potassium) <= 200 and 0 <= int(soil_moisture) <= 60 and 0 <= int(ph) <= 4:
                st.success("The best fertilizer to use in grapes is NPK 14-14-14 which contains 14% of nitrogen,phosphrous and potassium. \n\n Locally available well-rotted animal manure, such as cow or horse manure, can be an effective organic fertilizer for grapes plants\n\n  अंगूरमा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 14-14-14 हो जसमा 10% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n स्थानीय रूपमा उपलब्ध राम्ररी सडेको पशु मल, जस्तै गाई वा घोडाको मल, अंगूरको बोटको लागि प्रभावकारी जैविक मल हुन सक्छ।")
                st.image('https://partners.simplot.com/-/media/simplot-mvc/simplot-partners/images/products/best-and-apex/74420_apex_14-14-14_bag_mockup2-a1200x1200-jpg.jpg?h=600&la=en&mw=600&w=600',caption='NPK 14-14-14',use_column_width=True)
            else:
                st.success("You have entered wrong input values for grapes. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'watermelon':
            if 0 <= int(nitrogen) <= 100 and 0 <= int(phosphorus) <= 10 and 0 <= int(potassium) <= 50 and 0 <= int(soil_moisture) <= 60 and 0 <= int(ph) <= 4:
                st.success("The best fertilizer to use in watermelon is NPK 10-10-10 which contains 10% of nitrogen,phosphrous and potassium. \n\n Seaweed  as organic fertilizer enhances plant growth, improves fruit quality, and helps plants withstand stress\n\n  तरबूजमा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 10-10-10 हो जसमा 10% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n जैविक मलको रूपमा समुद्री शैवाल निकासीले बिरुवाको वृद्धि बढाउँछ, फलको गुणस्तर सुधार गर्छ, र बोटबिरुवाहरूलाई तनाव सहन मद्दत गर्छ")
                st.image('https://n1.sdlcdn.com/imgs/j/n/y/Greatindos-Premium-Quality-1000gram-NPK-SDL289482178-1-a9d2a.jpg',caption='NPK 10-10-10',use_column_width=True)
                st.image('https://www.agrifarming.in/wp-content/uploads/2022/10/Seaweed-Extract-Uses-in-Agriculture1-1024x768.jpg',caption='Seaweed (समुद्री शैवाल)')
            else:
                st.success("You have entered wrong input values for watermelon. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'apple':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 125 and 0 <= int(potassium) <= 200 and 0 <= int(soil_moisture) <= 50 and 0.0 <= int(ph) <= 6.5:
                st.success("The best fertilizer to use in apple is NPK 12-12-12 which contains 12% of nitrogen,phosphrous and potassium. \n\n Blood meal, soybean meal, composted chicken manure, cottonseed meal, and feather meal are all good, organic nitrogen sources for apple\n\n  तरबूजमा प्रयोग गर्ने सबैभन्दा राम्रो मल NPK 12-12-12 हो जसमा 12% नाइट्रोजन, फस्फ्रस र पोटासियम हुन्छ। \n\n रगतको खाना, भटमासको खाना, कम्पोष्ट गरिएको कुखुराको मल, कपासको बीउ र फेदर मील सबै राम्रो, स्याउका लागि जैविक नाइट्रोजन स्रोत हुन्।")
                st.image('https://partners.simplot.com/-/media/simplot-mvc/simplot-partners/images/products/best-and-apex/15010_12-12-12-conceptualmockup_2016-a1200x1200-jpg.jpg?h=600&la=en&mw=600&w=600',caption='NPK 12-12-12',use_column_width=True)
            else:
                st.success("You have entered wrong input values for apple. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        elif crop == 'orange':
            if 0 <= int(nitrogen) <= 20 and 0 <= int(phosphorus) <= 10 and 0 <= int(potassium) <= 10 and 0 <= int(soil_moisture) <= 60 and 0 <= int(ph) <= 4:
                st.success("The best fertilizer to use in orange is Jack's Class No.1.5 20-10-20 Citrus Food Fertilizer.\n\n Composted manure is organic orange fertilizer that can be added to the soil around the base of the tree or used as mulch. It is an excellent source of organic matter and other nutrients for oragne trees.\n\n  सुन्तलामा प्रयोग गर्नको लागि सबैभन्दा राम्रो मल ज्याकको कक्षा नं.1.5 20-10-20 सिट्रस फूड उर्वरक हो।\n\n कम्पोस्ट गरिएको मल जैविक सुन्तला मल हो जुन रूखको आधार वरपरको माटोमा थप्न सकिन्छ वा मल्चको रूपमा प्रयोग गर्न सकिन्छ। यो orange रूखहरूको लागि जैविक पदार्थ र अन्य पोषक तत्वहरूको उत्कृष्ट स्रोत हो।")
                st.image('https://cdn.shopify.com/s/files/1/0594/5583/2249/products/citrusfeed_1200x918.png?v=1675022344',caption='Jacks Class No.1.5 20-10-20 Citrus Food Fertilizer',use_column_width=True)
            else:
                st.success("You have entered wrong input values for orange. Please check again. \n\n तपाईंले गलत इनपुट दिनुभएको छ कृपया राम्रोसँग जाँच गर्नुहोस् र पुन: प्रयास गर्नुहोस्")
        else:
            st.success("Recommended Fertilizer for {} crop: Urea".format(crop))

if __name__ == '__main__':
    main()
