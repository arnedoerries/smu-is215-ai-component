# Kinokuniya Character Archetype Book Recommendation Service

### Disclaimers
> **First Disclaimer:** This repository is part of a university course project and represents a proof of concept for a character archetype book recommendation service as part of a proposed digital transformation strategy for Singapore-based bookstore Kinokuniya. We are in no direct association with Kinokunyia.

> **Second Disclaimer:** This microservice is a proof of concept, not a production-ready implementation. It seeks to demonstrate the application of a classifier neural network and corresponding user and data features to a unique book recommendation feature. A production-ready version would require diversifying the classifier across more character archetype labels and investing more time and resources into a quality training data set based on real user and book data.

> **Core Assumption:** This microservice assumes there is a way for Kinokuniya to digitally and automatically scrape a newly published book for characters and snippets of corresponding character descriptions from that book. In this proof of concept, we generated training data synthetically with LLMs such as ChatGPT and Claude.

### Context
- **University:** Singapore Management University
- **Course:** IS215 Digital Business
- **Professor:** Prof. Dr. Fiona Fui-Hoon Nah
- **Semester:** 2025/2026 Term 2
- **Group:** 8
- **Group members:** Arne, Carmen, Joshua, Megan, Mikhail, Shi Hui

### How to run the service
1. Clone the repository locally and open with IDE of choice
2. Optional but recommended: set up a local virtual environment and activate it
3. Install all required packages (in the virtual environment)
4. Open the terminal and run `fastapi dev` to start the service
5. Once the fastapi server is running, check the terminal output for a line that says `Documentation at http://127.0.0.1:8000/docs` and open the page
6. View the fastapi overview of the api endpoints and familiarize yourself with the required inputs
7. Use a local api endpoint testing tool like Postman to send requests to the service