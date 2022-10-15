# pysmart_meter
Idea here is to setup a fairly old iphone running pythonista app to take pictures of an electricity meter at defined
intervals.  The pictures should then get uploaded into icloud and will be OCR'd and so forth most likely with opencv
as part of the backend procesing which should run on most python setups.

So the project will have two parts - the pythonista folder will hopefully be small and cover what's required to take
photos at intervals on the phone and the rest will be image processing and then analyzing when energy usage is high and
whatever other analysis seems sensible.  Most likely we just have a raw table of meter readings and then I may try and
find some other project that provides analysis as no reason to think that hasn't been well catered for already somewhere

