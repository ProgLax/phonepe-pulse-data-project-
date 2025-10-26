
# PhonePe Pulse India Dashboard with Gemini AI

## Project Overview

This project creates an interactive dashboard using Streamlit to visualize and analyze digital payment trends in India based on the PhonePe Pulse dataset. The dashboard provides insights into transaction patterns, user growth, and geographical distribution of digital payments. Additionally, it integrates with Google Gemini AI to provide a conversational interface for querying the data and trends.

## Data Source

The data used in this project is sourced from the PhonePe Pulse GitHub repository, which contains aggregated data on transactions and users across various states, districts, and pincodes in India.

## Steps Performed

Here is a detailed breakdown of the steps executed in this notebook:

1.  **Cloning the PhonePe Pulse Data Repository**:
    - The official PhonePe Pulse data repository was cloned from GitHub to access the raw JSON data files.

2.  **Extracting File Paths**:
    - A helper function `extract_paths` was used to locate the specific directories containing aggregated and top transaction and user data within the cloned repository.

3.  **Loading and Processing Data**:
    - JSON data files for aggregated transactions, aggregated users, map transactions, map users, top transaction districts, top transaction pincodes, top user districts, and top user pincodes were read.
    - The JSON data, which is often nested, was loaded directly as dictionaries using `json.load` and then processed to extract relevant information.
    - Data was appended to respective dictionaries for each category (transactions by type, users by brand, transactions by district/pincode, users by district/pincode).
    - Robust checks were added to ensure the expected keys ('data', 'districts', 'pincodes', 'transactionData', 'usersByDevice', 'metric', etc.) were present before accessing the data, handling cases where data might be missing or have an unexpected structure.
    - The extracted data was then converted into pandas DataFrames (`agg_trans_df`, `agg_user_df`, `map_trans_df`, `map_user_df`, `top_trans_dist_df`, `top_trans_pin_df`, `top_user_dist_df`, `top_user_pin_df`).

4.  **Data Cleaning and Transformation**:
    - Data cleaning and transformation steps were applied to the loaded DataFrames. This included:
        - Merging geographical data (latitude and longitude) from `dist_lat_long.csv` with the relevant dataframes to enable map visualizations.
        - Converting data types where necessary (e.g., Year to string for categorical plotting).
        - Handling potential inconsistencies in state or district names.

5.  **Data Analysis and Aggregation**:
    - Data was aggregated and analyzed to derive key metrics and insights for the dashboard. This involved:
        - Grouping data by state, year, quarter, transaction type, brand, district, and pincode.
        - Calculating sums of transaction counts and amounts, and aggregating registered users and app opens.
        - Identifying top performing states, districts, and pincodes.

6.  **Saving Processed Data**:
    - The processed and cleaned dataframes were saved as CSV files in a 'Miscellaneous' directory (`agg_trans.csv`, `agg_user.csv`, etc.) for easy access by the Streamlit application.

7.  **Database Integration (SQLite)**:
    - The processed dataframes were pushed into a SQLite database (`phonepe_pulse.db`) for persistent storage and potential alternative data access methods.

8.  **Streamlit Application Development**:
    - The core Streamlit application file (`app.py`) was created/updated with the main layout, styling (including glassmorphism and animated gradient), and key metrics display.
    - Integration with Google Gemini AI was set up in `app.py`, loading the API key securely from Colab secrets and using the `gemini-pro-latest` model to power an interactive chatbot for data queries.
    - Individual Streamlit pages (`pages/1_📊_Overview.py`, `pages/2_💳_Transaction.py`, `pages/3_👥_Users.py`, `pages/4_📈_Trend_Analysis.py`, `pages/5_⚖️_Comparative_Analysis.py`, `pages/6_👤_About_Me.py`, `pages/7_👤_About.py`) were created/updated. These pages contain specific visualizations and analysis related to different aspects of the PhonePe Pulse data (Overview, Transactions, Users, Trend Analysis, Comparative Analysis, About Me, and About).
    - The "About Me" and "About" pages were customized to include profile information, links, and image placeholders with a layout resembling a LinkedIn profile.

9.  **Deployment with ngrok**:
    - The Streamlit application was launched using the `streamlit run` command.
    - `pyngrok` was used to create a public URL, making the local Streamlit server accessible over the internet. This allows the dashboard to be viewed and interacted with in a web browser.

## How to Run the Project

1.  **Clone the Repository**: Ensure the PhonePe Pulse data repository is cloned as described in Step 1.
2.  **Install Dependencies**: Install the necessary Python libraries (`streamlit`, `pyngrok`, `streamlit-player`, `streamlit-extras`, `xlsxwriter`, `openpyxl`, `plotly`, `seaborn`, `altair`, `google-generativeai`) using pip.
3.  **Set up Gemini API Key**: Add your Google Gemini API key to Colab secrets with the name `GOOGLE_API_KEY`.
4.  **Run the Notebook Cells**: Execute the notebook cells sequentially to load and process the data, create the Streamlit app files, and start the Streamlit server with ngrok.
5.  **Access the Dashboard**: Use the public URL provided in the output of the Streamlit cell to access the interactive dashboard in your web browser.

## Author

Laxman Rathod

---

*This README was generated based on the steps performed in the Colab notebook.*
