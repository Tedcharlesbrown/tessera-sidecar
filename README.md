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
	 - **It is vital that format, syntax, and quotations remain intact**

```
"COMPANION IP": "127.0.0.1",
"COMPANION PORT": "8888",
"OSC PORT": "5005",
"SETTINGS PAGE": "99"
```
- These are the default settings for Tessera Sidecar to get up and running
	- Companion IP
		- By default, it is talking to Companion via localhost
	- Companion Port
		- Companion port for TCP control
		- This can be found on the companion splash screen
	- OSC Port
		- Port used for OSC communication
	- Settings Page
		- Tessera Sidecar will label buttons with some boilerplate and communication heartbeat
```
"PROCESSOR": 0,
"IP": "192.168.0.105",
"MAX_BRIGHTNESS": "4000",
"PAGE": "1"
```
- There are currently 11 slots to add processors
	- Processor
		- Index number for processor
		- Note that the processor count starts at 0
	- IP
		- IP Address for the processor
	- Max brightness
		- Max brightness for the processor
	- Page
		- Which bitfocus companion page (bank), feedback will appear on
			- buttons 2 and 3 will be used on the corresponding page
 4. Import .companionconfig to Bitfocus Companion. *(optional)*

### Dependencies
- [Requests](https://pypi.org/project/requests/)
- [Python OSC](https://pypi.org/project/python-osc/)

