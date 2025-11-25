# json-ld-docu-gen

**Automated Documentation Generation from JSON-LD Data**

A powerful toolkit for enterprises to automatically generate comprehensive documentation from JSON-LD instance data. Visualize complex organizational data flows, technical system topologies, and process swimlanes through semantic linked data.

---

## 1st Steps - how to use it in a virtual python environment.

### optionally create a virtual environment like

```bash
python3 -m venv .venv
source .venv/bin/activate.fish
```

### install cruft

```bash
pip install --upgrade pip
pip install cruft
```

```bash
cruft create --help
```

```text
 Usage: cruft create [OPTIONS] TEMPLATE                                                                                                               
                                                                                                                                                      
 Expand a Git based Cookiecutter template into a new project on disk.                                                                                 
                                                                                                                                                      
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    template_git_url      TEMPLATE  The Cookiecutter template URI. [required]                                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --output-dir                   DIRECTORY  Where to output the generated project dir into [default: .]                                              │
│ --config-file                  PATH       Path to the Cookiecutter user config file                                                                │
│ --default-config       -d                 Do not load a config file. Use the defaults instead                                                      │
│ --extra-context                TEXT       A JSON string describing any extra context to pass to cookiecutter.                                      │
│ --extra-context-file   -E      PATH       Path to a JSON file describing any extra context to pass to cookiecutter.                                │
│ --no-input             -y                 Do not prompt for template variables and only use cookiecutter.json file content                         │
│ --directory                    TEXT       Directory within repo that holds cookiecutter.json file for advanced repositories with multi templates   │
│                                           in it                                                                                                    │
│ --checkout             -c      TEXT       The git reference to check against. Supports branches, tags and commit hashes.                           │
│ --overwrite-if-exists  -f                 Overwrite the contents of the output directory if it already exists                                      │
│ --skip                         TEXT       Default files/pattern to skip on update                                                                  │
│ --help                                    Show this message and exit.                                                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### build acme demo

#### generate initial source

```bash
cruft create --no-input \
    --skip envs \
    --config-file ./cookiecutter-acme-demo.yaml \
    --output-dir . \
    https://github.com/mleist/json-ld-docu-gen/
```

#### change to new source dir

```bash
cd acme-interfaces/
```

#### start microservice with json-ld data

```bash
docker compose up -d
```

#### generate the documentation

```bash
./make_all.sh
```

### see more documentation

[README_json-ld-docu-gen.md](./{{cookiecutter.jldg_prj_slug}}/README_json-ld-docu-gen.md)

### generated example PDF

[acme-demo.pdf](acme-demo.pdf)

---

**json-ld-docu-gen** — *Where data meets documentation.*
