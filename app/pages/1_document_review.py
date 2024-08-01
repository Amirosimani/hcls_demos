import re
import copy
import google.generativeai as palm
from google.generativeai.types import safety_types

import streamlit as st

import prompts

drp = prompts.DocReview()
st.session_state['button'] = False
# Get PaLM API
with st.sidebar:
    project_id = st.text_input("Your GCP Project ID", key="project_id")
# Get PaLM API
with st.sidebar:
    api_key = st.text_input("PaLM API Key", key="api_key", type="password")
    "[Get a PaLM API key](https://developers.generativeai.google/tutorials/setup)"


tab1, tab2, tab3 = st.tabs(["Terminology to Avoid", 
                            "Approved Abbreviation",
                            "General formatting"])

with tab1:
    st.markdown(
        """
    ## Terminology to Avoid
    Ensure that the document does not contain the following terms.

    | Term | Definition                           | Notes                                                                                    |
    |------|--------------------------------------|------------------------------------------------------------------------------------------|
    | CIP  | clean-in-place                       | Do not use abbreviation (conflict with calf intestinal phosphatase). Use full term only. |
    | DSI  | decontamination and staging isolator | Do not use abbreviation; use full term only.                                             |
    | RSMs | response surface model               | Do not use abbreviation; use full term only.                                             |
    """
    )

with tab2:
    st.markdown(
        """
    ## Approved Abbreviation
    Check whether an abbreviation in the “Approved Abbreviation Sample” is misused in the document.

    - WFI: Water for Injection (acronym).
    - WFI: Wellness Fitness Initiative.
    - WFI: Wood Floor International.
    - NMT: Not more than.
    - NMT: N-methyltyramine.
    - NMT: Not my type.                                       
    """
    )


with tab3:
    st.markdown(
        """
    ## General formatting

    1. Fix general formatting: Ensure that forms that will be electronically signed have the appropriate height and width to accommodate an e-signature within a validated signature system (i.e., Regulated DocuSign). Sizing of Boxes should minimally be Height = 1.25 inches Width = 2.5 inches; Correct any spelling errors, spacing, alignment (including alignment of tables), numbering of sections/steps, page numbering (if applicable) throughout the document;
    2. Ensure that all documents listed in the SOP are referenced in the “Referenced Documents” section.
    3. Fix procedure alignment: For each procedure in a SOP, there is often an overarching “policy” document that supersedes that procedure and dictates general rules / methodologies that each procedure should abide by.
    4. Regulatory changes: If the document refers to any regulatory bodies, check if these regulations have changed, if so,  flag the reference points and explain how the changes might impact the document. For example: if the mock SOP provided references the EMA regulation titled “ CHMP Opinion pursuant to Article 5(3) of Regulation (EC) No 726/2004 for nitrosamine impurities in human medicines”, and a section contains content directly impacted by this article, you should flag the section for further review.

    Make sure definitions align:
    
    * Ensure that like-for-like terms align with the definition provided in the approved glossary(as APPENDIX i).
    * Ensure that the document does not contain terminology to avoid. (as APPENDIX ii)
    * Identify definitions that are present in the document but not currently recorded in the glossary. For example: The term “Batch” is listed in the Mock SOP section “5.0 Definitions” but not present in the APPENDIX i.
    * Identify examples where a term is misused in the document based on the definition provided. (Reference APPENDIX i)
    * Check whether an abbreviation in the APPENDIX iii is misused in the document. Example: In the mock SOP, the abbreviation “NMT” is mentioned in “Procedure 8.3.3” and based on the context should be abbreviation of “Not more than.” However, in section “5.0 Definitions” NMT is defined as “N-methyltyramine.” Change "N-methyltyramine" to "Not more than" in section “5.0 Definitions”.
    * Consider the following general guidelines. Examples of these guidelines include:Use “sterile” with caution; sterility claims are applicable only to drug product. The use of “% change” or “% difference” is typically too vague. Ensure analysis is sufficiently descriptive and statistically relevant to the claim or conclusion being made.

    """
    )


st.markdown("""---""")

col1, col2 = st.columns(2)
model_id = col1.selectbox("Choose a model", ("Gemini", "MedLM"))
temperature = col2.slider('Select temperature', 0.0, 1.0, 0.1)

with st.form('my_form'):
    input_text = st.text_area('Text to analyze', drp.input("text") )
    submitted = st.form_submit_button('Analyse')


st.markdown("""---""")


def get_filled_prompt(prompt_template: str, replacements: dict[str, str]) -> str:
    ''' 
    Function to generate prompts
    '''
    filled_prompt = copy.deepcopy(prompt_template)
    for key, value in replacements.items():
        filled_prompt = filled_prompt.replace(key, value)
    return filled_prompt


def query_model(prompt: str, model=model_id, temperature=temperature) -> str:
    '''
    Function to generate response
    '''
    if  api_key or st.secrets.palm_api.key:
        key = api_key or st.secrets.palm_api.key
        palm.configure(api_key=key)
        r = palm.generate_text(
                                model=f"models/{model}",
                                prompt=prompt,
                                candidate_count=1,
                                temperature=temperature,
                                safety_settings=[{
                                    "category": safety_types.HarmCategory.HARM_CATEGORY_MEDICAL,
                                    "threshold": safety_types.HarmBlockThreshold.BLOCK_NONE
                                    },
                                    ]
                            )
        return r
    else:
        st.warning('Please enter your PaLM API key!', icon='⚠')


def format_output(raw_response):

    def parse_responses(raw_response):

        RESPONSE_KEYS = ['feedback', 'originalText', 'replaceWith']

        violations = raw_response.split('{')
        vio_responses = []
        for violation in violations:
            if ',' not in violation: continue
            outputs = violation.split(',')
            vio_response = {}
            for idx, output in enumerate(outputs):
                if ":" not in output: continue
                output_key, output_value = output.split(':')
                response_key = output_key.strip(" \"'\t\r\n}{[],")
                response_val = output_value.strip(" \"'\t\r\n}{[],")
                if response_key in RESPONSE_KEYS:
                    vio_response[response_key] = response_val
            if len(vio_response) > 0: vio_responses.append(vio_response)
        return vio_responses
    r = parse_responses(raw_response.result)
    return r


BASE_REPLACEMENTS = {
"{{CHECKLIST_AND_GUIDELINES}}": '', "{{PASSAGE}}": '',
}
ALIGNMENT_DEFS = [drp.prompt("DEFN_ALIGNMENT_APPROVED_GLOSSARY"), 
                drp.prompt("DEFN_ALIGNMENT_ABBREVIATION"),
                drp.prompt("DEFN_ALIGNMENT_GENERAL"),
                drp.prompt("DEFN_ALIGNMENT_TERMINOLOGY_TO_AVOID")
                ]

if not api_key:
    try:
        api_key = st.secrets.palm_api.key
    except Exception as err:
        st.warning('Please enter your PaLM API key!', icon='⚠')
if submitted:
    st.session_state['button'] = submitted
    i = 0
    results = []
    color_map = ["blue", "green", "orange", "violet"]
    output_text = drp.input("text_markdown")
    accepted_output = drp.input("text_markdown")

    for alignment_def in ALIGNMENT_DEFS:
        # generate prompt
        replacements = copy.deepcopy(BASE_REPLACEMENTS)
        replacements["{{CHECKLIST_AND_GUIDELINES}}"] = alignment_def
        replacements["{{PASSAGE}}"] = input_text
        filled_prompt = get_filled_prompt(drp.prompt("REVIEWER_PROMPT_TEMPLATE"), replacements)
        # send the query to Vertex Model 
        response = query_model(prompt=filled_prompt, model="text-bison-001")
        # Format output for better visualization
        response_formatted = format_output(response)
        for t in response_formatted:
            target = t["originalText"]
            replace = t['replaceWith']
            fb = t["feedback"]
            match = re.search(target.lower(), input_text.lower())
            if match and match.group(0) != "lot":
                span_begin = match.span()[0]
                span_end = match.span()[1]
                target_word = input_text[span_begin:span_end]
                print(match)
                output_text = re.sub(r"{}".format(target_word), ' ~~{}~~ :{}[{}]  :grey[(feedback: {})]'.format(target_word, color_map[i], replace, fb),
                                     output_text
                                          )
                accepted_output = re.sub(r"{}".format(target_word), ':{}[{}]]'.format(color_map[i], replace), accepted_output)
        i += 1





    st.session_state["output"] =  accepted_output     
    st.markdown(output_text)

if st.session_state['button']:
    col1,col2,col3,col4 = st.columns([3,3,0.5,0.5])
    col3.button(":thumbsup:")
    col4.button(":thumbsdown:")
