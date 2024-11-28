# Open WebUI Update Script

![Linux](https://img.shields.io/badge/Linux-Compatible-blue?logo=linux)  
![Bash](https://img.shields.io/badge/Script-Bash-yellow?logo=gnu-bash)  
![Docker](https://img.shields.io/badge/Docker-Required-blue?logo=docker)  
![Open WebUI](https://img.shields.io/badge/OpenWebUI-Compatible-brightgreen?logo=opensourceinitiative)

## Overview

This Linux command-line utility updates the Docker image for [Open WebUI](https://docs.openwebui.com/) and restarts the container. Open WebUI is an advanced, extensible front-end designed for interacting with inference servers like Ollama Inference Server and other LLM runners. It supports a wide range of AI-driven applications, from natural language processing to multi-modal inference.

The script simplifies the update process, ensuring you always have the latest features and improvements without manual configuration.

---

## Features

- **Automatic Docker Updates**: Pulls the latest Docker image for Open WebUI from the GitHub Container Registry.
- **Container Management**: Stops, removes, and restarts the Open WebUI container with the updated image.
- **Simplified Workflow**: Handles all necessary steps in one script, ensuring a smooth update process.
- **Detailed Logs**: Provides clear output at every step for easy debugging and verification.

---

## Usage

### Prerequisites
1. A Linux environment with:
   - **Docker** installed and running.
   - Access to pull images from Docker registries.
2. Permissions to execute Docker commands (e.g., part of the `docker` group).

### Run the Script & Example Output
```bash
./open-webui-update.bsh 
open-webui
open-webui
main: Pulling from open-webui/open-webui
2d429b9e73a6: Pull complete 
14dbff54af92: Pull complete 
71ba669986f7: Pull complete 
173289c0cbe5: Pull complete 
8d26e113c01f: Pull complete 
4f4fb700ef54: Pull complete 
871e11ec62a2: Pull complete 
61ae417586c7: Pull complete 
bbd9810c4d08: Pull complete 
eaaaa98c686c: Pull complete 
9bae6c909ed9: Pull complete 
a5ca31e679a9: Pull complete 
af1532e39986: Pull complete 
cf25bf840484: Pull complete 
a958349e5d71: Pull complete 
Digest: sha256:d5634a617860bbf2695136fe072bdb80fb008ace79e450052fa15c63f8693938
Status: Downloaded newer image for ghcr.io/open-webui/open-webui:main
ghcr.io/open-webui/open-webui:main
3c4686f26d8d9179778bc2b6171f2de6b2259e8c50d9cdfd8629d8647a963a71

```

---

## Installation Steps

1. **Download the Script**  
   Save the `open-webui-update.bsh` script to your local machine.

2. **Make It Executable**  
   ```bash
   chmod +x open-webui-update.bsh
   ```

3. **Run the Script**  
   Execute the script to update and restart the Open WebUI container:
   ```bash
   ./open-webui-update.bsh
   ```

---

## How It Works

1. **Image Update**:
   - Pulls the latest Docker image for Open WebUI from the GitHub Container Registry.
2. **Container Cleanup**:
   - Stops and removes the current Open WebUI container.
3. **Restart with Updated Image**:
   - Launches a new container using the updated image.
4. **Validation**:
   - Confirms the updated container is running and ready to use.

---

## Dependencies

- **Docker**: Required to manage containers and images.
- **Bash**: The script is written for Linux environments using Bash.

---

## About Open WebUI

Open WebUI is a highly versatile, self-hosted web interface for AI inference. It supports various models and servers, offering robust integration features, Markdown and LaTeX support, and a responsive design for desktop and mobile users.

### Key Features
- **Multi-Model Support**: Easily integrates with Ollama, OpenAI-compatible APIs, and other inference servers.
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Rich API Integration**: Expand functionality with custom plugins and APIs.
- **Secure and Flexible**: Granular permissions and customizable workflows for various user roles.

For more details, visit the [Open WebUI Documentation](https://docs.openwebui.com/).

---

## License

This project is licensed under the MIT License. See the full text of the license below:

---

MIT License

Copyright (c) 2024 George Knerr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
tion.

