# GNN-LinkPrediction
# Graph Neural Network (GNN) for Link Prediction
An interactive Deep Learning project to predict future connections in a social network using **Graph Convolutional Networks (GCN)**.

## Project Overview
This project implements a GNN model to solve the **Link Prediction** problem. It uses an **Encoder-Decoder** architecture where:
- **Encoder:** A 2-layer GCN that learns node embeddings from graph structure and features.
- **Decoder:** A dot-product based link predictor that calculates the probability of an edge between two nodes.



## Features
- **High Accuracy:** Achieved a **Test AUC Score of 0.89** on the Cora dataset.
- **Interactive UI:** Built with **Streamlit** to visualize the graph and predict links in real-time.
- **Dynamic Visualization:** Uses **Pyvis** for an interactive, physics-based social network graph.
- **Scalable:** Optimized for sparse graph computations.

## Tech Stack
- **Deep Learning:** PyTorch, PyTorch Geometric (PyG)
- **UI/Dashboard:** Streamlit
- **Graph Ops:** NetworkX, Pyvis
- **Data:** Cora Research Paper Dataset

## Demo Screenshot
<img width="1905" height="943" alt="image" src="https://github.com/user-attachments/assets/3b7ea799-870a-49bc-9382-3d8dc14e2a09" />





