# Documentation for Manim-Slides-Setup

## Warning
This project right now is still in development and not finished at all. I might change a lot of things in the future,
so be aware of that. Neither the code nor the documentation is finished in any way. Many things are still missing or 
outdated. With caution (and some appreciation for bad coding) go ahead and use it. If you find any bugs or have any 
suggestions, please let me know.

**Author:** Kaesekarl  
This is a framework to create slides with Manim. It uses the [manim CE library](https://github.com/ManimCommunity/manim/) 
to render the Animations and Slides. 
It also uses the [manim-presentation](https://github.com/galatolofederico/manim-presentation) library to create the Presentation 
itself. This is not necessary to use, but this Framework is intended to be used for Live-Presentations
The Design is heavily influenced by [karlosos LaTeX-Beamer Template](https://github.com/karlosos/zut-fibeamer).

## Installation
Please follow the instructions for Manim and Manim-Presentation. After that the Framework is basically some Designs and 
Helper Classes. I recommend you clone the repository and replace the content of the `scenes.py` file with the 
Animations you need.


## Helping (me (please))
Just a heads-up: I'm no professional in any way. I try to become one, but there is still a lot of things to be achieved before i deserve that title. If you have any ideas or wishes to be implemented or how to improve the code just let me know. If you want to contribute some code don't hesitate to improve the code yourself!

## Usage
### Overview
This framework provides some Presets and Tools to make a Presentation for a Live Audience. Before you start working 
with this framework you should have a look into [Manim](https://github.com/ManimCommunity/manim/) itself. The 
[Documentation](https://docs.manim.community/en/stable/index.html) is pretty good as well.

You don't need to know every little Detail about Manim to use this Framework, but since it is based on Manim you 
should have a basic understanding of how it works.

### Creating a Presentation
First you should create the slides with Manim like you normally would. After that, you can insert `self.pause()` 
into your file to create a breakpoint in your Animation. While presenting, the Animation will pause at that point 
and the tool will wait for you to press a key to continue.


