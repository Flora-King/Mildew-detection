import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"

        f"Farmy & Foods, are the client for this project and are facing a \n"
        f"challenge where their cherry plantations have been presenting\n"
        f"powdery mildew.\n\n"
        f"Powdery mildew is a parasitic fungal disease caused by \n"
        f"Podosphaera clandestina in cherry trees.\n"
        f"When the fungus begins to take over the plants, a layer of mildew\n"
        f"made up of many spores forms across the top of the leaves.\n\n"
        f"The disease is particularly severe on new growth, can slow down\n"
        f"growth of the plant and can infect fruit as well, \n"
        f"causing direct crop loss.\n\n"

        f"The process used by Farmy & Foods to verify presence of powdery\n"
        f"mildew is manual. An employee spends around 30 minutes on each\n"
        f"tree, taking a few samples of tree leaves\n"
        f"and verifying visually if the leaf is healthy or has powdery\n"
        f"mildew. If there is powdery mildew, the employee spends 1 minute\n"
        f"applying a specific compound to kill the fungus.\n"
        f"The company has thousands of cherry trees, located on multiple\n"
        f"farms across the country and tie saving solution is needed.\n\n"

        f"To address this challenge the IT team suggested an ML system that \n"
        f"uses a leaf image to instantly detect if it is healthy or has\n"
        F"powdery mildew.\n"
        f"A similar manual process is in place for other crops for detecting\n"
        f"pests, and if this initiative is successful,\n"
        f"there is a realistic chance to replicate this project for all \n"
        f"other crops.\n\n"
        f" \n\n")

    st.warning(
        f"**Project Dataset**\n\n"
        f"The dataset has **4208** cherry leaf images provided by\n"
        f"Farmy & Foods.\n"
        f"The images show: \n\n"
        f"* **2104** healthy cherry leaves and \n\n"
        f"* **2104** cherry leaves that have powdery mildew, a fungal \n"
        f"disease that affects many plant species.\n\n"
    )

    st.success(
        f"This project has two business requirements given by the client:\n\n"
        f"* 1 - The client is interested in conducting a study to visually\n"
        f"differentiate a healthy leaf from one with powdery mildew.\n\n"
        f"* 2 - The client is interested in predicting if a cherry leaf \n"
        f"is healthy or contains powdery mildew.\n\n"
    )

    st.write(
        f"For additional information, please **read**\n "
        f"[this project's README.md file]"
        f"(https://github.com/Flora-King/Mildew-detection.git)."
    )
