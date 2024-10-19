from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from rag_system import RAGSystem
from fastapi.responses import JSONResponse
from Backend.rag_system import RAGSystem


# Initialize the FastAPI app
app = FastAPI()

# Serve static files (HTML, CSS, JS) from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the RAG system (for processing queries and generating results)
rag_system = RAGSystem()

# Define a class for handling query requests
class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def handle_query(request: QueryRequest):
    try:
        # Process the query using the RAG system
        result = rag_system.process_query(request.query)
        return {"result": result}
    except Exception as e:
        # Handle any errors during processing
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/chart/{column_name}")
async def get_chart(column_name: str):
    try:
        # Generate a bar chart for the specified column
        chart_json = rag_system.create_bar_chart(column_name)
        return JSONResponse(content=chart_json, media_type="application/json")
    except Exception as e:
        # Handle any errors during chart creation
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    # Simple root route to test if FastAPI is running
    return {"message": "Welcome to the RAG-powered survey analysis tool!"}
