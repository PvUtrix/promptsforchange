#!/usr/bin/env node

// Script to update version information in the app
const fs = require('fs');
const { execSync } = require('child_process');

try {
    // Get current commit hash
    const commitHash = execSync('git rev-parse --short HEAD', { encoding: 'utf8' }).trim();
    
    // Get current date
    const currentDate = new Date().toISOString().split('T')[0];
    
    // Update the HTML file with current version
    let htmlContent = fs.readFileSync('index.html', 'utf8');
    
    // Update version in the About modal
    htmlContent = htmlContent.replace(
        /<span class="tech-value" id="appVersion">[^<]*<\/span>/,
        `<span class="tech-value" id="appVersion">${commitHash}</span>`
    );
    
    // Update last updated date
    htmlContent = htmlContent.replace(
        /<span class="tech-value" id="lastUpdated">[^<]*<\/span>/,
        `<span class="tech-value" id="lastUpdated">${currentDate}</span>`
    );
    
    fs.writeFileSync('index.html', htmlContent);
    
    // Update the JavaScript file with current version
    let jsContent = fs.readFileSync('script.js', 'utf8');
    
    // Update version in the updateAboutInfo function
    jsContent = jsContent.replace(
        /document\.getElementById\('appVersion'\)\.textContent = '[^']*';/,
        `document.getElementById('appVersion').textContent = '${commitHash}';`
    );
    
    fs.writeFileSync('script.js', jsContent);
    
    console.log(`✅ Version updated to ${commitHash} (${currentDate})`);
    
} catch (error) {
    console.error('❌ Error updating version:', error.message);
    process.exit(1);
}
