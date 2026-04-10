# Système Multi Agent Transformer pour resoudre le probleme SAT

## Description
Le present projet fait l'exploration l'utilisation des Transformers models pour le but de résoudre SAT problems et à pour but le performance en utilisant systèmes multi agents.

## Features
 - Generation des datasets SAT
 - Solveur base sur les transformations
 - Collaboration multi-agent
 - Evaluation des performances


## Installation
`pip install -r requirements.txt`

## Usage
`python3 main.py`

## Results
Il manque ajouter les graphiques des résults ici


## 1. Architecture

```text
sat-transformer-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── src/
│   ├── data/
│   │   ├── generator.py
│   │   ├── loader.py
│   │   └── preprocess.py
│   │
│   ├── models/
│   │   ├── transformer.py
│   │   └── multi_agent.py
│   │
│   ├── training/
│   │   ├── train.py
│   │   └── evaluate.py
│   │
│   └── utils/
│       └── metrics.py
│
├── experiments/
│   └── exp_01.py
│
├── results/
│
├── notebooks/
│   └── exploration.ipynb
│
├── README.md
├── requirements.txt
└── main.pys
```


Auteur
HAMC