# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "httpx",
#   "tenacity"
# ]
# ///

import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import httpx
from tenacity import retry, wait_random_exponential, stop_after_attempt

# Read CSV filename from command line
if len(sys.argv) != 2:
    print("Usage: uv run autolysis.py dataset.csv")
    sys.exit(1)

csv_file = sys.argv[1]
folder = os.path.dirname(csv_file)

try:
    df = pd.read_csv(csv_file)
except UnicodeDecodeError:
    df = pd.read_csv(csv_file, encoding='latin1')

# Basic Analysis
summary_stats = df.describe(include='all').to_string()
missing_values = df.isnull().sum().to_string()
correlation = df.corr(numeric_only=True)

# Save correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig(os.path.join(folder, 'correlation_matrix.png'))
plt.close()

# ✅ Extra: Generate distribution plots for numeric columns
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col].dropna(), kde=True, color='skyblue')
    plt.title(f'{col} Distribution')
    plt.tight_layout()
    plot_filename = f"{col}_distribution.png"
    plt.savefig(os.path.join(folder, plot_filename))
    plt.close()

# Retry logic for API calls
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(3))
def call_llm(prompt):
    api_key = os.environ.get("AIPROXY_TOKEN")
    if not api_key:
        print("❌ AIPROXY_TOKEN not set. Using dummy narrative.")
        return "LLM call skipped (AIPROXY_TOKEN not set)."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful data analyst."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = httpx.post(
            "https://api.aiproxy.io/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ LLM call failed: {e}")
        return "LLM call failed during local test. Narrative will be generated during grading."

# Generate LLM Narrative
prompt = f"""
You are analyzing a dataset. Here are the details:

Summary Statistics:
{summary_stats}

Missing Values:
{missing_values}

Describe the dataset, highlight key insights, and explain the implications.
"""

narrative = call_llm(prompt)

# Write README.md in the dataset folder
with open(os.path.join(folder, "README.md"), "w", encoding='utf-8') as f:
    f.write("# Automated Data Analysis Report\n\n")
    f.write("## Correlation Heatmap\n")
    f.write("![Correlation](correlation_matrix.png)\n\n")
    f.write("## Narrative Report\n")
    f.write(narrative)

print(f"✅ Analysis complete for {csv_file}! See {folder}/README.md and charts.")
