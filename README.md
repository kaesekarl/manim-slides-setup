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
Please follow the instructions for Manim and Manim-Slides. After that the Framework is basically some presets and 
Helper Functions. I recommend you clone the repository and replace the content of the `scenes.py` file with the 
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
To create a Presentation, you need to write the Code to produce the Animations and Slides.
Instead of using the `Scene` class from Manim, you should use the `Slide` class. It builds on top of the Scene class and provides some additional features.

The Basic interaction goes as follows:
1. You create the Mobjects you want to use in your Scene
2. You choose a Layout for your Scene. This can be done with the `apply_layout` Function. 
3. When you have all your Mobjects available, you can Create the Animations you want to use in your Scene.

Everytime you want to pause your Animations, you use `self.pause()`. This way Manim waits for you to press a key to 
continue your Presentation. I recommend using `self.wait()` after every pause to make sure the Animation is finished.

I am creating my own design for the Slides, but you can also create your own stuff. I set the parameters to feed the 
functions within the `design` directory. Simply change them to your liking.

### Presenting
To use the Presentation you created, you need to render it first. This can be done with the Command `manim -pqh
scenes.py <SceneName>`. 
This will render the Scene and open a Preview Window. You can use the `-ql` flag to render the Scene in low quality. 
This is useful if you want to render the Scene faster. Adding the `-p` flag will render the Scene and open a Preview.
In this preview, you will see the `self.pause()` instructions change nothing about the Animation. This is only 
relevant, when you Present them Live.

After you rendered the Scenes you want you simply run `manim-presentation <SceneNames>`. This will open a Window in 
which your Presentation will be shown. You can use the `--fullscreen` flag to open the Presentation in Fullscreen. 
You also have a little Window to show you some Information about the Presentation.

Caution for Users right now: Since im still working on this and nothing is fixed in place yet, so maybe you run into 
some bugs, errors or breaking changes. If you do, please let me know.
