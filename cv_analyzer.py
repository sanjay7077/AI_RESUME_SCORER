import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")  # Load API key from .env file
)

def analyze_cv(cv_text):
    # Prompt template for CV analysis
    prompt = f"""You are an AI hiring expert for an AI Research Engineer position.
    Please analyze the following CV and provide scores (0-100) for each category.
    
    CV Text:
    {cv_text}
    
    Evaluate and score based on these criteria:
    1. Technical Skills (ML/DL, programming): Score and explanation
    2. Research Experience: Score and explanation
    3. Education Background: Score and explanation
    4. Industry Experience: Score and explanation
    
    IMPORTANT: Provide ONLY the JSON response with no additional text or commentary.
    Format your response exactly like this:
    {{
        "technical_skills": {{
            "score": X,
            "explanation": "..."
        }},
        "research_experience": {{
            "score": X,
            "explanation": "..."
        }},
        "education": {{
            "score": X,
            "explanation": "..."
        }},
        "industry_experience": {{
            "score": X,
            "explanation": "..."
        }},
        "overall_score": X,
        "recommendation": "proceed/reject"
    }}
    """

    # Make API call
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI hiring assistant that evaluates CVs. Always respond with valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.1
    )
    
    # Get only the JSON part of the response
    response = completion.choices[0].message.content.strip()
    
    # Remove any additional text after the last closing brace
    last_brace_index = response.rfind('}')
    if last_brace_index != -1:
        response = response[:last_brace_index + 1]
    
    return response

# Example usage
def main():
    # Example CV text (you would normally read this from a file)
    sample_cv = """
    EDUCATION
    PhD in Machine Learning, Stanford University
    Research focus: Deep Learning for Computer Vision
    
    EXPERIENCE
    AI Research Scientist at Google Brain
    - Developed novel transformer architectures
    - Published 3 papers at NeurIPS
    
    SKILLS
    Python, PyTorch, TensorFlow, CUDA
    Deep Learning, Reinforcement Learning, NLP
    """
    
    result = analyze_cv(sample_cv)
    print(result)

if __name__ == "__main__":
    main()