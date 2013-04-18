For the moment these projects work mainly with the cygwin build as some defines are hard coded in the build settings.
Feel free to create any other build config (linux, mac,...).
It should even be possible to adapt to any platform changing the $(PLATFORM) variable to the platform used by scons (cygwin, linux, mac...) as already used in pathes :
../../build/$(PLATFORM)/release/...
Skai.
