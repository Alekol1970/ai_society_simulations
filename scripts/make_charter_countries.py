
"""make_charter_countries.py — build data/charter_countries.csv safely."""
import os, csv, random
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TARGET = os.path.join(DATA_DIR, "charter_countries.csv")
SOURCE = os.path.join(DATA_DIR, "cg_hr_data.csv")

def from_source():
    try:
        with open(SOURCE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            keep = [c for c in reader.fieldnames if c.lower() in {"country","code","cg","hr","region","year"}]
            if not keep: return None
            rows = [keep]
            for r in reader:
                rows.append([r.get(k, "") for k in keep])
            return rows
    except FileNotFoundError:
        return None

def demo_rows():
    random.seed(42)
    header = ["country","code","region","cg","hr","year"]
    regions = ["EU","APAC","AMER","MENA"]
    countries = [("CountryA","CTA"),("CountryB","CTB"),("CountryC","CTC"),("CountryD","CTD")]
    rows = [header]
    for name,code in countries:
        rows.append([name, code, random.choice(regions), 0.5, 0.5, 2024])
    return rows

def ensure_csv():
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(TARGET):
        print("Found existing data/charter_countries.csv — skip")
        return
    rows = from_source() or demo_rows()
    with open(TARGET, "w", newline='', encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    print("Wrote", TARGET)

if __name__ == "__main__":
    ensure_csv()
