import streamlit as st
from rdkit import Chem

# -------------------------
# Page Title
# -------------------------
st.set_page_config(page_title="Drug Chirality Analyzer")

st.title("🧪 Drug Chirality Analyzer")

st.write("Analyze chiral carbons and R/S configuration in drug molecules")

# -------------------------
# Drug Info
# -------------------------
st.subheader("💊 Drug: Rifampicin")

# SMILES for Rifampicin (contains multiple chiral centers)
default_smiles = "CC1=C(C(=O)NC(=O)[C@@H]2[C@H](O)[C@@H](O)[C@H](O)[C@H](O2)CO)C(=O)C3=C(C1=O)C4=C(C=C3O)C(=O)C5=C(C4=O)C=CC(=C5O)OC6=C(C=CC(=C6O)OC)OC"

smiles = st.text_input("Enter SMILES:", default_smiles)

# -------------------------
# Function
# -------------------------
def analyze_chirality(smiles):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return "❌ Invalid SMILES"

    mol = Chem.AddHs(mol)

    Chem.AssignAtomChiralTagsFromStructure(mol)
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
        result += f"🧪 Atom Index {idx} → Configuration: {config}\n"

    return result

# -------------------------
# Button
# -------------------------
if st.button("Analyze Chirality"):
    result = analyze_chirality(smiles)

    st.subheader("🔬 Result")
    st.text(result)

    st.info(
        "Rifampicin has multiple chiral centers. "
        "Each center has R or S configuration based on 3D arrangement."
    )
