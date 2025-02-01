from openai import OpenAI

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''). "
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

API_KEY = "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"

def parse_with_deepseek(dom_chunks, parse_description):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )

    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        system_prompt = template.format(dom_content=chunk, parse_description=parse_description)
        try:
            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt}
                ]
            )
            text_output = completion.choices[0].message.content
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(text_output)
        except Exception as e:
            print(f"Request failed: {e}")
            parsed_results.append("")

    return "\n".join(parsed_results)
    
