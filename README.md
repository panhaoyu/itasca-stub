# itasca-stub

This repository contains code to generate `itasca.pyi` for PFC600.

Itasca provide Python interface,
however, I want to write Python in Pycharm.
Itasca does not provide Pycharm interface,
So when I write PFC in Pycharm,
the keyword `itasca` is always red,
and there's no type hint.

Here is a preview.

![preview](https://raw.githubusercontent.com/panhaoyu/itasca-stub/master/doc/assets/preview.png)

## Installation

### Manual

I wrote these code to generate `itasca.py`.
If you want to use it,
just copy the `itasca.py` to `site-packages`.


I hope you know what is `site-packages`,
for I do not have time to explain this.
And I hope you can locate `site-packages` of PFC,
rather than `site-packages` of system default python.

### PIP

Okay, I've already upload this repo to `pypi`,
so you may try `pip`.

```cmd
pip install itasca-stub
```

Best wishes!

## Contribution Guide

This is a tiny repo,
for a small (maybe large, but rare used) programe.
I did only a little,
and perhaps you can do more.
You can just fork this repo,
or you can help me finish type system,
there's many things should do.
Just send me a PR!

BTW, if you are Itasca,
I'm willing to give this repo to you.