#scraper for SARS_CoV_2 Articles

import pandas as pd
import re
import datetime


# List of high impact journals
high_impact = ['nature.com', 'sagepub.com', 'mdpi.com', 'springer.com', 'oup.com', 'jamanetwork.com', 'sciencedirect.com',
               'lancet.com', 'plos.org', 'cell.com', 'wiley.com', 'acs.org', 'jmir.org', 'biomedcentral.com']
# Add more journals as needed

# List of keywords to search for in the 'Title1' column
keywords = [
    ["Variants", ["variant", "alpha", "delta", "omicron"]],
    ['genes_genomic_regions',['ACE2','ORF9b']],
    ["Lung_Cardio",['Cardiovascular','brugada','stemi', 'chest','Respiratory','Ventilatory','Intubation', 'Ventilatory','Cardiovascular injuries','heart']],
    ["long_covid",['Long Covid', 'long','post','post-covid','Post-Acute Sequela','neurological outcome','complications','complication']],
    ["molecules",['inhibitor', 'spike', 'nuclear','protease','reductase','esterase','antibodies','effector','fc-effector','heme','Nucleic','cellular','cell','Furin','RNA','peptides','proteins','protein','Aldose','T cells','B cells','Oxidative Stress','aptamer','binding','Compound','renin','angiotensin','Renin-Angiotensin','antioxidant','molecular','Reyanning']],
    ['non_human', ['Rhesus Macaques', 'zoonotic', 'zoonosis','lion','gorrilla']],
    ['pediatric',['peds','pediatric','neonatal','children','Infants','school','pediatrics']],
    ["Vaccine",['vaccine', 'vaccination','prior', 'mRNA vaccine', 'booster']],
    ['medication_treatment',['Nirmatrelvir','adjuvants','adjuvant', 'Cepharanthine', 'pharmacokinetics','medications','Fluvoxamine','Ozone','therapy','Interferon-beta Injections','Interferon','Traditional Plant Therapy','drug','Camostat','inactivation']],
    ['testing',['nasal swabs','rapid','antigen','testing']],
    ['immune',['immune response','immune']],
    ['clinical_trial',['clinical trial', 'phase 1', 'phase 2', 'phase 3','manufacturing','cohort','In silico screening','In silico']],
    ['inflammation',['MIS-C','Anti-Inflammatory','inflammatory']],
    ['breakthrough',['breakthrough']],
    ['anti',['antiviral','antimicrobrial','antibacterial','Antimicrobial','antibiotic','antiviral']],
    ['genetic_tools',['siRNAs','Metatranscriptome','transcriptomics','metabolomic','proteome','sequencing','NGS','next-generation','Epigenetic','genomic','Sequencing','Transcriptomic']],
    ['detection',['Aerosol','detection','Wastewater Surveillance','diagnostic','assay','exposure']],
    ['public_health',['seroprevalence','public health','environment','community','hesitancy','telehealth','transmission','epidemic','endemicity','Outbreak','Containment','Transmission','contact tracing','Epidemiology','Epidemiological','Sanitization','risk','surveillance','Post-Infection Mortality','mortality']],
    ['social',['mental health','mental',"isolation",'disability']],
    ['biomarkers',['Biomarkers','changes']],
    ['wellbeing',['healing','Sexual Activity','acceptance','mental health','Communication']],
    ['other_conditions',['herpes','herpesvirus','Epilepsy','diabetes','Ocular Neurogenic Palsy',"MIS-C",'bacterial','cancer','leukemia','Mucormycosis','Osteochondral','Hematological Malignancies','influenza','liver','Abducens palsy','palsy','Psychosis','Hippocampal Subfield Abnormalities','Laríngeas','clinical']],
    ['tech',['sensors','AI','machine learning','Machine Learning','Biosensing','biosensors','modeling','model','models','network','analysis']],
    ['symptoms',['symptoms','cough']],
    ['misc',['Phytoconstituents','Coronaviruses','Restriction Factors', 'Lipid Composition', 'Composition', 'Immune Ageing','Dynamic Disease Manifestations','Nanobody repertoire','Differential laboratory passaging']]
]


# Function to filter and save data
def filter_data(file_name):
    # Read the original CSV file
    df = pd.read_csv(file_name)

    # Exclude rows with NaN values in the 'Title_URL' column
    df = df.dropna(subset=['Title_URL'])

    # Filter rows for high impact journals
    high_impact_df = df[df['Title_URL'].str.contains('|'.join(high_impact), case=False)]

    # Create a new column 'Keyword' and initialize it with empty strings
    df['Keyword'] = ''

    # Iterate through the rows and check for keywords in the 'Title1' column
    for i, title in enumerate(df['Title1']):
        for keyword_list in keywords:
            keyword_group = keyword_list[1]
            for keyword in keyword_group:
                if re.search(keyword, title, re.IGNORECASE):
                    df.loc[i, 'Keyword'] = keyword_list[0]
                    break

    # Get the current date
    current_date = datetime.datetime.now().strftime("%m_%d")

    # Generate the new file names
    high_impact_file_name = f"high_impact_journals_{current_date}.csv"
    keyword_rows_file_name = f"keyword_rows_{current_date}.csv"
    both_file_name = f"highimpact_and_keyword_{current_date}.csv"

    # Filtered data for high impact journals
    high_impact_df.to_csv(high_impact_file_name, index=False)

    # Filtered data for keyword rows
    keyword_rows = df[df['Keyword'] != '']
    keyword_rows.to_csv(keyword_rows_file_name, index=False)

    # Filtered data for both high impact and keyword rows
    both_rows = df[(df['Keyword'] != '') & df['Title_URL'].str.contains('|'.join(high_impact), case=False)]
    both_rows.to_csv(both_file_name, index=False)

# Get the file name from the user
file_name = input("Enter the CSV file name: ")

# Call the filter_data function
filter_data(file_name)



def filter_data(file_name):
    df = pd.read_csv(file_name)
    df = df.dropna(subset=['Title_URL'])
    high_impact_df = df[df['Title_URL'].str.contains('|'.join(high_impact), case=False)]
    df['Keyword'] = ''
    for i, title in enumerate(df['Title1']):
        for keyword_list in keywords:
            keyword_group = keyword_list[1]
            for keyword in keyword_group:
                if re.search(keyword, title, re.IGNORECASE):
                    df.loc[i, 'Keyword'] = keyword_list[0]
                    break
    current_date = datetime.datetime.now().strftime("%m_%d")
    high_impact_file_name = f"high_impact_journals_{current_date}.csv"
    keyword_rows_file_name = f"keyword_rows_{current_date}.csv"
    both_file_name = f"highimpact_and_keyword_{current_date}.csv"
    high_impact_df.to_csv(high_impact_file_name, index=False)
    keyword_rows = df[df['Keyword'] != '']
    keyword_rows.to_csv(keyword_rows_file_name, index=False)
    both_rows = df[(df['Keyword'] != '') & df['Title_URL'].str.contains('|'.join(high_impact), case=False)]
    both_rows.to_csv(both_file_name, index=False)