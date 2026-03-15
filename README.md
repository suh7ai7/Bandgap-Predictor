\# Band Gap Predictor



A machine learning project that predicts the electronic band gap (eV) of inorganic materials using compositional features and LightGBM.



\## What it does

Given a chemical formula (e.g. `Rb2Te`), the model predicts how easily electricity flows through that material — useful for discovering new semiconductors, solar cell materials, and LEDs.



\## Results

\- \*\*RMSE: 0.7122 eV\*\*

\- \*\*R²: 0.8014\*\*



\## Dataset

\- Source: Materials Project via matminer `dielectric\\\_constant` dataset

\- 1056 inorganic compounds

\- License: CC-BY-4.0



\## Features

\- 132 ElementProperty features from matminer (Magpie preset)

\- Most important: MeltingT, MendeleevNumber, NdValence



\## Model

\- LightGBM regressor

\- Hyperparameter tuning with Optuna (20 trials, 5-fold CV)

\- Experiment tracking with MLflow

\- Interpretability via SHAP



\## How to run

```bash

conda env create -f environment.yml

conda activate bandgap

jupyter notebook bandgap\\\_predictor.ipynb

```



\## Project structure

```

bandgap-predictor/

├── bandgap\\\_predictor.ipynb   # main notebook

├── data/polymers.csv         # dataset

├── checkpoints/              # saved model

├── reports/                  # plots

└── environment.yml

```

