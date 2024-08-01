import json
from rouge import Rouge
import streamlit as st

import vertexai
from google.cloud import storage

from langchain.prompts import PromptTemplate
from langchain.llms import VertexAI

import prompts

pi = prompts.PhenotypeIntake()

MODEL_ID = "text-bison@002"
LOCATION = "us-central1"

PARAMETERS = {
    "max_output_tokens": 1024,
    "temperature": 0,
    "top_p": 0.8,
    "top_k": 40
  }
LOCATION = "us-central1"

# # Get PaLM API
with st.sidebar:
    project_id = st.text_input("Your GCP Project ID", key="project_id")
# Get PaLM API
with st.sidebar:
    api_key = st.text_input("PaLM API Key", key="api_key", type="password")
    "[Get a PaLM API key](https://developers.generativeai.google/tutorials/setup)"


st.title("✨ Phenotype Intake Summarization")
st.caption("Generate Patient Narrative using intake forms. powered by PaLM 🤖 + Langchain 🦜🔗")


section = st.selectbox("Choose section", ("Gastrointestinal and General Symptoms", "Weight History"))


col1, col2 = st.columns([3, 1])
model_id = col1.selectbox("Choose a model", ("Gemini", "MedLM"))
temperature = col2.slider('Select temperature', 0.0, 1.0, 0.0)


col1, col2 = st.columns([1, 3])
evaluate_on = col1.toggle('Evaluation Pipeline')
if evaluate_on:
    col2.file_uploader("Upload the evaluation set ([example](https://storage.mtls.cloud.google.com/hcls-demo-amir/2_eval_set.txt))")
    eval_metric = st.selectbox("Choose a metric", ("rouge-1", "rouge-2", "rouge-l"))

else:
    col2.empty()
   


def generate_response(input_text, section, project_id, model=MODEL_ID, parameters=PARAMETERS):
    section_templates = {
      "Gastrointestinal and General Symptoms": """\
    most bothersome symptom is Early Fullness.  This symptom started between2 and 5 years ago. Her symptom started insidious or gradual. She described the nature of this symptom as chronic symptom with periodic exacerbation.
    She has intermittent nausea which occur most days of the week. At its worst, the severity of her nausea reaches a level of 10 out of 10, while at its mildest, it is rated at 7 out of 10. It is worsened immediately after eating. There is nothing that relieve her nausea except for vomiting. Medication does not lead to an improvement in her nausea.
    Vomit: Occur in less than one hour after eating. She is able to recognize food content.
    She endorses intermittent suprapubic pain daily. Does not radiate. At its worst, the severity of her abdominal pain reaches a level of 4 out of 10, while at its mildest, it is rated at 1 out of 10. It is worsened in less than one hour after eating. It is not relieved by eating, walking/moving or having a bowel movement. Medications does not lead to an improvement in her abdominal pain. Pain and nausea occur separately.
    She experiences a sense that her stomach is full after eating only a small amount of food, bloating/distention immediately after eating. She notices visible distention. In addition, she has difficulty swallowing. The food gets stuck in her throat. Denies food going in the wrong way or coming back to her nose. She hasn’t been subjected to the Heimlich maneuver before.
    Positive history of reflux, reduced appetite, abnormal weight loss and gain, diarrhea, constipation but not alternated. She endorses change or alteration in her bowel habits.
    Her physicians have told her that the cause of her symptoms remains unknown.
    She also has fatigue, weakness, lightheadedness, fainting, vertigo, numbness and tingling, abnormal sweating, sensitivity to heat or cold, dry mouth, mouth sores, dry eyes, tinnitus,  and generalized body pain and arthralgias. Denies migraines or headaches, hearing loss.
    """,
      "Weight History": """\
    Weight: six months ago, her weight was 115 pounds, currently her weight is 125 pounds. When asked about her weight pattern over the past five years she described it as up and down, up and down.
    """
    }

    vertexai.init(project=project_id, location=LOCATION)
    llm = VertexAI(model_name=model, **parameters)
    
    prompt_template = PromptTemplate.from_template(pi.prompt("summarize")) 

    chain = prompt_template | llm
    response = chain.invoke({"context":input_text, 
                      "answer":section_templates[section]}
                      )
    
    return response

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


def load_gcs_file():
    
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("hcls-demo-amir")
    blob = bucket.get_blob("2_eval_set.txt")
    downloaded_file = blob.download_as_text(encoding="utf-8")

    return downloaded_file

def evaluate(generated_summary, reference_summary, metric):
    rouge = Rouge()
    eval_score = rouge.get_scores(generated_summary,reference_summary)
    return eval_score[0][metric]

def side_by_side(generated_summary, reference_summary, model=MODEL_ID):
    
    # LOCATION = "us-central1"
    vertexai.init(project=project_id, location=LOCATION)
    llm = VertexAI(model_name=model, temperature=0)

    prompt_template = PromptTemplate.from_template(pi.prompt("evaluate")) 

    chain = prompt_template | llm
    response = chain.invoke({"generated_summary":generated_summary, 
                      "reference_summary":reference_summary}
                      )
    
    return response
    

with st.form('my_form'):
  patient_data_text = st.text_area('Enter Input data:', pi.input("text") )
  submitted = st.form_submit_button('Submit')
    
  if not api_key:
    try:
        api_key = st.secrets.palm_api.key
    except Exception as err:
        st.warning('Please enter your PaLM API key!', icon='⚠')
  if submitted and api_key:
    if is_json(patient_data_text):
        llm_text = generate_response(patient_data_text, section, project_id)
        st.info(llm_text, icon="🤖")
    else:
        st.warning('Please enter a valid json file!', icon='⚠')


if submitted and evaluate_on:
    uploaded_file = load_gcs_file()
    valid_result = evaluate(llm_text, uploaded_file, eval_metric)
    st.write(f':bulb: The generate text has **{eval_metric}** of **{valid_result}**')

    # diff_button = st.button('Show me the differences between AI generated text and the evaluation data'):
    # if diff_button:  
    st.write(side_by_side(llm_text, uploaded_file))