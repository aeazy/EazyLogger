<style>
	mark{
	    color:red;
	}
</style>

# EazyLogger

A simple module to add color to Python log messages.

## Table of Contents

- [Installation](#installation)
- [Logger](#logger)
- [Examples:](#examples)
  - [Basic Example](#basic-example)

## Installation

Binary installer is available at the [Python Package Index (PyPi)](#).

```bash
pip install eazylogger
```

## Logger

> Parameters
> <strong id='Logger'>Logger</strong>(<b>name</b>, <b>msg_fmt</b><i>="[%(levelname)s] - %(message)s (%(name)s)"</i>, <b>info_fmt</b><i>="%(message)s"</i>)

Logger class with color-coded log messages.

> Parameters

<ul style='list-style: none'>
	<li id='Logger-name'>
		<b>name : <i>str</i></b>
		<ul style='list-style: none'>
			<li id='Logger-name-description'>String expression representing the name of the logger class.</li>
		</ul>
	</li>
</ul>
<ul style='list-style: none'>
	<li id='Logger-msg_fmt'>
		<b>msg_fmt : <i>str, default [%(levelname)s] - %(message)s (%(name)s)</i></b>
		<ul style='list-style: none'>
			<li id='Logger-msg_fmt-description'>String expression representing how the debug, warning, error, and critical log messages are formatted. Defaults to "[%(levelname)s] - %(message)s (%(name)s)".</li>
		</ul>
	</li>
</ul>
<ul style='list-style: none'>
	<li id='Logger-info_fmt'>
		<b>info_fmt : <i>str, default %(message)s</i></b>
		<ul style='list-style: none'>
			<li id='Logger-info_fmt-description'>String expression representing how the info and success messages are formatted. Defaults to "%(message)s".</li>
		</ul>
	</li>
</ul>

<hr>

## Examples

- [Basic Example](#basic-example)

### Basic Example

1. Import and instantiate `Logger` class:

   ```python
   # main.py
   from eazylogger import Logger
   logger = Logger(__name__)
   ```

2. Logging methods:

   ```python
   # main.py
   logger.debug("Example debug message")
   logger.info("Example info message")
   logger.warn("Example warning message")
   logger.error("Example error message")
   logger.critical("Example critical message")
   logger.success("Example success message")
   ```

   <br>

    <pre>
    <span style="color:white">[DEBUG] - Example debug message (__main__)</span>
    <span style="color:white">Example info message</span>
    <span style="color:yellow">[WARNING] - Example warning message (__main__)</span>
    <span style="color:red">[ERROR] - Example error message (__main__)</span>
    <span style="color:red">[CRITICAL] - Example critical message (__main__)</span>
    <span style="color:green">Example success message</span>
    </pre>

<h5>TESTING</h5>
