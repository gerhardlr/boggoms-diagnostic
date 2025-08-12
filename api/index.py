

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from helpers import get_root
from helpers.logging_config import get_logging_config
from helpers.db import get_db
from helpers.data_types import Event
from helpers.summary_page import make_plot


app = FastAPI()
templates = Jinja2Templates(directory="templates")

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


@app.post("/api/")
def post_event(event: Event):
    root = get_root()
    logger.info(f'pushing event{event}')
    return root.push(event)


@app.get("/api/")
def get_event():
    db = get_db()
    if result := db.ping():
        return {"message": f'DB is available with ping result: {result}'}
    return {"warning": f'DB is not available'}


@app.get("/api/metrics/", response_class=HTMLResponse)
def get_event_root(request: Request):
    db = get_db()
    if result := db.ping():
        html_plots = make_plot()
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "plot_paths": html_plots.paths,
                "plot_sources": html_plots.sources,
                "plot_dates": html_plots.dates,
            },
        )
    return {"warning": f'DB is not available'}
