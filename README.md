# Bid.cars Vehicle Auction Scraper

![Bid.cars Scraper](https://i.ibb.co/mr1wYksR/bid-cars-cover.png)

This Apify actor allows you to scrape vehicle auction data from bid.cars, a leading online vehicle auction platform. Extract comprehensive vehicle information including specifications, pricing, damage details, images, and auction status — perfect for automotive market research and vehicle valuation analysis.

<p align="center">
  <img src="https://apify-image-uploads-prod.s3.us-east-1.amazonaws.com/DevbkY3adMTBuoECt-actor-AhLmShew3GgNjSDt0-RSvtguxFDp-icon_copy.jpg" alt="Bid.cars Scraper" style="height: 60px; margin-right: 15px;" /><a href="https://apify.com/lexis-solutions/bid-cars-scraper" target="_blank">
    <img src="https://img.shields.io/badge/Try%20it%20on-Apify-0066FF?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDA4IiBoZWlnaHQ9IjQwOCIgdmlld0JveD0iMCAwIDQwOCA0MDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8zNDFfNDE1NykiPgo8cGF0aCBkPSJNMjE4LjY5NSAxMDRIMzAwLjk3QzMwMi42NDMgMTA0IDMwNCAxMDUuMzU3IDMwNCAxMDcuMDNWMjMyLjc2NkMzMDQgMjM1Ljc3OCAzMDAuMDgzIDIzNi45NDUgMjk4LjQzNCAyMzQuNDI1TDIxNi4xNTkgMTA4LjY5QzIxNC44NDEgMTA2LjY3NCAyMTYuMjg3IDEwNCAyMTguNjk1IDEwNFoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xODkuMzA1IDEwNEgxMDcuMDNDMTA1LjM1NyAxMDQgMTA0IDEwNS4zNTcgMTA0IDEwNy4wM1YyMzIuNzY2QzEwNCAyMzUuNzc4IDEwNy45MTcgMjM2Ljk0NSAxMDkuNTY2IDIzNC40MjVMMTkxLjg0IDEwOC42OUMxOTMuMTU5IDEwNi42NzQgMTkxLjcxMyAxMDQgMTg5LjMwNSAxMDRaIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNMjAyLjU5MSAyMDQuNjY4TDEwOS4xMjcgMjk4LjgzNUMxMDcuMjI5IDMwMC43NDcgMTA4LjU4MyAzMDQgMTExLjI3OCAzMDRIMjk2LjhDMjk5LjQ4MyAzMDQgMzAwLjg0MiAzMDAuNzcgMjk4Ljk2NyAyOTguODUyTDIwNi45MDggMjA0LjY4NUMyMDUuNzI2IDIwMy40NzUgMjAzLjc4MiAyMDMuNDY4IDIwMi41OTEgMjA0LjY2OFoiIGZpbGw9IndoaXRlIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMzQxXzQxNTciPgo8cmVjdCB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwNCAxMDQpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==&logoColor=white" alt="Try it on Apify" style="border-radius: 12px; height: 60px;" />
  </a>
</p>


---


## 📊 Actor Stats

| Stat | Value |
|------|-------|
| **Version** | `0.0.3` |
| **Last Update** | Nov 30, 2025 |

---


## 🚀 Key Features

- 🔎 Scrape listings from bid.cars search pages or individual vehicle pages
- 🚗 Extract detailed vehicle information (VIN, specs, damage, pricing)
- 📍 Location-based filtering across auction sites
- 💰 Comprehensive pricing data (prebid, estimates, final bids)
- 📄 Structured vehicle data extraction with 40+ fields
- 🌐 Proxy support for stable, anonymous scraping
- ⚙️ Anti-bot protection bypass
- 🖼️ Vehicle image and media URLs extraction
- 📊 Pagination support for large result sets

---

## ❓ Why Use This Actor

- ✅ Automate vehicle auction data collection
- ✅ Save hours of manual browsing and copying from bid.cars
- ✅ Build datasets for automotive market analysis and price tracking
- ✅ Monitor vehicle availability and pricing trends
- ✅ Integrate data into automotive platforms and tools
- ✅ Research vehicle values and auction performance

---

## 👥 Who Is This Actor Suitable For?

- 🚗 Auto dealers and auction buyers
- 📈 Automotive market researchers and analysts
- 🧠 Data scientists studying vehicle markets
- 🧰 Developers building automotive platforms
- 📚 Academic researchers studying auction markets
- 💼 Insurance companies and vehicle appraisers

---

## 📥 Input Schema

The actor accepts the following input parameters:

```json
{
  "startUrls": [
    {
      "url": "https://bid.cars/en/search/results?status=All&type=Automobile&make=All&model=All&year-from=1900&year-to=2026&auction-type=All&exterior-color=All&search-type=filters"
    },
    {
      "url": "https://bid.cars/en/lot/0-43058842/2018-Mazda-CX-5-JM3KFBCM2J0358047"
    }
  ],
  "maxItems": 100,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
```

### Input Parameters

- **startUrls** (required): Array of bid.cars search or detail URLs to scrape
- **maxItems** (optional): Maximum number of vehicles to scrape (default: 100)
- **proxyConfiguration** (optional): Proxy settings for anonymous scraping

---

## 📤 Output Schema

Each scraped vehicle returns the following structured data:

```json
{
  "lot": "0-42695247",
  "vin": "JTEBU5JR2H5453392",
  "name": "2017 Toyota 4runner, Trd Pro",
  "nameShort": "2017 Toyota 4runner, Trd Pro",
  "year": "2017",
  "make": "Toyota",
  "model": "4runner, Trd Pro",
  "tag": "2017-Toyota-4runner-JTEBU5JR2H5453392",
  "location": "Orlando (FL)",
  "odometer": 999999,
  "odometerUnit": "miles",
  "lossType": "Collision",
  "primaryDamage": "All over",
  "startCode": "Stationary",
  "seller": "Non-insurance C...",
  "sellerLong": "Non-insurance Company",
  "prebidPrice": "$425",
  "finalBid": null,
  "estimatedMin": 9880,
  "estimatedMax": 15990,
  "timeLeft": "0",
  "timeLeftFormatted": "0",
  "prebidCloseTime": "Wed 10 Sep, 15:30 GMT+2",
  "status": 2,
  "searchStatus": "live",
  "saleDocument": "Rebuildable",
  "saleDocumentExternal": "REBUILDABLE (Florida) - SALVAGE",
  "titleHasLien": false,
  "transmission": "Manual",
  "fuelType": "0",
  "driveType": "AWD",
  "engine": "4.0L, V6, 270HP",
  "keyInfo": "Missing",
  "hasVideo": false,
  "has360View": false,
  "videoUrl": null,
  "view360Url": null,
  "images": [
    "https://images.bid.cars/042695247_68c14101e5c52/2017-Toyota-4runner-JTEBU5JR2H5453392-1.jpg?ver=1527"
  ],
  "imagesLarge": [
    "https://pluto.bid.car/0-42695247/2017-Toyota-4runner-JTEBU5JR2H5453392-1.jpg?ver=1527"
  ],
  "detailUrl": "https://bid.cars/en/lot/2017-Toyota-4runner-JTEBU5JR2H5453392",
  "scrapedAt": "2025-09-10T13:27:18.513Z"
}
```

---

## 🌍 Looking for more Vehicle data?

| Scraper                                                                | Country       | Description                                                                                   |
| ---------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------- |
| [OTOMOTO Scraper](https://apify.com/lexis-solutions/otomoto)           | Poland        | Extract car listings, prices, and specs from one of Poland's largest automotive marketplaces. |
| [CarGurus.com Scraper](https://apify.com/lexis-solutions/cargurus-com) | United States | Collect vehicle data from CarGurus, including detailed specs, prices, and dealer info.        |
| [Carfax.com Scraper](https://apify.com/lexis-solutions/carfax-com)     | United States | Retrieve used car listings with history reports, pricing, and seller details from Carfax.     |

Explore these solutions to expand your data collection capabilities across automotive and auction websites.

---

👀 p.s.

Got feedback or need an extension?

Lexis Solutions is a [certified Apify Partner](https://apify.com/partners/find). We can help you with custom solutions or data extraction projects.

Contact us over [Email](mailto:scraping@lexis.solutions) or [LinkedIn](https://www.linkedin.com/company/lexis-solutions)

## Support Our Work 💝

If you're happy with our work and scrapers, you're welcome to leave us a company review [here](https://apify.com/partners/find/lexis-solutions/review) and leave a review for the scrapers you're subscribed to. It will take you less than a minute but it will mean a lot to us!
