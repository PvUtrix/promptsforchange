# Server Configuration Guide

## Issue: JSON files not loading in production

The app works locally but fails in production because the server is configured for SPA (Single Page Application) routing, which redirects all requests to `index.html`.

## Solutions

### 1. Nginx Configuration (Recommended)

The `nginx.conf` file has been updated to properly serve JSON files:

```nginx
# Serve JSON files directly
location ~* \.json$ {
    expires 1h;
    add_header Cache-Control "public";
    try_files $uri =404;
}
```

### 2. Apache Configuration

Use the provided `.htaccess` file for Apache servers.

### 3. Other Server Solutions

#### For Netlify
Add `_redirects` file:
```
/posts_metadata.json /posts_metadata.json 200
/* /index.html 200
```

#### For Vercel
Add `vercel.json`:
```json
{
  "rewrites": [
    {
      "source": "/posts_metadata.json",
      "destination": "/posts_metadata.json"
    },
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

#### For GitHub Pages
Add `_redirects` file in the root directory.

## Testing

Use the `test-json.html` file to test if JSON files are accessible:
1. Open `test-json.html` in your browser
2. Check the console for any errors
3. The page should show "✅ JSON loaded successfully!"

## Debug Steps

1. Check if `posts_metadata.json` exists in the production directory
2. Test direct access: `https://yourdomain.com/posts_metadata.json`
3. Check server logs for any routing issues
4. Verify MIME type is `application/json`

## Common Issues

- **SPA routing**: Server redirects all requests to `index.html`
- **Missing files**: JSON file not uploaded to production
- **MIME type**: Server not serving JSON with correct content type
- **Caching**: Browser cache serving old HTML instead of JSON
