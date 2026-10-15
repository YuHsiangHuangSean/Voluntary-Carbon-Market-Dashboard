# “Explain the Voluntary Carbon Market in 10 Minutes“ Dashboard

[Latest progress →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/PowerBI/dashboard/carbon_market_dashboard_draft_1.pbix)

Updated with newly released data through August 2026.

# Project overview
#Voluntary carbon market #Data cleaning #ETL #Data visualization #Python #Power BI

Purpose:

Explain the voluntary carbon market and identify future developments.

Method:

1. 21 expert interviews and policy research from [my thesis research](https://studenttheses.uu.nl/handle/20.500.12932/52522)

2. Cleaned, transformed, and analyzed data on 11,000 carbon projects to visualize market trends and insights using Python and Power BI

# Problem context
1. What is the voluntary carbon market?

There are many ways to reduce carbon emissions or remove carbon from the atmosphere. All of which, however, require funding. Voluntary carbon market directs funds from companies interested in mitigating climate change to projects that reduce/remove carbon.

2. How does the voluntary carbon market work?

Project developers reduce/remove carbon. Carbon standards issue and track carbon credits after they are verified. Buyers purchase carbon credits and fund project developers in doing so.

3. How is this project useful?

The voluntary carbon market has been debated for years, particularly over its role in climate change mitigation. Some see carbon credits as an essential tool for addressing hard-to-abate emissions, while others worry that they may distract from meaningful decarbonization efforts.

Yet during my thesis research, I found a more fundamental challenge: **Understanding the voluntary carbon market itself is surprisingly difficult.** The market is complex and fragmented, with multiple carbon standards, project types, certification schemes, and overlapping terminology.

By analyzing and visualizing publicly available data and combining them with my thesis findings, this project aims to make the voluntary carbon market more accessible and help users understand its current state and possible future development **in 10 minutes**:

- Where are carbon projects taking place?
- How are carbon credits generated?
- Who issues them?
- What are the key challenges facing the market?
- How has the market evolved over time?
- Which parts of the market are growing or declining?

# Data source
1. MSc thesis:

Huang, Y.H. (2026). Rebuilding legitimacy: Interaction dynamics of natural climate solution credits for European markets [Master's thesis, Utrecht University]. Utrecht University Student Theses Repository. [https://studenttheses.uu.nl/handle/20.500.12932/52522](https://studenttheses.uu.nl/handle/20.500.12932/52522)

2. Carbon project data:

Pamela Quartson, Barbara K Haya, Tyler Bernard, Aline Abayo, Xinyun Rong, Ivy S So, Micah Elias. (2026). Voluntary Registry Offsets Database v2026-08, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from: [https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database](https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database).

The current scope of this analysis is projects that issued or retired credits between Jan 2016 and Aug 2026, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR).

The current scope of this analysis is projects that issued or retired credits between Jan 2016 and Aug 2026, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR). There are other carbon standards, but these four already account for ~89% of the transaction volume in 2024. ([https://www.ecosystemmarketplace.com/publications/2025-state-of-the-voluntary-carbon-market-sovcm/](https://www.ecosystemmarketplace.com/publications/2025-state-of-the-voluntary-carbon-market-sovcm/))


# Data cleaning and transformation
Data cleaning and transformation are conducted using Python. Scripts are stored in the folder "scripts". export_data.py is the main script that executes the cleaning and transformation process.

The input is an Excel file with 70+ columns, listing 11000+ projects.

The output is two csv files: one project table with 14 columns listing project details, and one record table with 4 columns listing records of credit issuance and retirement (usage).

Both input and output are stored in the folder "data"

# Data visualization
Data modeling and visualization are conducted using Power BI Desktop.

The latest outcome is the file
[dashboard/carbon_market_dashboard_draft_1.pbix](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/PowerBI/dashboard/carbon_market_dashboard_draft_1.pbix)

# Dashboard screenshots
How are carbon credits generated - 2:

<img width="600" height="334" alt="image" src="https://github.com/user-attachments/assets/b59ac88d-5b06-47de-bf5d-d7430fd9b608" />

Who issues carbon credits:

<img width="600" height="337" alt="image" src="https://github.com/user-attachments/assets/51336aa2-6d83-4afb-bc8c-4abad25bc146" />

How stakeholders ensure credit quality:

<img width="600" height="336" alt="image" src="https://github.com/user-attachments/assets/4c65cace-ac23-4745-93f2-64aa43af1118" />

# Key insights
1. Forestry projects in Latin America used to be popular. Since 2023, this is no longer the case.

2. Cookstove projects in Sub-Saharan Africa represent a promising area for future growth. Gold Standard has established an early lead over other standards in this market.

3. The [growing media and academic scrutiny](https://www.theguardian.com/environment/2023/jan/18/revealed-forest-carbon-offsets-biggest-provider-worthless-verra-aoe) since the early 2020s has led to a shift in focus from credit quantity to quality, supported by the increasing usage of additional certification labels like ICVCM CCP, Article 6, and CORSIA.

# Next steps
1. Combine data with my thesis findings to produce more insights

2. Publish dashboards

3. Publish outcomes in a slide deck
