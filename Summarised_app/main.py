import streamlit as st
import requests

st.title("Rakshit Article Summary App")
text = st.text_area("Text to Summarise")
st.button("Summarise")

# get the api requests

API_KEY = "efc4aa65-42ab-4c62-909f-b0a7049f7a5d"
authorisation = API_KEY

summarise_endpoint = "https://api.oneai.com/api/v0/pipeline"

request_headers = {
    "api-key": authorisation,
    "content-type": "application/json"
}

api_payload = {
    "input": text,
    "input_type": "article",
    "content_type": "application/json",
    "steps": [{
        "skill": "summarize"
    }]
}

response = requests.post(summarise_endpoint,
                         json=api_payload,
                         headers=request_headers)

results = response.json()
print(results)

summarized_article = results['output'][0]['text']

st.write(summarized_article)

# '''
# Input : Breonna Taylor would be 27 today. She was 26 years old when she was shot to death by police after a day of serving her community as a first responder. Although her name has become known after her death, her life paints a legacy of light, love, and unparalleled kindness. Among others, she leaves behind her mother Tamika Palmer, her sister Ju’Niyah Palmer, her cousin Preonia Flakes, her older-sister-cousin Katrina Curry, and her best friends Alena Battle and Erinicka Hunter, all six of whom told Teen Vogue about the ways Breonna changed their lives for the better by living the “Bree way.”

# When Breonna was a child, her mother knew she was destined for greatness. Tamika recalls that after Breonna witnessed her take her diabetic grandmother’s blood sugar, Breonna was eager to do it too, foreshadowing Breonna’s future in the medical field. Reminiscing, Tamika says, “It was the cutest thing.”

# Throughout her life, those who knew her say Breonna expressed her love for others through empowerment and support. When she was in high school, her teacher called her mother because Breonna would not go to the pizza party in another classroom for students doing exceptionally well because her friends were not invited.

# When her mother received the call, she tells Teen Vogue that she said, “If your friends don’t want to see you do great, they’re not your friends.” To which Breonna replied, “I’m going to help my friends be great.” Later in life, her motto would become, “All you can do every day is wake, pray, and slay.”

# Output :

# Breonna Taylor was shot to death by police after a day of serving her community as a first responder. Her life paints a legacy of light, love, and unparalleled kindness. She leaves behind her mother Tamika Palmer, her sister Ju’Niyah Palmer and her cousin Preonia Flakes.

# '''
