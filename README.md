# Media Campaign Analysis

A FastAPI-based backend service for managing and analyzing media ad campaigns.  
Designed to track campaigns, ad sets, and ad performance metrics such as impressions, clicks, CTR, and conversions. Built to integrate with platforms like Meta Ads, providing actionable insights for campaign optimization.

## Features

- **Campaign Management**: Create, update, and delete campaigns, ad sets, and ads.
- **Performance Metrics**: Track impressions, clicks, CTR, CPC, and conversion rates.
- **Analytics API**: Generate aggregated reports by campaign, date, or ad set.
- **User Authentication**: JWT-based authentication for secure access.
- **MongoDB Integration**: Stores campaigns, ads, and analytics data.
- **CI/CD Ready**: Linting, testing, Docker build, and deployment pipelines using GitHub Actions.

## Tech Stack

- **Backend**: FastAPI  
- **Database**: MongoDB  
- **Auth**: JWT (JSON Web Tokens)  
- **Testing**: Pytest + HTTPX  
- **Containerization**: Docker & Docker Compose  
- **CI/CD**: GitHub Actions

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/spartan3108-py/media-campaign-analysis
   cd media-campaign-analysis
