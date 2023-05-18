import streamlit as st

crop_fertilizer_mapping = {
    "rice": {"N": 80, "P": 40, "K": 40, "pH": 5.5, "soil_moisture": 30},
    "maize": {"N": 80, "P": 40, "K": 20, "pH": 5.5, "soil_moisture": 50},
    "chickpea": {"N": 40, "P": 60, "K": 80, "pH": 5.5, "soil_moisture": 60},
    # Add more crops and their corresponding chemical values here
}

fertilizer_recommendations = {
    "NPK Fertilizer": "Apply NPK Fertilizer as per crop's requirement.",
    "Nitrogen Fertilizer": "Apply Nitrogen Fertilizer as per crop's requirement.",
    "Phosphorus Fertilizer": "Apply Phosphorus Fertilizer as per crop's requirement.",
    # Add more fertilizer recommendations here
}

def recommend_fertilizer(crop, chemical_values):
    # Retrieve the recommended fertilizer for the selected crop from the mapping
    recommended_fertilizer = ""

    if crop in crop_fertilizer_mapping:
        crop_values = crop_fertilizer_mapping[crop]
        # Compare the provided chemical values with the crop's values
        if all(chemical_values[key] >= crop_values[key] for key in chemical_values):
            recommended_fertilizer = "NPK Fertilizer"
        elif chemical_values["N"] >= crop_values["N"]:
            recommended_fertilizer = "Nitrogen Fertilizer"
        elif chemical_values["P"] >= crop_values["P"]:
            recommended_fertilizer = "Phosphorus Fertilizer"
        # Add more fertilizer recommendations based on your criteria

    return recommended_fertilizer

def main():
    st.title("Fertilizer Recommendation System")

    crop = st.selectbox("Select Crop", [""] + list(crop_fertilizer_mapping.keys()))

    if crop:
        st.subheader("Enter Chemical Values for {}".format(crop))
        chemical_values = {
            "N": st.number_input("Nitrogen"),
            "P": st.number_input("Phosphorus"),
            "K": st.number_input("Potassium"),
            "pH": st.number_input("pH Value"),
            "soil_moisture": st.number_input("Soil Moisture")
        }

        recommended_fertilizer = recommend_fertilizer(crop, chemical_values)
        if recommended_fertilizer:
            fertilizer_description = fertilizer_recommendations.get(recommended_fertilizer, "")
            st.success("Recommended Fertilizer for {}: {}".format(crop, recommended_fertilizer))
            st.info(fertilizer_description)
        else:
            st.warning("No specific recommendation for the selected crop and chemical values")

if __name__ == "__main__":
    main()
