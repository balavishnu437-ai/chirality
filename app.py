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

    st.info("This project analyzes chiral centers in complex drug molecules.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    # ✅ Rifampicin SMILES (real molecule)
    smiles = st.text_input(
        "Enter SMILES",
        "CC1=C(C(=O)NC(=O)[C@@H]2[C@H](O)[C@@H](O)[C@H](O)[C@H](O2)CO)C(=O)C3=C(C1=O)C4=C(C=C3O)C(=O)C5=C(C4=O)C=CC(=C5O)OC6=C(C=CC(=C6O)OC)OC"
    )

    # -------------------------------
    # FUNCTION: REAL CHIRAL ANALYSIS
    # -------------------------------
    def analyze_chirality(smiles):

        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            return None

        mol = Chem.AddHs(mol)

        Chem.AssignAtomChiralTagsFromStructure(mol)
        Chem.AssignStereochemistry(mol, force=True, cleanIt=True)

        chiral_centers = Chem.FindMolChiralCenters(
            mol,
            includeUnassigned=True,
            useLegacyImplementation=False
        )

        results = []

        for i, (idx, config) in enumerate(chiral_centers, start=1):
            atom = mol.GetAtomWithIdx(idx)

            results.append({
                "Center No": i,
                "Atom Index": idx,
                "Element": atom.GetSymbol(),
                "Hybridization": str(atom.GetHybridization()),
                "Configuration": config
            })

        return results

    # -------------------------------
    # ANALYZE BUTTON
    # -------------------------------
    if st.button("Analyze"):

        data = analyze_chirality(smiles)

        st.subheader("💊 Drug Name: Rifampicin")

        # ✅ STRUCTURE IMAGE
        st.markdown("### 🧬 Molecular Structure")
        st.image(
            "https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=5381226&t=l",
            caption="Rifampicin Chemical Structure",
            use_container_width=True
        )

        st.markdown("---")

        if data is None:
            st.error("❌ Invalid SMILES string")

        elif len(data) == 0:
            st.warning("⚠ No chiral centers found")

        else:
            st.success(f"🧪 Total Chiral Centers Detected: {len(data)}")

            df = pd.DataFrame(data)
            st.dataframe(df)

    # -------------------------------
    # BACK BUTTON
    # -------------------------------
    if st.button("⬅ Back"):
        st.session_state.page = "home"
