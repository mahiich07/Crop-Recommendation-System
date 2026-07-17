import streamlit as st
import joblib
import numpy as np
import base64

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()
    
img = get_base64("assets/FarmImage.jpg")

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load("../Models/crop_recommendation_model.pkl")
label_encoder = joblib.load("../Models/label_encoder.pkl")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(f"""
<style>


/* Background */
.stApp{{
background:linear-gradient(180deg,#EEF7EE,#F9FCF8);
}}

/* Main Container */
.block-container{{
    padding-top:2rem;
    padding-bottom:2rem;
}}

/* Sidebar */
section[data-testid="stSidebar"]{{
    background:#1F4D2E;
}}

section[data-testid="stSidebar"] *{{
    color:white;
}}

/* Hero Banner */

.hero{{

background:
linear-gradient(
rgba(27,94,32,0.35),
rgba(46,125,50,0.20)
),
url("data:image/jpg;base64,{img}");

background-size:cover;
background-position:center;
background-repeat:no-repeat;

padding:60px 40px;

border-radius:22px;

text-align:center;

color:white;

box-shadow:0 12px 30px rgba(0,0,0,.15);

margin-bottom:35px;

}}

.hero h1{{
    font-size:58px;
    font-weight:700;
    margin-bottom:12px;
}}

.hero h3{{
    font-size:24px;
    font-weight:500;
    margin-bottom:20px;
}}

.hero p{{
    font-size:20px;
    max-width:900px;
    margin:auto;
    line-height:1.6;
}}

/* Dashboard Cards */

.card{{
background:white;
border-top:6px solid #43A047;
border-radius:18px;
padding:18px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.card h2{{
color:#2E7D32;
margin-bottom:10px;
}}

.card p{{
font-size:18px;
color:#555;
}}

/* Result */

.result{{
background:white;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 5px 15px rgba(0,0,0,.08);
border-left:8px solid #2E7D32;
margin-top:30px;
}}

.result h1{{
    color:#2E7D32;
    font-size:64px;
    font-weight:700;
    margin:10px 0;
}}

/* Footer */

.footer{{
text-align:center;
margin-top:50px;
color:gray;
font-size:15px;
}}

label{{
color:#222 !important;
font-weight:600;
}}
            
/* ==========================================================
   BUTTON
========================================================== */

div.stButton > button{{
    width:100%;
    height:60px;
    background:linear-gradient(90deg,#2E7D32,#43A047) !important;
    color:white !important;
    font-size:20px;
    font-weight:700;
    border:none !important;
    border-radius:12px;
    transition:0.3s;
}}

div.stButton > button:hover{{
    background:linear-gradient(90deg,#1B5E20,#2E7D32) !important;
    color:white !important;
    border:none !important;
}}

div.stButton > button:focus{{
    color:white !important;
    border:none !important;
    box-shadow:none !important;
}}

div.stButton > button:active{{
    color:white !important;
}}
            
</style>
""", unsafe_allow_html=True)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("Project Details")

    st.markdown("---")

    st.subheader("Model")
    st.success("Naive Bayes")

    st.subheader("Accuracy")
    st.info("99.55%")

    st.subheader("Dataset")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Samples", "2200")

    with c2:
        st.metric("Crops", "22")

    st.markdown("---")

    st.subheader("Features")

    st.write("Nitrogen (N)")
    st.write("Phosphorus (P)")
    st.write("Potassium (K)")
    st.write("Temperature")
    st.write("Humidity")
    st.write("Soil pH")
    st.write("Rainfall")

    st.markdown("---")

    st.subheader("Developed By")

    st.write("**Mahi Chaudhary**")

    st.write("B.Tech Artificial Intelligence & Machine Learning")

    st.write("IGDTUW")

# ==========================================================
# HERO BANNER
# ==========================================================

st.markdown("""
<div class="hero">

<h1>Crop Recommendation System</h1>

<p>
AI-Powered Smart Farming Assistant
</p>

<p>
Predict the most suitable crop using soil nutrients
and environmental conditions with Machine Learning.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# DASHBOARD CARDS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
    <h2>Model</h2>
    <p>Naive Bayes</p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
    <h2>Accuracy</h2>
    <p>99.55%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">
    <h2>Dataset</h2>
    <p>2200 Samples</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.info("Enter the required soil and environmental values below to receive the most suitable crop recommendation.")

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown("""
<h2 style="
color:#2E7D32;
font-weight:700;
margin-bottom:10px;
">
Enter Soil & Environmental Details
</h2>
""", unsafe_allow_html=True)
st.write("")

left, right = st.columns(2)

# ==========================================================
# SOIL INFORMATION
# ==========================================================

with left:

    st.markdown("""
    <div class="card">
        <h2>Soil Information</h2>
        <p>Enter the soil nutrient values.</p>
    </div>
    """, unsafe_allow_html=True)

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=90.0
    )

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=42.0
    )

    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=43.0
    )

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

# ==========================================================
# ENVIRONMENTAL CONDITIONS
# ==========================================================

with right:

    st.markdown("""
    <div class="card">
        <h2>Environmental Conditions</h2>
        <p>Enter the weather parameters.</p>
    </div>
    """, unsafe_allow_html=True)

    temperature = st.number_input(
        "Temperature (°C)",
        value=20.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=200.0
    )

st.write("")
st.write("")

# ==========================================================
# PREDICTION
# ==========================================================

st.write("")
st.write("")

predict = st.button(
    "Recommend Crop",
    use_container_width=True
)

if predict:

    input_data = np.array([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    with st.spinner("🔍 Analyzing soil and environmental conditions..."):

        prediction = model.predict(input_data)

        crop = label_encoder.inverse_transform(prediction)

    st.success("✅ Prediction Completed Successfully")

    st.markdown(f"""
<div class="result">

<h2 style="color:#2E7D32; font-size:32px;">
🌾 Recommended Crop
</h2>

<h1>{crop[0].title()}</h1>

<p style="
font-size:18px;
color:#555;
line-height:1.7;
">
Based on the soil nutrients and environmental conditions provided,
<b>{crop[0].title()}</b> is predicted to be the most suitable crop for cultivation.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""
<div class="footer">

<h3 style="color:#2E7D32;">
Crop Recommendation System
</h3>

<p>
Developed by <b>Mahi Chaudhary</b>
</p>

<p>
B.Tech Artificial Intelligence & Machine Learning
</p>

<p>
Indira Gandhi Delhi Technical University for Women (IGDTUW)
</p>


</div>
""", unsafe_allow_html=True)



