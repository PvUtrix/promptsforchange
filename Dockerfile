# Use nginx as base image for serving static files
FROM nginx:alpine

# Install curl for healthcheck
RUN apk add --no-cache curl

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy all static files to nginx html directory
COPY index.html .
COPY styles.css .
COPY script.js .
COPY README.md .

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create necessary directories and set permissions
RUN mkdir -p /var/run /var/log/nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/run /var/log/nginx /var/cache/nginx /usr/share/nginx/html && \
    chmod -R 755 /var/run /var/log/nginx /var/cache/nginx /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
