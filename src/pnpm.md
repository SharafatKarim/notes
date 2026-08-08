# PNPM

## Global

### Install something globally

```bash
pnpm add -g <package-name>
```

> Make sure PNPM_HOME and ENV are all set!

### Update all global

```bash
pnpm up -g
```

### List all global packages

```bash
pnpm ls -g
```

### Remove a global package

```bash
pnpm rm -g nativefier 
```

### Interesting packages

```txt
pake-cli
```

## Local

### Update all local

```bash
pnpm update --interactive --latest
```

## Aliases

```bash
# Prefer pnpm over npm
alias npm="pnpm"
alias npx="pnpm dlx"
```
