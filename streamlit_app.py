# lets start

import random 
import streamlit as st # both are functions necessary, random for randomisation and st for the website

#here we can define the activities we want, the categories and how many in each one

warmer_activities = ["Speed dating", "Dance the Topic", "Pass the PASSel",
                      "OK, A bit foggy, No idea!", "Snowball", "Back to the board (Celebrity Head)"]

activity_1 = ["Jigsaw", "Moving Questions", "Lecture Summary", "KWLS Knowledge Reflection",
              "Teach Your Grandma", "Students Q, A & M"]

# so on so forth, depending on how many and what activities you would like in each category depends on you as a plf! :)

st.title("UniPASS Random Session Plan Generator!") # the title for our page

if st.button("Generate Random Session Plan"):
    st.write('### Your Random UniPASS Session Plan:')
    st.write(f"**Warmer:** {random.choice(warmer_activities)}")
    st.write(f"**Activity 1:** {random.choice(activity_1)}") # all the little symbols around the words are just formatting, the random.choice chooses an activity from that category randomly!


#Thats all! You can choose however many activities you would like and as many categories as you would like, using a random unipass session generator :)
#Thanks :)
