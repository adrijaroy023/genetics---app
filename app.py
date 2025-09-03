import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

st.set_page_config(page_title="Genetics Learning Hub", layout="wide")

st.title("🧬 Genetics Learning Hub")
st.write("An interactive app to explore genetics concepts, practice quizzes, and play fun games!")

# --- Sidebar Navigation ---
menu = ["Home", "Punnett Square", "MCQ Quiz", "Fun Facts"]
choice = st.sidebar.radio("Go to", menu)

# --- HOME ---
if choice == "Home":
    st.header("📊 DNA Base Distribution Example")
    bases = ["A", "T", "G", "C"]
    counts = [30, 30, 20, 20]

    fig, ax = plt.subplots()
    ax.bar(bases, counts, color=["#4CAF50", "#2196F3", "#FFC107", "#F44336"])
    ax.set_ylabel("Percentage")
    ax.set_title("DNA Base Composition Example")
    st.pyplot(fig)

    st.info("This is a demo graph of nucleotide distribution. You’ll find quizzes and games in the sidebar!")

# --- PUNNETT SQUARE ---
elif choice == "Punnett Square":
    st.header("🎲 Punnett Square Generator")

    st.write("Enter two parent genotypes (like `Aa` and `Aa`):")
    p1 = st.text_input("Parent 1", "Aa")
    p2 = st.text_input("Parent 2", "Aa")

    if len(p1) == 2 and len(p2) == 2:
        punnett = [a+b for a in p1 for b in p2]
        results = pd.Series(punnett).value_counts(normalize=True) * 100
        st.write("**Results (% probability):**")
        st.write(results)

        st.bar_chart(results)

# --- QUIZ ---
elif choice == "MCQ Quiz":
    st.header("📝 Genetics MCQ Practice")

    questions = [
        {
            "q": "Who is known as the father of genetics?",
            "options": ["Charles Darwin", "Gregor Mendel", "James Watson", "Francis Crick"],
            "answer": "Gregor Mendel"
        },
        {
            "q": "DNA is made up of repeating units called?",
            "options": ["Nucleotides", "Amino acids", "Fatty acids", "Polypeptides"],
            "answer": "Nucleotides"
        },
        {
            "q": "Which base pairs with Adenine in DNA?",
            "options": ["Thymine", "Guanine", "Cytosine", "Uracil"],
            "answer": "Thymine"
        }
    ]

    q = random.choice(questions)
    st.write(q["q"])
    ans = st.radio("Choose one:", q["options"])

    if st.button("Check Answer"):
        if ans == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is: {q['answer']}")

# --- FUN FACTS ---
elif choice == "Fun Facts":
    st.header("🎉 Fun Genetics Facts & Games")

    facts = [
        "Did you know? Humans share about 60% of their DNA with bananas 🍌",
        "If you stretched out all the DNA in your body, it would reach the sun and back many times! ☀️",
        "Eye color is controlled by multiple genes, not just one 👁️",
        "Identical twins have almost identical DNA, but not 100%! 🧑‍🤝‍🧑"
    ]

    st.write(random.choice(facts))

    st.subheader("Mini Game: Guess the Trait")
    st.write("A child has one parent with blue eyes (bb) and one with brown eyes (Bb). What’s the probability of the child having blue eyes?")
    guess = st.slider("Your guess (%)", 0, 100, 25)
    if st.button("Check Guess"):
        st.info("Correct probability: 50% (Bb or bb outcomes).")
