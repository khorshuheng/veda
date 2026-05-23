FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Install Git LFS for repositories that enforce LFS hooks.
RUN apt-get update
RUN apt-get install -y --no-install-recommends git-lfs \
    && rm -rf /var/lib/apt/lists/*

# Install uv globally for dependency and environment management.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && mv /root/.local/bin/uv /usr/local/bin/uv \
    && chmod +x /usr/local/bin/uv