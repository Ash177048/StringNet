# StringNet 🔐

A lightweight, encrypted communication system where access is controlled by a shared string. Messages are AES-encrypted using the string as a key and routed through a simple relay server.

## Features
- Temporary, untraceable channels using a shared string
- AES-256-CBC encryption with per-message IV
- Stateless, blind relay server
- Minimal setup (Python only)

## Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
