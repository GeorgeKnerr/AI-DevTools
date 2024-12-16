# 🛠️ AI-DevTools Repository 

**AI-DevTools** is a collection of powerful administrative and developer tools tailored to streamline workflows in AI-driven environments. From updating inference servers to managing advanced AI front-ends, this repository provides solutions to save time and optimize performance for AI applications.

---


## 🎯 Purpose
This repository simplifies routine tasks in AI environments, ensuring your tools are always up-to-date and configured for maximum efficiency. It is ideal for administrators, developers, and AI enthusiasts working with large language models and multi-modal inference solutions.

---

## 🚀 Get Started
1. Clone this repository:  
   ```bash
   git clone https://github.com/<your-username>/AI-DevTools.git
   ```
2. Navigate to the desired subdirectory.
3. Follow the instructions in the relevant `README.md` to use the scripts.

Feel free to contribute to this repository by submitting issues or pull requests. Let's build smarter AI environments together!

---

## 📂 Directory Overview

### 🔄 [Ollama Server Updater for Linux](./ollama-server-updater-linux)
A Linux command-line utility for seamlessly updating the **Ollama Inference Server** to its latest version. 

- **Ollama** is an efficient server for hosting and serving large language models, optimized for multi-modal AI applications.
- **Key Features**:
  - Manages dependencies.
  - Configures environment variables.
  - Restarts the Ollama service for uninterrupted operations.
  - Supports NVIDIA GPUs for high-performance inference.

**[Learn More](./ollama-server-updater-linux/README.md)**

---

### 🔄 [Open WebUI Updater for Linux](./open-webui-updater-linux)
A Linux command-line utility for keeping the **Open WebUI** Docker container up-to-date.

- **Open WebUI** is a versatile front-end for interacting with inference servers, including Ollama and other LLM runners.
- **Key Features**:
  - Updates the Docker image for the latest features.
  - Simplifies container restart and configuration.
  - Supports a wide range of AI-driven applications, from NLP to multi-modal inference.

**[Learn More](./open-webui-updater-linux/README.md)**

---

### 🔄 ngrok URL and Twilio Webhook Updater
A Python utility for automating the exposure of local services to the internet using ngrok and updating Twilio webhooks dynamically.

This script simplifies development by integrating ngrok and Twilio seamlessly, ensuring your local services are reachable for testing.
Key Features:

Automatically starts and manages an ngrok tunnel.
Fetches the public ngrok URL for HTTPS access.
Updates Twilio webhooks for SMS and Voice functionality.
Retry mechanism for reliable URL retrieval.

**[Learn More](./ngrok-url-twilio-webhook-updater/README.md)**

## 🏷️ Keywords
AI tools, large language models, multi-modal inference, Ollama Inference Server, Open WebUI, Docker automation, NVIDIA GPU, developer productivity, administrative scripts, Linux utilities, twilio, ngrok
