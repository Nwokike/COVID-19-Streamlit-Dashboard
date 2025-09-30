# CORD-19 Research Dashboard 🔬

An interactive dashboard built with Streamlit to analyze and explore the CORD-19 research dataset, which contains over a million scholarly articles about COVID-19 and related coronaviruses.

---

## ✨ Key Features

* **📈 Interactive Filtering:** Dynamically filter the entire dataset by a range of publication years.
* **📊 Data-Driven Metrics:** View key statistics like total publications and unique journals for the selected period.
* **📉 Publication Trends:** Visualize the growth of research publications over time with a clean line chart.
* **📝 Content Analysis:** Analyze the distribution of abstract lengths and discover key topics in paper titles through an insightful word cloud.
* **🖥️ Responsive UI:** A clean and modern user interface that works on any device.

---

## 📸 Application Preview

![Application Screenshot](<URL_to_your_screenshot.png>)

**Note:** To add your own screenshot, take a picture of your running app, add it to your GitHub repository, and replace the URL above.

---

## 🛠️ Tech Stack

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **Pandas:** For efficient data manipulation and analysis.
* **Matplotlib & Seaborn:** For creating static charts and plots.
* **WordCloud:** For generating the topic visualization.

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/COVID-19-Streamlit-Dashboard.git](https://github.com/YOUR_USERNAME/COVID-19-Streamlit-Dashboard.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd COVID-19-Streamlit-Dashboard
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run

Once the setup is complete, you can launch the application with the following command:

```bash
streamlit run app.py
