import plotly.express as px
import streamlit as st

def plot_score_history(df):
    if df.empty:
        st.info("No submissions yet.")
        return

    st.markdown("### Score Over Time")
    fig_score = px.line(df, y='Score', title="Score History", markers=True)
    st.plotly_chart(fig_score, use_container_width=True)

    st.markdown("### Functions, Classes, Loops, Conditionals")
    fig_patterns = px.bar(df[['Functions','Classes','Loops','Conditionals']].reset_index(),
                          x='index', y=['Functions','Classes','Loops','Conditionals'],
                          title="Patterns Detected per Submission")
    st.plotly_chart(fig_patterns, use_container_width=True)

    st.markdown("### Complexity Over Time")
    fig_complexity = px.line(df, y='Complexity', title="Complexity Score", markers=True)
    st.plotly_chart(fig_complexity, use_container_width=True)