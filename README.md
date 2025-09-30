# CORD-19 Data Analysis and Streamlit Application

This project is an assignment to perform a basic analysis of the CORD-19 research dataset. The process involves cleaning and exploring the data in a Jupyter Notebook (`explore.ipynb`) and presenting the key findings in an interactive web application built with Streamlit (`app.py`).

---

## 📋 Core Features

* **Interactive Filtering:** Filters the dataset to a specific range of publication years using a slider.
* **Publication Trends:** Displays a bar chart showing the number of research papers published over time.
* **Top Journals:** Creates a visualization of the top 10 journals with the most publications.
* **Keyword Analysis:** Generates a word cloud to identify the most frequent terms in paper titles.

---

## 💾 Dataset Setup

**Important:** Due to its large size, the dataset (`metadata.csv`) is **not** included in this repository. To run this application, you must download it first.

1.  **Download the Data:** Go to the [Kaggle CORD-19 Research Challenge page](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).
2.  **Locate and Place the File:** Download the `metadata.csv` file and place it inside the `data` folder in this project's directory.

The final folder structure should be:
```

Frameworks\_Assignment/
|-- data/
|   |-- metadata.csv   \<-- Your downloaded file goes here
|-- app.py
|-- explore.ipynb
|-- requirements.txt

````

---

## ⚙️ How to Run the Application

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nwokike/COVID-19-Streamlit-Dashboard/
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd COVID-19-Streamlit-Dashboard
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
The application will open in your default web browser.
````
