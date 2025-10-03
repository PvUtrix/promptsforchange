# 🚀 Deployment Guide

This guide covers various deployment options for the Prompts for Change Telegram Mini App.

## 📋 Prerequisites

- Git repository with your code
- Domain name (optional, for custom domain)
- Hosting service account (GitHub, Netlify, Vercel, etc.)

## 🌐 Deployment Options

### 1. GitHub Pages (Free)

**Steps:**
1. Push your code to a GitHub repository
2. Go to repository Settings → Pages
3. Select source: "Deploy from a branch"
4. Choose branch: `main`
5. Set folder: `/ (root)`
6. Save and wait for deployment

**URL:** `https://yourusername.github.io/repository-name`

**Pros:**
- Free hosting
- Automatic SSL
- Easy setup
- Version control integration

**Cons:**
- Limited to static sites
- No server-side processing

### 2. Netlify (Free Tier Available)

**Steps:**
1. Connect your GitHub repository to Netlify
2. Set build command: `echo "No build required"`
3. Set publish directory: `/`
4. Deploy

**URL:** `https://your-app-name.netlify.app`

**Pros:**
- Free tier available
- Automatic deployments
- Custom domains
- Form handling
- Serverless functions

**Cons:**
- Limited build minutes on free tier

### 3. Vercel (Free Tier Available)

**Steps:**
1. Import your repository to Vercel
2. Set framework preset to "Other"
3. Deploy

**URL:** `https://your-app-name.vercel.app`

**Pros:**
- Excellent performance
- Automatic deployments
- Custom domains
- Serverless functions
- Edge functions

**Cons:**
- Limited bandwidth on free tier

### 4. Coolify (Self-Hosted)

**Steps:**
1. Set up Coolify instance
2. Create new application
3. Connect Git repository
4. Configure Docker settings
5. Deploy

**URL:** `https://your-domain.com`

**Pros:**
- Full control
- No vendor lock-in
- Custom configurations
- Cost-effective for multiple projects

**Cons:**
- Requires server management
- Initial setup complexity

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
# Use nginx as base image for serving static files
FROM nginx:alpine

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy all static files to nginx html directory
COPY index.html .
COPY styles.css .
COPY script.js .

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create a non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

# Change ownership of the html directory
RUN chown -R nextjs:nodejs /usr/share/nginx/html && \
    chown -R nextjs:nodejs /var/cache/nginx && \
    chown -R nextjs:nodejs /var/log/nginx && \
    chown -R nextjs:nodejs /etc/nginx/conf.d

# Switch to non-root user
USER nextjs

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
```

### Build and Run
```bash
# Build the Docker image
docker build -t prompts-for-change .

# Run the container
docker run -p 80:80 prompts-for-change
```

### Docker Compose
```yaml
version: '3.8'
services:
  prompts-for-change:
    build: .
    ports:
      - "80:80"
    restart: unless-stopped
    environment:
      - NODE_ENV=production
```

## 🔧 Configuration Files

### nginx.conf
```nginx
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    sendfile        on;
    keepalive_timeout  65;
    
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;
    
    server {
        listen       80;
        server_name  localhost;
        
        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
            try_files $uri $uri/ /index.html;
        }
        
        location /health {
            access_log off;
            return 200 "healthy\n";
            add_header Content-Type text/plain;
        }
        
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

## 🌍 Domain Setup

### Custom Domain Configuration

1. **DNS Settings:**
   ```
   Type: CNAME
   Name: www
   Value: your-hosting-provider.com
   
   Type: A
   Name: @
   Value: your-hosting-provider-ip
   ```

2. **SSL Certificate:**
   - Most hosting providers offer automatic SSL
   - Let's Encrypt for self-hosted solutions
   - Cloudflare for additional security

3. **Redirects:**
   - Redirect HTTP to HTTPS
   - Redirect www to non-www (or vice versa)
   - Set up proper canonical URLs

## 📊 Performance Optimization

### Static File Optimization
- Enable gzip compression
- Set proper cache headers
- Optimize images and assets
- Use CDN for global distribution

### Security Headers
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
```

## 🔍 Monitoring and Analytics

### Health Checks
- Set up health check endpoints
- Monitor response times
- Track error rates
- Set up alerts

### Analytics
- Google Analytics
- Plausible Analytics
- Fathom Analytics
- Custom analytics solution

## 🚨 Troubleshooting

### Common Issues

1. **Build Failures:**
   - Check file permissions
   - Verify all required files are present
   - Review build logs

2. **Runtime Issues:**
   - Check server logs
   - Verify nginx configuration
   - Test health endpoints

3. **SSL Issues:**
   - Verify certificate installation
   - Check domain configuration
   - Test SSL configuration

### Debug Commands
```bash
# Check container status
docker ps
docker logs container-name

# Test nginx configuration
nginx -t

# Check health endpoint
curl -f http://localhost/health
```

## 📈 Scaling Considerations

### Horizontal Scaling
- Load balancers
- Multiple server instances
- Database clustering
- CDN implementation

### Vertical Scaling
- Increase server resources
- Optimize application performance
- Database optimization
- Caching strategies

## 🔄 CI/CD Pipeline

### GitHub Actions
```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Netlify
      uses: nwtgck/actions-netlify@v1.2
      with:
        publish-dir: '.'
        production-branch: main
        github-token: ${{ secrets.GITHUB_TOKEN }}
        deploy-message: "Deploy from GitHub Actions"
```

## 📞 Support

### Deployment Issues
- Check hosting provider documentation
- Review server logs
- Test locally first
- Verify configuration files

### Performance Issues
- Use browser dev tools
- Check network tab
- Monitor server resources
- Optimize assets

---

**Need help?** Check the [main README](../README.md) or open an issue on GitHub.
