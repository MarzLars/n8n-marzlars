# n8n Self-hosting Documentation

This repository contains a **GitHub Pages hosted documentation site** for self-hosting n8n. 

⚠️ **Important Clarification**: This site hosts **documentation only**, not the actual n8n application. GitHub Pages can only serve static HTML/CSS/JS files and cannot run backend applications like n8n.

## 🌐 Live Site

Visit the hosted documentation at: `https://marzlars.github.io/n8n-marzlars/`

## 📖 What This Repository Does

This repository provides comprehensive guides for:
- Installing n8n on your own servers (VPS, cloud platforms, etc.)
- Configuring n8n for production use
- Setting up SSL/TLS security
- Troubleshooting common issues
- Step-by-step deployment to various platforms (DigitalOcean, Railway, AWS, etc.)

## 🚀 To Actually Host n8n

n8n requires a server to run. You cannot host it on GitHub Pages. Here are your options:

### Quick Local Test
```bash
npx n8n
```

### Production Hosting Options
1. **Cloud Platforms**: DigitalOcean, AWS, Google Cloud, Azure
2. **Container Services**: Railway, Render, Heroku
3. **Self-hosted**: Your own VPS with Docker
4. **n8n Cloud**: Official hosted solution (easiest option)

See the [live documentation](https://marzlars.github.io/n8n-marzlars/) for detailed instructions.

## 📋 Contents

This documentation covers:

- **Installation and server setups** - Install n8n using npm, Docker, or other platforms
- **Configuration** - Environment variables and configuration options
- **Users and authentication** - Setting up user authentication systems
- **Scaling** - Managing data, modes, and processes at scale
- **Security** - SSL, SSO, 2FA, and security configurations
- **Starter kits** - AI workflow starter kit and templates

## 🚀 Setup Instructions (For This Documentation Site)

If you want to create your own copy of this documentation:

### 1. Fork or Clone This Repository
```bash
git clone https://github.com/MarzLars/n8n-marzlars.git
```

### 2. Enable GitHub Pages
1. Go to your repository settings on GitHub
2. Scroll down to "Pages" section
3. Under "Source", select "GitHub Actions"
4. The deploy.yml workflow will automatically deploy your site

### 3. Access Your Site
Your site will be available at: `https://YOUR_USERNAME.github.io/REPOSITORY_NAME/`

## 📁 Repository Structure

- `index.html` - Main documentation page with installation guides
- `style.css` - Styling for the documentation
- `README.md` - This file
- `.github/workflows/deploy.yml` - GitHub Actions workflow for deployment
- `github-pages-setup.md` - Detailed setup guide
- `script.py` - Python script used to generate initial files

## 🛠️ Customization

You can customize this documentation by:

- Editing the HTML content in `index.html`
- Modifying styles in `style.css`
- Adding additional pages
- Updating the deployment workflow in `.github/workflows/deploy.yml`

## 📚 Resources

- **Official n8n Documentation**: https://docs.n8n.io/hosting/
- **n8n Community Forum**: https://community.n8n.io
- **n8n GitHub**: https://github.com/n8n-io/n8n

## ⚠️ Important Notes

- This is a **static documentation site** for educational purposes
- **You cannot run n8n itself on GitHub Pages** - you need a proper server
- For actual n8n hosting, follow the deployment guides in the documentation
- For the most up-to-date information, always refer to the official n8n documentation
- Self-hosting n8n requires technical expertise - proceed with caution

## 🆘 Getting Help with n8n

If you need help with n8n itself (not this documentation site):
- Visit the [n8n Community Forum](https://community.n8n.io)
- Check the [official documentation](https://docs.n8n.io)
- Open an issue on [n8n's GitHub](https://github.com/n8n-io/n8n/issues)

## 📄 License

Content is based on n8n documentation. Please refer to n8n's licensing terms for usage rights.
