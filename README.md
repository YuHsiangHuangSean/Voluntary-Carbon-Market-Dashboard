# “Explain Voluntary Carbon Market in 5 Minutes“ Dashboard - work in progress

[Latest progress →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/PowerBI/dashboard/carbon_market_dashboard_draft_1.pbix)

Updated with newly released data through August 2026.

# Project overview
#Data cleaning #ETL #Data visualization #Python #Power BI

Cleaned, transformed, and analyzed complex carbon project data to visualize market trends and insights using Python and Power BI

# Problem context
1. What is voluntary carbon market?

There are many ways to reduce carbon emissions or remove carbon from the atmosphere. All of which, however, require funding. Voluntary carbon market directs funds from companies interested in solving climate change to projects that reduce/remove carbon.

2. How does voluntary carbon market work?

Project developers reduce/remove carbon. Carbon standards verify projects and issue carbon credits. Buyers purchase carbon credits and fund project developers in doing so.

3. How is this project useful?

During my thesis research, I found that everyone has an opinion about it ("It's a critical solution to climate change!", "It's a scam!"), but there is limted information that explains what voluntary carbon market is and what its current state is. By analyzing and visualizing publicly available data, this project aims to provide an overview of voluntary carbon market and answer questions like:

Where are carbon projects taking place? How are carbon credits generated? Who issues these credits? How do stakeholders ensure credit quality?

# Data source
Pamela Quartson, Barbara K Haya, Tyler Bernard, Aline Abayo, Xinyun Rong, Ivy S So, Micah Elias. (2026). Voluntary Registry Offsets Database v2026-08, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from: [https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database](https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database).

The current scope of this analysis is projects that issued credits between Jan 2016 and Aug 2026, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR).

# Data cleaning and transformation
Data cleaning and transformation are conducted using Python. Scripts are stored in the folder "scripts". export_data.py is the main script that executes the cleaning and transformation process.

The input is an Excel file with 70+ columns, listing 11000+ projects.

The output is two csv files: one project table with 14 columns listing project details, and one record table with 4 columns listing records of credit issuance and retirement (usage).

Both input and output are stored in the folder "data"

# Data visualization
Data modeling and visualization are conducted using Power BI Desktop.

The latest draft is the file
[dashboard/carbon_market_dashboard_draft_1.pbix](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/PowerBI/dashboard/carbon_market_dashboard_draft_1.pbix)

# Dashboard screenshots
HHow are carbon credits generated - 2:

<img width="600" height="334" alt="image" src="https://github.com/user-attachments/assets/b59ac88d-5b06-47de-bf5d-d7430fd9b608" />

Who issues carbon credits:

<img width="600" height="337" alt="image" src="https://github.com/user-attachments/assets/51336aa2-6d83-4afb-bc8c-4abad25bc146" />

How stakeholders ensure credit quality:

<img width="600" height="336" alt="image" src="https://github.com/user-attachments/assets/4c65cace-ac23-4745-93f2-64aa43af1118" />

# Key insights
1. Forestry projects in Latin America used to be popular. Since 2023, this is no longer the case.

2. Cookstove projects in Sub-Saharan Africa represent a promising area for future growth. Gold Standard has established an early lead over other standards in this market.

# Next steps
1. Include remaining credits (issued but not used) to provide insights on supply-demand dynamics

2. Combine data with my thesis findings to produce more insights
