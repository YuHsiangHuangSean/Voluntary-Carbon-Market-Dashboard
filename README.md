# Voluntary-Carbon-Market-Dashboard - working progress

# Project overview
Explaining voluntary carbon market in 5 Minutes

# Problem context
What is voluntary carbon market?

There are many ways to reduce carbon emissions or remove carbon from the atmosphere. All of which, however, require funding. Voluntary carbon market directs funds from companies interested in solving climate change to projects that reduce/remove carbon.

How does voluntary carbon market work?

Project developers reduce/remove carbon. Carbon standards verify projects and issue carbon credits. Buyers purchase carbon credits and fund project developers in doing so.

# Data source
Voluntary Registry Offsets Database by UC Berkeley (https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database).

The current scope of this analysis is projects that issued credits between 2016 and 2025, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR).

# Data cleaning and transformation
Data cleaning and transformation are conducted using Python.

The input is an Excel file listing 11000+ projects with 70+ columns.

The output is a project table as a csv file with 14 columns, and a credit issuance record table with 4 columns.

# Data visualization
Data visualization is conducted using Power BI Desktop.

The latest draft is the file dashboard/carbon_market_dashboard_draft_1.pbix

# Dashboard screenshots
<img width="673" height="377" alt="image" src="https://github.com/user-attachments/assets/f932686b-8044-44ab-92b9-65818ec24f6c" />
<img width="671" height="377" alt="image" src="https://github.com/user-attachments/assets/0d929762-86f7-4e2c-a501-f1886a874193" />

# Key insights
1. Forestry projects in Latin America used to be popular. Since 2023, this is no longer the case.

2. Cookstove projects in Sub-Saharan Africa represent a promising area for future growth, based on the volume of issued credits in recent years.

# Next steps
1. Include the entire life cycle of carbon credits, from reducing/removing carbon, issuing credits, to retiring(using) credits.

2. Include recent regulatory trends like the usage of additional certification labels
