import pandas as pd
import plotly.graph_objects as go
import statistics

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

