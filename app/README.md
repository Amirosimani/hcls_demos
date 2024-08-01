# GenAI HCLS usecases

## Run the Streamlit app locally
- create a virutal env `python3 -m venv .venv`
- activate the env `source .venv/bin/activate`
- install requirments `pip install -r requirments.txt`
- **local secret management**: `.streamlit/secrets.toml` for local runs. make sure you add it to `.gitignore`
- run the app:
 - export PROJECT_ID=$(gcloud info --format='value(config.project)')
 - `streamlit run ./app/🏠_Home.py`

## Deploy on Cloud Run
- In cloud shell or a terminal with gcloud cli installed and configured: 
 ```
 export PROJECT_ID=$(gcloud info --format='value(config.project)')
 gcloud builds submit --tag gcr.io/${PROJECT_ID}/<NAME>  
gcloud run deploy <NAME> --image gcr.io/${PROJECT_ID}/<NAME> --allow-unauthenticated --region=us-central1
```

### Neo4j local
docker run \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    neo4j:5.13.0