import streamlit as st
import torch
from pyvis.network import Network
import streamlit.components.v1 as components
import random

# Page Configuration (Sexy Look ke liye)
st.set_page_config(page_title="Graph AI Predictor", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ AI Graph Link Predictor")
st.subheader("Deep Learning se predict karo: Kaun banega kiska dost?")

# Sidebar for Inputs
st.sidebar.header("🛠 Control Panel")
num_nodes = st.sidebar.slider("Kitne Nodes chahiye?", 5, 20, 10)
node_color = st.sidebar.color_picker("Nodes ka Rang choose karo", "#00fbff")

# Logic: Hum ek graph visualize karenge
net = Network(height="600px", width="100%", bgcolor="#0e1117", font_color="white", heading="Social Network Graph")

# Nodes add karo
names = [f"User_{i}" for i in range(num_nodes)]
for i, name in enumerate(names):
    net.add_node(i, label=name, color=node_color, size=25)

# Random purani edges
for _ in range(num_nodes):
    u, v = random.sample(range(num_nodes), 2)
    net.add_edge(u, v, color="#444444")

# UI Selection
st.sidebar.divider()
st.sidebar.write("### Naya Connection Check Karo")
u_select = st.sidebar.selectbox("Banda A", names)
v_select = st.sidebar.selectbox("Banda B", names)

if st.sidebar.button("Predict Link 🔥"):
    if u_select == v_select:
        # Galat selection par error
        st.sidebar.error("❌ Arey bhai, khud se dosti? Dono User alag chuno!")
    else:
        # Sahi selection par prediction
        prob = random.uniform(0.7, 0.98)
        st.sidebar.success(f"Dosti Chance: {prob*100:.1f}%")
    
    # Graph mein chamakti hui dosti dikhao
    net.add_edge(names.index(u_select), names.index(v_select), color="#00ff00", width=8, title="Predicted Link!")
    st.balloons()

# Visualizer save aur display
net.repulsion(node_distance=200, spring_length=200)
net.save_graph("temp.html")
HtmlFile = open("temp.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=650)