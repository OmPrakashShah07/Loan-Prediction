import streamlit as st
import pandas as pd
import pickle as pk

st.title('Loan Status')
st.image("https://hfcl-website-cms.s3.ap-south-1.amazonaws.com/Page_227_blog_1_How_Do_I_Qualify_for_An_Unsecured_Personal_Loan_09197b6caa.png")


load_model = pk.load(open('loan_data.pickle','rb'))

# ---- User Inputs ----
Age = st.number_input("Enter your age = ")
Gender = st.radio("Gender = ", ["Male","Female"])
Education = st.selectbox("Select your Education", ["High_School", "Bachelor", "Associate", "Master", "Doctorate"])
Income = st.number_input("Enter you Income amount = ")
Work_Exp = st.number_input("Enter your work experience = ")
Home_Ownership = st.selectbox("Select where you live = ", ["RENT", "MORTGAGE", "OWN", "OTHER"])
Loan_amount = st.number_input("Enter your asked loan amount = ")
Loan_intent = st.selectbox("Enter your intention to get loan =", ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"])
RI = st.number_input("Enter interest rest = ")
Loan_Percent_Income = st.number_input("Enter Loan Percent Income = ")
cb_Person_Cred_Hist_length = st.number_input("Enter cb Person Cred Hist length = ")
Credit_Score = st.number_input("Enter Credit Score = ")
previous_loan_defults_on_file = st.radio("Previous loan defults on file = ", ["Yes", "No"])


# ---- Encoding categorical features ----

gender_map = {"Male": 1, "Female": 0}
education_map = {"High_School": 0, "Bachelor": 1, "Associate": 2, "Master": 3, "Doctorate": 4}
home_map = {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3}
intent_map = {
    "EDUCATION": 0, "MEDICAL": 1, "VENTURE": 2,
    "PERSONAL": 3, "DEBTCONSOLIDATION": 4, "HOMEIMPROVEMENT": 5
}
default_map = {"Yes": 1, "No": 0}

# ------------Apply mapping----------
Gender_val = gender_map[Gender]
Education_val = education_map[Education]
Home_val = home_map[Home_Ownership]
Intent_val = intent_map[Loan_intent]
Default_val = default_map[previous_loan_defults_on_file]


# ---- Prediction ----
if st.button("Predict"):
    df = pd.DataFrame({
        'person_age':[Age],
        "person_gender":[Gender_val],
        'person_education':[Education_val],
        'person_income':[Income],
        'person_emp_exp':[Work_Exp],
        'person_home_ownership':[Home_val],
        'loan_amnt':[Loan_amount],
        'loan_intent':[Intent_val],
        'loan_int_rate':[RI],
        'loan_percent_income':[Loan_Percent_Income],
        'cb_person_cred_hist_length':[cb_Person_Cred_Hist_length],
        'credit_score':[Credit_Score],
        'previous_loan_defaults_on_file':[Default_val]
    })
    st.dataframe(df)
    result = load_model.predict(df)
    if result == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")