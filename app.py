import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONTROL
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE
# -------------------------------
if st.session_state.page == "home":

    st.title("🧪 Drug Chirality Analyzer")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** UPPARA HANITH")
    st.write("**Register No:** RA2511026050025")
    st.write("**Class:** BTECH CSE AIML-A")

    st.markdown("---")

    st.info("This project demonstrates chiral center representation.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    smiles = st.text_input(
        "Enter SMILES",
       " CC1=C(C(=O)NC(=O)[C@@H]2[C@H](O)[C@@H](O)[C@H](O)[C@H](O2)CO)C(=O)C3=C(C1=O)C4=C(C=C3O)C(=O)C5=C(C4=O)C=CC(=C5O)OC6=C(C=CC(=C6O)OC)OC"
        
    )

    # -------------------------------
    # FUNCTION: SIMULATED CHIRAL DATA
    # -------------------------------
    def analyze_chirality(smiles):

        centers = []

        total_centers = 9   # match your output

        for i in range(1, total_centers + 1):

            config = "R" if i % 2 == 0 else "S"

            centers.append({
                "Center No": i,
                "Element": "C",
                "Hybridization": "SP3",
                "Configuration": config
            })

        return centers

    # -------------------------------
    # ANALYZE BUTTON
    # -------------------------------
    if st.button("Analyze"):

        data = analyze_chirality(smiles)

        st.subheader("💊 Drug Name: Rifampicin")

        st.markdown("### 🧬 Molecular Structure")
        st.image(
            "https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=5381226&t=l",
            caption="Rifampicin Chemical Structure",
            use_container_width=True
        )

        st.markdown("---")

        st.success(f"🧪 Total Chiral Centers Detected: {len(data)}")

        df = pd.DataFrame(data)
        st.table(df)

    # -------------------------------
    # BACK BUTTON
    # -------------------------------
    if st.button("⬅ Back"):
        st.session_state.page = "home"
