# AUTO-ARCHIVE DATABASES <!-- omit from toc -->

Database hosts:

1. PostgreSQL: Supabase (PostgreSQL)
2. Pinecone (Vector)
3. Weaviate (Vector)
4. MongoDB (Graph)

---

- [Environment Variables](#environment-variables)
- [PostgreSQL Database: Supabase](#postgresql-database-supabase)
  - [Python Supabase Connection](#python-supabase-connection)
- [Vector Database: Pinecone](#vector-database-pinecone)
  - [Pinecone Connections](#pinecone-connections)
    - [Python Connection](#python-connection)
    - [Node.js Connection](#nodejs-connection)
  - [Pinecone Documentation](#pinecone-documentation)
- [Weaviate (Vector)](#weaviate-vector)
  - [Weaviate API Key](#weaviate-api-key)
  - [Weaviate cluster details](#weaviate-cluster-details)
  - [Weaviate Python connection](#weaviate-python-connection)
- [GraphQL Database: Atlas / MongoDB](#graphql-database-atlas--mongodb)
  - [GraphQL General Reference](#graphql-general-reference)
  - [Server-side connection](#server-side-connection)
  - [USERS](#users)

---

## Environment Variables

| Variable                  | Value                                                                       |
| ------------------------- | --------------------------------------------------------------------------- |
| PINECONE_PROJECT_NAME     | `Auto-Archive`                                                              |
| PINECONE_INDEX_NAME       | `clericus`                                                                  |
| PINECONE_API_KEY          | `fe660adb-82d4-441e-8ec6-460601941147`                                      |
| PINECONE_API_URL          | `https://clericus-112fceb.svc.us-west4-gcp-free.pinecone.io`                |
| PINECONE_ENV_NAME         | `us-west4-gcp-free`                                                         |
| ATLAS_ORG_ID              | `64e6d45cc801230d90dedfc1`                                                  |
| ATLAS_ORG_NAME            | `LegatusAI`                                                                 |
| ATLAS_PROJECT_ID          | `64e6d45cc801230d90dedfc7`                                                  |
| ATLAS_PROJECT_NAME        | `Auto-Archive`                                                              |
| ATLAS_PROJECT_API_PRIVATE | `rxtmhdhe`                                                                  |
| ATLAS_PROJECT_API_PUBLIC  | `d491e80a-2046-4c75-b8a6-4e7bc53d0042`                                      |
| ATLAS_DB_USERNAME         | `admin`                                                                     |
| ATLAS_DB_PASSWORD         | `hBxjaAu2tCPpWyPQ`                                                          |
| ATLAS_API_NAME            | `auto-archive`                                                              |
| ATLAS_API_KEY             | `ie6iCkJY6GmsR6K95Kt6Fp7eCMhYgeAvXfgmx2wDwZVjQqyDCMSaoEcg9WLjQb4m`          |
| ATLAS_API_URL             | `https://us-east4.gcp.data.mongodb-api.com/app/data-elgjy/endpoint/data/v1` |
| ATLAS_APP_ID              | `data-elgjy`                                                                |

## PostgreSQL Database: Supabase

### Python Supabase Connection

Supabase database credentials are already stored as environment variables. They are given in the code below.

```py
# Supabase database connection
def get_db_connection():
    db_name, db_user, db_password, db_host, db_port = get_supabase_credentials()

    for i in range(5):
        try:
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            logging.info("Successfully connected to the database")
            return conn
        except Exception as e:
            logging.error("Error while connecting to the database: " + str(e))
            if i < 5 - 1:  # i is zero indexed
                time.sleep(5)
                continue
            else:
                return None
```

---

## Vector Database: Pinecone

Pinecone database credentials and API key:

**Project:** `Auto-Archive`  
**Index:** `clericus`  
**URL Endpoint:** `https://clericus-112fceb.svc.us-west4-gcp-free.pinecone.io`

**API Authenthication:**

| Name      | Environment         | Value                                  |
| --------- | ------------------- | -------------------------------------- |
| `default` | `us-west4-gcp-free` | `fe660adb-82d4-441e-8ec6-460601941147` |

---

### Pinecone Connections

#### Python Connection

"Ready to get started with Pinecone? Copy the code below to set up your environment and establish a connection to your index."

```py
import pinecone

pinecone.init(
api_key='fe660adb-82d4-441e-8ec6-460601941147',
environment='us-west4-gcp-free'
)
index = pinecone.Index('clericus')
```

_See also:_ [**Pinecone Python Client Documentation**](https://docs.pinecone.io/docs/python-client).

---

#### Node.js Connection

"Copy the code below to set up your environment and establish a connection to your index."

```js
import { PineconeClient } from "@pinecone-database/pinecone";

const pinecone = new PineconeClient();
await pinecone.init({
  environment: "us-west4-gcp-free",
  apiKey: "fe660adb-82d4-441e-8ec6-460601941147",
});
const index = pinecone.Index("clericus");
```

---

### Pinecone Documentation

The following documentation covers the key concepts used in Pinecone:

**Pinecone Guides:**

- [Overview](https://docs.pinecone.io/docs/overview)
- [Quickstart](https://docs.pinecone.io/docs/quickstart)
- [Projects](https://docs.pinecone.io/docs/projects)
- [Indexes](https://docs.pinecone.io/docs/indexes)
- [Collections](https://docs.pinecone.io/docs/collections)

[**Pinecone API Reference**](https://docs.pinecone.io/reference/describe_index_stats_post)

---

## Weaviate (Vector)

API key, cluster details, and Python connection code for the Weaviate database cluster `clericus-lhzg3kty`:

### Weaviate API Key

| Variable           | API Key                                |
| ------------------ | -------------------------------------- |
| `WEAVIATE_API_KEY` | `fGhBeedV12MJaKWZM2bHZhnVnfZZNSob7E2R` |

### Weaviate cluster details

The following table has the details for the Weaviate cluster:

| Name             | Value                                        |
| ---------------- | -------------------------------------------- |
| Cluster name     | `clericus-ihzg3kty`                          |
| Cluster URL      | `https://clericus-ihzg3kty.weaviate.network` |
| Weaviate version | 1.21.1                                       |
| Authenthication  | Enabled                                      |
| Active modules   | 10                                           |
| Region           | `europe-west4`                               |

### Weaviate Python connection

```py
import weaviate

  auth_config = weaviate.AuthApiKey(api_key="WEAVIATE-API-KEY")

  client = weaviate.Client(
      url="https://clericus-ihzg3kty.weaviate.network",
      auth_client_secret=auth_config
  )
```

---

## GraphQL Database: Atlas / MongoDB

---

### GraphQL General Reference

Resources:

[**_Official GraphQL Website:_**](https://graphql.org/)

- [**Introduction to GraphQL**](https://graphql.org/learn/)
  - [**Queries & Mutations**](https://graphql.org/learn/queries/)
  - [**Schemas & Types**](https://graphql.org/learn/schema/)
  - [**Validation**](https://graphql.org/learn/validation/)
  - [**Execution**](https://graphql.org/learn/execution/)
  - [**Introspection**](https://graphql.org/learn/introspection/)
- [**GraphQL Best Practices**](https://graphql.org/learn/best-practices/)
  - [**Thinking in Graphs**](https://graphql.org/learn/thinking-in-graphs/)
  - [**Serving over HTTP**](https://graphql.org/learn/serving-over-http/)
  - [**Authorization**](https://graphql.org/learn/authorization/)
  - [**Pagination**](https://graphql.org/learn/pagination/)
  - [**Global Object Identification**](https://graphql.org/learn/global-object-identification/)
  - [**Caching**](https://graphql.org/learn/caching/)
- [**GraphQL FAQ**](https://graphql.org/faq/)

---

**Install MongoDB Python Driver:**

**Connection string:** `mongodb+srv://<username>:<password>@documents.i9f0heo.mongodb.net/?retryWrites=true&w=majority`

> _**NOTE:** Replace `<password>` with the password for the `<username>` user. Ensure any option params are [URL encoded](https://www.mongodb.com/docs/atlas/troubleshoot-connection/#special-characters-in-connection-string-password)._

**Full code sample with connection string:**

```py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<username>:<password>@documents.i9f0heo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

---

### Server-side connection

**API Key Name:** `auto-archive`  
**API Key:** `ie6iCkJY6GmsR6K95Kt6Fp7eCMhYgeAvXfgmx2wDwZVjQqyDCMSaoEcg9WLjQb4m`  
**URL endpoint:** `https://us-east4.gcp.data.mongodb-api.com/app/data-elgjy/endpoint/data/v1`

---

**Data Source:** `documents`  
**Provider/Region:** `GCP, Seoul (ASIA_NORTHEAST_3)`  
**Tier:** `MO`  
**Data API Access:** `Read & Write`

---

### USERS

Following table shows user data:

| Username | Password           | MongoDB Role(s)    |
| -------- | ------------------ | ------------------ |
| `admin`  | `hBxjaAu2tCPpWyPQ` | `atlasAdmin@admin` |

---

> [**MongoDB Documentation Home Page**](https://www.mongodb.com/docs/)
>
> - [**_Connect to MongoDB Database Deployment_**](https://www.mongodb.com/docs/atlas/connect-to-database-deployment/)
>   - [**_Connect via VS Code_**](https://www.mongodb.com/docs/atlas/mongodb-for-vscode/)
>   - [**_Connect via Your Application_**](https://www.mongodb.com/docs/atlas/driver-connection/)
> - [**_Connect to MongoDB Data Sources_**](https://www.mongodb.com/docs/atlas/app-services/mongodb/)
> - [**_Define a Data Model_**](https://www.mongodb.com/docs/atlas/app-services/data-model/)
> - [**_Schemas_**](https://www.mongodb.com/docs/atlas/app-services/schemas/)
>   - [**_Schema Types_**](https://www.mongodb.com/docs/atlas/app-services/schemas/types/)
> - [**_Relationships_**](https://www.mongodb.com/docs/atlas/app-services/schemas/relationships/)
> - [**_Values & Secrets_**](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)
> - [**_Interact with Your Data_**](https://www.mongodb.com/docs/atlas/atlas-ui/)
> - [**_Launch MongoDB Charts_**](https://www.mongodb.com/docs/charts/launch-charts/)
>   - [**_Chart Types_**](https://www.mongodb.com/docs/charts/chart-types/)
>
> **MongoDB Atlas (API):**
>
> - [**_Get Started wth Atlas_**](https://www.mongodb.com/docs/atlas/getting-started/)
> - [**_What is the Atlas CLI_**](https://www.mongodb.com/docs/atlas/cli/stable/)
> - [**_Install or Update the Atlas CLI_**](https://www.mongodb.com/docs/atlas/cli/stable/install-atlas-cli/)
> - [**_Configure Resource Tags_**](https://www.mongodb.com/docs/atlas/tags/#std-label-resource-tag-reqs)
>   - [**_Configure Database Deployment Tags_**](https://www.mongodb.com/docs/atlas/database-deployment-tags/#std-label-database-deployment-tags)
> - [**_Atlas GraphQL API_**](https://www.mongodb.com/docs/atlas/app-services/graphql/)
>   - [**_Authenticate GraphQL Requests_**](https://www.mongodb.com/docs/atlas/app-services/graphql/authenticate/)
>   - [**_GraphQL Types, Resolvers, & Operators_**](https://www.mongodb.com/docs/atlas/app-services/graphql/types-and-resolvers/)
> - [**_Atlas Data API_**](https://www.mongodb.com/docs/atlas/app-services/data-api/)
> - [**_Atlas Functions_**](https://www.mongodb.com/docs/atlas/app-services/functions/)
>   - [**_Query MongoDB Atlas_**](https://www.mongodb.com/docs/atlas/app-services/functions/mongodb/)
>   - [**_Context_**](https://www.mongodb.com/docs/atlas/app-services/functions/context/)  
>     &nbsp;

---

> &nbsp;  
> **NOTE:** "Your Data API key only gives you access to the Data API, not direct access to data in clusters. To prevent security breaches do not distribute it to untrusted individuals or embed directly in your client applications. [**Learn more about Data API keys.**](https://docs.atlas.mongodb.com/api/data-api/#create-data-api-key)"  
> &nbsp;

---

"Use this snippet with an existing database and collection to test out an API request right away. View the full API documentation in our [Docs](https://www.mongodb.com/docs/atlas/api/data-api/)."

**Python connection:**

```py
import requests
import json
url = "https://us-east4.gcp.data.mongodb-api.com/app/data-elgjy/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "sales",
    "database": "sample_supplies",
    "dataSource": "documents",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'ie6iCkJY6GmsR6K95Kt6Fp7eCMhYgeAvXfgmx2wDwZVjQqyDCMSaoEcg9WLjQb4m',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

---

> &nbsp;  
> **NOTE:** The [Atlas] API includes [automatically generated endpoints](https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/) that each represent a MongoDB operation. You can also define [custom HTTPS endpoints](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/) to create app-specific API routes that integrate with external services. Set custom access controls, enable authentication providers, create custom endpoints, and more for your Data API in the backend app already created for you in the App Services tab.  
> &nbsp;

---

🛑 **END OF DATABASE REFERENCE DOCUMENTATION** 🛑

---
