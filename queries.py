import pandas as pd

#Consider the policy given in https://medpolicy.ibx.com/ibc/Commercial/Pages/Policy/3ac82d0c-32e3-4a54-be0e-fc60783c4108.aspx. 
# Give me five search terms that a medical provider is interested in and the expected answer for them. Give the result as Pandas df

link1 = "https://medpolicy.ibx.com/ibc/Commercial/Pages/Policy/77017542-a222-43a5-85ef-78e70d08c670.aspx"
# Define the search terms and their expected answers
data1 = [
    {
        "Term": "When is autonomic nervous system testing medically necessary?",
        "Answer": "ANS testing is medically necessary when used to evaluate symptoms like syncope, POTS, diabetic autonomic neuropathy, and small fiber neuropathy, after ruling out other causes and if results influence clinical decision-making."
    },
    {
        "Term": "What CPT codes are used for ANS testing?",
        "Answer": "CPT codes include 95921 (cardiovagal testing), 95922 (vasomotor testing), 95923 (combined testing), 95924 (sudomotor testing), and 95999 for unlisted or investigational tests."
    },
    {
        "Term": "Is SUDOSCAN covered by insurance?",
        "Answer": "No, SUDOSCAN is considered experimental/investigational and is not covered due to lack of validated clinical utility."
    },
    {
        "Term": "ICD-10 codes for autonomic dysfunction",
        "Answer": "Codes include G90.3, G90.4, E11.43, G90.A, among others depending on specific conditions related to autonomic dysfunction."
    },
    {
        "Term": "Can ANS testing be used for routine diabetic screening?",
        "Answer": "No, routine screening in asymptomatic individuals (even with diabetes) is not medically necessary and not covered."
    },
    {
        "Term": "What documentation is required for ANS testing reimbursement?",
        "Answer": "Documentation must include symptoms, prior test results ruling out other causes, and show how test results influence treatment. Lack of documentation can lead to denial."
    },
    {
        "Term": "Difference between medically necessary vs. investigational ANS testing",
        "Answer": "Medically necessary tests are validated and influence care. Investigational tests like ANSAR ANX 3.0 or SUDOSCAN are automated, non-validated, and not covered."
    },
    {
        "Term": "How often can ANS testing be done?",
        "Answer": "Testing should only be repeated if there is a change in clinical status or to evaluate treatment response. Routine testing is not covered."
    }
]

# Create DataFrame and save as CSV
df1 = pd.DataFrame(data1).head(5)
df1.rename(columns={'Term' : 'Search Term', 'Answer' : 'Expected Answer'}, inplace=True)




link2 = "https://medpolicy.ibx.com/ibc/Commercial/Pages/Policy/3ac82d0c-32e3-4a54-be0e-fc60783c4108.aspx"


# Define the search terms and expected answers
data2 = {
    "Search Term": [
        "Cranial helmet medical necessity criteria",
        "ICD-10 codes for plagiocephaly helmet coverage",
        "Cephalic index measurement standards",
        "Documentation requirements for helmet DME claims",
        "Age limits for cranial remolding orthosis"
    ],
    "Expected Answer": [
        "Criteria include age 3-18 months, failure of 8-week conservative therapy, and documented cranial asymmetry.",
        "Q67.3, Q67.4, M95.2, and various Q75.x codes depending on the type of craniosynostosis.",
        "Cephalic index should be at least ±2 SD from the mean based on age and gender-specific normative data.",
        "Must include timely signed standard written order, delivery confirmation, and clinical documentation of medical necessity.",
        "Covered for infants aged 3 to 18 months; optimal initiation between 3 and 6 months of age."
    ]
}

# Create the DataFrame
df2 = pd.DataFrame(data2)



link3 = "https://medpolicy.ibx.com/ibc/Commercial/Pages/Policy/86537148-8562-4da7-87ef-9ebe5abed28b.aspx"


# Define five search terms and their expected answers
data3 = {
    "Search Term": [
        "When should average-risk individuals start CRC screening?",
        "What colorectal cancer screening tests are covered for high-risk patients?",
        "Is Cologuard Plus covered by insurance?",
        "Are blood-based CRC screening tests like Epi proColon covered?",
        "What documentation is required for CRC screening coverage?"
    ],
    "Expected Answer": [
        "Screening begins at age 45 for average-risk individuals, as per ACS and USPSTF guidelines.",
        "High-risk individuals are covered at any age and frequency per provider recommendation; includes colonoscopy and other standard methods.",
        "No, Cologuard Plus is considered experimental/investigational and not covered.",
        "No, blood-based tests like Epi proColon are considered experimental/investigational and not covered.",
        "The individual's medical record must reflect the medical necessity for care provided; documentation must be available upon request."
    ]
}

# Create DataFrame
df3 = pd.DataFrame(data3)



link4 = "https://medpolicy.ibx.com/ibc/Commercial/Pages/Policy/84c1878f-0009-47d5-8883-e6a2090ddade.aspx"


data4 = {
    "Search Term": [
        "When is homocysteine testing covered?",
        "Is methylmalonic acid (MMA) testing covered for vitamin B12 deficiency?",
        "How often can B12 and folic acid testing be billed?",
        "Is holo-transcobalamin testing reimbursable?",
        "What documentation is required for B12/folate testing coverage?"
    ],
    "Expected Answer": [
        "Homocysteine testing is covered for borderline B12 deficiency, suspected homocystinuria, or thrombo-embolism under age 45 or in unusual locations.",
        "Yes, MMA testing is covered when vitamin B12 levels are borderline-low (200–300 pg/mL) or low (<200 pg/mL).",
        "Up to 3 times per year per test (B12 and folic acid) are covered for medically necessary diagnoses listed under CPT codes 82607, 82608, 82746, and 82747.",
        "No, holo-transcobalamin testing is considered experimental/investigational and is not covered.",
        "Provider documentation must support medical necessity. Records must be available upon request and may include office notes, test results, and provider history."
    ]
}

df4 = pd.DataFrame(data4)

df1['link'] = link1
df2['link'] = link2
df3['link'] = link3
df4['link'] = link4

df = pd.concat([df1, df2, df3, df4], axis=0)

df.to_csv("eval_samples.csv", index=False)

