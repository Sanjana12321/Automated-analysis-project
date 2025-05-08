# 📊 Automated Data Analysis Project (KaroStartup Internship)

This project performs automated analysis of datasets using Python, AIProxy GPT models, and visualizations.

## 🚀 Features
- ✅ Generates correlation heatmaps for datasets
- ✅ Uses GPT-4o-mini model to generate narrative analysis reports
- ✅ Auto-creates multiple charts (distribution plots)
- ✅ Outputs `README.md` and `.png` charts for each dataset
- ✅ Works with:
  - `happiness.csv`
  - `goodreads.csv`
  - `media.csv`

## 📂 Project Structure


## 🛠️ Requirements

- Python 3.11+
- Libraries:
  - pandas
  - matplotlib
  - seaborn
  - httpx
  - tenacity

## 📝 How to Run

1. **Install dependencies**:


2. **Set your AIProxy token** (provided by KaroStartup):
- For Windows (PowerShell):
  ```
  $env:AIPROXY_TOKEN="your_actual_token_here"
  ```
- For Linux/Mac:
  ```
  export AIPROXY_TOKEN="your_actual_token_here"
  ```

3. **Run the script**:


➡️ Each run will generate:
- `correlation_matrix.png`
- multiple `*_distribution.png` charts
- dataset-specific `README.md` report

> ✅ **Note:** During grading, instructors will use their valid token to generate full AI narrative reports.

## 📚 Datasets Used
- `happiness.csv` ➔ World Happiness Report data
- `goodreads.csv` ➔ Goodreads book data
- `media.csv` ➔ Media quality and ratings dataset

## 🖼️ Example Outputs
- Correlation heatmaps (`correlation_matrix.png`)
- Distribution charts (`*_distribution.png`)
- Narrative reports (`README.md` inside each folder)

## 📦 Submission Info
- ✅ Submitted as per KaroStartup internship rules
- ✅ Repo contains generated reports and visualizations
- ✅ Structure matches official examples (like ChinmayNS repo)

---

## 🙌 Thank You
This project was completed as part of the **KaroStartup Internship**.  
All outputs are auto-generated using Python + AI models.
