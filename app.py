import streamlit as st
import pandas as pd
from io import BytesIO

from src.jd_parser import parse_job_description
from src.ranker import rank_candidates

st.set_page_config(page_title="AI Candidate Ranking System")

st.title("🤖 AI Candidate Ranking System")
st.subheader("Team CipherNova")

uploaded_file = st.file_uploader(
    "Upload Job Description (.docx)",
    type=["docx"]
)

if uploaded_file is not None:

    # Save uploaded JD
    with open("temp_jd.docx", "wb") as f:
        f.write(uploaded_file.read())

    jd = parse_job_description("temp_jd.docx")

    if st.button("Rank Candidates"):

        with st.spinner("Ranking Candidates..."):

            df = rank_candidates(
                "data/candidates.jsonl",
                jd
            )

        st.success("Ranking Complete!")

        st.dataframe(df)

        # Create Excel file in memory
        output = BytesIO()

        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Submission")

        output.seek(0)

        st.download_button(
            label="📥 Download Submission (.xlsx)",
            data=output,
            file_name="submission.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )