from typing import Any, Dict, Optional, Sequence, Union
from datetime import datetime, timedelta
import json
import pandas as pd
import requests
from sqlalchemy import create_engine
from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

class LandInvToPostgresOperator(BaseOperator):
    def __init__(
        self,
        host: str,
        port: str,
        password: str,
        db: str,
        user: str,
        api_token: str,
        api_url: str = "https://data.cityofchicago.org/resource/",
        file_name: str = "chicago_land_inv",  # Define a default file name
        endpoint: str = "aksk-kvfp.json", #Default Endpoint
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.user = user
        self.api_url = api_url
        self.api_token = api_token
        self.file_name = file_name
        self.endpoint = endpoint

    def execute(self, context: Dict[str, Any]) -> None:
        # download it using requests via into a tempfile a pandas df
        with tempfile.TemporaryDirectory() as tmpdirname:
            api_url = self.api_url + self.endpoint
            self.log.info(f"API url is: {self.api_url}")

            limit = 100000
            offset = 0
            params = {
                '$limit': limit,
                '$offset': offset,
                
            }

            # Define the headers with the X-App-Token header
            headers = {
                'X-App-Token': self.api_token,
            }
            # Make a GET request to the API with the headers and parameters
            response = requests.get(api_url, headers=headers, params=params)

            df = pd.DataFrame()

            while True:
                # Make a GET request to the API with the headers and parameters
                response = requests.get(api_url, headers=headers, params=params)

                # Check the response status code
                if response.status_code == 200:
                    data = response.json()
                    df1 = pd.DataFrame(data)
                    df = pd.concat([df,df1],ignore_index=True)
                    self.log.info(f"Dataframe currently has {df.shape[0]} columns")


                    # If the number of results received is less than the limit, you've reached the end
                    if len(data) < limit:
                        break

                    # Increment the offset for the next page
                    offset += limit
                else:
                    self.log.info(f"Request failed with status code: {response.status_code}")
                    break
            post_con = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
            print(post_con)
            engine = create_engine(post_con)
            engine.connect()
            df.to_sql(name=self.file_name, con=engine, index=False, if_exists="replace")
            self.log.info("Table successfully loaded")

