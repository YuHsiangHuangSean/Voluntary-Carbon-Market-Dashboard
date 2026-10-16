# “Explain the Voluntary Carbon Market in 10 Minutes“ Dashboard

[Key insights →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/tree/main#key-insights)

[Interactive dashboard (pbix, Power BI Desktop/Service needed) →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/main/dashboard/voluntary_carbon_market_dashboard.pbix)

[Static dashboard (PDF) →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/main/dashboard/voluntary_carbon_market_dashboard.pdf)

[Concise version (Stay tuned!)]

Updated with newly released data through August 2026.

# Project overview
#Voluntary carbon market #Data cleaning #ETL #Data visualization #Python #Power BI

Purpose:

Explain the voluntary carbon market and identify its challenge, trend, and future developments.

Method:

1. 21 expert interviews and policy research from [my thesis research](https://studenttheses.uu.nl/handle/20.500.12932/52522)

2. Cleaned, transformed, and analyzed data on 11,000 carbon projects to visualize market trends and insights using Python and Power BI

# Problem context
1. What is the voluntary carbon market?

There are many ways to reduce carbon emissions or remove carbon from the atmosphere. All of which, however, require funding. The voluntary carbon market directs funds from companies interested in mitigating climate change to projects that reduce/remove carbon.

2. How does the voluntary carbon market work?

**Project developers** reduce/remove carbon. **Carbon standards** issue and track carbon credits after they are verified. **Buyers** purchase carbon credits and fund project developers in doing so.

3. How is this project useful?

The voluntary carbon market has been debated for years, particularly over its role in climate change mitigation. Some see carbon credits as an essential tool for addressing hard-to-abate emissions, while others worry that they may distract from meaningful decarbonization efforts.

Yet during my thesis research, I found a more fundamental challenge: **Understanding the voluntary carbon market itself is surprisingly difficult.** The market is complex and fragmented, with multiple carbon standards, project types, certification schemes, and overlapping terminology.

By analyzing and visualizing publicly available data and combining them with my thesis findings, this project aims to make the voluntary carbon market more accessible and help users understand its current state and possible future development **in 10 minutes**:

- Where are carbon projects taking place?
- How are carbon credits generated?
- Who issues them?
- What is the key challenge facing the market?
- What is the overall trend over the years?
- Which parts of the market are growing?
- What are the future developments?

# Data source
1. MSc thesis:

Huang, Y.H. (2026). Rebuilding legitimacy: Interaction dynamics of natural climate solution credits for European markets [Master's thesis, Utrecht University]. Utrecht University Student Theses Repository. [https://studenttheses.uu.nl/handle/20.500.12932/52522](https://studenttheses.uu.nl/handle/20.500.12932/52522)

2. Carbon project data:

Pamela Quartson, Barbara K Haya, Tyler Bernard, Aline Abayo, Xinyun Rong, Ivy S So, Micah Elias. (2026). Voluntary Registry Offsets Database v2026-08, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from: [https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database](https://gspp.berkeley.edu/berkeley-carbon-trading-project/offsets-database).

The current scope of this analysis is projects that issued or retired credits between Jan 2016 and Aug 2026, verified by one of the four major carbon standards (Verra, Gold Standard, ACR, CAR). There are other carbon standards, but these four already account for ~89% of the transaction volume in 2024. ([https://www.ecosystemmarketplace.com/publications/2025-state-of-the-voluntary-carbon-market-sovcm/](https://www.ecosystemmarketplace.com/publications/2025-state-of-the-voluntary-carbon-market-sovcm/))


# Data cleaning and transformation
Data cleaning and transformation are conducted using Python. Scripts are stored in the folder "scripts". export_data.py is the main script that executes the cleaning and transformation process.

The input is an Excel file with 70+ columns, listing 11000+ projects.

The output is two csv files: one project table with 14 columns listing project details, and one record table with 4 columns listing records of credit issuance and retirement (usage).

Both input and output are stored in the folder "data"

# Data visualization
Data modeling and visualization are conducted using Power BI Desktop.

The outcome is the following files in "dashboard":

[Interactive dashboard (pbix, Power BI Desktop/Service needed) →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/main/dashboard/voluntary_carbon_market_dashboard.pbix)

[Static dashboard (PDF) →](https://github.com/YuHsiangHuangSean/Voluntary-Carbon-Market-Dashboard/blob/main/dashboard/voluntary_carbon_market_dashboard.pdf)

# Dashboard screenshots
How are carbon credits generated:

<img width="600" height="338" alt="image" src="https://github.com/user-attachments/assets/113dd452-57f8-4e9e-9217-96582fe684e3" />


Who issues carbon credits:

<img width="600" height="338" alt="image" src="https://github.com/user-attachments/assets/b73e333f-b56d-4332-9a1d-bed5966962db" />

What are the future developments:

<img width="600" height="339" alt="image" src="https://github.com/user-attachments/assets/7e89a88a-e1ab-4b15-bf73-de5a95b6df75" />

# Key insights
1. Forestry projects, including REDD+, in Latin America have lost momentum. Once a major source of credits, the segment has declined noticeably since 2023.

2. Cookstove projects in Sub-Saharan Africa stand out as a potential growth segment. Gold Standard has established an early lead over other major standards in this area

3. The project quality controversies have driven a transition from quantity to quality. 

4. Additional certification labels are supporting this transition. ICVCM-CCP-approved, Article-6-authorized, and CORSIA-eligible labels still represent a relatively small share of the market (particularly Article 6), but their presence is steadily growing.

5. The transition from quantity to quality also coincides with a shift from voluntary to compliance-driven demand. While some major voluntary buyers are slowing their purchases, CORSIA is expected to bring more international airlines into the market as its coverage expands.

# Next steps

1. Interviewee validation and feedback collection

2. Publish dashboards
