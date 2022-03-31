import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CACHE_TIMEOUT = 60 * 60 * 6  # 6 hours in seconds
REDIS_URL = os.environ.get("REDIS_URL")
if REDIS_URL:
    CACHE_SETTINGS = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": os.environ.get("REDIS_URL", "redis://localhost:6379"),
        "CACHE_DEFAULT_TIMEOUT": CACHE_TIMEOUT,
        "CACHE_KEY_PREFIX": "360covidtracker",
    }
else:
    CACHE_SETTINGS = {
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": os.getenv(
            "CACHE_DIR", os.path.join(os.path.dirname(__file__), ".cache")
        ),
        "CACHE_DEFAULT_TIMEOUT": CACHE_TIMEOUT,
    }

DISABLE_UPDATE = os.getenv("DISABLE_UPDATE", "False").lower() in ("true", "1", "t")
DB_URL = os.getenv("DB_URL")
GOOGLE_ANALYTICS = os.getenv("GOOGLE_ANALYTICS")
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MAPBOX_STYLE = "carto-positron"
DATA_DIR = os.getenv("DATA_DIR", os.path.join(os.path.dirname(__file__), "assets/data"))
GRANTS_DATA_FILE = os.getenv(
    "GRANTS_DATA_FILE", os.path.join(DATA_DIR, "grants_data.json")
)
GRANTS_DATA_PICKLE = os.getenv(
    "GRANTS_DATA_PICKLE", os.path.join(DATA_DIR, "grants_data.pkl")
)
WORDS_PICKLE = os.getenv("WORDS_PICKLE", os.path.join(DATA_DIR, "ngrams.pkl"))
FUNDER_IDS_FILE = os.getenv(
    "FUNDER_IDS_FILE", os.path.join(DATA_DIR, "funder_ids.json")
)
SOURCES = {
    "recipientOrganizationPostcode": "Postcode of recipient organisation",
    "recipientOrganizationLocation": "Location of recipient organisation",
    "beneficiaryLocation": "Location of grant beneficiaries",
}
THREESIXTY_COLOURS = [
    # "#153634", # Grey
    "#DE6E26",  # Orange
    "#4DACB6",  # Teal
    "#EFC329",  # Yellow
    "#BC2C26",  # Red
    "#0B1B1A",  # Darker grey
    "#6F3713",  # Darker orange
    "#27565B",  # Darker teal
    "#786114",  # Darker yellow
    "#5E1613",  # Darker red
]

FUNDER_GROUPS = {
    "lottery": {
        "name": "National Lottery distributors",
        "funder_ids": {
            "GB-GOR-PB188": "National Lottery Community Fund",
            "GB-COH-RC000766": "Sport England",
            "GB-GOR-PC390": "National Lottery Heritage Fund",
            "GB-CHC-1036733": "Arts Council",
        },
    },
    "community-foundations": {
        "name": "UK Community Foundations",
        "funder_ids": {
            "GB-CHC-1091628": "Community Foundation for Staffordshire",
            "GB-CHC-1047625": "County Durham Community Foundation",
            "GB-CHC-1096892": "Leeds Community Foundation",
            "GB-CHC-1068887": "Community Foundation for Lancashire & Merseyside",
            "GB-CHC-1086516": "Bedfordshire & Luton Community Foundation",
            "GB-CHC-1155173": "Berkshire Community Foundation",
            "GB-CHC-1073861": "Heart of Bucks Community Foundation",
            "GB-CHC-1103314": "Cambridgeshire Community Foundation",
            "GB-CHC-1143711": "Cheshire Community Foundation",
            "GB-CHC-1002722": "Community Foundation for Calderdale",
            "GB-NIC-105105": "Community Foundation for Northern Ireland",
            "GB-CHC-1111600": "Community Foundation for Surrey",
            "GB-CHC-1123126": "Wiltshire Community Foundation",
            "GB-COH-02273708": "Community Foundation for Tyne and Wear",
            "GB-CHC-1074655": "Community Foundation for Wales",
            "GB-CHC-1099977": "Cornwall Community Foundation",
            "GB-CHC-1075120": "Cumbria Community Foundation",
            "GB-CHC-1057923": "Devon Community Foundation",
            "GB-CHC-1122113": "Dorset Community Foundation",
            "GB-CHC-1147789": "East End Community Foundation",
            "GB-CHC-1052061": "Essex Community Foundation",
            "GB-CHC-1017504": "Forever Manchester",
            "GB-CHC-1039485": "Foundation Derbyshire",
            "GB-SC-SC022910": "Foundation Scotland",
            "GB-CHC-900239": "Gloucestershire Community Foundation",
            "GB-CHC-1100417": "Hampshire & Isle of Wight Community Foundation",
            "GB-CHC-1117345": "Heart of England Community Foundation",
            "GB-CHC-1045304": "Heart of England Community Foundation",
            "GB-CHC-1094935": "Herefordshire Community Foundation",
            "GB-CHC-1156082": "Hertfordshire Community Foundation",
            "GB-CHC-1084361": "Kent Community Foundation",
            "GB-CHC-1135322": "Leicestershire & Rutland",
            "GB-CHC-1092328": "Lincolnshire Community Foundation",
            "GB-CHC-1091263": "London Community Foundation",
            "GB-CHC-295107": "Milton Keynes Community Foundation",
            "GB-CHC-1069538": "Nottinghamshire Community Foundation",
            "GB-CHC-1110817": "Norfolk Community Foundation",
            "GB-CHC-1094646": "Northamptonshire Community Foundation",
            "GB-CHC-1135258": "One Community Foundation",
            "GB-CHC-1151621": "Oxfordshire Community Foundation",
            "GB-CHC-1080418": "Quartet Community Foundation",
            "GB-COH-04530979": "Somerset Community Foundation",
            "GB-CHC-1140947": "South Yorkshire Community Foundation",
            "GB-CHC-1109453": "Suffolk Community Foundation",
            "GB-CHC-1113226": "Sussex Community Foundation",
            "GB-CHC-1166471": "Two Ridings Community Foundation",
            "GB-CHC-1102266": "Worcestershire Community Foundation",
        },
    },
    "central-government": {
        "name": "Central Government",
        "funder_ids": {
            "GB-GOR-D2": "Cabinet Office",
            "GB-GOR-D1198": "Department for Business, Energy and Industrial Strategy",
            "GB-GOR-D5": "Department for Digital, Culture, Media and Sport",
            "GB-GOR-D6": "Department for Education",
            "GB-GOR-D7": "Department for Environment, Food and Rural Affairs",
            "GB-GOR-D8": "Department for International Development",
            "GB-GOR-D1196": "Department for International Trade",
            "GB-GOR-D9": "Department for Transport",
            "GB-GOR-D10": "Department for Work and Pensions",
            "GB-GOR-D12": "Department of Health and Social Care",
            "GB-GOR-D13": "Foreign and Commonwealth Office",
            "GB-GOR-D25": "HM Revenue & Customs",
            "GB-GOR-D16": "Home Office",
            "GB-GOR-D4": "Ministry for Housing, Communities and Local Government",
            "GB-GOR-D17": "Ministry of Defence",
            "GB-GOR-D18": "Ministry of Justice",
            "GB-CHC-1177627": "Armed Forces Covenant Fund",
        },
    },
}

PRIORITIES = [
    "GB-CHC",
    "GB-SC",
    "GB-NIC",
    "GB-EDU",
    "GB-LAE",
    "GB-PLA",
    "GB-LAS",
    "GB-LANI",
    "GB-GOR",
    "GB-COH",
]

AMOUNT_BINS = [0, 500, 1000, 2000, 5000, 10000, 100000, 1000000, float("inf")]
AMOUNT_BIN_LABELS = [
    "Under £500",
    "£500 - £1k",
    "£1k - £2k",
    "£2k - £5k",
    "£5k - £10k",
    "£10k - £100k",
    "£100k - £1m",
    "Over £1m",
]
INCOME_BINS = [-1, 10000, 100000, 250000, 500000, 1000000, 10000000, float("inf")]
INCOME_BIN_LABELS = [
    "Under £10k",
    "£10k - £100k",
    "£100k - £250k",
    "£250k - £500k",
    "£500k - £1m",
    "£1m - £10m",
    "Over £10m",
]
AGE_BINS = pd.to_timedelta([x * 365 for x in [-1, 1, 2, 5, 10, 25, 200]], unit="D")
AGE_BIN_LABELS = [
    "Under 1 year",
    "1-2 years",
    "2-5 years",
    "5-10 years",
    "10-25 years",
    "Over 25 years",
]

STOPWORDS = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "you're",
    "you've",
    "you'll",
    "you'd",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "she's",
    "her",
    "hers",
    "herself",
    "it",
    "it's",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "that'll",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "don't",
    "should",
    "should've",
    "now",
    "d",
    "ll",
    "m",
    "o",
    "re",
    "ve",
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't" "toward",
    "towards",
    "work",
    "works",
    "help",
    "continue",
    "works",
    "provide",
    # covid-specific words
    "covid19",
    "19",
    "covid",
    "people",
    "grant",
    "during",
    "pandemic",
    "coronavirus",
]

PROMETHEUS_AUTH_USERNAME = os.environ.get("PROMETHEUS_AUTH_USERNAME", "prom")
PROMETHEUS_AUTH_PASSWORD = os.environ.get("PROMETHEUS_AUTH_PASSWORD", "1234")
