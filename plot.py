import pandas as pd
import plotly.graph_objects as go
import statistics

SECONDS_PER_MONTH = 60 * 60 * 24 * 30

class Plot:
    def __init__(self):
        pass

    def plot_std_data(self, deltas_months: list[float]):
        if not deltas_months:
            print("⚠️ Nessun dato disponibile per il plotting")
            return

        avg = statistics.mean(deltas_months)
        std = statistics.stdev(deltas_months) if len(deltas_months) > 1 else 0.0

        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=deltas_months,
            name="Delta (mesi)",
            marker_color="lightblue",
            opacity=0.7,
            xbins=dict(size=1)  # bucket di 1 mesi
        ))

        fig.add_trace(go.Scatter(
            x=[avg, avg],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Media",
            line=dict(color="red", dash="dash")
        ))

        fig.add_trace(go.Scatter(
            x=[avg - std, avg - std],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Media - σ",
            line=dict(color="green", dash="dot")
        ))
        fig.add_trace(go.Scatter(
            x=[avg + std, avg + std],
            y=[0, len(deltas_months)],
            mode="lines",
            name="Media + σ",
            line=dict(color="green", dash="dot")
        ))

        fig.update_layout(
            title="Distribuzione dei delta tra i deal (in mesi)",
            xaxis_title="Delta (mesi)",
            yaxis_title="Frequenza",
            bargap=0.2,
            template="plotly_white"
        )

        fig.show()

