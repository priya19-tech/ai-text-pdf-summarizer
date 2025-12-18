import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="AI Text & PDF Summarizer",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------
# Custom CSS (Colors + Animation)
# -------------------------------------------------
st.markdown("""
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

/* Title styling */
.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
    opacity: 0.9;
}

/* Card style */
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    color: white;
    border: none;
    padding: 12px 30px;
    font-size: 18px;
    border-radius: 30px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
}

/* Summary points */
.summary-point {
    background: rgba(255, 255, 255, 0.2);
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    animation: slideUp 0.6s ease-in-out;
}

/* Animations */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes slideUp {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Load Hugging Face Summarizer
# -------------------------------------------------
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

summarizer = load_summarizer()

# -------------------------------------------------
# Helper: Chunk text for full coverage
# -------------------------------------------------
def chunk_text(text, chunk_size=800):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

# -------------------------------------------------
# UI Content
# -------------------------------------------------
st.markdown("<div class='main-title'>🧠 AI Text & PDF Summarizer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Full Coverage • Free AI • Point-wise Summary</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
text_input = st.text_area("✍️ Enter text to summarize", height=220)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📄 Or upload a PDF file", type=["pdf"])
st.markdown("</div>", unsafe_allow_html=True)

pdf_text = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            pdf_text += extracted
    st.success("✅ PDF uploaded and text extracted successfully")

# -------------------------------------------------
# Summarize Button
# -------------------------------------------------
if st.button("✨ Summarize"):
    final_text = text_input.strip() if text_input.strip() else pdf_text.strip()

    if final_text == "":
        st.warning("⚠️ Please enter text or upload a PDF.")
    else:
        with st.spinner("🧠 Analyzing and summarizing full content..."):
            chunks = chunk_text(final_text)
            all_summaries = []

            for chunk in chunks:
                result = summarizer(
                    chunk,
                    max_length=500,
                    min_length=120,
                    do_sample=False
                )
                all_summaries.append(result[0]["summary_text"])

        full_summary = " ".join(all_summaries)
        points = full_summary.split(". ")

        st.markdown("## ✅ Full Summary (Point-wise)")
        for i, point in enumerate(points, start=1):
            if point.strip():
                st.markdown(
                    f"<div class='summary-point'><b>{i}.</b> {point.strip()}</div>",
                    unsafe_allow_html=True
                )
