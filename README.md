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
 - Import .companionconfig to Bitfocus Companion. *(optional)*
 
 ## OSC Commands
 Most commands are accessed by sending multiple arguments in each message. In Bitfocus, the action is called "Send message with multiple arguments".
In all cases, the first argument is always the Processor ID. This can be set in the settings.json file.
 - Brightness Select
	 - Sets selected processor at designated intensity value
   	- Syntax: `/brightness`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Intensity *(int)*
- Brightness Percentage
	 - Sets selected processor at designated intensity percentage
   	- Syntax: `/brightness/percent`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Percentage *(int)*
 - Brightness Step
	 - Steps the brightness by a specified amount
   	- Syntax: `/brightness/step`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Step amount (make negative for decreasing steps) *(int)*
   	 - Note: Brightness step also needs a message sent without arguments in order to continuously send the step command. `/on` when pressed and `/off` when released

- Temperature Select
	 - Sets selected processor at designated intensity value
   	- Syntax: `/brightness`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Temperature *(int)*
- Temperature Step
	 - Steps the temperature by a specified amount
   	- Syntax: `/temperature/step`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Step amount (make negative for decreasing steps) *(int)*
   	 - Note: Temperature step also needs a message sent without arguments in order to continuously send the step command. `/on` when pressed and `/off` when released

- Blackout
	 - Sets selected processor at designated intensity value
   	- Syntax: `/blackout`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Toggle *(int)*

- Freeze
	 - Sets selected processor at designated intensity value
   	- Syntax: `/freeze`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Toggle *(int)*

- Test Pattern
	 - Sets selected processor at designated intensity value
   	- Syntax: `/test`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Toggle *(int)*

- Test Pattern Select
	 - Sets selected processor at designated intensity value
   	- Syntax: `/test`
   	- Arguments: 2
	   	1. Processor ID *(int)*
	   	2. Test Pattern Selection *(int) or (str)*
	   	``"brompton", "brompton-overlay", "white", "red", "green", "blue", "cyan", "magenta", "yellow", "black",
    "grid", "scrolling-grid", "forty-five-degree-grid", "scrolling-forty-five-degree-grid", "checkerboard", "scrolling-checkerboard",
    "gradient", "scrolling-gradient", "colour-bars",  "strobe", "smpte-bars", "scrolling-smpte-bars", "custom-colour"
 `` 

### Dependencies
- [Requests](https://pypi.org/project/requests/)
- [Python OSC](https://pypi.org/project/python-osc/)

