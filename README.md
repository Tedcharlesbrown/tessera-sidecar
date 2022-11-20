# Tessera Sidecar
## What
Tessera Sidecar is a custom python solution for easier control of [Brompton processors](https://www.bromptontech.com/). Working alongside [Bitfocus Companion](https://bitfocus.io/companion) (or any device/software that will send OSC). Tessera Sidecar listens to OSC commands, which it then maps to HTTP requests, which are available in the [Brompton API](https://dl.bromptontech.com/tessera/docs/TesseraIPControlAPI3_2_0_Beta4.pdf)

## Why
Bitfocus Companion is amazing, but;

 1. There is some limitation on  button control, such as holding down a button to make the action continuous.
 2. I don't know how to edit companion modules

## Installation

 1. Download newest package
 2. Unzip files to a local folder
	 - If you have a previously used settings.json file, you don't need to replace it!
 3. Open settings.json in a text editor of your choice.
	 - If there is no settings.json, running the program will create one in the same folder as the application.
 
``
{
	"COMPANION IP": "127.0.0.1",
	"COMPANION PORT": "8888",
	"OSC PORT": "5005",
	"SETTINGS PAGE": "99"
}
``



 4. Import .companionconfig to Bitfocus Companion. *(optional)*

### Dependencies
- [Requests](https://pypi.org/project/requests/)
- [Python OSC](https://pypi.org/project/python-osc/)

