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

Where are carbon projects taking place? How are carbon credits generated? Who issues these credits?

# Data source
Pamela Quartson, Barbara K Haya, Tyler Bernard, Aline Abayo, Xinyun Rong, Ivy S So, Micah Elias. (2026). Voluntary Registry Offsets Database v2026-08, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from: [https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database](https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database).

The current scope of this analysis is projects that issued credits between Jan 2016 and Aug 2026, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR).

# Data cleaning and transformation
Data cleaning and transformation are conducted using Python. Scripts are stored in the folder "scripts". export_data.py is the main script that executes the cleaning and transformation process.

The input is an Excel file with 70+ columns, listing 11000+ projects.

The output is three csv files: one project table with 14 columns listing project details, and two tables with 4 columns each that list records of credit issuance, and credit retirement (usage) respectively.

Both input and output are stored in the folder "data"

# Data visualization
Data modeling and visualization are conducted using Power BI Desktop.

The latest draft is the file
[dashboard/carbon_market_dashboard_draft_1.pbix](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/PowerBI/dashboard/carbon_market_dashboard_draft_1.pbix)

# Dashboard screenshots
How are carbon credits generated - 2:

<img width="1228" height="687" alt="image" src="https://github.com/user-attachments/assets/05085765-7052-4587-bf4f-f2de283ff37d" />

Who issues carbon credits:

<img width="1226" height="685" alt="image" src="https://github.com/user-attachments/assets/42c26c11-4286-4acc-b4b7-de2a0ac199c0" />

# Key insights
1. Forestry projects in Latin America used to be popular. Since 2023, this is no longer the case.

2. Cookstove projects in Sub-Saharan Africa represent a promising area for future growth. Gold Standard has established an early lead over other standards in this market.

# Next steps
1. Combine data with my thesis findings to produce more insights
