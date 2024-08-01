import base64
from time import sleep
import streamlit as st
import PyPDF2

import vertexai
from vertexai.language_models import TextGenerationModel

from langchain.prompts import PromptTemplate


LOCATION = "us-central1"

with st.sidebar:
    project_id = st.text_input("Your GCP Project ID", key="project_id")

with st.sidebar:
    api_key = st.text_input("PaLM API Key", key="api_key", type="password")
    "[Get a PaLM API key](https://developers.generativeai.google/tutorials/setup)"

project_id = "amir-genai-bb"

vertexai.init(project=project_id, location=LOCATION)


st.title("✨ Knowledge Worker Assistant: CCI")
st.caption(
    "Detect and Highlight Commercially Confidential Information before publishing using LLMs 🌴 + Langchain 🦜🔗"
)


def extract_data(f_input):
    reader = PyPDF2.PdfReader(f_input)
    num_pages = len(reader.pages)
    print(f"Loaded pdf with {num_pages} pages")
    pages_list = [reader.pages[i].extract_text() for i in range(num_pages)]

    return pages_list


uploaded_file = st.file_uploader("Upload your .pdf file", type="pdf")

rule_input = st.selectbox(
    "Choose the CCI Asset",
    ("Dose and dosage regimen information", "Presentations of the active ingredient"),
)

col1, col2, col3 = st.columns([2, 1, 1])
model_id_input = col1.selectbox("Choose a model", (["text-bison@002"]))
temperature_input = col2.slider("Select temperature", 0.0, 1.0, 0.0)
submitted = col3.button("Analyse 🤖",  type="primary")

st.markdown("""---""")


@st.cache_resource
def load_models(model_id=model_id_input):
    model = TextGenerationModel.from_pretrained(model_id)
    return model


def detect_cci(text, rule=rule_input, temperature=temperature_input):

    model = load_models()
    model_config = {
        "temperature": temperature,
        "top_p": .8,
        "top_k": 40,
        "candidate_count": 1,
        "max_output_tokens": 2048,
    }

    prompt_template = PromptTemplate.from_template(
        """
    You are an FDA drug reviewer that needs to check if there is any occurence of an information \
    from a given checklist in a given document.
    The information can be in the form of explicit or implicit statements that are related to the checklist but not directly mentioned.
    Please go through the document sentence by sentence and make a note of all instances of the topic or anything remotely related to the topic. feel free to over report.
    It is extremely important to have high recall so that you can catch all instances of the topic even when they are remotely related.\
    for example if the topic is "risk", you should also report related topics like "side effects" or "safety" or "experimental" to name a few.

    Here is the checklist:
    {CHECKLIST}

    Passage:
    {DOCUMENT}

    If there or no occurances, return [] otherwise use the following JSON format to record violations:
    ["originalText": <sentence in the passage>
    Answer:
    """
    )
    prompt = prompt_template.format(CHECKLIST=rule,
                                     DOCUMENT=text)
    print("Prompt is created")
    response = model.predict(
            prompt=prompt,
            **model_config
            )
    
    return response

if uploaded_file and submitted:
    with st.spinner("Ingesting the uploaded pdf file..."):
        input_text = extract_data(uploaded_file)
        print("Loaded the input file")
    with st.spinner("Detecting CCI. Hang tight!"):
        cci_page = st.empty()
        cci_counter = 0
        cci_text = []
        for idx, page in enumerate(input_text[:10]):
            r = detect_cci(page)
            sleep(0.4)
            if r.text.strip() != '[]':
                 cci_text.append([idx+1, r.text.strip()])
                 with cci_page.container():
                    st.write(f"🚨 Found potential CCI in page **{idx+1}**.")
                    cci_counter += 1
        
    cci_page.empty()
    st.success(f"Your  file is fully processed! Found CCI in {cci_counter} pages! 😭")

    st.dataframe(cci_text)

