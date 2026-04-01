import streamlit as st
from rdkit import Chem

# -------------------------------
# SESSION CONTROL (for page switch)
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE (Your Details)
# -------------------------------
if st.session_state.page == "home":
    
    st.title("🧪 Drug Chirality Analyzer Project")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** Vishnu")  # <-- change this
    st.write("**Register No:** 123456")  # <-- change this
    st.write("**Class:** B.Sc Chemistry")  # <-- change this

    st.markdown("---")
    
    st.write("This project detects chiral carbons and their R/S configuration in drug molecules.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    st.write("Enter a SMILES string to detect chiral centers")

    smiles = st.text_input(
        "SMILES Input",
        "COc1ccc2c(c1)CCN(C[C@H]3CCc4cc(OC)c(OC)cc4C3)C2"
    )

    def analyze_chirality(smiles):
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            return "❌ Invalid SMILES"

        mol = Chem.AddHs(mol)
        Chem.AssignStereochemistry(mol, force=True, cleanIt=True)

        chiral_centers = Chem.FindMolChiralCenters(
            mol,
            includeUnassigned=True,
            useLegacyImplementation=False
        )

        if not chiral_centers:
            return "❌ No chiral centers found"

        result = ""
        for idx, config in chiral_centers:
            result += f"🧪 Atom {idx} → {config}\n"

        return result

    if st.button("Analyze"):
        result = analyze_chirality(smiles)
        st.text(result)

    # Back button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"