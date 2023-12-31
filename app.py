import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import project_summary
from app_pages.page_price_cor_study import page_sale_price_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis
from app_pages.page_sale_price_predictor import page_sale_price_predictor
from app_pages.page_ml_predict_price import page_ml_predict_price

"""
This python file is to add the pages on the dashboard
and also to run the app
"""

app = MultiPage(app_name="Housing Price Predictor")

app.add_page("Quick Project Summary", project_summary)
app.add_page("House Price Correlation Study", page_sale_price_study_body)
app.add_page("Project Hypothesis", page_project_hypothesis)
app.add_page("Sale Price Predictor", page_sale_price_predictor)
app.add_page("ML: House Price Prediction", page_ml_predict_price)

app.run()
