import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    st.write("### Hypotesis 1 and validation")

    st.success(
        f"Infected leaves have clear marks differentiating them from the\n"
        f"healthy leaves."
    )
    st.info(
        f"We suspect cherry leaves affected by powdery mildew have clear marks"
        f"typically the first symptom is a light-green, circular lesion on\n"
        f"either leaf surface,"
        f"then a subtle white powdery growth develops in the infected area."
    )
    st.write("To visualize a thorough investigation of infected and healthy leaves visit the Leaves Visualiser tab.")

    st.warning(
        f"The model was able to detect such differences and learn how to\n"
        f"differentiate and generalize in order to make accurate predictions."
        f" A good model trains its ability to predict classes on a batch\n"
        f"of data without adhering too closely to that set of data.\n"
        f" In this way the model is able to generalize and predict \n"
        f"future observation reliably because it didn't 'memorize'\n"
        f"the relationships between features and labels as seen in\n"
        f"the training dataset but the general pattern from feature to labels."
    )

    st.write(
        f"For additional information, please visit **read** "
        f"[this project's README.md file]"
        f"(https://github.com/Flora-King/Mildew-detection.git)."
    )
