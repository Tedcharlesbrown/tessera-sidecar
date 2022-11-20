# Tessera Sidecar
## What
Tessera Sidecar is a custom python solution for easier control of [Brompton processors](https://www.bromptontech.com/). Working alongside [Bitfocus Companion](https://bitfocus.io/companion) (or any device/software that will send OSC).

## Why
Bitfocus Companion is amazing, but;

 1. There is some limitation on  button control, such as holding down a button to make the action continuous.
 2. I don't know how to edit companion modules

## How
Tessera Sidecar listens to OSC commands, which it then maps to HTTP requests, which are available in the [Brompton API](https://dl.bromptontech.com/tessera/docs/TesseraIPControlAPI3_2_0_Beta4.pdf)

### Dependencies
- [Requests](https://pypi.org/project/requests/)
- [Python OSC](https://pypi.org/project/python-osc/)

