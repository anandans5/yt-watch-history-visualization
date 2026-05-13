# YouTube Watch Habits: Behavioral Analysis Data Engineering

##  Project Overview
This project serves as an exploratory data analysis (EDA) of personal digital footprints using YouTube Watch History. As a student specializing in **Data Science and Cybersecurity**, I developed this tool to transform raw, semi-structured JSON exports from Google Takeout into actionable behavioral insights.

The core objective is to identify consumption patterns while maintaining a high standard of data privacy and security.

##  Technical Stack
*   **Language:** Python 3.12+
*   **Data Processing:** `pandas` (for efficient handling of JSON nested structures)
*   **Visualization:** `matplotlib` (for temporal distribution analysis)
*   **System Integration:** `json`, `datetime`


## Getting Started

### 1. Data Acquisition
1.  Visit [Google Takeout](https://takeout.google.com/).
2.  Select **YouTube and YouTube Music** only.
3.  Ensure the format is set to **JSON**.
4.  Once downloaded, extract and place `watch-history.json` in the project root.

### 2. Installation
```bash
pip install pandas matplotlib
