import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics():
    version = 'v1'
    st.info(
        f"This page details how the dataset was divided, how the model performed on that data."
    )
    st.write("### Images distribution per data set and label ")

    labels_distribution = plt.imread(
        f"assets/streamlit_app_images/Labels_frequencies.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("---")

    st.write("### Model Performance History")

    st.warning(
        f"**Model Performance**\n\n"
        f"The Loss is the sum of errors made for each example in training\n"
        f"(loss) or validation (val_loss) sets.\n\n"
        f"Loss value implies how poorly or well a model behaves after each\n"
        f"iteration of optimization.\n\n"
        f"The accuracy is the measure of how accurate the model's prediction\n"
        f"(accuracy) is compared to the true data (val_acc).\n\n"
        f"When good model performs well on unseen data it means that it's\n"
        f"able to generalize and didn't fit too closely to training dataset.")

    st.write("Model Training Accuracy")
    model_clf = plt.imread(
        f"/workspaces/Mildew_Detection_pjkt/outputs/v1/model_training_acc.png")
    st.image(model_clf, caption='Model Accuracy')

    st.write("Model Training Loss")
    model_clf = plt.imread(
        f"/workspaces/Mildew_Detection_pjkt/outputs/v1/model_training_losses.png")
    st.image(model_clf, caption='Model Loss')

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))

    st.write(
        f"For additional information, please visit **read** "
        f"[this project's README.md file]\n"
        f"(https://github.com/Flora-King/Mildew-detection.git)."
    )
