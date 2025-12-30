# Electric_Vehicle_US_Washington
EV Market Analysis (Python, Google Sheets) Analyzed 270k+  U.S EV records to identify manufacturer dominance, top model trends, and the shift toward fully electric using EDA and data visualization.

Project Overview
The adoption of electric vehicles (EVs) has grown rapidly in recent years due to advancements in technology and increased focus on sustainable transportation.  
This project analyzes large-scale U.S. electric vehicle registration data based only on the state of Washington (WA) to understand manufacturer dominance, model popularity, and market trends over time, with a specific focus on the shift toward fully electric vehicles.


Problem Statement

Electric Vehicle Market Analysis Based on Manufacturer and Model Trends in the State Of Washington
The objective of this project is to analyze electric vehicle registration data in order to:
- Identify leading EV manufacturers and popular models
- Study EV adoption trends over time
- Examine whether the market is shifting toward fully electric vehicles (BEVs)
- Observe improvements in EV technology using electric range data

Dataset
- Source: U.S. Open Data (Electric Vehicle Population Data)
- Size: ~270,000 vehicle records approx.
- Key Features Used:
  - Make
  - Model
  - Model Year
  - Electric Vehicle Type (BEV / PHEV) *Battery EV's or Plug-in Hybrid Ev's
  - Electric Range (km)
  - State

Each row in the dataset represents One registered electric vehicle.

---

Tools & Technologies
- Google Sheets
  - Initial data exploration
  - Pivot tables for manufacturer and EV type analysis
- Python
  - Data cleaning and preprocessing
  - Exploratory Data Analysis (EDA)
  - Trend analysis and visualization
- Libraries Used
  - pandas
  - matplotlib (was also gonna use seaborn but it felt un-wanted)
	
(SQL was intentionally not used in this project as spreadsheet analysis was sufficient for aggregation, and Python was better suited for time-series insights.)

---

Analysis & Visualizations
The following analyses were performed:

- EV Adoption Over Time
  - Year-wise growth of EV registrations

- Top EV Manufacturers
  - Market concentration and dominance

- Top EV Models
  - Most popular EV models based on registrations

- BEV vs PHEV Distribution
  - Comparison of fully electric and plug-in hybrid vehicles over time

All visualizations use color-blind friendly palettes and appropriate chart types (bar charts, stacked bars, line charts) to ensure clarity and accessibility.



Key Insights

- The EV market is highly concentrated, with a small number of manufacturers accounting for a large share of registrations.
- Electric vehicle adoption has increased significantly in recent years, indicating accelerated market growth.
- Battery Electric Vehicles (BEVs) show faster growth compared to Plug-in Hybrid Electric Vehicles (PHEVs), suggesting a clear shift toward fully electric mobility.
- Average electric range has improved over time, reflecting advancements in EV technology and battery efficiency.
- A limited number of EV models dominate registrations, highlighting strong consumer preference for established models.

---

Conclusion

This analysis demonstrates how large-scale vehicle registration data can be used to understand market behavior and technology trends in the electric vehicle industry.  
By combining spreadsheet-based exploration with Python-driven analysis and visualization, the project provides a clear view of EV adoption patterns and market evolution in the United States.

---

Project Structure

- XLSX_CSV Files – Contains the original electric vehicle dataset downloaded from data.gov (USA) and spreadsheet files used for initial exploration.
- Python_&Viz – Contains Python scripts or notebooks used for data cleaning, analysis, and visualization.
- README – Project documentation describing objectives, methodology, and key insights.

Dataset Access

- The dataset used in this project is large (62.1 MB) and therefore not included in this repository.
	-Source: https://catalog.data.gov/dataset/electric-vehicle-population-data

