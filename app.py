import streamlit as st
import numpy as np

# -------------------------------------------------
# App Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="AI-Based Concept Fragility Analyzer",
    layout="centered"
)

# -------------------------------------------------
# Title & Description
# -------------------------------------------------
st.title("AI-Based Concept Fragility Analyzer")
st.write(
    "Analyze whether a student's understanding of a concept is "
    "**Strong**, **Fragile**, or **Memorized** based on performance consistency."
)

st.divider()

# -------------------------------------------------
# Input Section (USER INPUT IS TAKEN HERE)
# -------------------------------------------------
st.subheader("Enter Performance Details")

avg_score = st.slider(
    "Average Score",
    min_value=0,
    max_value=100,
    value=70
)

score_variance = st.slider(
    "Score Variance",
    min_value=0,
    max_value=300,
    value=50
)

time_taken = st.slider(
    "Time Taken (seconds)",
    min_value=50,
    max_value=300,
    value=150
)

# -------------------------------------------------
# Analyze Button
# -------------------------------------------------
if st.button(" Analyze Concept"):
    # -------------------------------------------------
    # FINAL LOGIC (RULE-BASED OVERRIDE)
    # -------------------------------------------------
    if avg_score >= 80 and score_variance >= 50 and time_taken >= 180:
        result = "Memorized"
    elif avg_score >= 80 and score_variance < 50:
        result = "Strong"
    else:
        result = "Fragile"

    # -------------------------------------------------
    # Output Section
    # -------------------------------------------------
    st.divider()
    st.subheader("Result")

    if result == "Strong":
        st.success(" **Strong Understanding**")
        st.write("✔ Consistent performance across difficulty levels.")
        st.write("✔ Good conceptual clarity.")

    elif result == "Memorized":
        st.info(" **Memorized Knowledge**")
        st.write("• High average score but large variation.")
        st.write("• High time taken indicates rote memorization.")
        st.write("• Recommended to focus on conceptual understanding.")

    else:
        st.warning("**Fragile Understanding**")
        st.write("• Inconsistent or weak performance.")
        st.write("• Concept breaks under variation.")
        st.write("• Needs revision and mixed-difficulty practice.")
