from PIL import Image
import streamlit as st
import altair as alt
import pandas as pd

image = Image.open("images/dna.png")

st.image(image, use_column_width = True)
st.write("""## DNA Nucleotide Count Web App
This app count the nucleotide composition of a query DNA  sequence
* **Credit:** Project guided by dataprofessor on freeCodeCamp.org, tutorial link: (https://www.youtube.com/watch?v=JwSS70SZdyM&t=11s)""")
st.write("""***""")
st.header("""Enter DNA Sequence""")

sample_sequence =   "-Sample DNA:\nAGTCATGGGTGCTGAGCTGAGACGGCGTCGATGCATAGCGGACTTTCGGT\nCAGTCGCAATTCCTCACGAGACTGGTCCTGTTGTGCGCATCACTCTCAAT\nGTACAAGCAACCCAAGAAGGCTGAGCCTGGACTCAACCGGTTGCTGGGTG\nAACTCCAGACTCGGGGCGACAACTCTTCATACATAGAGCAAGGGCGTCGA\nACGGTCGTGAAAGTCTTAGTACCGCACGTACCAACTTACTGAGGATATTG\nCCTGAAGCTGTACCGTTTTAGGGGGGGAAGGTTGAAGATCTCCTCTTCTC\nATGACTGAACTCGCGAGGGCCGTGTTGCCGGTTCCTTCAGAGGTTAAAGA\nACAAAGGCTTACTGTGCGCAGAGGAACGCCCATTTAGCGGCTGGCGTTTT\nGAATCCTCGGTCCCCCTTGTCTATCCAGATTAATCCAATTCCCTCATTTA\nGGACCCTACCAAGTCAACATTGGTATATGAATGCGACCTCGAAGAGGCCG\nCCTAAAAATGACAGTGGTTGGTGCTCTAAACTTCATTTGGTTAACTCGTG\nTATCAGCGCGATAGGCTGTTAGAGGTTTAATATTGTATGGCAAGGTACTT\nCCGGTCTTAATGAATGGCCGGGAAAGGTACGCACGCGGTATGGGGGGGTG\nAAGGGGCGAATAGACAGGCTCCCCTCTCACTCGCTAGGAGGCAATTGTAT\nAAGAATGCATACTGCATCGATACATAAAACGTCTCCATCGCTTGCCCAAG\nTTGTGAAGTGTCTATCACCCCTAGGCCCGTTTCCCGCATATTAACGCCTG\nATTGTATCCGCATTTGATGCTACCGTGGTTGAGTCAGCGTCGAGCACGCG\nGCACTTATTGCATGAGTAGAGTTGACTAAGAGCCGTTAGATGCCTCGCTG\nTACTAATAGTTGTCGACAGATCGTCAAGATTAGAAAACGGTAGCAGCATT\nATCGGAGGTTCTCTAACTAGTATGGATAGCCGTGTCTTCACTGTGCTGCG"

sequence = st.text_area(label = "Sequence:", value = sample_sequence, height=250)
sequence = "".join(sequence.splitlines()[1:])
# sequence
st.write("""***""")

st.header(f"""INPUT QUERY: """)
st.write("""{sequence if len(sequence) <= 70 else sequence[:68]+ '...'}""")

st.write("""***""")

st.header("""OUTPUT (DNA Nucleotide Count):""")

def count_nucleotides(seq):
    return dict([
        ("A",seq.count("A")),
        ("T",seq.count("B")),
        ("G", seq.count("G")),
        ("C", seq.count("C"))
    ])

st.subheader("1. Print Dictionary")
X = count_nucleotides(sequence)
X

st.subheader("2. Print Text")

st.write(f"""
There are {X["A"]} adenine (A), {X["T"]} thymine (T), \n
{X["G"]} guanine (G), and {X["C"]} cytocine (C)
""")

X_label = list(X)
X_values = list(X.values())

st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index").reset_index().rename({0:"count", "index":"nucleotide"}, axis=1)
st.write(df)

st.subheader("4. Display Barchart")

p = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)
p = p.properties(
    width = alt.Step(80)
)

st.write(p)

