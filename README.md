# itasca-stub

This repository contains code to generate `itasca.pyi` for PFC 7.00.

Itasca provides great python interface, But it is too weak compared to PyCharm.
When writing PFC in PyCharm, the keyword `itasca` has no typehint.
Thus, the project is developed, and here's a preview.

![preview](https://raw.githubusercontent.com/panhaoyu/itasca-stub/master/doc/assets/preview.png)

## Installation

### Manual

Copy the `itasca` directory to your python `site-packages` directory.
Make sure to copy to your current environment.
If the internal Python of PFC is used, then you should copy to the path like:
`Itasca\PFC700\exe64\python36\Lib\site-packages`.

### pip

```cmd
pip install itasca-stub-pfc7
```

Best wishes!

## Contribution

You can submit issues and PRs at any time, welcome for your contribution!