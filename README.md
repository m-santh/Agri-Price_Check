# AgriPriceGPT: Unlocking Pricing Insights for commodity food items in India 🇮🇳

![i want an image 0](https://github.com/m-santh/Agri-Price_Check/assets/8970135/58cd6be4-622b-4d3d-a815-871d19222096)

credit: gencraft.com

## About AgriPriceGPT
AgriPriceGPT is an AI-powered application that connects to a real-time **SQLite database** and generates data embeddings. It utilizes Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build a real-time Large Language Model (LLM)-enabled data pipeline in Python, combining data from multiple databases.

## How to Use

Explore and gain insights into the state wise pricing for commodity food prices in India. Feel free to ask questions like on price indicators across different commodity foods based on any state.. 

### Pricing indicators availible

### 167 commodity foods
PADDY(DHAN)
COTTON
SOYABEANS
GROUND NUT
MOONG WHOLE (GREEN GRAM)
MUSTARD SEED (SARSON)
GUAR SEEDS
CHILLI
APPLE
WHEAT
MAIZE
BAJRA
ONION
URAD (BLACK GRAM)
CHANA
CASTOR SEED
POTATO
TOMATO
SESAMUM(SESAME/GINGELLY/TIL)
WHITE PEAS
PADDY
GARLIC
TURMERIC
JOWAR (SORGHUM)
ARHAR DAL SPLIT(RED GRAM SPLIT)
MOATH DAL
CAULIFLOWER
BRINJAL
LEMON
POMEGRANATE
BANANA
GREEN CHILLI
JAGGERY
CUMMIN SEED(JEERA)
CUCUMBAR(KHEERA)
LENTIL(MASUR)
CORIANDAR
CABBAGE
COWPEA
COPRA
PUMPKIN
GINGER
LADIES FINGER (BHINDI)
ORANGE
BOTTLE GOURD
BITTER GOURD
SWEET LEMON (MOSAMBI)
COCONUT
PEAS GREEN (PODS)
GROUNDNUT PODS_80 KG(TN)
GINGELLY_(TN)
WALNUT
POINTED GOURD (PARVAL)
PAPAYA
ISBGOL
SUN FLOWER SEEDS
RADDISH
RIDGE GOURD
KINNOW
CAPSICUM
BARLEY (JAU)
GUAVA
TINDA
COCONUT
BANANA RAW
COTTON SEED
CARROT
ISABGUL (PSYLLIUM)
LINSEED
SWEET POTATO
CLUSTER BEANS
KULTHI(HORSE GRAM)
AJWAIN
PINE APPLE
METHI SEEDS
SPINACH
SWEET CORN
WATER MELON
CHIKOOS(SAPOTA)
IVY GOURD
COLACASIA
LOBIA
AMLA
CORIANDER(LEAVES)
FRENCH BEANS (FRASBEAN)
MUSK MELON
TAMARIND FRUIT
LAKH/TEORA
PEAR(MARASEBU)
DRUMSTICK
GHERKIN
TARAMIRA
RICE
BEETROOT
SOUNF (FENNEL SEEDS)
LESSER YAM
METHI(LEAVES)
GRAPES
MANGO
SPONGE GOURD
BETAL LEAVES
PLUM
RAGI (FINGER MILLET)
APRICOT(JARDALU/KHUMANI)
CASHEWNUTS
TAMARIND
SNAKE GUARD
SPRING ONION
BETELNUTS
SILK COCOON
MARI GOLD
TEVADA
LOBIA PODS
STRAW BERRY
CUSTARD APPLE (SHARIFA)
PERSIMON(JAPANI FAL)
TAPIOCA
MILLETS
CUMBU-HYBRID
BROCCOLI
FISH
TUBER ROSE
PEACH
CHILLI RED
TURNIP
RUBBER
MINT LEAVES
SQUASH(CHAPPAL KADOO)
SAFFLOWER
PRAWN
BER(ZIZYPHUS/BOREHANNU)
ARHAR (TUR/RED GRAM)
BROAD BEANS
VEGETABLES
CARNATION
JUTE
SEM
JIMIKAND (SURAN)
CRAB
MUSHROOM
GRAPEFRUIT
JACK FRUIT
NIGER SEED (RAMTIL)
NEEM
FIBER CROPS
ARROWROOT
BLACK PEPPER WHOLE
RAPESEED
HONEY
SUNHEMP
SPICES
ALMOND(BADAM)
GERBERA
CHERRY
CURRY LEAVES
LEMON
RAJMA
SAFFRON
KHARBUJA
MAHUA FLOWER
MAHUA SEED(HIPPE SEED)
SWEET CORN
BENGAL GRAM (CHANA DAL)
LITCHI
PONGAM SEEDS
REETHA
MISCELLANEOUS 

### Trading volumes and prices for last one month.

---

## End User
The primary end users of AgriPriceGPT are Farmers, Consumers, and middlemen interested in gaining insights into the current prices of commoditieis in India. Secondary users may include government boids, industries who can use this to moderate prices.

---

## Industry Impact
AgriPriceGPT has the potential to have a significant impact on the Agriculture industry in India. It provides a convenient and efficient way to access real-time food prices in India, allowing stakeholders to make informed decisions. 

---

## Business Value
AgriPriceGPT offers a valuable service by bridging the gap between data sources and actionable insights. It can be monetized by offering premium features or data analysis services to farmers and industries interested in discovering current prices in India. The application can generate revenue through subscription models or consulting services for data-driven decision-making.

---

## Utilization of the LLM App
- AgriPriceGPT utilizes the LLM (Large Language Model) App features provided by Pathway to build a real-time data pipeline.
- The LLM App enables natural language processing capabilities, allowing users to ask questions in plain language and receive relevant nutrition insights.
- AgriPriceGPT leverages the LLM's ability to process and analyze text data to extract meaningful information from various sources, including its connection to an SQL database.
- This direct connection to the database enhances AgriPriceGPT's capabilities, as it can access and analyze data that already resides in multiple applications and databases, providing users with comprehensive insights about food prices and trends. This streamlining of data retrieval and analysis significantly improves the efficiency and effectiveness of the application.
- 

## Code sample

The code establishes a connection with the database and generates a JSONL file whenever there are updates in the database. The variable "last_known_row_count" monitors these updates to ensure real-time generation of the JSON file.

```python
import sqlite3
# import json

def generate_jsonl_file():
    c.execute('SELECT * FROM my_table')
    rows = c.fetchall()
    column_names = [column[0] for column in c.description]
    
    with open('data/data.jsonl', 'w') as f:
        for row in rows:
            inner_dict_str = str({column_names[i]: row[i] for i in range(len(column_names))})
            outer_json_str = '{"doc": "' + inner_dict_str.replace('"', '\\"') + '"}'
            f.write(outer_json_str + '\n')

# Initialize last_known_row_count
last_known_row_count = 0

conn = sqlite3.connect('nutri_nfhs5_india.db')
c = conn.cursor()

while True:  
    # Check current row count
    c.execute('SELECT COUNT(*) FROM my_table')
    current_row_count = c.fetchone()[0]
    
    # Compare with last known row count
    if current_row_count != last_known_row_count:
        generate_jsonl_file()
        last_known_row_count = current_row_count


```
The JSONL file will be subsequently processed using the Pathway API 
```python
import pathway as pw

from common.embedder import embeddings, index_embeddings
from common.prompt import prompt


def run(host, port):
    # Given a user question as a query from your API
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )
    print("1",query,response_writer)
    # Real-time data coming from external data sources such as jsonlines file
    sales_data = pw.io.jsonlines.read(
        "./data",
        schema=DataInputSchema,
        mode="streaming"
    )
    print("2",sales_data)

    # Compute embeddings for each document using the OpenAI Embeddings API
    embedded_data = embeddings(context=sales_data, data_to_embed=sales_data.doc)
    print("3",embedded_data)
    # Construct an index on the generated embeddings in real-time
    index = index_embeddings(embedded_data)
    print("4",index)
    # Generate embeddings for the query from the OpenAI Embeddings API
    embedded_query = embeddings(context=query, data_to_embed=pw.this.query)
    print("5",embedded_query)
    # Build prompt using indexed data
    responses = prompt(index, embedded_query, pw.this.query)
    print("6",responses)
    # Feed the prompt to ChatGPT and obtain the generated answer.
    response_writer(responses)
    print("7",response_writer)
    # Run the pipeline
    pw.run()


class DataInputSchema(pw.Schema):
    doc: str


class QueryInputSchema(pw.Schema):
    query: str

```
## How to run the project

Example only supports Unix-like systems (such as Linux, macOS, BSD). If you are a Windows user, we highly recommend leveraging Windows Subsystem for Linux (WSL) or Dockerize the app to run as a container.
![Peek 2023-11-03 15-04](https://github.com/AnimeshN/chatgpt-database-python-nutrition/assets/17973453/41d17008-0bd0-4f8a-b8f3-4a260b0c5853)


### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

Then, follow the easy steps to install and get started using the sample app.

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/AnimeshN/AgriPriceGPT-database-python.git
```

Next,  navigate to the project folder:

```bash
cd AgriPriceGPT-database-python
```

### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `{OPENAI_API_KEY}` configuration value with your key. 

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
```

### Step 3: Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```
### Step 4 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv pw-env && source pw-env/bin/activate
```

### Step 5: Run and start to use it

You start the application by navigating to `llm_app` folder and running `main.py`:

```bash
python main.py
```

When the application runs successfully, you should see output something like this:


### Step 6: Run Streamlit UI for file upload

You can run the UI separately by navigating to `cd examples/ui` and running Streamlit app
`streamlit run app.py` command. It connects to the Discounts backend API automatically and you will see the UI frontend is running http://localhost:8501/ on a browser:


## Test the sample app


When the user uploads this file to the file uploader and asks questions:

```text
Tell me about high Blood pressure situation in India?
```

You will get the response as its expected on the UI.

```text
Based on the given data, the situation of diabetes in India can be summarized as follows:

High Blood Sugar in 15-49 year old women: The data value is 8.1%.
Women age 15-49 who reported that they have diabetes: The data value is 1.9% (equivalent to 6,827,000 women).
Women age 15-49 with diabetes who have sought treatment: The data value is 80.7% (equivalent to 289,981,000 women).

```

Credit: NutriGPT as the baseline developed by Animesh.
