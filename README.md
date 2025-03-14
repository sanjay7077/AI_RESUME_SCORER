# AI_RESUME_SCORER

## Requirements
1. groq   
2. python-dotenv   
3. streamlit   
4. PyPDF2  # for PDF processing

## process

Load Environment Variables

The script loads environment variables using dotenv, specifically the GROQ_API_KEY.
Initialize Groq Client

A Groq API client is instantiated with the API key.
Define analyze_cv(cv_text) Function

This function takes a CV (as text input).
It constructs a structured prompt asking the AI to score the CV based on:
Technical Skills (ML/DL, programming)
Research Experience
Education Background
Industry Experience
The AI is instructed to return only a JSON response containing scores, explanations, and an overall recommendation (proceed/reject).
Make API Call

The function sends the prompt to Groq’s chat model (mixtral-8x7b-32768).
The model responds with structured JSON output.
Post-Processing

The function extracts the JSON from the AI response, ensuring no extra text is included.
Example Execution (main())

A sample CV is provided.
The analyze_cv() function is called with this sample CV.
The AI-generated evaluation is printed.

# Streamlit
To Run : streamlit run app.py
