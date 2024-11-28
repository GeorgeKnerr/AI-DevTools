
# Ollama Update Script

![Linux](https://img.shields.io/badge/Linux-Compatible-blue?logo=linux)  
![Bash](https://img.shields.io/badge/Script-Bash-yellow?logo=gnu-bash)  
![GPU Support](https://img.shields.io/badge/GPU-Supported-brightgreen?logo=nvidia)  
![Systemd](https://img.shields.io/badge/Systemd-Enabled-orange?logo=systemd)

## Overview

This is a Linux command-line utility for updating the [Ollama Inference Server](https://ollama.ai/) to the latest version. Ollama is a highly efficient server designed for hosting and serving large language models, optimized for multi-modal AI applications.

The script ensures seamless updates, manages dependencies, configures environment variables, and restarts the Ollama service. It supports NVIDIA GPUs for high-performance inference workloads.

---

## Features

- **Automatic Version Check**: Identifies the currently installed version of Ollama.
- **Latest Version Installation**: Downloads and installs the latest release.
- **GPU Support**: Configures GPU compatibility for NVIDIA CUDA or other supported libraries.
- **Service Management**: Automatically creates, enables, and starts a systemd service for Ollama.
- **Environment Updates**: Updates system environment variables as needed.
- **Comprehensive Logs**: Provides detailed output at every step for transparency.

---

## Usage

### Prerequisites
1. A Linux environment with:
   - **Systemd** installed and enabled.
   - **curl** for downloading the latest release.
2. Root or sudo access to perform system updates and configurations.

### Run the Script & Example Output
```bash
$ ./ollama-update.bsh 

Checking ollama's current version:
ollama version is 0.4.0

Downloading and installing latest ollama:
>>> Installing ollama to /usr/local
>>> Downloading Linux amd64 bundle
######################################################################## 100.0%
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
>>> NVIDIA GPU installed.

Checking ollama's current version:
ollama version is 0.4.6

Backing up the original service file...

Updating the Environment variable...

Reloading systemd daemon...

Restarting ollama.service...

Checking status of ollama.service...
● ollama.service - Ollama Service
     Loaded: loaded (/etc/systemd/system/ollama.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-11-28 11:12:39 EST; 1s ago
   Main PID: 8569 (ollama)
      Tasks: 13 (limit: 76932)
     Memory: 77.3M
        CPU: 571ms
     CGroup: /system.slice/ollama.service
             └─8569 /usr/local/bin/ollama serve

Nov 28 11:12:39 aiops1 systemd[1]: Started Ollama Service.
Nov 28 11:12:39 aiops1 ollama[8569]: 2024/11/28 11:12:39 routes.go:1197: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VE…0.0.0.0:11434 OL
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.540-05:00 level=INFO source=images.go:753 msg="total blobs: 174"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.541-05:00 level=INFO source=images.go:760 msg="total unused blobs removed: 0"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.541-05:00 level=INFO source=routes.go:1248 msg="Listening on 0.0.0.0:11434 (version 0.4.6)"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.542-05:00 level=INFO source=common.go:135 msg="extracting embedded files" dir=/tmp/ollama1073380129/runners
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.580-05:00 level=INFO source=common.go:49 msg="Dynamic LLM libraries" runners="[cpu_avx2 cuda_v11 cuda_v12 rocm cpu cpu_avx]"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.580-05:00 level=INFO source=gpu.go:221 msg="looking for compatible GPUs"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.913-05:00 level=INFO source=types.go:123 msg="inference compute" id=GPU-134a539b-011f-dcc0-6bb2-c884e4153fdf library=cuda…lable="23.2 GiB"
Nov 28 11:12:39 aiops1 ollama[8569]: time=2024-11-28T11:12:39.913-05:00 level=INFO source=types.go:123 msg="inference compute" id=GPU-ddaf2138-5143-912f-552f-10338f991930 library=cuda…lable="23.2 GiB"
Hint: Some lines were ellipsized, use -l to show in full.

Environment variable update complete.

Restarting ollama.service that servies the api:

Checking if ollama server is running on 0.0.0.0:14365
tcp        0      0 0.0.0.0:11434           0.0.0.0:*               LISTEN      8616/ollama         

ollama update complete.
```

---

## Installation Steps

1. **Download the Script**
   Save the `ollama-update.bsh` script to your local machine.

2. **Make It Executable**
   ```bash
   chmod +x ollama-update.bsh
   ```

3. **Run the Script**
   Execute the script as a superuser to ensure it can modify system files:
   ```bash
   sudo ./ollama-update.bsh
   ```

---

## How It Works

1. **Version Check**: Uses the `ollama version` command to identify the current version.
2. **Download Latest Release**: Fetches the latest Linux amd64 bundle from Ollama's servers.
3. **Configure System**:
   - Adds users to necessary groups (e.g., `render`, `video`, `ollama`).
   - Updates system environment variables.
   - Configures and restarts the Ollama systemd service.
4. **Validation**:
   - Ensures the service is running.
   - Confirms the server is listening on the appropriate port.

---

## Dependencies

- **curl**: For downloading files.
- **Systemd**: For service management.
- **NVIDIA GPU Drivers** (optional): To leverage GPU acceleration.

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