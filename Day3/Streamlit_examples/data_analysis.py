import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Streamlit Data Analysis App")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        # Display raw data
        st.subheader("Raw Data")
        st.write(df)

        # Display summary statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())

        # Visualize data
        st.subheader("Data Visualization")

        # Select columns for visualization
        selected_columns = st.multiselect("Select columns for visualization", df.columns)

        if selected_columns:
            # Create pairplot
            pairplot = sns.pairplot(df[selected_columns])
            st.pyplot(pairplot)

            # Create histogram
            for column in selected_columns:
                plt.figure()
                plt.hist(df[column])
                plt.title(f"Histogram of {column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                st.pyplot(plt)

if __name__ == "__main__":
    main()