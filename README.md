# SARS_CoV_2_article_scraping
A workflow to pull articles weekly from Google Scholar about the SARS_CoV_2 pandemic. 

![Google Scholar Search Sars-CoV-2 coronavirus and COVID-19](https://github.com/acapria/SARS_CoV_2_article_scraping/assets/131828886/ab9973de-0122-487f-b5fc-d718101322a4)



This workflow was created to reduce the burden of flipping through google scholar pages for articles about SARS-CoV-2

## Octoparse
This workflow starts with google scholar then uses octoparse to read through the google scholar page and pull the data. 

## File Manipulation
Then the outputted CSV from octoparse is running the python script #scraper for SARS_CoV_2 Articles.py

## Test Files
As you can see there are 3 different outputs 



### Keyword Groups

|Keyword Label | Key Word Output |
|--------------|------------------|
|Variants, |Variant, Alpha, Delta, Omicron |
|genes_genomic_regions|ACE2, ORF9b|
|Lung_Cardio|Cardiovascular, Brugada, Stemi, Chest, Respiratory, Ventilatory, Intubation, Ventilatory, Cardiovascular injuries, Heart|
|long_covid|Long Covid, Long, Post, Post-covid, Post-Acute Sequela, Neurological outcome, Complications, Complication|
|Molecules|Inhibitor, Spike, Nuclear, Protease, Reductase, Esterase, Antibodies, Effector, fc-effector, Heme, Nucleic, Cellular, Cell, Furin, RNA, Peptides, Proteins, Protein, Aldose, T cells, B cells, Oxidative Stress, Aptamer, Binding, Compound, Renin, Angiotensin, Renin-Angiotensin, Antioxidant, Molecular, Reyanning|
|non_human|Rhesus Macaques, zoonotic, zoonosis, Lion, gorrilla |
|pediatric|Peds, Pediatric, Neonatal, Children, Infants, School, Pediatrics|
|Vaccine|Vaccine, Vaccination, Prior, mRNA vaccine, Booster|
|Medication_treatment|Nirmatrelvir, Adjuvants, Adjuvant, Cepharanthine, Pharmacokinetics, Medications, Fluvoxamine, Ozone, Therapy, Interferon-beta Injections, Interferon, Traditional Plant Therapy, Drug, Camostat, Inactivation|
|Testing|Nasal swabs, Rapid, Antigen, Testing|
|Immune|Immune response, Immune|
|clinical_trial|clinical trial, Phase 1, Phase 2, Phase 3, Manufacturing, Cohort, In silico screening, In silico|
|Inflammation|MIS-C, Anti-Inflammatory, Inflammatory|
|Breakthrough|Breakthrough|
|Anti|Antiviral, Antimicrobrial, Antibacterial, Antimicrobial, Antibiotic, Antiviral |
|genetic_tools|siRNAs, Metatranscriptome, Transcriptomics, Metabolomic, Proteome, Sequencing, NGS, Next-generation, Epigenetic, genomic, Sequencing, Transcriptomic |
|detection|Aerosol, Detection, Wastewater Surveillance, Diagnostic, Assay, Exposure |
|public_health|Seroprevalence, Public Health, Environment, Community, Hesitancy, Telehealth, Transmission, Epidemic, Endemicity, Outbreak, Containment, Transmission, Contact tracing, Epidemiology, Epidemiological, Sanitization, Risk, Surveillance, Post-Infection Mortality, Mortality|
|Social|Mental Health, Mental, Isolation, Disability|
|Biomarkers|Biomarkers, Changes|
|wellbeing|healing, Sexual Activity, Acceptance, Mental Health, Communication |
|other_conditions|herpes, Herpesvirus, Epilepsy, Diabetes, Ocular Neurogenic Palsy, MIS-C, Bacterial, Cancer, Leukemia, Mucormycosis, Osteochondral, Hematological Malignancies, Influenza, Liver, Abducens palsy, Palsy, Psychosis, Hippocampal Subfield Abnormalities, Laríngeas, Clinical|
|Tech|Sensors, AI, Machine learning, Machine Learning, Biosensing, Biosensors, Modeling, Model, Models, Network, Analysis|
|Symptoms|Symptoms, Cough|
|Misc|Phytoconstituents, Coronaviruses, Restriction Factors, Lipid Composition, Composition, Immune Ageing, Dynamic Disease Manifestations, Nanobody Repertoire, Differential laboratory passaging|

### High-Impact Journals
Nature, Sagepub, MDPI, Springer, oup, JAMA network, ScienceDirect, Lancet, PLOS, Cell, Wiley, ACS, JMIR, Biomedcentral
