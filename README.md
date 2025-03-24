# Prometheus Pusher

Prometheus Pusher is a minimal yet powerful Python library that enables you to automatically push Prometheus metrics from your application to a Pushgateway. It is ideal for short-lived jobs, multi-worker systems, and services where the pull-based Prometheus model is not practical.

## 🚀 Features

- 🔄 Periodically pushes metrics to Prometheus Pushgateway.
- 🧠 Supports custom CollectorRegistry and any Prometheus metrics.
- 🧩 Compatible with any Python framework (FastAPI, Flask, Celery, CLI scripts, etc.).
- 🏷 Automatically adds unique worker_id (UUID) and instance hostname.
- 🛠 Simple and extensible interface.

## Installation

You can install library via pip:

```bash
pip install git+https://github.com/mykyta-ishchenko/prometheus-pusher.git
```

You can install library via poetry:

```bash
poetry add git+https://github.com/mykyta-ishchenko/prometheus-pusher.git
```
