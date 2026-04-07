Multimodal RAG for Automotive Manufacturing Assistant

## Project Overview

This project implements a Multimodal Retrieval-Augmented Generation (RAG) system tailored for automotive manufacturing assistance. It allows users to ingest PDF documents containing text, tables, and images, index them using vector embeddings, and query the system with natural language questions to receive context-aware answers grounded in the documents.

## Features

- **Multimodal Document Ingestion**: Extracts text, tables, and images from PDF files.
- **Vector-Based Retrieval**: Uses FAISS and HuggingFace embeddings for efficient similarity search.
- **LLM-Powered Generation**: Generates answers using a lightweight language model.
- **RESTful API**: Built with FastAPI for easy integration.
- **Source Attribution**: Provides page numbers and content types for transparency.

## Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd multimodal-rag-automotive
   ```

2. Install dependencies:

   ```bash
   pip install fastapi uvicorn langchain langchain-community langchain-huggingface faiss-cpu transformers pillow pymupdf openai python-dotenv
   ```

3. Set up environment variables:

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

2. Ingest a PDF document:

   Use the `/ingest` endpoint to upload a PDF file.

3. Query the system:

   Use the `/query` endpoint with a natural language question.

### API Endpoints

- `GET /health`: Check if the service is running.
- `POST /ingest`: Upload and process a PDF file.
- `POST /query`: Ask a question and get an answer with sources.

## Architecture

The system consists of the following components:

- **Ingestion**: Parses PDFs to extract text, tables, and images.
- **Vector Store**: Indexes content using FAISS.
- **Retrieval**: Performs similarity search on queries.
- **Models**: Uses LLMs for answer generation and vision models for image description.

## Requirements

- Python 3.8+
- OpenAI API key for image processing

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

Problem Statement

In modern automobile manufacturing environments, engineers and maintenance teams rely heavily on a wide range of technical documents such as machine manuals, standard operating procedures (SOPs), fault diagnostic guides, and equipment datasheets. These documents are typically distributed in PDF format and contain a mixture of unstructured text, structured tables, and complex engineering diagrams. Despite the availability of such documentation, extracting actionable insights in real time remains a significant challenge on the shop floor.

The primary domain of this problem is automobile manufacturing, particularly within production lines involving conveyors, programmable logic controllers (PLCs), drives such as Siemens G120, and robotic assembly systems. Engineers frequently encounter situations where machines generate fault codes (e.g., F7801), abnormal behaviors, or unexpected stoppages. Resolving these issues requires searching through extensive manuals, cross-referencing tables, and interpreting diagrams, which is both time-consuming and error-prone.

The challenge is further compounded by the multimodal nature of these documents. Critical information is often embedded in tables (e.g., parameter ranges, torque specifications), while root cause explanations may be described in textual paragraphs. Additionally, wiring diagrams and process flow images provide essential context that cannot be captured through text alone. Traditional keyword-based search systems fail to retrieve relevant information across these modalities effectively, especially when queries are phrased in natural language.

This problem is distinct from generic document question-answering systems due to several domain-specific complexities. First, the terminology used in manufacturing is highly specialized, involving technical jargon related to automation systems, drives, and industrial communication protocols. Second, the presence of structured tables requires semantic understanding beyond simple text matching. Third, engineering diagrams demand visual interpretation to extract meaningful insights. Finally, the consequences of incorrect information can lead to production downtime, safety risks, and financial losses, making accuracy and grounding critical.

A Retrieval-Augmented Generation (RAG) approach is particularly well-suited to address this problem. Unlike fine-tuned models that require extensive labeled data and frequent retraining, RAG systems dynamically retrieve relevant information from a knowledge base at query time. This ensures that responses are grounded in actual documents and remain up-to-date as new manuals or SOPs are added. Furthermore, RAG enables the integration of multimodal data by converting images into textual summaries using vision-language models, allowing them to be indexed alongside text and tables.

The proposed system ingests multimodal PDF documents, extracts and processes text, tables, and images, and builds a unified vector-based index. When a user submits a natural language query, the system retrieves the most relevant chunks across all modalities and generates a context-aware response using a language model. The system also provides source references, including page numbers and content types, ensuring transparency and traceability.

A successful implementation enables engineers to quickly diagnose machine faults, understand parameter settings, and interpret technical diagrams without manually navigating lengthy documents. It reduces troubleshooting time, improves operational efficiency, and democratizes access to critical knowledge across the organization.