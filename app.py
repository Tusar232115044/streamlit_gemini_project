import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate note summary and quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")

    images = st.file_uploader("Upload photos of your file", type = ['jpg','jpeg','png'], accept_multiple_files = True)

    pill_image = []

    for img in images:
            
        pill_img = Image.open(img)
            
        pill_image.append(pill_img)

    if images:
    
        if len(images) > 3:
            st.error("Upload at maximum 3 images") 
        else: 
            st.subheader("Uploaded images")   
            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)


    selected_option = st.selectbox("Enter the difficulty of your quiz", ('Easy','Medium','Hard'), index = None)

    #if selected_option :

       # st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")

    #else:
        #st.error("You must select a difficulty")

    pressed = st.button("Click the button to initiate AI",  type = "primary")


if pressed:

    if not images:
         st.error("You must upload 1 image")

    if not selected_option:
         st.error("You must select a difficulty")

    if images and selected_option:

        with st.container(border = True):
            st.subheader("Your Notes")

            with st.spinner("AI is writing notes for you"):

                generated_notes = note_generator(pill_image)
                st.markdown(generated_notes)



        with st.container(border = True):
            st.subheader("Audio Transaction")

            with st.spinner("The notes are being converted into voice"):

                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace(",","")
                generated_notes = generated_notes.replace(".","")
                generated_notes = generated_notes.replace("","")
                generated_notes = generated_notes.replace("*","")

                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript) 
            


        with st.container(border = True):
            st.subheader(f"Quiz level ({selected_option})")

            with st.spinner("AI is generating the quizzes"):

                quiz = quiz_generator(pill_image, selected_option)
                st.markdown(quiz)

