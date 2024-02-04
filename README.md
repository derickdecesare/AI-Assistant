# AI Assistant Using OpenAI API

This repository contains the code for an AI Assistant that leverages OpenAI's API. The assistant can perform tasks such as speech-to-text, text generation, and text-to-speech. This project is intended to be connected to a Raspberry Pi for microphone input.

# Getting Started

These instructions will get your copy of the project up and running on your local machine.

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

#### Clone the repository

bash or powershell - in your terminal

```
git clone [URL to your repository]
cd [repository name]
```

#### Set up a Python virtual environment

Create a virtual environment:
bash or windows ( linux or mac or windows )

```
python3 -m venv venv
```

Activate the virtual environment:
Windows:

```
.\\venv\\Scripts\\activate
```

macOS/Linux:

```
source venv/bin/activate
```

Install required packages

```
pip install -r requirements.txt
```

### Usage

#### Initialize the OpenAI client

#### Set up .env file

- Create a .env file in the root of the directory
- Add our OpenAI API key

```
OPENAI_API_KEY=your-api-key-here
```
