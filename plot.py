import pandas as pd
import numpy as np
import plotly.graph_objects as go
import statistics

from entities.deal import Deal

SECONDS_PER_MONTH = 60 * 60 * 24 * 30
OUTPUT_PLOT_FOLDER = "./plots/"

class Plot:
    def __init__(self):
        pass

    # png_generation: to enable pgn generation
    def plot_std_data(self, deltas_months: list[float], title: str, xlabel: str, ylabel: str, png_generation: bool = False, file_output_name: str = ""):
        avg = statistics.mean(deltas_months)
        std = statistics.stdev(deltas_months) if len(deltas_months) > 1 else 0.0

        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=deltas_months,
            name="Delta (months)",
            marker_color="lightblue",
            opacity=0.7,
            xbins=dict(size=1)  # bucket size = 1
        ))

        fig.add_trace(go.Scatter(
            x=[avg, avg],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Avg",
            line=dict(color="red", dash="dash")
        ))

        fig.add_trace(go.Scatter(
            x=[avg - std, avg - std],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Avg - σ",
            line=dict(color="green", dash="dot")
        ))
        fig.add_trace(go.Scatter(
            x=[avg + std, avg + std],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Avg + σ",
            line=dict(color="green", dash="dot")
        ))

        fig.update_layout(
            title=title,
            xaxis_title=xlabel,
            yaxis_title=ylabel,
            bargap=0.2,
            template="plotly_white"
        )

        if png_generation:
            fig.write_image(f"{OUTPUT_PLOT_FOLDER}{file_output_name}")

        fig.show()


    def plot_deals_over_time(self, deals: list[Deal], window: int = 4, png_generation: bool = False, file_output_name: str = ""):
        df = pd.DataFrame([{"deal_date": d.deal_date} for d in deals])

        # Raggruppamento per periodo
        df["period"] = df["deal_date"].dt.to_period("Q").dt.to_timestamp()
        deals_per_period = df.groupby("period").size().reset_index(name="n_deals")

        # Istogramma (barre)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=deals_per_period["period"],
            y=deals_per_period["n_deals"],
            name="Deals",
            marker_color="steelblue",
            opacity=0.8
        ))

        # Linea di tendenza con media mobile
        deals_per_period["moving_avg"] = deals_per_period["n_deals"].rolling(window=window, min_periods=1).mean()

        fig.add_trace(go.Scatter(
            x=deals_per_period["period"],
            y=deals_per_period["moving_avg"],
            mode="lines",
            name=f"Moving Average ({window})",
            line=dict(color="red", width=2)
        ))

        fig.update_layout(
            title=f"Deals count (Quarter) with trend ({window})",
            xaxis_title=f"Time (Quarter)",
            yaxis_title="Deals count",
            bargap=0.2,
            template="plotly_white"
        )

        if png_generation:
            fig.write_image(f"{OUTPUT_PLOT_FOLDER}{file_output_name}")

        fig.show()

