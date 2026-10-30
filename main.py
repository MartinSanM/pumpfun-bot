import asyncio
import logging
from src.config_loader import load_config
from src.sniper import PumpFunSniper

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

async def main():
    config = load_config()
    mode = "DRY RUN (Simulation)" if config.dry_run else "LIVE TRADING"
    logging.info(f"Pump.fun Sniper + ML Scorer Initialized | Mode: {mode}")
    logging.info(
        f"Buy: {config.buy_amount_sol} SOL | Slippage: {config.slippage_bps} bps | "
        f"Min ML Win Prob: {config.min_ml_win_prob:.0%} | TP: +{config.take_profit_pct}% | SL: -{config.stop_loss_pct}%"
    )

    sniper = PumpFunSniper(config)
    await sniper.listen_new_tokens()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[INFO] Sniper stopped cleanly.")
