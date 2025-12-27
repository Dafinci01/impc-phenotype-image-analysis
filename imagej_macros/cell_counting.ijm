//convert to grayscle 
run("8-bit");


//threshold image automatically
setAutoThreshold("Otsu dark");
run("Convert to mask");

//Seprate touching pobjects
run("Watershed");


//count particles(cells)
run("Analyze Particles....", "size=50-infinity show=Outlinesdisplay summarize");
