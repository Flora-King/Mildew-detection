import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.leaves_visualizer import leaves_visualizer_body
from app_pages.mildew_detector import mildew_detector_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.ml_performance_metrics import ml_performance_metrics

# Create an instance of the app
app = MultiPage(app_name="Cherry Powdery Mildew detector")

# Add app pages
app.add_page("Quick Project Summary", project_summary_body)
app.add_page("Leaves Visualiser", leaves_visualizer_body)
app.add_page("Mildew Detector", mildew_detector_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("ML Performance Metrics", ml_performance_metrics)

# Run the app
app.run()
