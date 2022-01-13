
# crypto-quotes
Dockerized microservice that pulls BTC/USD prices and saves them to a database which can be accessed later.

*Stack: Docker, Django, Redis, Nginx, Celery, Postgres*

To run the application:
```
1. make build
2. make up
```
More make commands defined in the `Makefile` for easy access to shell and logs to each container.

---
**API Endpoints:**

The API endpoints are protected and can only be accessed by passing an `api-token` header in the request, which nginx handles. The value for the token is: `I0sC0eb50q`. Please find the postman collection for the below two requests [here](https://github.com/mythxn/crypto-quotes/blob/main/postman-collection.json).

---

From our database, the below endpoint returns the last BTCUSD price fetched.
```
GET /api/v1/quotes
```
*Sample Response*

```
[
    {
        "model": "myapp.exchangerate",
        "pk": 1,
        "fields": {
            "exchange_rate": 43669.99,
            "last_refreshed": "2022-01-13T05:48:01Z"
        }
    },
    {
        "model": "myapp.exchangerate",
        "pk": 2,
        "fields": {
            "exchange_rate": 43669.99,
            "last_refreshed": "2022-01-13T05:48:01Z"
        }
    },
    {
        "model": "myapp.exchangerate",
        "pk": 3,
        "fields": {
            "exchange_rate": 43669.99,
            "last_refreshed": "2022-01-13T05:48:01Z"
        }
    },
    ...
]
```
---
Below endpoint sends a request to AlphaVantage to retrieve the current BTCUSD exchange rate and saves the rate into the database.
```
POST /api/v1/quotes
```
*Sample Response*

```
[
    {
        "model": "myapp.exchangerate",
        "pk": 20,
        "fields": {
            "exchange_rate": "43818.25000000",
            "last_refreshed": "2022-01-13T13:45:01"
        }
    }
]
```
---
**Automated Tasks**

Additionally, *django-celery-beat* was used to set up an automated task that would check AlphaVantage for the current price and save it into our database every **hour**.

---
**Environment Variables**

AlphaVantage API keys and other secrets are passed into the container as environment secrets and used by the container, which is configured in the docker-compose file.
