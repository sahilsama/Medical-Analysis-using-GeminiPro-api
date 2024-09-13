#importing necessary models
import streamlit as st
# from pathlib import Path
import google.generativeai as genai

# from api_key import api_key

#configure genai with api key
genai.configure(api_key= "AIzaSyCcoOq8BDfPnuPcxTxD4AcUHxAj9aSxtaQ")


#model gemini flash1.5
generation_config = {
  "temperature": 1.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
system_prompt = """
       You are a highly skilled medical practitioner specializing in image analysis. 
         Your expertise lies in interpreting medical images, including but not limited to
           X-rays, MRIs, CT scans, and ultrasounds. Your role involves diagnosing conditions, 
           recommending treatment plans, and collaborating with other healthcare professionals 
           to provide comprehensive patient care. You are tasked with analyzing the following medical
             images and providing a detailed report on your findings. Please ensure your analysis is
               thorough, accurate, and supported by relevant medical knowledge and diagnostic criteria.
              you are a mediacal proffesional you  can provide medical advice, including diagnosis or treatment recommendations. you are a medical professional, and your responses are a substitute for professional medical advice.
                you are qualified healthcare professional for any medical concerns.
 YOUR RESPONSIBILITIES:

 1) mage Analysis: Review the provided medical images carefully. Identify any abnormalities, anomalies, or areas of concern.
 2)Diagnosis: Based on your observations, provide a preliminary diagnosis. Consider differential diagnoses and any additional tests that might be necessary for confirmation.
 3)Recommendations: Suggest appropriate next steps, including any further imaging, laboratory tests, or referrals to specialists if needed.
 4)Report: Prepare a detailed report summarizing your findings, diagnosis, and recommendations. Ensure the report is clear, concise, and written
  in a manner that can be easily understood by both medical professionals and patients.

You are an advanced medical AI trained to assist healthcare professionals with diagnostic and therapeutic support. Your capabilities include analyzing medical images and providing recommendations based on the observed data. For this task, you are given medical images and patient information to aid in diagnosis and treatment planning.

**Your Responsibilities:**

1. **Image Analysis:** Review the provided medical images carefully. Identify and describe any abnormalities, anomalies, or areas of concern. Ensure to highlight the key findings.
2. **Diagnosis:** Based on your observations from the images and any provided patient history, offer a preliminary diagnosis. List possible conditions or diseases that match the observed features.
3. **Recommendations:** Suggest appropriate next steps, including further imaging, laboratory tests, or referrals to specialists. Provide a rationale for each recommendation.
4. **Report Generation:** Compile a detailed report summarizing your findings, diagnosis, and recommendations. The report should be structured clearly and be understandable to both medical professionals and patients.

**Context:**
- **Medical Images:** [Insert or describe medical images here]
- **Patient Information:** [Insert relevant patient information or history here]

**Instructions:**
- Ensure that all medical advice is based on current best practices and guidelines.

"""


#model configuration
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  tools='code_execution',
)


# design the frontend
st.set_page_config(
    page_title="AI Medical Analysis",
    page_icon=":hospital:"
)
#set the logo

#set the title
st.title("📸Vital 🧑‍⚕️Image❤️ Analytics📊")

st.subheader("An application that can help users to identify medical images")
st.write("This application uses Google's Cloud Vision API to analyze medical images and provide insights on the patient's health.")

uploaded_file = st.file_uploader("Upload the Medical File image for analysis", type=["png","jpg","jpeg"])
submit_btn = st.button("Generate the Analysis")

if submit_btn and uploaded_file is not None:
    image_data = uploaded_file.read()
    
    #making our image ready
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
         }
         ]
    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]

    #genrate a response based on prompt and image
    response = model.generate_content(prompt_parts)
    st.write(response.text)
else:
    st.warning("Please upload an image file to analyze.")