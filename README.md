# Rag
# RAG-Powered Survey Analysis Tool

This project implements a survey analysis tool powered by Retrieval-Augmented Generation (RAG). It allows users to query datasets and visualize the results through a simple web interface.

## Project Structure

- **Backend**: Contains the FastAPI application that handles queries and processes data using RAG.
- **Frontend**: Contains the static files for the web interface (HTML, CSS, JavaScript).
- **Data**: Folder for storing datasets used for querying.

## Features

- Query datasets and get insights in response to user queries.
- Visualize dataset columns with bar charts using Plotly.

## Setup

### Requirements

The following Python packages are required:

- fastapi
- uvicorn
- pydantic
- pandas
- plotly

You can install the required packages using:

```bash
pip install -r requirements.txt
