import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_deepseek

st.title("AI Web Scraper with DeepSeek")
st.markdown("### Powered by OpenRouter's DeepSeek AI")

# Keep DOM chunks and full cleaned content in session state so we don't re-scrape again
if "dom_chunks" not in st.session_state:
    st.session_state.dom_chunks = None
if "cleaned_content" not in st.session_state:
    st.session_state.cleaned_content = None

# Step 1: Scrape website
url = st.text_input("Enter Website URL")
if st.button("Scrape Website"):
    if url:
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)
        st.session_state.cleaned_content = cleaned_content
        st.session_state.dom_chunks = split_dom_content(cleaned_content)
        st.success("Website scraped successfully and DOM content is ready!")
    else:
        st.warning("Please enter a URL before scraping.")

st.markdown("---")

# Display dropdown and chat-style parsing only if DOM content is available
if st.session_state.dom_chunks:
    with st.expander("View DOM Content"):
        st.markdown("### Extracted DOM Content")
        st.text_area("DOM Content", value=st.session_state.cleaned_content, height=300)
    
    st.markdown("#### DeepSeek Chat-Style Parsing")
    parse_description = st.text_area("Parse/Chat Instructions", "Ask or parse multiple times here...")
    if st.button("Parse with DeepSeek", key="parse_btn"):
        parsed_content = parse_with_deepseek(st.session_state.dom_chunks, parse_description)
        st.write("Parsed/Chat Response:")
        st.write(parsed_content)
else:
    st.markdown("### Please scrape a website to view DOM content and use DeepSeek Chat.")

st.markdown("---")
st.markdown("**Credits:** Made by [Ansh Jain](https://www.linkedin.com/in/ansh--jain) Powered by DeepSeek API.")
