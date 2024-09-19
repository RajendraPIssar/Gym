import streamlit as st
import pandas as pd
import random
import base64

# Load the dataset
df = pd.read_csv(r"cleaned_megaGymDataset.csv", index_col=0)

# Dropping duplicates and NaN values
df.drop_duplicates(inplace=True, keep='first')
df.dropna(inplace=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the background image
add_bg_from_local(r"C:\Users\ACER\Downloads\background_image.jpg")  # Make sure the image is in the app's folder

# Dictionary of equipment images
equipment_images = {
    "Bands": "Bands.jpg",
    "Barbell": "barbell.jpg",
    "Body Only": "Body Only.jpg",
    "Barbell": "barbell.jpg",
    "Cable": "Cable Machine.jpg",
    "Dumbbell": "Dumbbell.jpg",
    "Exercise Ball": "ExerciseBall.jpg",
    "E-Z Curl Bar": "E-Z Curl Bar.jpg",
    "Foam Roll": "Foam Roll.jpg",
    "Kettlebells": "Kettlebell.jpg",
    "Machine": "Machine.jpg",
    "Medicine Ball": "Medicine Ball.jpg"
}

# Streamlit app code
st.title("Gym and Healthy Planner - Weekly Plan Generator")

# Dropdown checklist for exercise types (minimum 2 required)
exercise_types = ['Cardio', 'Olympic Weightlifting', 'Plyometrics', 'Powerlifting', 'Strength', 
                  'Stretching', 'Strongman']

selected_types = st.multiselect("Choose at least two exercise types", exercise_types)

if len(selected_types) < 2:
    st.warning("Please select at least two exercise types.")

# Input for age
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)

# Dropdown for number of muscles to train per day (2 or 3)
muscles_per_day = st.selectbox("How many muscles to train per day?", [2, 3])

# Button to generate weekly plan
if st.button("Generate Weekly Plan"):
    if len(selected_types) < 2:
        st.warning("You need to select at least two exercise types.")
    else:
        # Filter the DataFrame by selected exercise types
        filtered_df = df[df['Type'].isin(selected_types)]
        
        if age >= 50:
            # Randomly assign Beginner or Intermediate level if age is greater than or equal to 50
            filtered_df['Level'] = filtered_df.apply(
                lambda x: random.choice(['Beginner', 'Intermediate']), axis=1
            )
            
            # Check if there are enough exercises for each body part
            body_parts = filtered_df['BodyPart'].unique()
            if len(body_parts) < muscles_per_day:
                st.error("Not enough variety in body parts for the selected number of muscles per day.")
            else:
                # Generate the weekly plan
                weekly_plan = []
                for day in range(1, 8):  # 7 days in a week
                    # Ensure we have enough exercises and each body part is covered
                    daily_plan = []
                    available_body_parts = list(body_parts)
                    
                    for _ in range(muscles_per_day):
                        if available_body_parts:
                            body_part = random.choice(available_body_parts)
                            available_body_parts.remove(body_part)
                            
                            exercises_for_body_part = filtered_df[filtered_df['BodyPart'] == body_part]
                            if not exercises_for_body_part.empty:
                                exercise = exercises_for_body_part.sample(1).iloc[0]
                                daily_plan.append(exercise)
                    
                    # Prepare the output for each day
                    st.write(f"**Day {day}:**")
                    for _, row in pd.DataFrame(daily_plan).iterrows():
                        st.write(f"- **Exercise:** {row['Title']}")
                        st.write(f"  - **Body Part:** {row['BodyPart']}")
                        st.write(f"  - **Type:** {row['Type']}")
                        st.write(f"  - **Level:** {row.get('Level', 'Not Specified')}")
                        st.write(f"  - **Rating:** {row['Rating']}")
                        st.write(f"  - **Equipment:** {row['Equipment']}")
                        st.write(f"  - **Sets:** 4")
                        st.write(f"  - **Reps:** 8")
                        
                        # Display equipment image if available
                        equipment = row['Equipment']
                        if equipment in equipment_images:
                            st.image(equipment_images[equipment], caption=f"Equipment: {equipment}", use_column_width=True)

        else:
            # Handle users below 50
            min_exercises_per_type = 2
            exercises_per_day = muscles_per_day
            total_exercises_needed = 7 * exercises_per_day
            
            # Prepare a DataFrame to keep track of exercises to be included
            exercise_plan = pd.DataFrame()

            for exercise_type in selected_types:
                # Filter exercises by type and sort by rating (assuming a 'Rating' column exists)
                exercises_by_type = filtered_df[filtered_df['Type'] == exercise_type].sort_values(by='Rating', ascending=False)
                
                # Ensure at least 2 exercises of this type are included
                if len(exercises_by_type) < min_exercises_per_type:
                    st.error(f"Not enough exercises available for the type {exercise_type}.")
                    continue
                
                # Select the top exercises by rating
                exercises_to_include = exercises_by_type.head(min_exercises_per_type)
                exercise_plan = pd.concat([exercise_plan, exercises_to_include])
                
            # Randomly select exercises to fill the weekly plan
            remaining_exercises_needed = total_exercises_needed - len(exercise_plan)
            if remaining_exercises_needed > 0:
                remaining_exercises = filtered_df[~filtered_df.index.isin(exercise_plan.index)]
                # Ensure we do not try to sample more exercises than available
                if len(remaining_exercises) < remaining_exercises_needed:
                    remaining_exercises_needed = len(remaining_exercises)
                exercise_plan = pd.concat([exercise_plan, remaining_exercises.sample(n=remaining_exercises_needed)])

            # Generate weekly plan ensuring coverage
            plan_df = pd.DataFrame(exercise_plan)
            for day in range(1, 8):
                daily_plan = plan_df.sample(n=min(exercises_per_day, len(plan_df))).reset_index(drop=True)
                
                # Prepare the output for each day
                st.write(f"**Day {day}:**")
                for _, row in daily_plan.iterrows():
                    st.write(f"- **Exercise:** {row['Title']}")
                    st.write(f"  - **Body Part:** {row['BodyPart']}")
                    st.write(f"  - **Type:** {row['Type']}")
                    st.write(f"  - **Level:** {row.get('Level', 'Not Specified')}")
                    st.write(f"  - **Rating:** {row['Rating']}")
                    st.write(f"  - **Equipment:** {row['Equipment']}")
                    st.write(f"  - **Sets:** 4")
                    st.write(f"  - **Reps:** 8")

                    # Display equipment image if available
                    equipment = row['Equipment']
                    if equipment in equipment_images:
                        st.image(equipment_images[equipment], caption=f"Equipment: {equipment}", use_column_width=True)
