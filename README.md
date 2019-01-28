# DeltaHacksV

Team of Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault. We are tackling the Materials Engineering Challenge.

## Running

You can run either `python Main.py` or `python MainNoGUI.py` (you might have to specify your version of Python) to use either the GUI or non-GUI version of the software, respectively.

## Description of Problem

The properties of materials depend on the way in which atoms and defects are arranged in the material. For this reason, materials engineers observe the material using optical and electron microscopes. The images they take are often like attached figures. What we would like you to do, is to measure the fractions of the light and dark “phases” in these figures. The fraction could simply be expressed as number of pixels of a given color over the total number of pixels. The problem is complicated by the lighting conditions. Sometimes you’ll get very good contrast between the phases (e.g. micro1.png) and sometimes there is less contrast. In addition, the light and dark phases may contain “particles” like those shown in micro2.png. You will be awarded (25) points for achieving each of the targets listed below as well as (50) points for the user interface and ease of use.

Target 1: Measure the fraction of the dark phase with an accuracy of 0.5% or better in an image that does not contain particles (e.g. micro1.png).

Target 2: Measure the fraction of the dark phase with an accuracy of 0.5% or better in an image that contains particles (e.g. micro3.png). For images with particles, the particles inside the dark phase should be counted with the dark phase and the ones inside the light phase should be counted with the light phase.

Target 3: Same as target 2, but you will be given images with uneven lighting conditions.

Target 4: You need to measure the average size (equivalent diameter) of the grains in the images. The “grains” simply refer to the polygons that make the images.

Target 5: You are able to produce a histogram of the grain size.

On the day of the challenge, you will be provided with over 300 images to practice on.

-- Taken from DeltaHacks website
