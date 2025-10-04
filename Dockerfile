# Multi-stage build for Prompts for Change
FROM python:3.9-alpine AS builder

# Install build dependencies
RUN apk add --no-cache gcc musl-dev

# Install Python dependencies
RUN pip install pyyaml

# Set working directory
WORKDIR /app

# Copy source files
COPY content/ ./content/
COPY scripts/ ./scripts/
COPY package.json ./
COPY index.html ./
COPY styles.css ./
COPY script.js ./

# Build the application
RUN python3 scripts/build_system.py

# Production stage
FROM nginx:alpine

# Install curl for healthcheck
RUN apk add --no-cache curl

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy built files from builder stage
COPY --from=builder /app/index.html .
COPY --from=builder /app/styles.css .
COPY --from=builder /app/script.js .
COPY --from=builder /app/posts_metadata.json .

# Using default nginx configuration

# Create necessary directories and set permissions
RUN mkdir -p /var/run /var/log/nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/run /var/log/nginx /var/cache/nginx /usr/share/nginx/html && \
    chmod -R 755 /var/run /var/log/nginx /var/cache/nginx /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]