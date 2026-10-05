# AI & Data Science Job Market Dashboard

## 1. Project Overview
This project aims to build an interactive web dashboard to analyze and compare the supply of university graduates and the demands of the job market in the fields of AI, Data Science, and Statistics. It visualizes the global job market, educational pipeline, and skill mismatch.

## 2. Target Audience
* Policymakers
* University Administrators
* HR Professionals
* Students

## 3. Data Sources & Schema
The dashboard utilizes mock data modeled after the following open data sources:
* **Graduates Data:** NCES IPEDS Data Center
* **Employment, Salary, & Demographics:** Kaggle Machine Learning & Data Science Survey
* **Job Volume & Projections:** U.S. Bureau of Labor Statistics (BLS)
* **Hiring Companies:** Data Scientist Job Postings Dataset
* **Required Skills:** O*NET OnLine Database
* **Experience Levels:** Data Science Job Salaries (ai-jobs.net)

Data segments include:
* Entry-Level (0-2 years)
* Mid-Level (3-5 years)
* Expert-Level (Senior/Director, 5+ years)

## 4. Dashboard Structure

The dashboard is divided into three distinct tabs with cross-filtering capabilities:

### Tab 1: Supply Side - Graduates and Learned Skills
* Graduates Trend (Bar/Line Chart)
* Core Curriculum (Table/Tag Cloud)
* Employment Tracking (Stacked Bar/Line Chart)
* Tuition Fees (Bar Chart)

### Tab 2: Demand Side - Job Market and Required Skills
* Open Positions (KPI/Time Series)
* Required Skills (Horizontal Bar/Treemap)
* Top Hiring Companies (Data Table)
* Salary by Experience Level (Box Plot/Bar Chart)

### Tab 3: Gap Analysis - Skill Mismatch
* Skill Mismatch Analysis (Radar Chart or Diverging Bar Chart)

## 5. Technical Stack & Architecture
* **Backend:** Python
* **Frontend/Visualization:** Dash by Plotly
* **Architecture:** Single-file application structure using Python and Dash.
* **Interactivity:** Dynamic filtering and cross-filtering across all charts within tabs.
