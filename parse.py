import os
from openai import OpenAI

# Load API Key from environment variables
API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    raise ValueError("DEEPSEEK_API_KEY is not set. Update your .env or GitHub Secrets.")

# Improved template for better parsing and understanding
TEMPLATE = """
You are an advanced AI assistant specializing in structured data extraction from HTML.
Your goal is to analyze and extract key insights from the provided webpage content.

**Instructions:**
1. Understand the provided HTML content and identify relevant information.
2. Extract the meaningful text while removing unnecessary elements (scripts, styles, etc.).
3. Maintain formatting and logical structure in the extracted text.
4. Follow the specific parsing instructions provided below.

---
**HTML Content:**
{dom_content}

**Parsing Instructions:**
{parse_description}

Return the cleaned and well-structured text in a readable format.
"""

def parse_with_deepseek(dom_chunks, parse_description):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )

    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        system_prompt = TEMPLATE.format(dom_content=chunk, parse_description=parse_description)
        try:
            completion = client.chat.completions.create(
                model="deepseek/chat",
                messages=[{"role": "system", "content": system_prompt}]
            )
            text_output = completion.choices[0].message.content.strip()
            print(f"✅ API Response for Batch {i}: {text_output}")  # Debugging Line
            parsed_results.append(text_output)
        except Exception as e:
            print(f"❌ API Call Failed: {e}")  # Debugging Line
            parsed_results.append("[Error: Unable to process this batch]")
    
    return "\n".join(parsed_results)
