"""
Example: How to call the bid-cars-scraper actor using Apify API Client

For full documentation of the Apify Client for Python, see: https://docs.apify.com/api/client/python
For full documentation of the actor, see: https://apify.com/lexis-solutions/bid-cars-scraper

Note: This example uses the Apify API Client (apify-client) to call actors from external code.
If you want to create Actors, use the Apify SDK (apify) instead:
https://docs.apify.com/sdk/python/docs/overview/introduction
"""

import os
from apify_client import ApifyClient


def run_actor():
    """Run the bid-cars-scraper actor and retrieve results."""
    # Initialize the ApifyClient with your API token
    # Get your API token from https://console.apify.com/account/integrations
    client = ApifyClient(token=os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

    # Start the actor run and wait for it to finish
    # The .call() method starts the actor and waits for completion automatically
    actor_id = "lexis-solutions/bid-cars-scraper"
    print(f"Starting actor: {actor_id}")

    run = client.actor(actor_id).call(
        run_input={
            "startUrls": [{"url":"https://bid.cars/en/search/results?search-type=filters&status=All&type=Automobile&make=All&model=All&year-from=1900&year-to=2026&auction-type=All&exterior-color=All"}],
            "maxItems": 100,
            "proxyConfiguration": {"useApifyProxy":True},
        }
    )

    # Get the dataset ID from the completed run
    dataset_id = run["defaultDatasetId"]
    print(f"Actor run completed! Dataset ID: {dataset_id}")

    # Get the results from the dataset
    dataset_items = client.dataset(dataset_id).list_items()
    items = dataset_items.items
    print(f"Retrieved {len(items)} items from the dataset.")
    print("Results:", items)
    return items


if __name__ == "__main__":
    run_actor()
