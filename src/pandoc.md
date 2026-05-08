# pandoc

## podman

```bash
podman run --rm \
       --volume "$(pwd):/data:Z" \
       pandoc/extra analysis.md -o analysis-2.pdf
```
