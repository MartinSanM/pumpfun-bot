# Pump.fun Solana Sniper Bot + ML Token Scorer

High-speed, modular Solana token sniper for Pump.fun launches featuring a pre-trained Gradient Boosting ML classifier, historical training/evaluation datasets, automatic Take-Profit / Stop-Loss tracking, and externalized key configuration.

## Repository Structure
- `data/raw/pumpfun_launches_historical.csv`: Full historical dataset (1,500 token launches with on-chain & social features).
- `data/processed/train_dataset.csv`: Training split (1,200 launches).
- `data/processed/eval_dataset.csv`: Holdout evaluation split (300 launches).
- `data/processed/eval_predictions.csv`: Model evaluation predictions with win probabilities.
- `models/token_scorer_model.pkl`: Pre-trained Gradient Boosting model artifact ready for live inference.
- `models/evaluation_metrics.json`: Holdout evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC, Feature Importances).
- `ml/train_model.py` & `ml/evaluate_model.py`: Scripts to retrain and evaluate the ML model on new data.
- `ml/features.py`: Real-time feature extraction pipeline.
- `src/`: Live WebSocket sniper engine (`sniper.py`), transaction builder (`trader.py`), and externalized key loader (`config_loader.py`).
- `keys.example.json` & `.env.example`: Templates for inputting your private key and RPC/API keys without hardcoding secrets.

## Key Input File (`keys.json` or `.env`)
No private keys or API keys are hardcoded anywhere in the repository.
1. On first run, the bot automatically generates `keys.json` from `keys.example.json`.
2. Paste your `SOLANA_PRIVATE_KEY`, `RPC_HTTPS_URL`, and optional `PUMPPORTAL_API_KEY` into `keys.json`.
3. Both `keys.json` and `.env` are listed in `.gitignore` so your secrets are never exposed on GitHub.

## Training, Evaluating & Running
```bash
pip install -r requirements.txt

# Retrain the model
python -m ml.train_model

# Run evaluation suite
python -m ml.evaluate_model

# Start the sniper bot
python main.py
```
