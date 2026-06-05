# PNPM

## Install something globally

```bash
pnpm add -g <package-name>
```

> Make sure PNPM_HOME and ENV are all set!

## Update all global

```bash
pnpm up -g
```

## Update all local

```bash
pnpm update --interactive --latest
```

## Aliases

```bash
# Prefer pnpm over npm
alias npm="pnpm"
alias npx="pnpm dlx"
```
