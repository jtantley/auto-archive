> # 📜 Auto-Archive Project Documentation
>
> **Program**: **`Auto-Archive`**  
> **Created by:** **`Joseph T. Antley`**  
> **Current:** **`v0.0.3-dev [🚧]`**  

---

## Project Summary

**Auto-Archive** is a historical preservation and archival tool that revolutionizes the fields of historical preservation, archival research, and general historiography. Auto-Archive provides an innovative method that combines cutting-edge technologies to permanently change historical digital preservation through automation and artificial intelligence (AI).

Auto-Archive provides a user-friendly web app where users can upload and process documents effortlessly, using Python for the program's core backend code and a Flask framework for the frontend web app. Auto-Archive leverages AI and natural language processing (NLP) to automate the digital preservation and archival process by automatically generating comprehensive profiles for uploaded historical documents. These archive profiles include titles, summaries, categories, extracted entities, and more. Document profiles are saved in the Auto-Archive database. Users can use the frontend web app to browse uploaded documents.

_In future versions:_ Users can interact with an AI assistant named 'Clericus' using the frontend web app. Clericus will have full access to the Auto-Archive database and full permissions, so users can use Clericus to search, analyze, update, compare, etc.

---

## Architecture

### Backend

The Auto-Archive backend is coded primarily with **🐍 Python** `3.11.4`. It consists of multiple modules and files.

---

### Frontend

Auto-Archive uses a Flask web app as its frontend interface.

#### Document processing

When users upload documents, Auto-Archive creates a `document profile` for the document using the program's document processor. As part of the `document profile`, the document processor:

- generates document profile title
- generates document summary
- categorizes document
- extracts entities from document
- saves full document text

Auto-Archive's document processor leverages the 📡 OpenAI API and the 📚 **`spaCy`** library for NLP and entity-related functions. As of `v0.0.3-dev`, Auto-Archive uses `gpt-3.5-turbo-16k`.

---

## Clericus (AI Assistant)

> **NOTE (09/21/23):** `Clericus` is in **`Active Development`** as part of `v0.0.3-dev` and so is not currently live. However, here are some brief libraries/tools/features planned for `Clericus`:  
> &nbsp;

🤖 **Clericus** is the name of the AI assistant and chatbot included with Auto-Archive. Since it is still in development, only a few details/tools related to Clericus'a development are listed here:

- **OpenAI API**
  - LLM model: `gpt-3.5-turbo-16k`
  - Chat completions
  - Function calling
    - Internet search function
- **LangChain** (possibly)

It is planned that Clericus will have full read-and-write access to all databases so that users can use Clericus as a tool to query documents.

---

> &nbsp;
> _🚧 More coming soon 🚧_  
> &nbsp;

---
