# Auto-Archive Readme File

> ![Auto-Archive Logo-Banner](app/static/images/banner-650x100.png)
>
> ## 📜 Auto-Archive Project Documentation <!-- omit from toc -->
>
> **Program**: **`Auto-Archive`**  
> **Created by:** **`Joseph T. Antley`**  
> **Current:** **`v0.0.3-dev [🚧]`**  
> **Updated:** September 20, 2023

---

## Contents <!-- omit from toc -->

- [Auto-Archive Readme File](#auto-archive-readme-file)
  - [Project Summary](#project-summary)
    - [Architecture](#architecture)
      - [Backend](#backend)
      - [Frontend](#frontend)
    - [Clericus (AI Assistant)](#clericus-ai-assistant)
    - [Database Systems](#database-systems)
      - [Database Accounts](#database-accounts)
    - [Frontend Web App](#frontend-web-app)
    - [Backend Files](#backend-files)
      - [Directory Structure](#directory-structure)
        - [Folder/File Details](#folderfile-details)
      - [Database Structure](#database-structure)
    - [Env Variables](#env-variables)
  - [Version Roadmap](#version-roadmap)
    - [Active Development](#active-development)
      - [`v0.0.3`: _Clericus Update II_](#v003-clericus-update-ii)
    - [Planned Versions](#planned-versions)
      - [`v0.0.4`: _Web App Framework Update_](#v004-web-app-framework-update)
      - [`v0.0.5`: _Handwriting Update_](#v005-handwriting-update)
      - [`v0.0.6`: _Knowledge Graph (infrastructure) Update_](#v006-knowledge-graph-infrastructure-update)
      - [`v0.0.7`: _Knowledge Graph (backend) Update_](#v007-knowledge-graph-backend-update)
      - [`v0.0.8`: _Knowledge Graph (frontend) Update_](#v008-knowledge-graph-frontend-update)
      - [`v0.0.9`: _Historical Context Update_](#v009-historical-context-update)
      - [`v0.1.0`: _Beta Release!_](#v010-beta-release)
  - [Changelog](#changelog)
    - [`v0.0.3-dev` ⚙️](#v003-dev-️)
    - [`v0.0.25` Changelog](#v0025-changelog)
    - [`v0.0.2` Changelog](#v002-changelog)
      - [Version System Update](#version-system-update)
    - [`v0.0.19` Changelog](#v0019-changelog)
    - [`v0.0.18` Changelog](#v0018-changelog)
      - [Entity Functions](#entity-functions)
      - [Database Expansion](#database-expansion)
      - [`v0.0.18` Frontend](#v0018-frontend)
    - [`v0.0.17` Changelog](#v0017-changelog)
      - [Category Function](#category-function)
      - [`v0.0.17` Frontend](#v0017-frontend)
    - [`v0.0.16` Changelog](#v0016-changelog)
    - [`v0.0.1` Changelog](#v001-changelog)
  - [📌️ Miscellaneous](#️-miscellaneous)
    - [PromptLayer](#promptlayer)
    - [📈 Marketability](#-marketability)
  - [Dev Credit](#dev-credit)
    - [Tools](#tools)

&nbsp;

---

## Project Summary

<!-- no header bar -->

|                                                           |                                   |
| --------------------------------------------------------- | --------------------------------- |
| ![Auto-Archive Icon](app/static/images/favicon-48x48.ico) | Current Version: **`v0.0.3-dev`** |

**Auto-Archive** is a historical preservation and archival tool that revolutionizes the fields of historical preservation, archival research, and general historiography. Auto-Archive provides an innovative method that combines cutting-edge technologies to permanantly change historical digital preservation through automation and artificial intelligence (AI).

Auto-Archive provides a user-friendly web app where users can upload and process documents effortlessly, using Python for the program's core backend code and a Flask framework for the frontend web app. Auto-Archive leverages AI and natural language processing (NLP) to automate the digital preservation and archival process by automatically generating comprehensive profiles for uploaded historical documents. These archive profiles include titles, summaries, categories, extracted entities, and more. Document profiles are saved in the Auto-Archive database. Users can use the frontend web app to browse uploaded documents.

_In future versions:_ Users will be able to use interact with an AI assistant named 'Clericus' using the frontend web app. Clericus will have full access to the Auto-Archive database and full permissions, so users will be able to use Clericus to search, analyze, update, compare, etc.

---

### Architecture

> **NOTE (08/25/23):** `v0.0.25-dev` is currently in progress.
>
> 📡 **OpenAI API**: Auto-Archive uses OpenAI LLM for multiple functions, including document processing. As of `v0.0.25`, Auto-Archive uses the `gpt-3.5-turbo-16k` model.

---

#### Backend

The Auto-Archive backend is coded primarily in **🐍 Python** `3.11.4`. It consists of multiple modules and files which are detailed later in this documentation.

---

#### Frontend

**Document processing:** When users upload documents, Auto-Archive creates a `document profile` for the document using the program's document processor. As part of the `document profile`, the document processor:

- generates document profile title
- generates document summary
- categorizes document
- extracts entities from document
- saves full document text

Auto-Archive's document processor leverages the 📡 OpenAI API and the 📚 **`spaCy`** library for the NLP and entity-related functions.

---

### Clericus (AI Assistant)

> **NOTE (08/27/23):** `Clericus` is in **`Active Development`** as part of `v0.0.25-dev` and so is not currently live and/or functional.
>
> However, here are some brief libraries/tools/features planned for `Clericus`:  
> &nbsp;

🤖 **Clericus** is the name of the AI assistant and chatbot that will be included in Auto-Archive `>v0.0.25`. Since it is still in development, only a few details/tools used by Clericus is listed here:

- **LangChain**
- **OpenAI API**
  - LLM model: `gpt-3.5-turbo-16k`
  - Chat completions
  - Function calling

It is planned that Clericus will have full read and write access to the document database so that users can use Clericus as a tool to query documents.

---

### Database Systems

Through `v0.0.2-dev`, Auto-Archive exclusively used **`Supabase`**, a PostgreSQL **RDBMS** (Relational Database Management System).

As part of the project's development roadmap, Auto-Archive will transition to using one or more `NoSQL` databases: for example, a vector database (**`Pinecone`**), graph database (**`MongoDB`**), or both.

---

#### Database Accounts

> _**As of 08-23-2023**_ **(`v0.0.25-dev`):**

Auto-Archive has accounts and credentials for each of the following database hosts:

**RDBMS:**

- 🗄️💾 PostgreSQL database:
  - [**Supabase**](https://supabase.com/dashboard/projects)

**NoSQL:**

- 🗄️📈 Vector database:
  - [**Pinecone**](https://app.pinecone.io/)
- 🗄️🕸 Document/graph database:
  - [**MongoDB**](https://cloud.mongodb.com/)

> ---
>
> For all database credentials (API keys, user names, passwords, connection URLs, etc.), see the [**🌍️️🔐 Env Variables**](#env-variables) section of this readme file.

---

### Frontend Web App

> 🚧🔱 **Current Dev Version:** **`v0.0.25-dev`**

The Auto-Archive frontend is a 💻 **web application**. Auto-Archive uses **`Flask`** as the frontend web app framework. Following the current dev roadmap, **`Vue.js`** will replace **`Flask`** as the frontend framework for `v0.0.3`. The framework is used to create and connect the frontend web app and UI with the Auto-Archive backend.

As of `v0.0.2`, the frontend has two primary functions:

- upload documents
- browse document profiles

> **NOTE:** The `Clericus` chatbot module (see below) is currently in development and will be the third primary function of the frontend web app.

_The following applies to pre-`v0.0.3` versions of Auto-Archive._

> _**NOTE:** The web app can be accessed at [http://localhost:5000](http://localhost:5000)._

| Page Name         | Template                 | Navigation           | Description                                                                               |
| :---------------- | :----------------------- | :------------------- | :---------------------------------------------------------------------------------------- |
| base              | `base.html`              | _hidden_             | Flask "container" template used as the common structure for all other template pages      |
| Home              | `index.html`             | `/`                  | Users can navigate to the other main pages of the web interface from here.                |
| Upload Document   | `upload.html`            | `/upload`            | Users can upload a document to be auto-archived.                                          |
| Upload Successful | `upload_successful.html` | `/upload_successful` | Confirms to the user that the upload was a success.                                       |
| Archive           | `archive.html`           | `/archive`           | Users can browse all documents in the database. & interact with the Clericus AI Assistant |

Other important frontend files are the CSS spreadsheet (`app\static\css\style.css`) and static image and icon assets, including a banner-image, favicon, and logo/icon image.

---

### Backend Files

#### Directory Structure

> &nbsp;  
> **🚧 Update-in-progress for `v0.0.3`.**  
> **🚀 Updated for `v0.0.25`.**  
> &nbsp;

**🗃️ Note:** _Auto-Archive uses an hierarchical directory structure._

The project directory structure is explained below. Visual diagrams of the current structure are shown below and text explanations of each folder and their contents are then provided.

---

**Directory:** Visual Diagrams

**Auto-Archive directory structure (image):**

> 📌 NOTE: Previous image was for `v0.0.17` and the directory structure shown in the image diverged too much from the current `v0.0.3` structure.
>
> **An updated image diagram of the `v0.0.3` directory structure will be added soon.**

---

**Auto-Archive directory structure (ASCII):**

    root
    ├── _misc
    |   ├── _chatGPT_bard_etc
    |   ├── _clericus_dev
    |   ├── _custom_notebooks
    |   ├── _integrations_
    |   ├── _ref
    |   ├── _screenshots
    |   ├── htr_hwr
    |   ├── _ref
    |   ├── python_scripts
    |   └── openai_api_documentation.txt
    ├── app
    │   ├── static
    │   │   ├── css
    │   │   │   └── style.css
    │   │   ├── fonts
    │   │   ├── icons
    │   │   ├── images
    │   │   │   ├── stock
    │   │   │   ├── svg_files
    │   │   │   ├── banner-650x100.png
    │   │   │   ├── clericus_banner.png
    │   │   │   ├── favicon-16x16.png
    │   │   │   ├── favicon-32x32.png
    │   │   │   ├── favicon-48x48.ico
    │   │   │   ├── icon-192x192.png
    │   │   │   ├── icon-512x512.png
    │   │   │   └── icon-180x180.png
    │   ├── templates
    │   │   ├── archive.html
    │   │   ├── base.html
    │   │   ├── clericus.html
    │   │   ├── index.html
    │   │   ├── upload.html
    │   │   └── upload_successful.html
    │   ├── __init__.py
    │   └── routes.py
    ├── core
    │   ├── __init__.py
    │   ├── clericus.py
    │   ├── db_operations.py
    │   ├── document_processor.py
    │   └── logging_config.py
    ├── docs
    │   └── database
    |   |   ├── database_structure.md
    |   |   └── databases.md
    │   ├── doc_assets
    │   └── env_variables
    |   |   ├── env-variables.txt
    |   |   └── local_env_variables.txt
    │   ├── project_notebooks
    │   ├── test_documents
    │   ├── directory_structure.md
    ├── logs
    ├── uploads
    └── run.py
    └── requirements.txt
    └── readme.md

---

##### Folder/File Details

> &nbsp;  
> ⚠️ **The following sections have not been fully updated for `v0.0.3`.** ⚠️
>
> _The following directory structure explanation was last fully completed for `v0.0.2`. It has been tweaked, but not completed, up to `v0.0.3`._
>
> ---

**_Icon Key:_**

    📁 = directory folder
    🐍 = Python file (`.py`)
    📚 = Markdown file (`.md`)
    📓 = Jupyter notebook (`.ipynb`)
    📄 = Text file (`.txt`)
    🖼️ = Image file (`.ico`, `.jpg`, `.png`,`.svg`)
    💾 = Log file (`.log`)
    🌐 = HTML file (`.html`)
    💡 = CSS file (`.css`)

---

**The `root` directory contains the following folders and files:**

- 📁 `\\_misc`: This folder contains miscellaneous files, including custom notebooks, reference documentation, etc.
- 📁 `\\app`: This folder contains the files for the Auto-Archive web application frontend. It includes the `routes.py` file, the HTML files, the CSS stylesheet, and image assets.
- 📁 `\\core`: This folder contains Archive-AI's core functionality. It includes modules to perform the program's core functions.
- 📁 `\\docs`: This folder contains miscellaneous documents, including prompts and test upload documents.
- 📁 `\\logs`: This folder contains all log files to assist in debugging.
- 📁 `\\uploads`: Uploaded documents are placed here when processed
- 📚 `readme.md`: A file that describes the Auto-Archive program (a.k.a., the file you're reading now).
- 📄 `requirements.txt`: A file that lists the Python packages that Auto-Archive requires.
- 🐍 `run.py`: The main Python file that runs the Auto-Archive program.

**The `\\app` folder contains the following files and folders:**

- 📁 `\\static`: This folder contains static web app files for the frontend UI.
  - 📁 `\\css`
    - 💡 `style.css`
  - 📁 `\\images`
    - 📁 `\\_archived_images`
    - 📁 `\\stock_images`
    - 📁 `\\svg_files`
    - 🖼️ `banner-650x100.jpg`
    - 🖼️ `banner-650x100.png`
    - 🖼️ `clericus_banner.png`
    - 🖼️ `favicon-16x16.png`
    - 🖼️ `favicon-32x32.png`
    - 🖼️ `favicon-48x48.ico`
    - 🖼️ `icon-180x180.png`
    - 🖼️ `icon-192x192.png`
    - 🖼️ `icon-512x512.png`
    - 🖼️ `icon-720x720.jpg`
    - 🖼️ `icon-720x720.png`
    - 🖼️ `icon-3456x3456.png`
- 📁 `\\templates`: This folder contains the HTML files used to render the program's frontend web pages.
  - 🌐 `archive.html`
  - 🌐 `base.html`
  - 🌐 `index.html`
  - 🌐 `upload.html`
  - 🌐 `upload_successful.html`
- 🐍 `__init__.py`: An empty file that marks the app folder as a Python package.
- 🐍 `routes.py:` A file that defines the routes for the Auto-Archive web app.

**The `\\core` folder contains the following:**

- 🐍 `__init__.py`: An empty file that marks the core folder as a Python package.
- 🐍 `clericus.py`: Module containing the backend for the Clericus AI Assistant.
- 🐍 `db_operations.py`: Module containing database operations.
- 🐍 `document_processor.py`: Module containing all functions for processing documents after upload.
- 🐍 `log_config.py`: Module containing error logging configuration.

**The `\\docs` folder contains the following:**

- 📁 `\\doc_assets`: Contains images and any other assets used in local documentation files.
- 📁 `\\test_documents`: Contains a large sample of .txt files that are used to upload during development to test the program.
- 📚 `database_structure.md`: Current structure of the Cloud vector database hosted by Supabase.
- 📚 `directory_structure.md`: ASCII visual of the Auto-Archive program directory structure; it is also contained in this README file.
- 📄 `local_env_variables.txt`: List of environment variables for API keys, credentials, etc., for local machine

**The `\\logs` folder contains the following:**

- 💾 New `.log` file for each module for each session.

**The `\\uploads` folder:**

- 📄 Text file or Word document files are placed in this folder after document is processed

---

#### Database Structure

⏳ **SECTION INCOMPLETE -- COMING SOON** ⏳
&nbsp;

> **NOTE:** Auto-Archive versions before `v0.0.3-dev` used **Supabase** (PostgreSQL database provider) as the only project database. Supabase was used as a traditional relational database.
>
> One of the major tasks of `v0.0.3-dev` is to **integrate new database hosts and structures**.
>
> The current dev roadmap requires `v0.0.3` to create a new database and switch to a provider of one of the two following types of databases:
>
> - **Vector database** [Pinecone]
> - **Graph database** [MongoDB]
>
> Switching to either of these database types should allow for more context and provide more detail and functionality to knowledge graphs. (Knowledge graphs are planned to be implemented in later dev versions.)
>
> Since we are changing database providers and types in the near feature, this section will not be more detailed until work on `v0.0.3-dev` begins.  
> &nbsp;

---

### Env Variables

> 🌍️️🔐 _See the project's_ **`.env`** _file._

---

## Version Roadmap

Version updates are marked with one of these three:

> 🛠🔜 `⚙️ active development`  
> 🛠🔜 `📝 active planning`  
> 🛠🆕 `🚀 update complete`

---

### Active Development

| Main            | Dev                  |
| --------------- | -------------------- |
| **💾 `v0.0.2`** | **`⚙️ v0.0.25-dev`** |

---

`v0.0.2-dev` tasks:

> **NOTE: All variations of `v0.0.2` are focused on building the AI assistant. When the _backend_ of the Clericus AI/LLM is complete, `v0.0.25` will be complete.**
>
> **Any versions labelled between `v0.0.25` and `v0.0.3` will deal primarily with bug fixes and error resolutions.**

---

---

#### `v0.0.3`: _Clericus Update II_

`⚙️ active development 🛠`

🎯 **CLERICUS AI ASSISTANT IMPROVEMENT**

> **Task:** Improve `Clericus` with new features, tools, & abilities

1. Updating Clericus to incorporate the following libraries/APIs:
   - **OpenAI API**
     - **`gpt-3.5-turbo-16k` model**
     - **Function calling**
     - **Chat completions**
   - **LangChain**
     - Use: Tools, chain logic
   - **LlamaIndex**
     - Use: Enhance knowledge graph query & analytical functions

---

> **_ChatGPT-4 (08/23/2023):_**
>
> Steps to Complete the Goal:
>
> - Identify Core Functionalities: List the specific functionalities that Clericus needs to have, such as querying the database, text analysis, conversation handling, etc.
> - Select Libraries and Tools: Research and select the best libraries and tools for each functionality, including database interaction, natural language processing, and conversation management.
>
> - Design the Architecture: Create a high-level architecture of how Clericus will interact with the existing Auto-Archive system, including the database, document processing, and user interface.
> - Develop the Database Interaction Layer: Write the code to enable Clericus to query and interact with the Supabase database.
>
> - Integrate the LLM Model: Incorporate the gpt-3.5-turbo-16k model for natural language processing and conversation handling.
> - Implement Conversation Logic: Develop the conversation logic, including handling user queries, performing analysis, and managing the conversation flow.
> - Test and Optimize: Test Clericus with various scenarios and optimize for performance and user experience.
> - Document and Deploy: Write documentation for Clericus and deploy it as part of the Auto-Archive system.
>
> ---
>
> Step 1: Identify Core Functionalities
>
> We need to define the specific functionalities that Clericus will have. Here's a preliminary list, and please feel free to add, modify, or remove any items:
>
> - Query Database: Retrieve information from the Supabase database, such as document profiles, summaries, categories, etc.
> - Text Analysis: Analyze text as requested by the user, including summarization, categorization, entity extraction, etc.
> - Conversational Interface: Engage in natural language conversation with users, understanding queries, and providing responses.
> - Question & Answer System: Answer specific questions related to the archive, such as details about a particular document, statistics, trends, etc.
> - Integration with Auto-Archive: Seamless integration with the existing Auto-Archive system, including document upload, profile creation, and browsing.
> - User Assistance: Provide help and guidance to users in navigating the Auto-Archive system, including tutorials, tips, and troubleshooting.
> - Customizable Interactions: Allow users to customize their interaction with Clericus, such as preferred language, level of detail in responses, etc.
> - Security & Privacy: Ensure that interactions with Clericus are secure, and user data is handled with privacy in mind.

🎯 **NEW CLERICUS AI FRONTEND**

- Implement the frontend of Clericus AI chatbot into the new Vue/React web app framework
- Fully functioning with database access

NOTE: Reason for switching at this point is it they are preferable for more advanced dynamic features and it will be easier before the planned `v0.0.5` Knowledge Graph update [details below].

---

### Planned Versions

---

#### `v0.0.4`: _Web App Framework Update_

`📝 active planning`

🎯 **NEW FRONTEND FRAMEWORK & RECREATE WEB**

- Switch framework from Flask to **_Vue_** OR **_React_**
- Recreate the web app using the new frontend framework
  - Use the [**Storybook.js**](https://storybook.js.org/) tool if helpful
  - Use the [**Docusaurus 2.0**](https://docusaurus.io/) tool if helpful

**NOTE:** The reason for switching web app frameworks is that Vue or React are preferred over Flask for more advanced dynamic features, and it will be easier before the planned v0.0.4 Knowledge Graph update [details below].

---

#### `v0.0.5`: _Handwriting Update_

`📝 active planning`

🎯 **AUTO-OCR/HTR**

- Transkribus API
  - [Transkribus Processing API](https://transkribus.eu/processing/swagger/#/)
- Support image files
- Include as part of document processing

---

#### `v0.0.6`: _Knowledge Graph (infrastructure) Update_

`📝 active planning`

🎯 **KNOWLEDGE GRAPH INFRASTRUCTURE:**

- Replace relationship/entity/database system with knowledge graph system
- Switch from Supabase to truple database provider

---

#### `v0.0.7`: _Knowledge Graph (backend) Update_

`📝 active planning`

🎯 **KNOWLEDGE GRAPH BACKEND:**

- New functions to work with data from knowledge graphs instead of postgreSQL database.

---

#### `v0.0.8`: _Knowledge Graph (frontend) Update_

`📝 active planning`

🎯 **KNOWLEDGE GRAPH FRONTEND:**

- Update/create new functions to work with data from knowledge graphs instead of previous postgreSQL database.

---

#### `v0.0.9`: _Historical Context Update_

`📝 active planning`

🎯 **AI HISTORICAL CONTEXT ANALYSIS**

**Task:** Update Clericus LLM with improved historical context analysis abilities.

---

_Techniques to improve the historical context knowledge and analytical abilities of Clericus, by ChatGPT-4 [Code Interpreter] (08/22/2023):_

> &nbsp;  
> Improving the historical context analysis ability of the Auto-Archive AI Clericus agent can be achieved through several means. This enhancement would allow the system to better understand the temporal significance, origin, and relevance of the documents being processed.
>
> Here's a list of recommendations to consider:
>
> **1. Integrate a Specialized NLP Model for Historical Context:**
>
> - Train or use pre-trained models specifically focused on historical texts.
> - Include features to detect temporal expressions, historical events, and significant figures.
> - Integrate with existing databases or knowledge graphs of historical facts.
>
> **2. Utilize Temporal Embeddings:**
>
> - Apply temporal embeddings to capture time-related information in texts.
> - Consider using models that can understand chronological relationships between events.
> - Implement Historical Ontologies and Knowledge
>
> **3. Graphs:**
>
> - Build or integrate existing ontologies that capture historical concepts, relationships, and events.
> - Utilize knowledge graphs to provide context-aware insights and connections between historical entities.
>
> **4. Enhance Entity Recognition and Linking:**
>
> - Enhance entity recognition algorithms to identify and link historical figures, places, and events.
> - Connect recognized entities with existing databases or encyclopedias to provide in-depth context.
>
> **5. Incorporate Expert-Reviewed Content and Annotations:**
>
> - Collaborate with historians or subject matter experts to review and annotate data.
> - Include expert-curated content to provide authoritative insights and context.
>
> **6. Adaptive Learning from User Feedback:**
>
> - Implement feedback loop where users can correct or enhance the historical context.
> - Utilize user feedback for continuous model improvement and fine-tuning.
>
> **7. Cross-Referencing with Authoritative Sources:**
>
> - Create a mechanism to cross-reference information with authoritative historical databases or libraries.
> - Provide links to original sources or scholarly references to validate historical context.
>
> **8. Integrate Multilingual Support:**
>
> - Consider adding support for texts in different languages, as historical context can vary across cultures and regions.
> - Utilize translation services or multilingual models to handle documents in various languages.  
>   &nbsp;

---

#### `v0.1.0`: _Beta Release!_

`📝 active planning`

🎯 **AUTO-ARCHIVE -- BETA RELEASE**:

- Ensure program functions as intended
- Knowledge graphs displaying correctly
- Clericus AI working correctly
- No major bugs

---

`end of dev roadmap section`

---

## Changelog

---

👨‍💻 **Active Development:** `v0.0.3` 🚧

---

### `v0.0.3-dev` ⚙️

`⚙️ active development 🛠`

> _Dev for `v0.0.3` officially began on 08/29/23 after the new Clericus web app page was created._

**Goal for `v0.0.3-dev`:** Improved & Functioning Clericus AI Assistant

**9-20-2023:**

- Updated Clericus files (`clericus.py`, `clericus.html`, `routes.py`)
- Clericus conversational memory now functioning correctly

**9-21-2023:**

- Created `\static\js` folder
- Made Clericus frontend more modular by moving the JavaScript code on the `clericus.html` page to its own file (`\static\js\clericus.js`)

---

### `v0.0.25` Changelog

`🚀 update complete`

> 🚀 **`v0.0.25`** _completed August 29, 2023_ 🚀

---

> ![Clericus AI Chat Page (`v0.0.25`)](docs\doc_assets\clericus_frontend_v0.0.25-alpha.jpg "`clericus.html` page created for `v0.0.25`")
> Functioning `clericus.html` page created for `v0.0.25`.
>
> ---

**08/29/2023:**

- Created dedicated frontend page for the Clericus AI chatbot: `clericus.html` (see screenshot above)
- Frontend formatting of chat module
- Updated `routes.py` to integrate `clericus.html` web app page & connect with `clericus.py` backend file
- Updated `clericus.py` to create basic conversational AI for MVP
- Removed Clericus chatbot module from `archive.html` page

**08/27/2023:**

- `archive.html` chat module updates:
  - Changed font to `lexend` & imported from Google
  - Added spacing a light background colors to user and system messages in the chat window to make it more readable/easier to distinguish between user messages & Clericus messages
  - Updated JS so user input appears in the window immediately; for Clericus, it says `Clericus: Thinking...` (with animated ellipises) until the message is posted.
  - Updated JS so you can press "enter" to send user input instead of having to click the "Send" button
- Decided to create a dedicated web app page for the Clericus chatbot to make development less complex and less likely to disturb the archive page.

**08/26/2023:**

- Created `log_config.py` file in `\\core` folder
- Updated other project files so all log configuration occurs in the new `log_config.py` file.
- Worked on getting Clericus functional without much luck. Started over with creating the `clericus.py` backend from scratch.
- Goal accomplished: functioning conversational chatbot module on the archive page.
  - Created functioning `clericus.py`
  - Routes added to `routes.py`
  - Updated chatbot JavaScript on `archive.html`

**08/25/2023:**

- Moved formal `clericus.py` file to `\\core` folder
- Moved all main `v0.0.2` files to new `_backup` folder
- Expanded Clericus code to be more conversational (w/ ChatGPT-4)
- Added Pinecone database connections (w/ Bard)

**08/24/2023:**

- Created template `clericius.py` file [`clericus-v0.0.25-dev]
- Created database accounts for Pinecone (vector) & MongoDB (GraphQL)

---

### `v0.0.2` Changelog

`🚀 update complete`

    🚀 `v0.0.2` completed August 23, 2023 🚀

---

📝 **Updated Documentation:**

- 📑 **Update readme file**
- 🗃️ **Improve organization** of all documentation & directory files.
- ✒️ **Note ALL changes/updates** to any part of the program/project documentation.

#### Version System Update

> _The Auto-Archive development versioning system was updated on 08/16/2023 to better follow the Semantic Versioning standard._

The update to the versioning system is simple and should not result in any confusion this early in development. The only changes to the versioning system are:

1. Push the version number forward by one decimal ("0.2.0" becomes "0.0.2")
2. Remove decimal between `v` and the version number ("v0.0.2" instead of "v.0.0.2")

The following table shows the original Auto-Archive version syntax compared with the new syntax that follows the Semantic Versioning standard.

| Old       | New       |
| --------- | --------- |
| `v0.0.1`  | `v0.0.1`  |
| `v.0.1.5` | `v0.0.15` |
| `v.0.2.0` | `v0.0.2`  |

---

> **⭐️ NOTE:** Updating the new versioning syntax across the project is _in-progress_, but previous version styles may still be encounted in some files, documentation, etc. If the old syntax is encountered, the conversion is simple, and users can refer to the above table.

---

**"Subversion" System:**

Sometimes version numbers are extended during development when there are multiple 'versions' of the same file(s) in development that stem from the same primary version. The purpose of subversioning is to keep strict track of progress and changes during active development.

The "subversion" syntax may appear in different ways in project files and documentation.

The following table shows examples of how file subversion syntax may appear. Note that the subversion syntax is not as strict as the primary version number.

| Version  | Subversion        |
| -------- | ----------------- |
| `v0.0.2` | `v0.0.2.0823`     |
| `v0.0.2` | `v0.0.2.0823:1`   |
| `v0.0.2` | `v0.0.2.0823:2`   |
| `v0.0.2` | `v0.0.2:0823`     |
| `v0.0.2` | `v0.0.2[:0823]`   |
| `v0.0.2` | `v0.0.2-0823`     |
| `v0.0.2` | `v0.0.2.dev.0823` |
| `v0.0.2` | `v0.0.2-dev.0823` |

Subversion syntax is not strict since it is usually used much more temporarily than standard versioning. The primary purpose of adding a subversion number is to distinguish between different dev-versions of project files that stem from the same version.

The only rule for adding a subversion number is that the number should either be the month/year (MMYY) or date (MMDDYY). For example, both `v0.0.2.0823` and `v0.0.2.081923` would be acceptable. If the full date is given as part of the subversion, it is assumed that is the date when that stem of `v0.0.2` began.

---

### `v0.0.19` Changelog

`🚀 update complete`

    🚀 `v0.0.19` completed August 11, 2023 🚀

- created clericus.py module with chatbot functions
- reworked layout of Archive Page to have the page split vertically and the Clericus chat module take up the right 30% of the archive.html viewport
- Clericus Chat Module added to archive.html page
- routes.py file split from run.py file
- Clericus routes added to routes.py
- Archive Profiles have a "Download full text" button instead of displaying full text
- Archive Profile entities listed horizontally in a table structure
- profile summaries truncated to max 30 words on default page; full summary is shown in profile modal window

---

### `v0.0.18` Changelog

`🚀 update complete`

    🚀 `v0.0.18` completed August 4, 2023 🚀

#### Entity Functions

Basic entity-related functions were added to `v0.0.18`. The new functions use the **`spaCy`** library to extract & classify entities from documents.

After extraction & classification, entities and their relationship with the document are stored in the database (see below).

#### Database Expansion

The database architecture was updated for `v0.0.18` to incorporate entity-data from new functions. Two new tables were added to the database: `entities` & `profile_entities`.

The `entities` table is a list of unique entities extracted from documents. Each entitiy has a unique `entity_id`. When saving entities to the database, the program checks the `entities` table to see if the `entity` already exists. If not, it adds the entity table. If the entity is already listed, the program notes the `entity_id` to use in the `profile_entities` table.

The `profile_entities` table is a junction table used for the one-to-many relationships between documents and extracted entities. The table has three columns: `profile_entity_id`, `profile_id`, & `entity_id`.

---

#### `v0.0.18` Frontend

`v0.0.18` features major updates to the "Archive" (`archive.html`) page. Archive profiles are now listed in a table structure with a "View Profile" button for each.

The "View Profile" button opens the "Profile" -- a modal window showing all of the documents' stored information, including extracted entities. See screenshots below.

**Archive page - default layout:**

![Archive Page (`v0.0.18`)](docs\doc_assets\archive-page-v018.jpg)

**Archive page - profile window:**

![Profile Modal Window -- Archive Page (`v0.0.18`)](docs\doc_assets\profile-modal-window-v018.jpg)

---

### `v0.0.17` Changelog

`🚀 update complete`

    🚀 `v0.0.17` completed: August 2, 2023 🚀

**8/2/2023**:

- changed database credentials to environmental variables
- split database operations from `run.py` into new file: `core/db_operations.py`
- split logging operations/configurations into new file: `core/logging_config.py`
- added embedding functions for summarization & categorization NLP functions
- updated database to store embeddings
- fixed minor bugs

**8/1/2023:**

- added first version of NLP category classification function
- built new database architecture
- updated `archive.html` frontend

&nbsp;

---

#### Category Function

The `v0.0.17` update included a new`classify_document` function using embeddings. Here is a summarization of the `v0.0.17` function by ChatGPT-4 [Code Interpreter] (08/02/2023):

> &nbsp;  
> This code assumes that the `generate_embedding` function creates embeddings for a given text, and `calculate_similarity` computes the cosine similarity between two embeddings, which is a common measure for text embedding similarity.
>
> The logic of the `classify_document` function is as follows:
>
> 1. For each document category, it generates an embedding for the representative prompt text.
> 2. It calculates the cosine similarity between the document's embedding and each category's embedding.
> 3. It assigns the document to the category with the highest cosine similarity score, provided that the score is above a certain threshold. If no score is above the threshold, it assigns the document to the "Other" category.  
>    &nbsp;

---

#### `v0.0.17` Frontend

`🚀 update complete`

Updates to the Archive page (`archive.html`):

- fixed page functionality
- document list restructured as a sortable table

I reformatted the "Upload Successful" page slightly (`upload_successful.html`) to make it more simple/functional/user-friendly. See the screenshot below.

!["Upload Successful" Page (v0.0.17) -- 08/02/2023](docs\doc_assets\upload_successful-v017.jpg)

---

### `v0.0.16` Changelog

`🚀 update complete`

    🚀 `v0.0.16` completed July 31, 2023 🚀

The following features/changes were part of the `v0.0.16` update:

1. **Confirmed OpenAI API** used correctly.
2. **Added a _"Successful Upload"_ page (`upload_successful.html`)**: Users are redirected to this page after successfully uploading a file. Page should have text saying upload was successful and large buttons for "Upload another document" and "Browse the archive".
3. **Updated "Archive" page (`archive.html`)**: Add an "Upload a Document" button (`upload.html`) to the right side of the "Back to Home" button.
4. **Updated "Upload" page (`upload.html`)**: add "Back to Home" and "Browse Database" buttons that mirror Archive page
5. **Increased the token limit**: Increase the amount of text that the program can process. If the file's text is still too long, notify the user that their file is too long instead of hitting an error. Token segmentation implemented for texts longer than the 4096 token limit.
6. **More accurate titles & summaries for long texts:** The program now generates relatively accurate titles and summaries for longer texts that require token segmentation.
7. **More specific title instructions:** Document titles will always be complete thoughts and not contain quotation marks.
8. **New `document_processor.py` module:** The `document_processor` functions have been removed from the main `run.py` file and are now located in a new `document_processor.py` module file. The `run.py` file pulls the `document_processor.py` code when it needs it. The new `document_processor.py` file is located in the `/core` folder.
9. **Image Assets:** Favicon, icon/logo, and banner image assets are now included in the program's frontend web interface, and the HTML files have been updated to incorporate them into the new layout.

&nbsp;

---

`🚀 update complete`

### `v0.0.1` Changelog

The stable version of `v0.0.1` included the following basic features:

- Users can upload text documents
- Automatic generation of document title and summary generation
- Automatic archival of document text and data in vector database as "Archive Profiles"
- Web interface frontend where users can upload documents and view the database's Archive Profiles

&nbsp;

---

> &nbsp;  
> 👷 **NOTE:** The following sections are under construction & have not been fully updated for `v0.0.2`. 👷  
> &nbsp;

---

## 📌️ Miscellaneous

### PromptLayer

> 📅 **08/26/2023:** Created `PromptLayer` account while creating Clericus assistant.

```py
import promptlayer

promptlayer.api_key = "pl_2730caed02c60579edcde4c9e5582e62"
```

PromptLayer documentation links:

- [**PromptLayer: Quickstart**](https://docs.promptlayer.com/quickstart)
- [**PromptLayer: Getting Started (Tutorial)**](https://docs.promptlayer.com/getting_started)
- [**PromptLayer: Python**](https://docs.promptlayer.com/languages/python)
- [**PromptLayer: JavaScript**](https://docs.promptlayer.com/languages/javascript)
- [**PromptLayer: LangChain**](https://docs.promptlayer.com/languages/langchain)
- [**PromptLayer: REST API**](https://docs.promptlayer.com/languages/rest-api)
- [**PromptLayer Features: Tagging Requests**](https://docs.promptlayer.com/features/prompt-history/tagging-requests)
- [**PromptLayer Features: Sharing Prompts**](https://docs.promptlayer.com/features/prompt-history/sharing-prompts)
- [**PromptLayer Features: Prompt Registry**](https://docs.promptlayer.com/features/prompt-registry)
- [**PromptLayer Reference: REST API**](https://docs.promptlayer.com/reference/rest-api-reference)
  - [**`POST` Track Request**](https://docs.promptlayer.com/reference/track-request)
  - [**`GET` Get Prompt Template**](https://docs.promptlayer.com/reference/get-prompt-template)
  - [**`POST` Publish Prompt Template**](https://docs.promptlayer.com/reference/publish-prompt-template)
  - [**`POST` Track Score**](https://docs.promptlayer.com/reference/track-score)
  - [**`POST` Track Prompt**](https://docs.promptlayer.com/reference/track-prompt)
  - [**`POST` Track Metadata**](https://docs.promptlayer.com/reference/track-metadata)
  - [**`GET` Get Prompt Templates**](https://docs.promptlayer.com/reference/get-prompts)

---

**08/16/2023:**

> Updated the dev versioning system to better follow [Semantic Versioning](https://semver.org/)standards. Details about the update are given in the `v0.0.2` changelog section above.
> &nbsp;

### 📈 Marketability

**08/18/2023:**

> To eventually market Auto-Archive, decision was made to **pivot Auto-Archive's purpose & functions completely for historical records**. Modern business documents are easier to OCR and extract data, but the market is saturated with competition, including from major companies like Microsoft and IBM. By optimizing Auto-Archive completely as a way to document and preserve historical records, we target a small niche, but it provides the greatest chance of profitability for the program.

**🚀 PLANNED AUTO-ARCHIVE DIFFERENTIATORS:**

- ✍️ Automatic & accurate HTR/HWR
- 🤖 AI Assistant and expert archivist, preservationist, historian, & analyst
- **📜 Advanced historical context analysis**

---

## Dev Credit

### Tools

The following tools, platforms, etc. were used during the Archive-AI development:

- Bard (Google)
- ChatGPT (OpenAI)
- Flask
- Supabase
- Visual Studio Code
- GitHub Copilot

&nbsp;

---

&nbsp;

> ## 🛑 **End of Auto-Archive Documentation** 🛑
>
> ### [⬆️ Return to Top ⬆️](#auto-archive-readme-file) <!-- omit from toc -->
>
> &nbsp;  
> ![Auto-Archive Logo-Banner](app/static/images/banner-650x100.png)

&nbsp;

---
