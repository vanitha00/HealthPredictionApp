import streamlit as st
import pandas as pd
from datetime import date
from database import (
    add_patient,
    view_patients,
    delete_patient,
    update_patient,
    get_patient_by_id
)
from prediction import predict_health

st.title("🏥 Health Prediction Application")

# Form

name = st.text_input("Full Name")

dob = st.date_input(
    "Date of Birth",
    min_value=date(1950, 1, 1),
    max_value=date.today()
)

email = st.text_input("Email Address")

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

# Save Record
if st.button("Submit"):

    if "@" not in email:
        st.error("Please enter a valid email address")

    else:

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient(
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Patient Record Saved Successfully!")
# Display Records

st.subheader("All Patients")

patients = view_patients()

if patients:

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df)

# Delete Record

st.subheader("Delete Patient")

delete_id = st.number_input(
    "Enter Patient ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Patient"):

    delete_patient(delete_id)

    st.success("Patient Deleted Successfully!")

#Update Record
st.subheader("Update Patient")

update_id = st.number_input(
    "Enter Patient ID",
    min_value=1,
    step=1,
    key="uid"
)

if st.button("Load Patient"):

    patient = get_patient_by_id(update_id)

    if patient:

        st.session_state["patient"] = patient

    else:
        st.error("Patient Not Found")

if "patient" in st.session_state:

    patient = st.session_state["patient"]

    name_u = st.text_input(
        "Name",
        value=patient[1],
        key="name_u"
    )

    dob_u = st.text_input(
        "DOB",
        value=patient[2],
        key="dob_u"
    )

    email_u = st.text_input(
        "Email",
        value=patient[3],
        key="email_u"
    )

    glucose_u = st.number_input(
        "Glucose",
        value=float(patient[4]),
        key="glucose_u"
    )

    haemoglobin_u = st.number_input(
        "Haemoglobin",
        value=float(patient[5]),
        key="haemoglobin_u"
    )

    cholesterol_u = st.number_input(
        "Cholesterol",
        value=float(patient[6]),
        key="cholesterol_u"
    )

    remarks_u = predict_health(
    glucose_u,
    haemoglobin_u,
    cholesterol_u
   )

    if st.button("Update Record"):

        update_patient(
            patient[0],
            name_u,
            dob_u,
            email_u,
            glucose_u,
            haemoglobin_u,
            cholesterol_u,
            remarks_u
        )

        st.success("Patient Updated Successfully")