# Business Requirements Document (BRD)
## Project: AI, Data Science, and Statistics - Workforce vs Job Market Dashboard

### 1. Project Overview
**Objective:** Develop an interactive web dashboard to analyze and compare the supply of university graduates (Supply) and the demands of the job market (Demand) in the fields of AI, Data Science, and Statistics. 
**Target Audience:** Policymakers, University Administrators, HR Professionals, and Students.

### 2. Technical Stack & Architecture
*   **Backend:** Python
*   **Frontend/Visualization:** Plotly (specifically Dash by Plotly to support Python backend in a single-file application structure).
*   **Interactivity requirement:** **Cross-filtering is mandatory.** All charts within the same tab must be linked. Clicking or selecting a data point in one chart (e.g., selecting a specific university program) must automatically filter and update all other charts in that same tab.

### 3. Dashboard Structure & Functional Requirements

The dashboard must be divided into three distinct Tabs:

#### Tab 1: Supply Side - Graduates and Learned Skills (ปริมาณคนที่จบ และ skills ที่เรียนมา)
**Objective:** Visualize the educational pipeline and output.
*   **Component 1.1 - Graduates Trend (Bar/Line Chart):** Show the names of degree programs (e.g., B.S. Data Science, M.S. AI) and the number of graduates produced each year.
*   **Component 1.2 - Core Curriculum (Table/Tag Cloud):** Display mandatory courses/skills taught in each specific program relevant to the field.
*   **Component 1.3 - Employment Tracking (Stacked Bar/Line Chart):** Show the number/percentage of graduates employed in Year 1, Year 2, and Year 3 post-graduation.
*   **Component 1.4 - Tuition Fees (Bar Chart):** Compare the tuition fees across different programs.

#### Tab 2: Demand Side - Job Market and Required Skills (ปริมาณงานที่จ้าง และ skills ที่ต้องการ)
**Objective:** Visualize current industry demands and compensation.
*   **Component 2.1 - Open Positions (KPI/Time Series):** Display the total volume of open job positions over time or by sub-field.
*   **Component 2.2 - Required Skills (Horizontal Bar/Treemap):** Rank the most demanded technical and soft skills extracted from job postings.
*   **Component 2.3 - Top Hiring Companies (Data Table):** List companies actively hiring, including industry and number of open roles.
*   **Component 2.4 - Salary by Experience Level (Box Plot/Bar Chart):** Show starting salaries and average salaries categorized by experience levels (Entry, Mid-level, Senior/Expert).

#### Tab 3: Gap Analysis - Skill Mismatch (วิเคราะห์ Skill Mismatch)
**Objective:** Directly compare Tab 1 and Tab 2 to identify gaps in the market.
*   **Component 3.1 - Skill Mismatch Analysis (Radar Chart or Diverging Bar Chart):** Overlay the "Skills Taught" (from Tab 1) against the "Skills Demanded" (from Tab 2). Highlight areas where there is an oversupply of a skill or a critical shortage (e.g., Universities teach R heavily, but jobs demand Python).

---

### 4. Directives for AI Agent (Antigravity Handoff Prompt)

**Role:** You are an expert Python Developer and Data Visualizer.
**Task:** Generate a complete, runnable Dash application (Python) using `dash`, `dash-bootstrap-components` (for layout), and `plotly` in a **SINGLE `.py` file**.

**Instructions:**
1.  **Mock Data:** Generate comprehensive `pandas` DataFrames at the top of the file to simulate the data required for all three tabs. Ensure the data keys match so cross-filtering and the Tab 3 Mismatch analysis can function properly.
2.  **Layout:** Use `dcc.Tabs` to separate the 3 views. Use a clean grid layout for the charts within each tab.
3.  **Callbacks (Crucial):** Write Dash `@app.callback` functions to ensure **Cross-Filtering**. For example, if a user clicks on a specific degree program in Tab 1's bar chart, the tuition, employment, and curriculum components in Tab 1 must update to reflect *only* that program.
4.  **Tab 3 Logic:** In the callback for Tab 3, dynamically calculate the difference between the mock demand skills and supply skills to render the Skill Mismatch chart.
5.  **Output:** Provide ONLY the raw Python code required to run the Dash app.