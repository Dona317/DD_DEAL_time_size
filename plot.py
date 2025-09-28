import pandas as pd
import numpy as np
import plotly.graph_objects as go
import statistics

from entities.deal import Deal

SECONDS_PER_MONTH = 60 * 60 * 24 * 30

class Plot:
    def __init__(self):
        pass

    def plot_std_data(self, deltas_months: list[float], title: str, xlabel: str, ylabel: str):
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

        fig.show()


    def plot_deals_over_time_by_flag(
            self,
            deals: list[Deal],
            field_name: str,
            window: int = 4,
            log_scale: bool = False
        ):
        df = pd.DataFrame([{
            "deal_date": d.deal_date,
            "flag": getattr(d, field_name, False)
        } for d in deals])

        # Raggruppamento per periodo
        df["period"] = df["deal_date"].dt.to_period("Q").dt.to_timestamp()
        deals_per_period = df.groupby(["period", "flag"]).size().reset_index(name="n_deals")

        # Pivot per separare True / False
        pivot = deals_per_period.pivot(index="period", columns="flag", values="n_deals").fillna(0)
        pivot = pivot.rename(columns={True: f"{field_name} True", False: f"{field_name} False"}).reset_index()

        fig = go.Figure()

        # Barre True / False (senza testo)
        if f"{field_name} True" in pivot.columns:
            fig.add_trace(go.Bar(
                x=pivot["period"],
                y=pivot[f"{field_name} True"],
                name=f"{field_name} True",
                marker_color="orange",
                opacity=0.8
            ))

        if f"{field_name} False" in pivot.columns:
            fig.add_trace(go.Bar(
                x=pivot["period"],
                y=pivot[f"{field_name} False"],
                name=f"{field_name} False",
                marker_color="steelblue",
                opacity=0.8
            ))

        # Media mobile per True
        if f"{field_name} True" in pivot.columns:
            pivot["ma_true"] = pivot[f"{field_name} True"].rolling(window=window, min_periods=1).mean()
            fig.add_trace(go.Scatter(
                x=pivot["period"],
                y=pivot["ma_true"],
                mode="lines",
                name=f"{field_name} True Moving Avg ({window})",
                line=dict(color="darkorange", width=2)
            ))

        # Media mobile per False
        if f"{field_name} False" in pivot.columns:
            pivot["ma_false"] = pivot[f"{field_name} False"].rolling(window=window, min_periods=1).mean()
            fig.add_trace(go.Scatter(
                x=pivot["period"],
                y=pivot["ma_false"],
                mode="lines",
                name=f"{field_name} False Moving Avg ({window})",
                line=dict(color="blue", width=2)
            ))

        fig.update_layout(
            barmode="stack",
            title=f"Deals count (Quarter) - {field_name} True vs False with trend ({window})",
            xaxis_title=f"Time (Quarter)",
            yaxis_title="Deals count (log scale)" if log_scale else "Deals count",
            bargap=0.2,
            template="plotly_white",
            yaxis_type="log" if log_scale else "linear"
        )

        fig.show()

        return pivot



