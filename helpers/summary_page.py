from typing import NamedTuple
import plotly.express as px
import pandas as pd
from .db import get_db


class Info(NamedTuple):
    dates: pd.DataFrame
    sources: pd.DataFrame
    paths: pd.DataFrame


def get_info():
    db = get_db()
    path_info = []

    for path in db.get_set("paths"):  # type: ignore
        path_info.append({'path': path, 'count': int(
            db.get(f'{path}_count'))})  # type: ignore
    source_info = []
    for source in db.get_set("sources"):  # type: ignore
        source_info.append({'source': source, 'count': int(
            db.get(f'{source}_count'))})  # type: ignore
    date_info = []
    for date in db.get_set("dates"):  # type: ignore
        date_info.append({'date': date, 'count': int(
            db.get(f'{date}_count'))})  # type: ignore
    dates = pd.DataFrame(date_info)
    sources = pd.DataFrame(source_info)
    paths = pd.DataFrame(path_info)
    return Info(dates, sources, paths)


class HTMLFigures(NamedTuple):
    paths: str
    dates: str
    sources: str


def make_plot():
    info = get_info()
    fig_sources = px.bar(info.sources, x="source",
                         y="count", title="Counts per Source")
    fig_paths = px.bar(info.paths, x="path", y="count",
                       title="Counts per Path")
    fig_dates = px.bar(info.dates, x="date", y="count",
                       title="Counts per Date")
    return HTMLFigures(
        fig_paths.to_html(full_html=False),
        fig_dates.to_html(full_html=False),
        fig_sources.to_html(full_html=False)
    )
