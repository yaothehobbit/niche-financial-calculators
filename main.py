from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="RS Fund Management - Financial Calculators")

app.mount("/niche_calc/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

CALCULATORS = [
    {
        "id": "fee-impact",
        "title": "Investment Fee Impact Calculator",
        "subtitle": "See how expense ratios eat your returns over 30 years",
        "icon": "chart-line",
        "category": "Investment",
        "keywords": "expense ratio calculator, investment fee calculator, fund fee impact",
    },
    {
        "id": "coast-fire",
        "title": "Coast FIRE Calculator",
        "subtitle": "Find when you can stop saving and coast to retirement",
        "icon": "umbrella-beach",
        "category": "FIRE",
        "keywords": "coast fire calculator, coast fire number, early retirement calculator",
    },
    {
        "id": "capital-gains-tax",
        "title": "Capital Gains Tax by State",
        "subtitle": "Compare federal + state capital gains tax across all 50 states",
        "icon": "landmark",
        "category": "Tax",
        "keywords": "capital gains tax calculator by state, state capital gains tax rates",
    },
    {
        "id": "roth-conversion",
        "title": "Roth Conversion Ladder Planner",
        "subtitle": "Optimize yearly Roth conversions to minimize lifetime taxes",
        "icon": "stairs",
        "category": "Tax",
        "keywords": "roth conversion calculator, roth conversion ladder, roth ira conversion",
    },
    {
        "id": "401k-optimizer",
        "title": "401(k) Match Optimizer",
        "subtitle": "Maximize your employer match — don't leave free money on the table",
        "icon": "piggy-bank",
        "category": "Investment",
        "keywords": "401k match calculator, employer match optimizer, 401k contribution calculator",
    },
    {
        "id": "brrrr",
        "title": "BRRRR Method Calculator",
        "subtitle": "Analyze Buy, Rehab, Rent, Refinance, Repeat deals step by step",
        "icon": "home",
        "category": "Real Estate",
        "keywords": "brrrr calculator, brrrr method, buy rehab rent refinance repeat",
    },
    {
        "id": "rental-cashflow",
        "title": "Rental Property Cash-on-Cash Return",
        "subtitle": "Calculate your true return on invested capital for rental properties",
        "icon": "building",
        "category": "Real Estate",
        "keywords": "cash on cash return calculator, rental property ROI, rental yield calculator",
    },
    {
        "id": "fire-variable",
        "title": "FIRE Number Calculator (Variable Spending)",
        "subtitle": "Plan for different spending phases in early retirement",
        "icon": "fire",
        "category": "FIRE",
        "keywords": "fire calculator, fire number calculator, financial independence calculator, early retirement",
    },
    {
        "id": "debt-payoff",
        "title": "Debt Avalanche vs Snowball Calculator",
        "subtitle": "Compare strategies and find the fastest path to debt freedom",
        "icon": "credit-card",
        "category": "Debt",
        "keywords": "debt avalanche calculator, debt snowball calculator, debt payoff calculator, debt free calculator",
    },
    {
        "id": "se-tax",
        "title": "Self-Employment Tax Calculator by State",
        "subtitle": "Estimate your federal + state self-employment tax as a freelancer",
        "icon": "briefcase",
        "category": "Tax",
        "keywords": "self employment tax calculator, freelancer tax calculator, self employed tax by state",
    },
]


@app.get("/niche_calc", response_class=HTMLResponse)
@app.get("/niche_calc/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "calculators": CALCULATORS},
    )


@app.get("/niche_calc/{calc_id}", response_class=HTMLResponse)
async def calculator_page(request: Request, calc_id: str):
    calc = next((c for c in CALCULATORS if c["id"] == calc_id), None)
    if not calc:
        return HTMLResponse("Calculator not found", status_code=404)
    return templates.TemplateResponse(
        f"calculators/{calc_id}.html",
        {"request": request, "calc": calc, "calculators": CALCULATORS},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
