<<<<<<< HEAD
# Road_Accidents
=======
# Road Accidents in France: Data Analysis and Severity Prediction (2023-2024)

## Overview
This project analyzes road accidents across France using 2023-2024 data. It covers 109,224 accidents involving 250,976 individuals, with a focus on understanding accident patterns and predicting severity outcomes.

The analysis is structured in four main parts:
1. **Data Exploration** - Understanding raw data structure and quality
2. **Data Preparation** - Cleaning, integration, and feature engineering
3. **Exploratory Data Analysis** - Temporal, geographic, and contextual patterns
4. **Model Training** - Machine learning for severity prediction

## Project Structure

```
Road Accidents/
├── Road Accidents/
│   ├── 1- Exploring Data.ipynb           # Initial data exploration
│   ├── 2- Data Preparation.ipynb         # Data cleaning and integration
│   ├── 3- Exploratory Data Analysis.ipynb # Statistical and geographic analysis
│   └── 4- Model Training.ipynb           # Machine learning model development
├── Road_Accidents_Report.tex              # Comprehensive LaTeX report
├── README.md                              # This file
├── .gitignore                             # Git ignore patterns
└── requirements.txt                       # Python dependencies
```

## Data Sources

The project uses four linked datasets:
- **Characteristics (caract)**: Accident-level attributes (lighting, weather, time, collision type)
- **Locations (lieux)**: Geographic coordinates, road type, agglomeration status
- **Users (usagers)**: Individual injury outcomes (killed, hospitalized, injured, uninjured)
- **Vehicles (vehicules)**: Vehicle counts and information

Data format: CSV with semicolon delimiter and UTF-8 encoding (French standard).

## Key Findings

### Severity Insights
- **Overall severity rate**: 36.11% (accidents with serious injury or death)
- **Temporal peak**: 2-4 AM (night accidents 40% more severe than day)
- **Urban advantage**: Paris severity 9.32% vs. national 36.11% (safer infrastructure, lower speeds)
- **Weather impact**: Snow/fog increase severity by 50% compared to normal conditions

### Risk Factors (Feature Importance)
1. **Hour of day** (18.5%) - Night-time is deadliest
2. **Road type** (25.7%) - Departmental and local roads more dangerous
3. **Agglomeration** (24.3%) - Countryside riskier than urban areas
4. **Collision type** (7.5%) - Head-on collisions inherently severe
5. **Number of vehicles** (9.8%) - More vehicles = higher severity risk

### Geographic Findings
- **Top risk zones**: Orleans area, central Paris, various intersections across France
- **Black spots**: 200+ high-risk zones identifiable through clustering
- **Urban patterns**: Front-to-rear collisions dominant; pedestrian accidents critical

## Model Performance

### Random Forest Classifier
- **Accuracy**: 67%
- **Precision (Severe)**: 55% (reliable severity predictions)
- **Recall (Severe)**: 57% (catches 57% of severe accidents)
- **ROC-AUC**: 0.72 (good discrimination)

### Architecture
- **Ensemble**: 100 decision trees
- **Features**: 45 (after one-hot encoding of temporal, weather, road, collision features)
- **Class weighting**: Balanced (addresses class imbalance)
- **Training set**: 87,371 accidents (80%)
- **Test set**: 21,843 accidents (20%)

## Recommendations

### Immediate Actions
1. **Night-time safety campaigns** - Enhanced enforcement 2-4 AM
2. **Black spot interventions** - Signal upgrades, road markings, speed enforcement
3. **Weather-responsive measures** - Automatic speed reduction in adverse conditions

### Medium-Term Strategy
1. Infrastructure improvements (lighting, road markings, safer intersections)
2. Enhanced data collection (driver demographics, vehicle details)
3. Model deployment for real-time risk scoring and resource allocation

### Technical Improvements
1. Gradient boosting models (XGBoost, LightGBM)
2. Additional features: driver age/history, vehicle type, traffic density
3. Cross-validation and hyperparameter optimization
4. SMOTE for better class balance handling

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the Analysis

1. **Data Exploration**
```bash
jupyter notebook "1- Exploring Data.ipynb"
```

2. **Data Preparation**
```bash
jupyter notebook "2- Data Preparation.ipynb"
```

3. **EDA**
```bash
jupyter notebook "3- Exploratory Data Analysis.ipynb"
```

4. **Model Training**
```bash
jupyter notebook "4- Model Training.ipynb"
```

### Generating the Report
```bash
pdflatex Road_Accidents_Report.tex
# Output: Road_Accidents_Report.pdf
```

## Dependencies

- pandas >= 1.3.0
- numpy >= 1.20.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- scikit-learn >= 0.24.0

## Data Cleaning Summary

- **Initial records**: 109,224 accidents
- **Final records**: 109,214 accidents (after filtering unknown values)
- **Duplicates removed**: 31,884 location records
- **Missing values**: Filtered critical unknown codes (-1) in weather, lighting, agglomeration, intersection type

## Limitations

1. **Missing features**: Driver age/experience, alcohol involvement, vehicle safety ratings
2. **Geographic scope**: Includes overseas territories (DOM-TOM) alongside mainland
3. **Temporal scope**: Only 2 years of data (2023-2024)
4. **Class imbalance**: Severe accidents underrepresented (36% vs. 64%)

## Future Work

- [ ] Collect additional driver and vehicle features
- [ ] Implement gradient boosting models for improved predictions
- [ ] Deploy real-time API for risk scoring
- [ ] Create interactive dashboard for geographic visualization
- [ ] Develop mobile app for driver risk alerts
- [ ] Validate model on 2025 data (out-of-time validation)

## Author

Data Science Project - March 2026

## License

This project uses publicly available French road accident data. For data terms, see the French government data portal (data.gouv.fr).

## References

- French road accident classification: Official BAAC (Bulletin d'Analyse d'Accidents Corporels) format
- Data source: data.gouv.fr - Base de données des accidents corporels de la circulation
>>>>>>> 353ae31 (Initial commit: road accidents analysis)
