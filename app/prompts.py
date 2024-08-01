###### 1-DOCUMENT REVIEW #########

class DocReview():
    def prompt(self, section):
        
        prompt_dict = {
            "DEFN_ALIGNMENT_APPROVED_GLOSSARY": """
            Definition alignment
Ensure that like-for-like terms align with the definition provided in the approved glossary. (Reference “Approved Glossary Sample”)
Identify definitions that are present in the document but not currently recorded in the glossary.
Identify examples where a term is misused in the document based on the definition provided. (Reference “Approved Glossary Sample”)


APPENDIX
Approved Glossary Sample

 Term: Baseline lots
 Definition: A combination of development, clinical, and, if applicable, commercial lots used to determine comparability statistical ranges.
 Notes: In-use
 Term: Clinical lots
 Definition: Product lots used for clinical studies referenced in a regulatory submission. In most CMC regulatory submission sections, specific clinical studies and phases do not need to be identified. Release and stability data from these lots are included in commercial license applications.
 Notes: In-use
 Term: Development lots
 Definition: Lots that are representative of the clinical and/or commercial manufacturing process used to determine comparability statistical ranges in addition to all relevant clinical and, if applicable, commercial lots. Release and stability data from these lots are included in commercial license applications.
 Notes: In-use
 Term: Lot
 Definition: Term used when specific lot numbers are referenced, which is typically the main applicability in Tier 1 documents (e.g. PPQ lots, clinical lots). Note that SOP-0503 v7.0 states that batch and lot are interchangeable. Definition here is to provide consistency for use in TechDev documentation.
 Notes: In-use
 Term: Prototype
 Definition: Original RNA sequence(s) of a product with an approved marketing application or authorized under Emergency Use Authorization (e.g. CX-024414 mRNA, mRNA-1273 LNP, and mRNA-1273 DP).
 Notes: In-use
 Term: Registration lots
 Definition: Product lots used for demonstration of commercial process consistency and comparability (typically commercial process PPQ and/or comparability demonstration lots). Release and stability data from these lots are included in commercial license applications.
 Notes: In-use
 Term: Variant(s)
 Definition: RNA sequences filed following a prototype approval/authorization or sequences included in an initial marketing application for a multi-valent or seasonal product. Can also be referred to as “seasonal variant(s)”.
 Notes: In-use
 Term: Analytical Target Profile
 Definition: ATP is a prospective description of the desired performance of an analytical procedure that is used to measure a quality attribute. The analytical target profile is defined by the requirements of the reportable value produced by the procedure.
 Notes: In-use
 Term: Critical Quality Attribute
 Definition: CQA is a physical, chemical, biological, or microbiological property or characteristic that can potentially impact the safety and/or efficacy of the product and should be within an appropriate limit, range, or distribution to ensure the desired product quality.
 Notes: In-use
 Term: Analytical Method Development
 Definition: AMD is a series of documented laboratory studies that are carried out through systematic screening and/or optimization of instrumental and sample preparation conditions to identify conditions to minimize or avoid bias, to optimize variability, and to establish robust operating parameters that have the potential to meet the ATP.
 Notes: In-use
""",
            "DEFN_ALIGNMENT_TERMINOLOGY_TO_AVOID":"""
            Terminology to avoid
            Ensure that the document does not contain terminology to avoid. (Reference “Terminology to Avoid Sample”)

            Terminology to Avoid Sample

            Term: CIP
            Definition: clean-in-place
            Notes: Do not use abbreviation (conflict with calf intestinal phosphatase). Use full term only.
            Term: DSI
            Definition: decontamination and staging isolator
            Notes: Do not use abbreviation; use full term only.
            Term: RSM
            Definition: response surface model
            Notes: Do not use abbreviation; use full term only.
            """,
            "DEFN_ALIGNMENT_ABBREVIATION":"""
            Approved abbreviation
            Check whether an abbreviation in the “Approved Abbreviation Sample” is misused in the document.

            Approved Abbreviation Sample

            Abbreviation: WFI
            Definition: Water for Injection (acronym)
            Abbreviation: WFI
            Definition: Process Pharmaceutical water
            Abbreviation: WFI
            Definition: Wellness Fitness Initiative
            Abbreviation: WFI
            Definition: Wood Floor International
            Abbreviation: NMT
            Definition: Not more than
            Abbreviation: NMT
            Definition: N-methyltyramine
            Abbreviation: NMT
            Definition: Not my type
            """,
            "DEFN_ALIGNMENT_GENERAL":"""
General guidelines
Consider the following general guidelines. Examples of these guidelines include:
Use “sterile” with caution; sterility claims are applicable only to drug product.
The use of “% change” or “% difference” is typically too vague. Ensure analysis is sufficiently descriptive and statistically relevant to the claim or conclusion being made.
""",
            "GEN_FORMATTING":"""
            General formatting
            1. Ensure that forms that will be electronically signed have the appropriate height and width to accommodate an e-signature within a validated signature system (i.e., Regulated DocuSign). Sizing of Boxes should minimally be Height = 1.25 inches Width = 2.5 inches
            2. Correct any spelling errors, spacing, alignment (including alignment of tables), numbering of sections/steps, page numbering (if applicable) throughout the document.
            3. Ensure that all documents listed in the SOP are referenced in the “Referenced Documents” section. (See section 3.0 of SOP example.)
            """,
            "PROCEDURE":"""
            PROCEDURE
            Preparation of mRNA
            Clean and sanitize the mRNA Synthesizer using the Clean-In-Place (CIP) system.
            1.2 Load the mRNA raw material (Part Number 1234) into the mRNA Synthesizer. Ensure the raw material is sourced from the designated Baseline Lots.
            1.3 Set the Synthesizer to the appropriate parameters for mRNA synthesis as per manufacturer's instructions. The parameters should be consistent with those used for Development Lots.
            1.4 Start the synthesis process and monitor the system for any errors or alerts.
            1.5 Upon completion of the synthesis process, collect the synthesized mRNA for the next step. Assign a unique Lot number for tracking.
            Formulation into LNPs
            2.1 Clean and sanitize the LNP Formulator using the CIP system.
            2.2 Load the synthesized mRNA and lipid nanoparticles (Part Number 5678) into the LNP Formulator.
            2.3 Set the Formulator to the appropriate parameters for LNP formulation as per manufacturer's instructions. These parameters should be consistent with those used for Development Lots.
            2.4 Start the formulation process and monitor the system for any errors or alerts.
            2.5 Upon completion of the formulation process, collect the mRNA formulated LNPs for the next step.
            Control of Nitrosamine Impurities
            3.1 Perform a nitrosamine test on the collected mRNA formulated LNPs using the designated testing equipment.
            3.2 If nitrosamine levels are above the acceptable limit, discard the batch and start the process again from step 1. Document this action in the Lot record.
            3.3 If nitrosamine levels are within or NMT acceptable limits, proceed to the next step.
            Quality Control and Packaging
            4.1 Perform quality control tests on the mRNA formulated LNPs as per SOP-XXXX. These tests should be consistent with those performed on Clinical Lots.
            4.2 If the batch passes all quality control tests, proceed to packaging.
            4.3 Package the final product in the designated vaccine vials as per SOP-XXXX.
            4.4 Label the vials with the Lot number, manufacturing date, and expiry date.
            4.5 Store the packaged vaccines in the designated storage area under appropriate conditions.
            Documentation and Reporting
            5.1 Document all process parameters, test results, and any deviations in the Batch Record. Include a record of the mRNA synthesis and formulation process.
            5.2 Report the completion of the batch to the Quality Assurance department for review and release.
            5.3 Update the Inventory Management System with the details of the manufactured batch.
            5.4 Archive the Batch Record as per SOP-XXXX.
            """,
            "REVIEWER_PROMPT_TEMPLATE":"""
                You are a reviewer that needs to check the adherence
                of a document or passage with a given checklist of guidelines. Make a note of
                all violoations to the guidelines.

                Here is the checklist and guidelines:
                {{CHECKLIST_AND_GUIDELINES}}

                Passage:
                {{PASSAGE}}

                If there or no violoations return [] otherwise use the following JSON format to record violations:
                [{"feedback": <rule that was violated>, "originalText": <sentence in the passage>, "replaceWith": <corrected sentence satisfying the rule>}, ...<more instances of violations and corrections>]

                Answer:
"""

        }

        return prompt_dict[section]
    

    def input(self, section):

        input_text = {
            "text": """
Preparation of mRNA

1.1 Clean and sanitize the mRNA Synthesizer using the Clean-In-Place (CIP) system.
1.2 Load the mRNA raw material (Part Number 1234) into the mRNA Synthesizer. Ensure the raw material is sourced from the designated Baseline Lots.
1.3 Set the Synthesizer to the appropriate parameters for mRNA synthesis as per manufacturer's instructions. The parameters should be consistent with those used for Development Lots.
1.4 Start the synthesis process and monitor the system for any errors or alerts.
1.5 Upon completion of the synthesis process, collect the synthesized mRNA for the next step. Assign a unique Lot number for tracking.
Formulation into LNPs
2.1 Clean and sanitize the LNP Formulator using the CIP system.
2.2 Load the synthesized mRNA and lipid nanoparticles (Part Number 5678) into the LNP Formulator.
2.3 Set the Formulator to the appropriate parameters for LNP formulation as per manufacturer's instructions. These parameters should be consistent with those used for Development Lots.
2.4 Start the formulation process and monitor the system for any errors or alerts.
2.5 Upon completion of the formulation process, collect the mRNA formulated LNPs for the next step.
Control of Nitrosamine Impurities
3.1 Perform a nitrosamine test on the collected mRNA formulated LNPs using the designated testing equipment.
3.2 If nitrosamine levels are above the acceptable limit, discard the batch and start the process again from step 1. Document this action in the Lot record.
3.3 If nitrosamine levels are within or NMT acceptable limits, proceed to the next step.
Quality Control and Packaging
4.1 Perform quality control tests on the mRNA formulated LNPs as per SOP-XXXX. These tests should be consistent with those performed on Clinical Lots.
4.2 If the batch passes all quality control tests, proceed to packaging.
4.3 Package the final product in the designated vaccine vials as per SOP-XXXX.
4.4 Label the vials with the Lot number, manufacturing date, and expiry date.
4.5 Store the packaged vaccines in the designated storage area under appropriate conditions.
Documentation and Reporting
5.1 Document all process parameters, test results, and any deviations in the Batch Record. Include a record of the mRNA synthesis and formulation process.
5.2 Report the completion of the batch to the Quality Assurance department for review and release.
5.3 Update the Inventory Management System with the details of the manufactured batch.
5.4 Archive the Batch Record as per SOP-XXXX.
""",
            "text_markdown": """
Preparation of mRNA

* 1.1 Clean and sanitize the mRNA Synthesizer using the Clean-In-Place (CIP) system.
* 1.2 Load the mRNA raw material (Part Number 1234) into the mRNA Synthesizer. Ensure the raw material is sourced from the designated Baseline Lots.
* 1.3 Set the Synthesizer to the appropriate parameters for mRNA synthesis as per manufacturer's instructions. The parameters should be consistent with those used for Development Lots.
* 1.4 Start the synthesis process and monitor the system for any errors or alerts.
* 1.5 Upon completion of the synthesis process, collect the synthesized mRNA for the next step. Assign a unique Lot number for tracking.
Formulation into LNPs
* 2.1 Clean and sanitize the LNP Formulator using the CIP system.
* 2.2 Load the synthesized mRNA and lipid nanoparticles (Part Number 5678) into the LNP Formulator.
* 2.3 Set the Formulator to the appropriate parameters for LNP formulation as per manufacturer's instructions. These parameters should be consistent with those used for Development Lots.
* 2.4 Start the formulation process and monitor the system for any errors or alerts.
* 2.5 Upon completion of the formulation process, collect the mRNA formulated LNPs for the next step.
Control of Nitrosamine Impurities
* 3.1 Perform a nitrosamine test on the collected mRNA formulated LNPs using the designated testing equipment.
* 3.2 If nitrosamine levels are above the acceptable limit, discard the batch and start the process again from step 1. Document this action in the Lot record.
* 3.3 If nitrosamine levels are within or NMT acceptable limits, proceed to the next step.
Quality Control and Packaging
* 4.1 Perform quality control tests on the mRNA formulated LNPs as per SOP-XXXX. These tests should be consistent with those performed on Clinical Lots.
* 4.2 If the batch passes all quality control tests, proceed to packaging.
* 4.3 Package the final product in the designated vaccine vials as per SOP-XXXX.
* 4.4 Label the vials with the Lot number, manufacturing date, and expiry date.
* 4.5 Store the packaged vaccines in the designated storage area under appropriate conditions.
Documentation and Reporting
* 5.1 Document all process parameters, test results, and any deviations in the Batch Record. Include a record of the mRNA synthesis and formulation process.
* 5.2 Report the completion of the batch to the Quality Assurance department for review and release.
* 5.3 Update the Inventory Management System with the details of the manufactured batch.
* 5.4 Archive the Batch Record as per SOP-XXXX.
""",
        }
        return input_text[section]
    

###### 2-PHENOTYPe #########
class PhenotypeIntake():
    def prompt(self, section):

        prompts = {
                    "summarize":"""\
    You are a helpful medical knowledge assistant. Your goal is to go through the key value pairs of ###Patient History### and update the ###Answer Template### accordingly.

    Instructions:
    - Delete the parts that are not relevant to the patient specially when they haven't provided any answer to a question.
    - when the patient has selected UNKNOWN, write the sentence in a sentence that reads fluently.
    - Provide useful, complete and scientifically grounded answers.
    Evaluate which contexts are most relevant and prioritize comprehensively capturing their details in your response.
    - Take your time and reason through the patient history and the provided answer template.

    ###Patient History###
    {context}


    ###Answer Template###
    {answer}
    """,
                    "evaluate":"""
            You are a helpful medical assistant. Read the two separate inputs (Generated Text and Reference Text) on patient history and find exactly where the two texts are different. 
        
            go through the result and drop rows that say the exact same things but in different ways. ignore grammatical errors.  Use the following examples as your guide:
            semantically the same:
            |Generated Text | Reference Text |
            | ----------- | ----------- |
            | This symptom started between 2 and 5 years ago. | This symptom started between 2 and 5 years ago. |
            | Medication does not lead to an improvement in her nausea. | Medication does not lead to an improvement in her nausea.|
            | Pain and nausea occur separately. | The pain and nausea occur separately. |
            semantically different:
            | At its worst, the severity of her nausea reaches a level of 10 out of 10, while at its mildest, it is rated at 7 out of 10. | At its worst, the severity of her nausea reaches a level of 10 out of 10, while at its mildest, it is rated at 5 out of 10. |


            Return the semantically different answers side by side in a markdown table.                    

            Generated Text:
            {generated_summary}


            Reference Text
            {reference_summary}
        """,

        }

        return prompts[section]

    def input(self, section):
        input = {
            "text": 
            """
{  "Please select all the symptoms you are experiencing?":"Early fullness",
   "From all the symptoms you have selected before please choose the most bothersome.":"",
   "If other, please name your symptom:":"",
   "When did your predominant symptom begin?":"More than 5 years ago.",
   "How did your predominant symptom start?":"Unknown",
   "To the best of your knowledge, did your predominant symptom":"unknown",
   "Which best describes the current nature of your predominant symptom?":"Chronic symptom with periodic exacerbations with worsening of symptom.",
   "Do you experience any nausea?":"yes",
   "How often does this nausea occur?":"Daily",
   "On the days you have nausea, is it intermittent or constant":"Constant",
   "On a scale of 0-10, what is the lowest nausea you experience when you have it?":5,
   "On a scale of 0-10, what is the highest nausea you experience when you have it?":10,
   "What makes the nausea worse?":"Eating",
   "How long after eating, bowel movement, moving or walking does the nausea get worse?":"1 to 4 hours",
   "What makes the nausea better?":"Bowel movement",
   "How long after eating, bowel movement, moving or walking does the nausea get better?":"More than four hours",
   "Do medications lead to an improvement in your nausea?":"No",
   "Have you had any vomiting?":"Yes",
   "If you vomit, how soon after eating?":"1 to 4 hours",
   "Can you recognize what you ate in the vomitus?":"No",
   "Does vomiting relieve your nausea?":"Yes",
   "Do you experience any abdominal pain?":"Yes",
   "Where do you feel the most severe abdominal pain?":"5- Periumbilical",
   "Do you feel pain anywhere else in your abdomen?":"Yes",
   "Please specify where?":"2- Epigastric",
   "How often does this pain occur?":"Daily",
   "On the days you have pain, is it intermittent or constant?":"Constant",
   "On a scale of 0-10, what is the lowest pain you experience when you have it?":4,
   "On a scale of 0-10, what is the lowest pain you experience when you have it?":10,
   "What makes the pain worse?":"Eating",
   "How long after eating, bowel movement, moving or walking does the pain get worse":"1 to 4 hours",
   "What makes the pain better?":"Bowel movement",
   "How long after eating, bowel movement, moving or walking  does the paing get better":"More than four hours",
   "Do medications lead to an improvement in your abdominal pain?":"No",
   "Do the abdominal pain and nausea go together or separate":"Together",
   "Do you experience a sense that your stomach is full after eating only a small amount of food?":"Yes",
   "Do you experience bloating/distention?":"Yes",
   "Is your bloating/distention related to eating?":"Yes",
   "How long after eating?":"1 to 4 hours",
   "Do you notice visible distention?":"Yes",
   "Do you experience heartburn/reflux?":"Yes",
   "Do you have a reduced appetite?":"Yes",
   "Have you had any abnormal or unintentional weight loss":"Yes",
   "Have you had any abnormal weight gain?":"No",
   "Do you experience constipation?":"No",
   "Do you experience diarrhea?":"Yes",
   "Do you experience both diarrhea and constipation, or alternating diarrhea/constipation?":"No",
   "Have you had any change or alteration in your bowel habits":"No",
   "What have your doctors told you about the cause of these symptoms? (Check all that apply)":[
      "Irritable Bowel Syndrome",
      "Other"
   ],
   "Did you have any of these symptoms as a child?":"No",
   "General symptoms":{
      "Do you experience any malaise or fatigue?":"Yes",
      "Have you experienced any weakness?":"Yes",
      "Do you get headaches or migraines?":"No",
      "Do you experience lightheadedness or dizziness?":"Yes",
      "Have you ever fainted?":"Yes",
      "Do you experience vertigo, or a sensation that your surroundings are moving or spinning?":"No",
      "Do you experience any tingling, prickling, numbness, or burning in your hands, arms, legs and/or feet?":"Yes",
      "Do you have any abnormal sweating?":"Yes",
      "Do you have a sensitivity to, or intolerance of, heat or cold?":"No",
      "Do you experience dry mouth?":"Yes",
      "Do you have dry eyes?":"No",
      "Do you get mouth sores?":"No",
      "Have you ever had tinnitus, or ringing in the ears?":"No",
      "Have you had any hearing loss?":"No",
      "Do you experience generalized body pain?":"No",
      "Do you have any joint pain?":"No"
   }
}
""",
        }

        return input[section]