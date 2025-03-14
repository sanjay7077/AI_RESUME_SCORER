import streamlit as st
from cv_analyzer import analyze_cv
import PyPDF2
import io

def main():
    st.title("AI Resume Score")
    
    # File upload
    uploaded_file = st.file_uploader("Upload CV (PDF or TXT)", type=["pdf", "txt"])
    
    if uploaded_file:
        # Read file content
        if uploaded_file.type == "application/pdf":
            # Process PDF file
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            cv_text = ""
            for page in pdf_reader.pages:
                cv_text += page.extract_text()
        else:
            cv_text = uploaded_file.read().decode()
        
        if st.button("Analyze CV"):
            with st.spinner("Analyzing CV..."):
                result = analyze_cv(cv_text)
                st.json(result)

if __name__ == "__main__":
    main()