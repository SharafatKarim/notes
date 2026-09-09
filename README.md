# 🌱 Notes & Digital Garden

[![Deploy Quartz site to GitHub Pages](https://github.com/SharafatKarim/notes/actions/workflows/deploy.yml/badge.svg)](https://github.com/SharafatKarim/notes/actions/workflows/deploy.yml)
[![Quartz v5](https://img.shields.io/badge/Powered%20by-Quartz%20v5-blue)](https://quartz.jzhao.xyz/)
[![Obsidian](https://img.shields.io/badge/Vault-Obsidian-purple)](https://obsidian.md/)

Welcome to my personal digital garden, wiki, and knowledge repository. This repository stores structured notes, engineering cheat sheets, university coursework, software configurations, and project initiatives — built with **Obsidian** and rendered as a static web garden using **[Quartz v5](https://quartz.jzhao.xyz/)**.

🌐 **Live Garden**: [sharafat.is-a.dev/notes](https://sharafat.is-a.dev/notes)

---

## 🧭 Vault Structure

The vault is organized into modular knowledge domains:

```
content/
├── 🎓 academic/          # University coursework, OS, AI, Networks, DBMS, and exam solves
├── 🛠️ tech/              # Systems, Linux, Python, C++, Docker, databases, and dev workflows
├── 🧰 tools/             # Curated developer utilities, security, and desktop applications
├── 🚀 projects/          # Open-source projects, Rising Flare, PSTU campus initiatives
├── 🌿 personal/          # Profile, contact information, articles, and reading lists
├── 🌐 web/               # Web bookmarks, online services, and feed setups
├── 🎮 fun/               # Anime watchlists, gaming notes, and leisure
└── 📚 collections/       # Curated collections and media archives
```

---

## 🚀 Local Development

### Prerequisites

- **Node.js**: `v22+` or `v24`
- **pnpm**: `v10+` (or `npm`)

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SharafatKarim/notes.git
   cd notes
   ```

2. **Install dependencies**:
   ```bash
   pnpm install
   ```

3. **Install Quartz plugins**:
   ```bash
   pnpm quartz plugin install
   ```

4. **Start the local preview server**:
   ```bash
   pnpm quartz build --serve
   ```
   Open [http://localhost:8080](http://localhost:8080) to browse the digital garden locally.

5. **Build for production**:
   ```bash
   pnpm quartz build
   ```

---

## 🚢 Deployment & CI/CD

Automatic deployment to **GitHub Pages** is configured via GitHub Actions in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) on pushes to the `v5` branch.

---

## 📝 License & Attribution

- Content & Notes © [Sharafat Karim](https://github.com/SharafatKarim)
- Site Generator powered by [Quartz v5](https://github.com/jackyzha0/quartz) (MIT License)
