# cadlib for Python

Python bindings for the SimScale `cadlib` library: load a CAD model input
to a workflow method and run geometry queries on it (volume, bounding box,
tessellation, …), with typed Pydantic models for every parameter and result.

> [!NOTE]
> `cadlib` is meant to be used in the Docker image that implements the workflow
> method. It is not intended for validations.

You need CPython 3.12 or newer.

## Install

```bash
pip install simscale-cadlib
```

The package is `simscale-cadlib`; in code it is `cadlib`. The wheel is
self-contained, its only dependency is `pydantic>=2`. It bundles the native
library, so there is no install script: locally, in CI and in Docker,
`pip install` is the whole setup, and the library always matches the package.

Pin the version as usual, e.g. `simscale-cadlib==<version>` in
`requirements.txt`, or `poetry add simscale-cadlib@<version>`.

```python
import cadlib
print(cadlib.__version__)
```

## Usage

```python
from cadlib import Cad, VolumeParameters

# Load the CAD model from the CAD data map entry of the method's input parameters.
cad = Cad.load(request.data_map.cad)

# Query methods are async.
result = await cad.volume(VolumeParameters(entity_ids=["B1_TE5"]))
```

- **Load once, reuse.** Each `Cad.load` rebuilds the model, which is expensive,
  so load once and run every query on the same `Cad`.
- **Errors** are either a `cadlib.CadExpectedError`, a known domain error with an
  `error_code`, or a `cadlib.CadUnexpectedError`. The codes are listed in
  [ERRORS.md](ERRORS.md).
- **Parameters and results** are Pydantic models. Attributes are snake_case;
  `model_dump(by_alias=True)` gives the camelCase field names.

## Docker

Use a glibc base image (see [Supported platforms](#supported-platforms)). The
wheel bundles the native library: `pip install` is the only setup step.

```dockerfile
FROM python:3.12-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "-m", "myservice"]
```

On Alpine, `pip` finds no matching wheel and fails with
`No matching distribution found for simscale-cadlib`.

## Supported platforms

| OS | Architecture | Wheel | Requires |
|----|--------------|-------|----------|
| Linux | x86_64, aarch64 | `manylinux_2_28` | glibc 2.28 or newer (Debian 10+, Ubuntu 20.04+, RHEL 8+) |
| macOS | aarch64 (Apple silicon) | `macosx_11_0_arm64` | macOS 11 or newer |
| Windows | x86_64 | `win_amd64` | Windows 10 or newer |

One wheel per platform covers CPython 3.12 and every newer version.

Alpine and other musl-based distributions are not supported: the library is
built for glibc and cannot load on musl. Intel Macs and Windows on Arm are not
supported either.

## License

MIT, see [LICENSE](LICENSE).
