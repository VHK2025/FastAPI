---
title: GetAround Price Predictor API
emoji: 🚗
colorFrom: blue
colorTo: purple
sdk: static
app_file: app.py
license: mit
---

# 🚗 GetAround Price Predictor API

Bienvenue sur cette API basée sur FastAPI qui permet de prédire **le prix d'une location de voiture** sur la plateforme GetAround grâce à un modèle de machine learning.

## ⚙️ Endpoints disponibles

### `POST /predict`
Prédit le prix de la location.

#### Exemples de données envoyées :
```json
{
  "feature_1": 12.0,
  "feature_2": 1.0,
  "feature_3": 35.0
}
