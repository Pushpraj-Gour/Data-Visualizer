import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


# Setting page configuration

st.set_page_config(page_title="Data Visualiser",
                   layout= "centered",
                   page_icon="📊")

# Title
st.title("📊 Data Visualiser - Web App")

#getting the working directory to file
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

#Listing the files present with us

files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#Drop down for all the files
selected_file = st.selectbox("Select a file",files_list,index=None)

st.write(selected_file)

if selected_file:

    # getting the absolute path of the selected file
    file_loc = os.path.join(folder_path,selected_file)

    #reading the file with the help of pandas

    df = pd.read_csv(file_loc)

    col1,col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        #User selection of columns

        x_axis = st.selectbox("Select the X-axis",options=columns + ["None"])
        y_axis = st.selectbox("Select the Y-axis",options=columns + ["None"])

        plot_list = ["Line Plot","Bar Chart","Count Plot","Scatter Plot","Distribution Plot"]

        selected_plot = st.selectbox("Select which plot you needed :",plot_list)


#Button to generate plots
if st.button("Generate Plot"):

    # fig,ax = plt.subplot(figsize=(6,4))
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    if selected_plot=="Line Plot":
        sns.lineplot(x=df[x_axis],y=df[y_axis],ax=ax)

    elif selected_plot=="Bar Chart":
        sns.barplot(x=df[x_axis],y=df[y_axis],ax=ax)

    elif selected_plot=="Scatter Plot":
        sns.scatterplot(x=df[x_axis],y=df[y_axis],ax=ax)

    elif selected_plot=="Distribution Plot":
        sns.histplot(df[x_axis],kde=True,ax=ax)

    elif selected_plot=="Count Plot":
        sns.countplot(x=df[x_axis],ax=ax)

    #adjust label size
    ax.tick_params(axis="x",labelsize=10)
    ax.tick_params(axis="y",labelsize=10)

    #title axes labels
    plt.title(f"{selected_plot} of {y_axis} vs {x_axis}",fontsize=12)
    plt.xlabel(x_axis,fontsize=10)
    plt.ylabel(y_axis,fontsize=10)

    st.pyplot(fig)