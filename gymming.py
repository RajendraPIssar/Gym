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
add_bg_from_local(r"background_image.jpg")  # Make sure the image is in the app's folder

# Dictionary of equipment images
equipment_images = {
    "Bands": "Bands.jpg",
    "Barbell": "barbell.jpg",
    "Body Only": "Body Only.jpg",
    "Cable": "Cable Machine.jpg",
    "Dumbbell": "Dumbbell.jpg",
    "Exercise Ball": "ExerciseBall.jpg",
    "E-Z Curl Bar": "E-Z Curl Bar.jpg",
    "Foam Roll": "Foam Roll.jpg",
    "Kettlebells": "Kettlebell.jpg",
    "Machine": "Machine.jpg",
    "Medicine Ball": "Medicine Ball.jpg"
}

# Dictionary to map exercise titles to video (GIF) paths
exercise_videos = {
    "Close-grip bench press": r"bench-press-regular-bench-press.gif.mp4",
    exercise_videos = {
    "Close-grip bench press": r"bench-press-regular-bench-press.gif.mp4",
    "Partner plank band row":"17d1d9804a967bd3378445dff31b9f8b.gif",
    "Banded crunch isometric hold":"055920ed631d97d2501744cf85f19fd4.gif",
    "FYR Banded Plank Jack" : "giphy.gif" ,
    "Crunch":"7BhM.gif",
    "Decline band press sit-up":"xdb-48n-decline-band-press-sit-up-m2-16x9.jpg",
    "Band low-to-high twist":"resistance-band-pull-up-standing-twists-exercise.gif",
    "Barbell roll-out":"27627.gif",
    "Barbell Ab Rollout - On Knees":"294.gif",
    "Decline bar press sit-up":"xdb-44n-decline-press-sit-up-m2-16x9.jpeg",
    "Bench barbell roll-out":"xdb-85e-bench-barbell-roll-out-m1-16x9.jpeg",
    "Barbell Side Bend":"Barbell Side Bend.gif",
    "Seated bar twist":"4830.gif",
    "Single-arm landmine pull and press":"2_0330a930-6d73-4070-8dc3-9f34225eadb4.webp",
    "30 Barbell":"barbell-rollout-hip.jpeg",
    "Decline plate sit-up":"xdb-40n-decline-plate-sit-up-m2-16x9.jpeg",
    "KV Barbell Hip Thrust":"KV Barbell Hip Thrust.jpg",
    "Kettlebell Windmill": r"19155.gif",
    "Dumbbell V-Sit Cross Jab": r"22963.gif",
    "Dumbbell spell caster": r"5501.gif",
    "Dumbbell side bend": r"4587.jpg",
    "Landmine twist": r"15365.gif",
    "Sledgehammer swing": r"7844.jpg",
    "Cable reverse crunch": r"11751.gif",
    "Leg Pull-In": r"336.gif",
    "Adductor SMR": r"xdb-9s-adductor-smr-m2-16x9.jpg",
    "Thigh adductor": r"25465.jpg",
    "Lateral hop": r"XWHWRL.gif",
    "Single-leg lying cross-over stretch": r"9274.gif",
    "Standing hip circle": r"2864.jpg",
    "Brachialis SMR": r"Brachialis-SMR-perspectyve.gif",
    "Wide-grip barbell curl": r"barbell-standing-wide-grip-biceps-curl-exercise.gif",
    "Close-grip EZ-bar curl": r"352.jpg",
    "Preacher Curl": r"483623.jpg",
    "Close-grip barbell curl": r"1023947.jpg",
    "Drag curl": r"213463.jpg",
    "Reverse-grip barbell curl": r"192846.jpg",
    "Biceps curl to shoulder press": r"293856.jpg",
    "Concentration curl": r"12947.jpg",
    "Dumbbell Bicep Curl": r"2384y.jpg",
    "Cross-body hammer curl": r"98.gif",
    "Standing concentration curl": r"the-optimal-you-standing-concentration-curls.jpg",
    "Alternate Hammer Curl": r"alternating-dumbbell-hammer-curl-exercise.gif",
    "Standing Dumbbell Reverse Curl": r"12345.jpg",
    "Palms-out incline biceps curl": r"92364.jpg",
    "Straight-arm plank with biceps curl": r"plank-straight-arm-kickback-exercise-illustration-spotebi.gif",
    "Face-down incline dumbbell biceps curl": r"232619.jpg",
    "Plate hammer curl": r"20347.jpg",
    "Overhead cable curl": r"3927.jpg",
    "Standing One-Arm Cable Curl": r"One-Arm-Cable-Curl.gif",
    "Standing Biceps Cable Curl": r"14911.gif",
    "Cable rope hammer curl": r"29521.jpg",
    "Lying cable biceps curl": r"12523.jpg",
    "Cable rope preacher hammer curl": r"7252.gif",
    "Lying Close-Grip Bar Curl On High Pulley": r"143254.jpg",
    "Machine Preacher Curls": r"252324.jpg",
    "EZ-Bar Curl": r"235212.jpg",
    "Calf SMR": r"213251233.jpg",
    "Standing barbell calf raise": r"23523.jpg",
    "Weighted donkey calf raise": r"2352323.jpg",
    "Smith Machine Calf Raise": r"23523423.jpg",
    "Standing Calf Raises": r"23058.jpg",
    "Calf Raise": r"2347324.jpg",
    "Wall calf stretch": r"937dd77b8c95826c3033a14c9e60e9bc",
    "Close-grip bench press": r"2035720.jpg",
    "bench press": r"bcd205cf9e64811981d715deebaa41da.gif",
    "Pushups": r"pushup.gif",
    "Incline Push-Up": r"incline.jpg",
    "Palms-down wrist curl over bench": r"29364.jpg",
    "Palms-up wrist curl over bench": r"027348.jpg",
    "Standing behind-the-back wrist curl": r"20358023.gif",
    "finger curl": r"8263492.jpg",
    "Seated palms-up wrist curl": r"26375629.jpg",
    "Seated palms-down wrist curl": r"Palms+Down+Barbell+Wrist+Curl.jpeg",
    "Partner farmer's walk": r"62934729.jpg",
    "Suitcase Dumbbell Carry": r"72534.jpg",
    "Dumbbell farmer's walk": r"592364.jpg",
    "Piriformis SMR": r"6237854.jpg",
    "Barbell glute bridge": r"23567.jpg",
    "Kettlebell thruster": r"73764.jpg",
    "Single-leg cable hip extension": r"00478e1c27d437375b18bd18ff008d52.gif",
    "Standing hip extension": r"2354.jpg",
    "Lying glute stretch": r"37246.jpg",
    "Exercise ball hip thrust": r"2358629.jpg",
    "Scissors Jump": r"scissor-skier-exercise-illustration.jpg",
    "Bar shoulder extension stretch": r"823dh.jpg",
    "Incline EZ-bar skullcrusher": r"23984629.jpg",
    "Behind-the-head skullcrusher": r"348562.jpg",
    "Standing barbell overhead triceps extension": r"235230.jpg",
    "Reverse-grip bench press": r"9375.jpg",
    "Dumbbell floor press": r"7234.jpg",
    "Seated triceps press": r"23964.jpg",
    "Tricep Dumbbell Kickback": r"23875.jpg",
    "Double-arm triceps kick-back": r"db-tricep-kickback.gif",
    "Single-arm dumbbell triceps extension": r"2783864.jpg",
    "Dumbbell skullcrusher": r"872364.jpg",
    "Reverse Grip Triceps Pushdown": r"24786.gif",
    "Incline cable straight-bar triceps extension": r"82357.jpg",
    "Machine Triceps Extension": r"253.gif",
    "Bodyweight triceps press": r"273549.jpg",
    "EZ-Bar Skullcrusher": r"283r6w.jpg"

    # Add more exercise titles and their corresponding GIF paths
}

    # Add more exercise titles and their corresponding video paths
}

# Function to display video
def display_video(video_path, title, width=300):
    st.write(f"**{title}**")  # Display title as caption above the video
    st.video(video_path, start_time=0)  # Use st.video to display MP4

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
                        
                        # Display exercise video if available
                        exercise_title = row['Title']
                        if exercise_title in exercise_videos:
                            video_path = exercise_videos[exercise_title]
                            display_video(video_path, exercise_title)

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
                    
                    # Display exercise video if available
                    exercise_title = row['Title']
                    if exercise_title in exercise_videos:
                        video_path = exercise_videos[exercise_title]
                        display_video(video_path, exercise_title)
