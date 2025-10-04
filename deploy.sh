#!/bin/bash

# Deployment script for Prompts for Change
echo "🚀 Deploying Prompts for Change..."

# Check if posts_metadata.json exists
if [ ! -f "posts_metadata.json" ]; then
    echo "❌ Error: posts_metadata.json not found!"
    exit 1
fi

echo "✅ posts_metadata.json found ($(wc -c < posts_metadata.json) bytes)"

# Create a simple test to verify the file
echo "📋 Creating deployment verification..."
cat > verify-deployment.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Deployment Verification</title>
</head>
<body>
    <h1>Deployment Verification</h1>
    <div id="status">Checking...</div>
    <script>
        fetch('posts_metadata.json')
            .then(response => {
                if (response.ok) {
                    document.getElementById('status').innerHTML = '✅ JSON file is accessible';
                } else {
                    document.getElementById('status').innerHTML = '❌ JSON file not accessible: ' + response.status;
                }
            })
            .catch(error => {
                document.getElementById('status').innerHTML = '❌ Error: ' + error.message;
            });
    </script>
</body>
</html>
EOF

echo "✅ Verification file created"

# List all files that should be deployed
echo "📁 Files to deploy:"
ls -la *.html *.js *.css *.json *.md 2>/dev/null || echo "Some files not found"

echo "🎉 Deployment preparation complete!"
echo ""
echo "Next steps:"
echo "1. Upload all files to your production server"
echo "2. Ensure posts_metadata.json is in the root directory"
echo "3. Test with verify-deployment.html"
echo "4. Check server configuration for JSON file serving"
